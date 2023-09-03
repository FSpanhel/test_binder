"""
Very basic configuration that is used for the scripts in this folder.

Instead of a .py-file you can also use configuration files.
I would also suggest to use dataclasses (or related modules) instead of
dictionaries.
"""
from os.path import abspath

from dsc.setup_python_project.pyscaffold_test.cml import make_docstring_help_description
from dsc.setup_python_project.pyscaffold_test.model import SimpleLinearRegression

data = {
    "source": abspath("data/dsc.db"),
    "sql_query": (
        """
        SELECT *
        FROM broadcast
        WHERE genre = 'Spielfilm'
            AND start_time_agf >= '2018-01-01'
            AND end_time_agf <= '2018-12-31'
        """
    ),
    "feature": "month",
    "target": "duration",
    "pd_query": "channel in 'RTL'",
    "storage_interim": abspath("data/interim/data_transformed.csv"),
    "storage_processed": abspath("data/processed/target_feature.csv"),
}

model = {"model": SimpleLinearRegression, "storage": abspath("model.pkl")}

prediction = {"source": data["storage_processed"], "storage": abspath("prediction.csv")}

report = {"storage": abspath("reports/prediction.ipynb")}
figure = {"storage": abspath("reports/figures/in_sample_prediction.png")}

if __name__ == "__main__":
    make_docstring_help_description(__doc__)
