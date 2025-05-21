import sqlite3
from dataclasses import dataclass
from sqlite3 import Connection, Cursor


@dataclass
class Note:
    id: int
    title: str
    content: str
    user: int


@dataclass
class User:
    id: int
    name: str
    password: str
    created_at: int
    updated_at: int


class ValidationError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class NoteDAO:
    """Data Access Object for notes."""

    def __init__(self, conn: Connection):
        self.conn: Connection = conn
        self.cursor: Cursor = conn.cursor()

    def username_to_id(self, user: str) -> int:
        """Convert a username to a user ID.
        If the user does not exist, return 0.

        Args:
            user (str): The username.
        Returns:
            int: The user ID if found, 0 otherwise.
        Raises:
            UserNotFoundError: If the user does not exist.
        """
        user_id: tuple[int, ...] = self.cursor.execute(
            "SELECT id FROM user WHERE name = ?", (user,)
        ).fetchone()
        if not user_id:
            raise UserNotFoundError("User not found.")
        return user_id[0]

    def get_notes(self) -> dict[tuple[int, str], Note]:
        """Get all notes from the database.
        Returns a dictionary with the user ID and title as the key,
        and the Note object as the value.

        Args:
            user (int | str): The user ID or username.
        Returns:
            dict[tuple[int, str], Note]: A dictionary with the user ID and title
            as the key, and the Note object as the value.
        >>> from model_note import NoteDAO, Note
        >>> notes dict[tuple[int, str], Note] = dao.get_notes()
        >>> note: Note = notes[(user_id, title)]

        """
        self.cursor.execute("SELECT * FROM note")
        rows: list[tuple[int, str, str, int]] = self.cursor.fetchall()
        return {
            (note.user, note.title): note
            for row in rows
            for note in [Note(*row)]
        }

    def get_notes_by(self, user: int | str) -> dict[str, Note]:
        """Get all notes from the database for a specific user.

        Returns a dictionary of the user's notes with the title as the key
        and the `Note` object as the value.

        Args:
            user (int | str): The user ID or username.

        Returns:
            dict[str, Note]: A dictionary with the title as the key
            and the `Note` object as the value.

        Raises:
            UserNotFoundError: If the user does not exist.

        Usage:
        >>> from model_note import NoteDAO, Note
        >>> notes: dict[str, Note] = dao.get_notes()
        >>> note: Note = notes[(user_id, title)]

        """
        if isinstance(user, str):
            user = self.username_to_id(user)
        self.cursor.execute("SELECT * FROM note WHERE user_id = ?", (user,))
        rows: list[tuple[int, str, str, int]] = self.cursor.fetchall()
        return {
            note.title: note
            for row in rows
            for note in [Note(*row)]
        }

    def find_user(self, user: str | int) -> None | User:
        """Find a user by username or ID.

        Args:
            user (str | int): The username or user ID.

        Returns:
            None | User: The User object if found, None otherwise.
        """
        if isinstance(user, str):
            try:
                user = self.username_to_id(user)
            except UserNotFoundError:
                return None

        row: tuple[int, str, str, int, int] = self.cursor.execute(
            "SELECT * FROM user WHERE id = ?", (user,)
        ).fetchone()
        return User(*row)

    def add_user(self, user: str, password: str) -> None:
        """Add a user to the database.

        Args:
            user (str): The username.
            password (str): The password.
        """
        with self.conn:
            self.cursor.execute(
                "INSERT INTO user (name, password) VALUES (?, ?)",
                (user, password),
            )

    def authenticate(self, user: int | str, hashed_password: str) -> int:
        """Authenticate a user by username or ID and hashed_password.

        Args:
            user (int | str): The user ID or username.
            hashed_password (str): The password.

        Returns:
            int: The user ID if authenticated successfully.
        Raises:
            ValidationError: If the username or hashed_password is invalid.
            UserNotFoundError: If the user does not exist.

        """

        if isinstance(user, str):
            user = self.username_to_id(user)

        valid_user: None | tuple[int, str, str, int, int] = self.cursor.execute(
            "SELECT * FROM user WHERE id = ? AND password = ?",
            (user, hashed_password),
        ).fetchone()
        if not valid_user:
            raise ValidationError("Failed to authenticate!")
        return User(*valid_user).id

    def add_note(
        self,
        user: int | str,
        title: str,
        content: str | list[str]
    ) -> None:
        """Add a note to the database.
        If title and content are None, prompt the user for input.
        If content is a list, join it into a string.

        Args:
            user (int | str): The user ID or username.
            title (str): The title of the note.
            content (str | list[str]): The content of the note.

        Raises:
            sqlite3.IntegrityError: If the user already has a
            note with the same title.
            UserNotFoundError: If the user does not exist.
        """
        if isinstance(user, str):
            user = self.username_to_id(user)

        if isinstance(content, list):
            content = "\n".join(content)

        with self.conn:
            cursor = self.cursor

            existing: None | tuple[int, str, str, int] = cursor.execute(
                "SELECT 1 FROM note WHERE user_id = ? AND title = ?",
                (user, title),
            ).fetchone()
            if existing:
                # User already has a note with this title
                raise sqlite3.IntegrityError()

            cursor.execute(
                "INSERT INTO note (title, content, user_id) VALUES (?, ?, ?)",
                (title, content, user)
            )

    def edit_note(self, note_id: int, new_content: str):
        """Edit a note in the database.

        Args:
            note_id (int): The ID of the note to edit.
            new_content (str): The new content of the note.
        """
        with self.conn:
            self.cursor.execute(
                "UPDATE note SET content = ? WHERE id = ?",
                (new_content, note_id),
            )

    def delete_note(self, note_id: int):
        """
        Delete a note from the database.

        Args:
            note_id (int): The ID of the note to delete.
        """
        with self.conn:
            self.cursor.execute("DELETE FROM note WHERE id = ?", (note_id,))

    def delete_by_title(self, user: str | int, title: str):
        """Delete a note by title.

        Args:
            user (str | int): The user ID or username.
            title (str): The title of the note to delete.
        """
        if isinstance(user, str):
            user = self.username_to_id(user)
        with self.conn:
            self.cursor.execute(
                "DELETE FROM note WHERE title = ? AND user_id = ?",
                (title, user),
            )
