"""
`python3 put_emails_into_csv students_Data_Science_Challenge.csv`
extracts the emails of `students_Data_Science_Challenge.csv` and puts
them into `email.csv`.
"""
import os
import sys

import pandas as pd

if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(sys.argv[1]), "email.csv")
    (
        pd.read_csv(sys.argv[1], delimiter=";")
        .filter("Email")
        .to_csv(output_path, index=False, header=False)
    )
    print(f"> {output_path} created")
