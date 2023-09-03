"""
Load feature for prediction and fitted model, predict new target values.

Input:
    - cfg.prediction: ['source']
    - cfg.data: ['feature']
    - cfg.model: ['storage']
Output:
    - cfg.prediction['storage']
"""
import cfg

from dsc.setup_python_project.pyscaffold_test.cml import make_docstring_help_description
from dsc.setup_python_project.pyscaffold_test.data import load_data
from dsc.setup_python_project.pyscaffold_test.model import load_model, store_prediction

if __name__ == "__main__":
    make_docstring_help_description(__doc__)
    # -- load model and X_predict
    X_predict = load_data(cfg.prediction["source"], [cfg.data["feature"]])
    model = load_model(cfg.model["storage"])

    # -- predict
    prediction = model.predict(X_predict)
    store_prediction(prediction, cfg.prediction["storage"])
