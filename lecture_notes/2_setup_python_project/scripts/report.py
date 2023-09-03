"""
Creates a very basic Jupyter notebook report.

Input:
    - cfg.prediction: ['storage', 'source']
    - cfg.data: ['feature']
Output:
    - cfg.figure: ['storage]
    - cfg.report: ['storage']
"""
from textwrap import dedent

import cfg
import nbformat
import pandas as pd
from nbconvert.preprocessors import ExecutePreprocessor as EP
from nbformat import NotebookNode
from nbformat import v4 as NB
from nbformat.v4 import new_markdown_cell
from pyscaffold_test_fs.cml import make_docstring_help_description
from pyscaffold_test_fs.data import load_data
from pyscaffold_test_fs.plot import plot_x_vs_yy


def md(text: str) -> NotebookNode:
    return new_markdown_cell(dedent(text))


if __name__ == "__main__":
    make_docstring_help_description(__doc__)
    # -- create plot
    prediction = pd.read_csv(cfg.prediction["storage"])
    data = load_data(cfg.prediction["source"])
    plot = plot_x_vs_yy(data[cfg.data["feature"]], data[cfg.data["target"]], prediction)
    plot.savefig(cfg.figure["storage"])
    print(
        "> Stored figure, which is required for the report, in"
        f" {cfg.figure['storage']}."
    )

    # -- create notebook
    nb = NB.new_notebook()

    nb["cells"] = [
        md(
            f"""
            - To create this report run ```python3 scripts/report.py```.
            - The target is {cfg.data['target']}, the feature is {cfg.data['feature']}.
            - The model is {cfg.model['model'].__name__}.
            """
        ),
        md(
            f"""
            # Visualization of target values and corresponding predictions
            <div>
            <img src="{cfg.figure['storage']}" alt="In-sample prediction" width=1000/>
            <div/>
            """
        ),
    ]

    # -- execute notebook: not required because we only have markdown cells
    if False:
        ep = EP(timeout=600, kernel_namel="pyscaffold_test")
        ep.preprocess(nb)  # , {'metadata': {'path': 'scripts/'}})

    # -- save notebook
    nb_path = cfg.report["storage"]
    with open(nb_path, "w") as f:
        nbformat.write(nb, f)
    print(f"> Report is available at {nb_path}")
