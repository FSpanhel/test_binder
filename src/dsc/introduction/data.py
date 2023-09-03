""" Data which is used in /lecture_notes/0_introduction/1_data_and_projects.ipynb"""
import pandas as pd

example_pin = pd.DataFrame(
    {
        "member_id": [1, 1, 1, 1, 1],
        "channel": ["No-TV", "ARD", "P7", "RTL", "No-TV"],
        "start": [
            pd.Timestamp("2020-01-01 03:00:00"),
            pd.Timestamp("2020-01-01 14:12:00"),
            pd.Timestamp("2020-01-01 18:00:00"),
            pd.Timestamp("2020-01-01 20:00:01"),
            pd.Timestamp("2020-01-01 23:30:00"),
        ],
        "end": [
            pd.Timestamp("2020-01-01 14:11:59"),
            pd.Timestamp("2020-01-01 17:59:59"),
            pd.Timestamp("2020-01-01 20:00:00"),
            pd.Timestamp("2020-01-01 23:30:01"),
            pd.Timestamp("2020-01-02 02:59:59"),
        ],
    }
)

viewing_duration = pd.DataFrame(
    {
        "member_id": [1, 1, 2, 2],
        "weight": [50, 50, 25, 25],
        "target_group": ["Erw. 14-49"] * 4,
        "channel": ["ARD", "P7", "No-TV", "ARD"],
        "start": pd.DatetimeIndex(
            [
                "2020-01-01 15:00:00",
                "2020-01-01 16:30:00",
                "2020-01-01 15:00:00",
                "2020-01-01 16:00:00",
            ]
        ).tolist(),
        "end": pd.DatetimeIndex(
            [
                "2020-01-01 16:29:59",
                "2020-01-01 16:59:59",
                "2020-01-01 15:59:59",
                "2020-01-01 16:59:59",
            ]
        ).tolist(),
    }
)

viewing_duration["viewing_duration"] = (
    viewing_duration["end"] - viewing_duration["start"] + pd.Timedelta(seconds=1)
)  # noqa

potential = viewing_duration.drop_duplicates(subset=["member_id"])["weight"].sum()
