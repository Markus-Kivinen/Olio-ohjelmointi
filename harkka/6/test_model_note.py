import locale
from datetime import datetime
from hashlib import md5

from db_conn import DBConn
from model_note import Note, NoteDAO


def fetch_all_notes_and_users(
    db_conn: DBConn,
) -> tuple[
    list[tuple[int, str, str, int]], list[tuple[int, str, str, int, int]]
]:
    """Fetch all notes and users from the database."""
    cursor = db_conn.connection.cursor()
    notes: list[tuple[int, str, str, int]] = cursor.execute(
        "SELECT * FROM note"
    ).fetchall()
    users: list[tuple[int, str, str, int, int]] = cursor.execute(
        "SELECT * FROM user"
    ).fetchall()
    return notes, users


def group_notes_by_user(
    notes: list[tuple[int, str, str, int]],
    users: list[tuple[int, str, str, int, int]],
) -> dict[str, list[Note]]:
    """Group notes by user."""
    notes_by_user: dict[str, list[Note]] = {}
    # Map user_id to username
    user_map: dict[int, str] = {user[0]: user[1] for user in users}

    for note in notes:
        note_object: Note = Note(*note)
        username: str = user_map.get(note_object.user, "Unknown User")
        notes_by_user.setdefault(username, []).append(note_object)

    return notes_by_user


def print_notes_by_user(notes_by_user: dict[str, list[Note]]) -> None:
    """Print all notes grouped by user."""
    print("All notes in the database:")
    for username, note_objects in notes_by_user.items():
        print(f"\n  User: {username}")
        for note in note_objects:
            print(" ", note)


def format_timestamp(timestamp: int) -> str:
    """Convert a Unix timestamp to a human-readable date string.
    The format is based on the system locale."""
    locale.setlocale(locale.LC_TIME, "")
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def print_all_users(users: list[tuple[int, str, str, int, int]]) -> None:
    """Print all users in the database."""
    print("\nAll users in the database:")
    for user in users:
        created_at = format_timestamp(user[3])
        updated_at = format_timestamp(user[4])
        print(
            f"  id: {user[0]}, name: {user[1]}, password: {user[2]}, "
            + f"created: {created_at}, updated: {updated_at}"
        )


with DBConn("test.db", ["drop_tables.sql", "setup.sql"]) as db_conn:
    note_dao: NoteDAO = NoteDAO(db_conn.connection)
    # demo_user is created in setup.sql
    note_dao.add_note("demo_user", "Unique_note", "hello\nworld")
    note_dao.add_note("demo_user", "duplicate_note", ["Hello", "World"])

    _ = db_conn.connection.execute(
        "INSERT INTO user (name, password) VALUES (?, ?)",
        ("another_user", md5("demo_password".encode()).hexdigest()),
    )
    note_dao.add_note("another_user", "Unique_too", "hello\nMe")
    note_dao.add_note("another_user", "duplicate_note", ["Hello", "Olli"])

with DBConn("test.db") as db_conn:
    notes, users = fetch_all_notes_and_users(db_conn)
    notes_by_user = group_notes_by_user(notes, users)
    print_notes_by_user(notes_by_user)
    print_all_users(users)
