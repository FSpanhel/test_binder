""" Run from root directory. """
import os
import re
import sqlite3

import pandas as pd

date_regex = r"\d\d\d\d_\d\d_\d\d"


class DataBase:
    """- DataBase.create inserts records from 'self.path2csv' to the sqlite
      database 'self.path'
    - DataBase.connect.query can be used to query the database and
      return the result as pd.DataFrame.
    - Data.close closes the connection.
    """

    def __init__(self, path2csv: str = "./data/csv") -> None:
        self.path2csv = path2csv
        self.path = "./data/dsc.db"
        # required because sqlite3.connect() is still a connection object even if close
        self.connected = False
        self.connection: sqlite3.Connection
        # self.connect()

    def connect(self) -> None:
        """Connects to the database."""
        if self.connected:
            print("> already connected")
        else:
            # self.close()
            try:
                db_exists = os.path.exists(self.path)
                connection = sqlite3.connect(self.path)
            except Exception as e:
                raise e
            else:
                self.connection = connection
                self.connected = True
                if not db_exists:
                    print(f"> created {self.path}")
                print(f"> connected to {self.path}")

    def close(self) -> None:
        """Closes the connection to the database."""
        if self.connected:
            self.connection.close()
            self.connected = False
            print(f"> closed connection to {self.path}")
        else:
            print("> there is no connection")

    def delete(self) -> None:
        """Deletes the database."""
        if self.connected:
            self.close()
        if not os.path.exists(self.path):
            print("> there is no database that can be deleted")
        else:
            os.remove(self.path)
            print(f"> deleted {self.path}")
            self.db_exists = False

    def create(self) -> None:
        """Creates the database with all tables using all files in self.path2csv."""
        if os.path.exists(self.path):
            self.delete()
        self.connect()
        folders = []
        for item in os.listdir(self.path2csv):
            if re.match(date_regex, item):
                folders.append(os.path.join(self.path2csv, item))
        if len(folders) > 0:
            for folder in folders:
                print(f"> reading folder: {folder}")
                self.append_records_from_date_folder(folder)
            print("> done!")
        else:
            print("> no database created")

    def append_records_from_date_folder(self, folder: str) -> None:
        """Append records into the database using a specific folder of self.path2csv."""
        assert self.connected, "> no database connection"
        tables = self._read_tables_from_date_folder(folder)
        for _name, _df in tables.items():
            _df.to_sql(_name, con=self.connection, index=False, if_exists="append")

    def _read_tables_from_date_folder(self, folder: str) -> dict[str, pd.DataFrame]:
        """
        The name of the folder must be a valid date, e.g., folder = './csv/2019_12_31.'
        """
        folder_name = os.path.basename(folder)
        assert re.match(date_regex, folder_name)

        files = [os.path.join(folder, file) for file in os.listdir(folder)]
        assert len(files), "no files to be read"

        tables = {}
        for file in files:
            name, format = os.path.basename(file).rsplit(".", 1)
            if format == "zip":
                tables[name] = self._read_csv(file)
                print(
                    f"> appended {len(tables[name])} records into"
                    " {os.path.join(self.path, name)} until {folder_name}"
                )
            else:
                raise ValueError("format must be zip")
        return tables

    def _read_csv(self, path: str, format_: str = "zip"):
        return pd.read_csv(path, sep=";", compression=format_)  # noqa

    def query(self, query: str):
        return pd.read_sql_query(query, self.connection)


if __name__ == "__main__":
    db = DataBase()
    db.create()
    db.close()
