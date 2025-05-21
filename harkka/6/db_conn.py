import sqlite3
import sys
from pathlib import Path
from sqlite3 import Connection


class DBConn:
    """Database connection class for SQLite.

    Arguments:
        path (str): Path to the SQLite database file.
        init_scripts (None | str | list[str]): SQL scripts to execute
            during initialization. Can be a single script or a list
            of scripts. If None, no scripts are executed.
    """

    def __init__(
        self,
        path: str = "notes.db",
        init_scripts: None | str | list[str] = None
    ):
        self._path: Path = Path(path)
        self._connection: None | Connection = None
        self._init_scripts: list[str] = []
        if isinstance(init_scripts, str):
            self._init_scripts.append(init_scripts)
        elif isinstance(init_scripts, list):
            self._init_scripts = init_scripts[:]

    @staticmethod
    def load_sql(filepath: str) -> str:
        """Load a SQL script from a file."""
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Failed to read '{filepath}' file.")
            sys.exit(-1)

    def connect(self) -> Connection:
        """Connect to the SQLite database."""
        if self._connection:
            return self._connection
        self._connection = sqlite3.connect(self._path)
        return self._connection

    @property
    def connection(self) -> Connection:
        """Get the current database connection."""
        return self.connect()

    def initialize(self):
        """Initialize the database by connecting and
        executing startup SQL scripts."""
        connection = self.connect()
        with connection:
            cursor = connection.cursor()
            for init_script in self._init_scripts:
                sql = self.load_sql(init_script)
                cursor.executescript(sql)

    def disconnect(self):
        """Disconnect from the database."""
        if self._connection:
            self._connection.close()
            self._connection = None

    def __enter__(self) -> "DBConn":
        self.initialize()
        return self

    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: None | object,
    ) -> bool:
        self.disconnect()
        return True
