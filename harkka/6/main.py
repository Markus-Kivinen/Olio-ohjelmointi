import sqlite3
import string
from hashlib import md5

from db_conn import DBConn
from kirje import Kirje, KirjeDetails
from menu import Menu
from model_note import Note, NoteDAO, UserNotFoundError, ValidationError


class Main:
    def __init__(self, db_conn: None | DBConn):
        print("Program starting.")
        self.db_conn: DBConn = db_conn or DBConn("notes.db", "setup.sql")
        self.db_conn.initialize()
        self.current_user: int = 0
        self.dao: NoteDAO = NoteDAO(self.db_conn.connection)

        self.note_menu: Menu = Menu().add_options(
            {
                "1": ("List notes", self.list_notes),
                "2": ("View note", self.view_note),
                "3": ("Add note", self.add_note),
                "4": ("Edit note", self.edit_note),
                "5": ("Delete note", self.delete_note),
                "0": ("Logout", self.exit_notemenu),
            }
        )

        self.login_menu: Menu = Menu().add_options(
            {
                "1": ("Login", self.login),
                "2": ("Register", self.register),
                "0": ("Exit", self.exit),
            }
        )

    def handle_menu(self, menu: Menu) -> None:
        menu.enabled = True
        while menu.enabled:
            print(menu.get_option_tree())
            user_input = menu.get_input()
            if not menu.has_option(user_input):
                print("Invalid option.")
                return
            opt = menu.options[user_input]
            if opt.function:
                opt.function()

    def login(self):
        """Prompt the user for credentials and authenticate."""

        print("Insert credentials below:")
        username = input("Insert username: ")
        password = input("Insert password: ")
        hashed_password = md5(password.encode()).hexdigest()

        try:
            user_id = self.dao.authenticate(username, hashed_password)
            print("Authenticated!\n")
            self.current_user = user_id
            self.login_menu.enabled = False
            self.note_menu.opt_name = f"User '{username}' options:"
            self.handle_menu(self.note_menu)
        except (UserNotFoundError, ValidationError):
            print("Failed to authenticate!\n")

    def validate_input(
        self, user_input: str, is_password: bool = False
    ) -> bool:
        """Validates the username/password.
        Input must be between 4 and 10 characters long,
        and can only contain lower case characters 'a-z',
        upper case characters 'A-Z', and special characters '_' and '-'.
        If is_password is True, digits are also allowed.

        Args:
            user_input (str): The username to validate.
            is_password (bool): If True, validate as a password.
        Returns:
            bool: True if the user_input is valid, False otherwise.
        """
        input_type = "Username"

        validchars: str = string.ascii_lowercase + "_-"
        if is_password:
            validchars += string.digits
            input_type = "Password"

        if len(user_input) < 4:
            print(f"{input_type} must be minimum of '4' characters long.\n")
            return False
        elif len(user_input) > 10:
            print(f"{input_type} must be maximum of '10' characters long.\n")
            return False

        valid = set(user_input.lower()).issubset(validchars)
        if not valid:
            print(
                f"{input_type} can only contain:\n"
                + "1. Lower case characters 'a-z'\n"
                + "2. Upper case characters 'A-Z'\n"
                + "3. Special characters '_' and '-'\n"
            )
            return False
        return True

    def register(self):
        """Register a new user."""

        username = input("Insert username: ")
        if not self.validate_input(username):
            return

        password = input("Insert password: ")
        if not self.validate_input(password, True):
            return

        # CodeGrader does not actually check this
        repeated_pw = input("Insert password again: ")
        if password != repeated_pw:
            print("Passwords do not match.\n")
            return
        hashed_password = md5(password.encode()).hexdigest()

        if self.dao.find_user(username):
            print("Username already exists.\n")
            return

        self.dao.add_user(username, hashed_password)
        print("Registration completed!\n")

    def list_notes(self):
        """List all notes in the database by user."""
        notes: dict[str, Note] = self.dao.get_notes_by(self.current_user)
        if not notes:
            print("There are no notes.\n")
            return

        note_content = "\n".join(
            f"{note.id} - {note.title}" for note in notes.values()
        )
        memo_details = KirjeDetails(
            content=note_content,
            header_separation=" - ",
            headers={"ID": "Title", "Title": " notes "},
        )
        memo_list = Kirje(memo_details)
        memo_list.display("streamlined")
        print("")

    def view_note(self):
        """View a note in the database."""
        title = input("Search note by title: ")
        notes: dict[str, Note] = self.dao.get_notes_by(self.current_user)
        if not notes:
            print("Not found.\n")
            return

        note = notes.get(title, None)
        if note:
            memo_details = KirjeDetails(
                content=note.content,
                header_separation=" - ",
                headers={"ID": f"{note.id}", "Title": f"{note.title}"},
            )
            current_memo = Kirje(memo_details)
            current_memo.display("default")
            print("")

    def add_note(self):
        """Add a note to the database."""
        title = input("Insert title: ")
        rows = int(input("Insert the amount of rows: "))
        content = "\n".join(
            input(f"Insert row {i + 1}: ") for i in range(rows)
        )
        try:
            self.dao.add_note(self.current_user, title, content)
            print("Note stored!\n")
        except sqlite3.IntegrityError:
            print("Error while inserting note.")

    def edit_note(self):
        """Edit a note in the database."""
        title = input("Insert note title: ")
        notes: dict[str, Note] = self.dao.get_notes_by(self.current_user)
        note = notes.get(title, None)
        if not note:
            print(f"'{title}' not found.\n")
            return

        rows = note.content.split("\n")
        edit_row = int(
            input(
                "Insert row number to edit " + f"1-{len(rows)}, 0 to cancel: "
            )
        )
        if not edit_row:
            print("Cancelled.\n")
            return

        rows[int(edit_row) - 1] = input("Insert replacement row: ")
        self.dao.edit_note(note.id, "\n".join(rows))
        print("Edit completed!\n")
        return

    def delete_note(self):
        """Delete a note in the database."""
        title = input("Delete note (insert title): ")

        notes: dict[str, Note] = self.dao.get_notes_by(self.current_user)

        note = notes.get(title, None)
        if not note:
            print(f"'{title}' not found.\n")
            return

        self.dao.delete_note(note.id)
        print("Note deleted.\n")

    def exit_notemenu(self):
        """Exit the note menu."""
        print("")
        self.note_menu.enabled = False
        self.handle_menu(self.login_menu)

    def exit(self):
        """Exit the program."""
        self.login_menu.enabled = False
        self.db_conn.disconnect()
        print("\nProgram ending.")


if __name__ == "__main__":
    db_conn = DBConn("notes.db", "setup.sql")
    app = Main(db_conn)
    app.handle_menu(app.login_menu)
