"""
Helper for the DVC exercise in
lecture_notes/1_version_control/3_exercise.ipynb.

Creates the file 'movies_2018.csv' which contains
all distinct movies titles from 2018-01-01 until
{arg}-12-31, where arg is the first argument that
is provided to this program when it is run.

Program should be run from the root directory of
the project using `python3 -m dsc.version_control.exercise_dvc YYYY`
"""
if __name__ == "__main__":
    import sqlite3
    import sys

    import pandas as pd

    until = sys.argv[1]
    connection = sqlite3.connect("data/dsc.db")
    cursor = connection.cursor()
    output = "data/movies_2018.csv"

    def execute_query(query: str):
        return pd.read_sql_query(query, connection)

    movies = execute_query(
        f"""
        SELECT DISTINCT(title)
        FROM broadcast
        WHERE genre = 'Spielfilm'
            AND start_time_agf >= '2018-01-01'
            AND end_time_agf <= '{until}-12-31'
        """
    )

    movies.to_csv(output, index=False)
    print(f"> created {output}, with data until {until}-12-31")
