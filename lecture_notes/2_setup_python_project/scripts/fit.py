"""
Load data, transform and store, aggregate and store, fit a model to aggregated
data and store.

Input:
    - cfg.data: ['source', 'sql_query', 'feature', 'target', 'pd_query']
    - cfg.model: ['model']
Output:
    - cfg.data: ['storage_interim', 'storage_processed']
    - cfg.model: ['storage']
"""
import cfg

from dsc.setup_python_project.pyscaffold_test.cml import make_docstring_help_description
from dsc.setup_python_project.pyscaffold_test.data import (
    mean_target_per_group,
    query_data_from_db,
    store_data,
    transform_data,
)
from dsc.setup_python_project.pyscaffold_test.model import store_model

if __name__ == "__main__":
    make_docstring_help_description(__doc__)
    # -- load and transform data
    df = query_data_from_db(query=cfg.data["sql_query"], path=cfg.data["source"])
    df = transform_data(
        df,
        columns2lower=True,
        freq_col=cfg.data["feature"],
        query=cfg.data["pd_query"],
    )
    store_data(df, cfg.data["storage_interim"])

    # -- create data for modeling
    df_agg = mean_target_per_group(df, cfg.data["feature"], cfg.data["target"])
    store_data(df_agg, cfg.data["storage_processed"])

    # -- fit and store model
    y = df_agg[cfg.data["target"]]
    X = df_agg[cfg.data["feature"]]
    Model = cfg.model["model"]

    model = Model().fit(X, y)
    store_model(model, cfg.model["storage"])
