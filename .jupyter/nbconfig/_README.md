- https://mikkelhartmann.dk/2018/08/02/configuring-jupyter-notebook.html -> How to configure nb extensions.
- By default, the configuration is globally stored in `~/.jupyter/nbconfig/notebook.json`.
- To make a configuration for a specific Git repo, run from the the root of the Git repo
  ```conda env config vars set JUPYTER_CONFIG_DIR=$(pwd)```
  to set the result of `jupyter --config-dir` to the root of the Git repo instead of `~/.jupyter`
- The nb extensions config is read from order `nbconfig/notebook.json` which is located in the the result of  `jupyter --config-dir`.
- Thus, create the file `git_repo/nbconfig/notebook.json` to configure https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions

In order to fix the TOC, I have to set the following in notebook.json:

```
"toc2": {
    "toc_sidebar": false,
    "toc_position": {
    "height": "calc(100% - 180px)",
    "width": "360px",
    "left": "0px",
    "top": "200px"
    },
}
```

Moreover, the following in common.json allows extensions that are not compatible

```
{
  "nbext_hide_incompat": false
}
```
