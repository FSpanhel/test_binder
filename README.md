# Data Science Challenge

- This repo provides all materials for this course.
- Information about the course can be found at the [Course Overview](COURSE.md).
- Note that notebooks or programs in this repo should be run in the corresponding [environment](#environment).

## Repo Organization
Description of relevant folders and files:
```
├── AUTHORS.md              <- List of developers and maintainers.
├── CHANGELOG.md            <- Changelog to keep track of updates.
├── CONTRIBUTING.md         <- Guidelines for contributing to this project.
├── COURSE.md               <- Information about the course.
├── LICENSE.txt             <- License.
├── README.md               <- The top-level README.
├── data                    <- Data should be placed here.
├── docs/_build/html        <- Documentation.
├── environment.yml         <- The conda environment file.
├── lecture_notes           <- Contains the lecture notes that will be presented.
├── src/dsc                 <- Python package that is used for this course.
```

## Documentation
Open the [docs](docs/_build/html/index.html) with a browser to see the documentation of this repo.

## Installation
### Cloning
To copy this remote repository to a local repository you need [Git] which should already be installed if you are using a unix-based OS.

If your OS is Windows you can use [WSL] or [Git For Windows].
- I highly recommend to use [WSL].
- You can easily access [WSL] via [VSCode] using the [remote extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).
- Click [here](https://code.visualstudio.com/docs/remote/remote-overview) for more information.


To clone the repo with SSH, run the following command in the terminal.

```sh
git clone git@gitlab.lrz.de:fspanhel/dsc.git
```

See https://docs.gitlab.com/ee/user/ssh.html how to use SSH keys to communicate with GitLab.

Alternatively, you can clone with HTTPS using

```sh
git clone https://gitlab.lrz.de/fspanhel/dsc.git
```


### Environment

In order to set up the necessary environment you need [(mini)conda](https://docs.conda.io/en/latest/miniconda.html) (or [mamba]).

#### Installing miniconda on Linux using the bash shell
- Run
```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh``` in the terminal to download miniconda.
- Run ```bash Miniconda3-latest-Linux-x86_64.sh``` to install miniconda. Press space to scroll down when you read the terms and agree to them by typing 'yes'.
- Close the terminal or run ```source ~/.bashrc```.
- You should now be able to activate conda by typing ```conda activate```.
- If not, try ```conda init``` and then ```conda activate``` again.

#### Creating the environment
- From the root directory of the cloned git repo, you can create the 'dsc' environment by running  ```conda env create -f environment.yml``` in the terminal.
- Setting up the environment takes a while (mamba is much faster).
- You can activate the environment using ```conda activate dsc```.  
- You should always activate the environment when you are working with this Git repo.
- If you are using VS Code you can find [here](https://code.visualstudio.com/docs/python/environments#_work-with-python-interpreters) instructions how to automatically activate the environment when you open the dsc folder with VS Code.

Note: If something like ```python3 -m dsc...``` does not run, please run ```pip install -e .``` from the root of this repo.

## Starting notebook servers
In the terminal, run ```jupyter notebook``` to start a notebook server which can be accessed via a browser.
- To set the notebook extensions, run ```python3 -m dsc.notebook``` in the terminal.
  - If `~/.jupyter/nbconfig/notebook.json` exists already, please edit `~/.jupyter/nbconfig/notebook.json` accordingly by considering `nbconfig.json`.
  - Note that the notebook extensions are only considered the next time you launch a Juypter notebook server.
- To present notebooks located in `lecture_notes/` as slides press alt + r (on Windows). You might need to zoom out so that everything is visible on a slide.

<!-- pyscaffold-notes -->

## Note

This project has been set up using [PyScaffold] 4.3.1.

[conda]: https://docs.conda.io/
[mamba]: https://github.com/mamba-org/mamba
[PyScaffold]: https://pyscaffold.org/
[Git]: https://git-scm.com/
[Git for Windows]: https://gitforwindows.org/
[WSL]: https://learn.microsoft.com/en-us/windows/wsl/install
[VSCode]: https://code.visualstudio.com/
