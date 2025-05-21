from pathlib import Path
import sqlite3

DB_FILEPATH: Path = Path(__file__).parent / "dev.db"
DB_CONN: sqlite3.Connection = sqlite3.connect(DB_FILEPATH)
