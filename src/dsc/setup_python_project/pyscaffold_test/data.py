"""
Query, transform, aggregate, store and load data.
"""


import sqlite3
from os.path import abspath
from typing import List, Optional

import pandas as pd


def query_data_from_db(query: str, path: str) -> pd.DataFrame:
    """
    Returns the result of the query 'query' from  the database 'path' as
    pd.DataFrame.
    """
    connection = sqlite3.connect(path)
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def transform_data(
    df: pd.DataFrame,
    columns2lower: bool = True,
    freq_col: str = "month",
    query: Optional[str] = None,
) -> pd.DataFrame:
    """
    Transforms df.

    Args:
        column2lower: If True, convert all columns of 'df' to lower case.
        freq_col: Must be a string that is a valid attribute of pandas.Series.dt,
            e.g, ['month', 'day_of_week', 'hour', 'quarter', ...].
            Adds the resulting pd.Series as column to 'df'.
        filter_row: If provided, must be a string that is consistent with
            pd.DataFrame.query..

    Returns:
        Transformed dataframe.
    """
    df = df.copy()
    if columns2lower:
        df.columns = df.columns.str.lower()
    df[freq_col] = getattr(pd.to_datetime(df["start_time_agf"]).dt, freq_col)  # type: ignore  # false positive  # noqa
    if query:
        df = df.query(query).copy()
    return df


def mean_target_per_group(
    df: pd.DataFrame,
    group_cols: List[str],
    target: str,
) -> pd.DataFrame:
    """
    Aggregates the column 'target' of 'df' by taking the mean over 'group_cols'.
    """
    df_agg = df.groupby(group_cols)[target].mean().reset_index()
    return df_agg


def store_data(df: pd.DataFrame, path: str) -> None:
    """
    Pickles 'df' as 'path'.
    """
    df.to_csv(path)  # type: ignore  # false positive which is raised because pandas uses internally pd._typing.FilePath as type for path but this is not recognized by the public pandas-stubs # noqa # fmt: skip
    print(f"> Stored data in {abspath(path)}")


def load_data(path: str, subset: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Loads columns 'subset' of 'df' from 'path'.
    """
    return pd.read_csv(path, usecols=subset)
