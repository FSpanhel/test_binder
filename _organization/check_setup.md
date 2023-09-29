# Check installation
*Install mambaforge* -> Isabella or Docker
install_mambaforge.sh

*Clone the course repo* -> RUNS
git clone git@gitlab.lrz.de:dsc/2023/course.git

*Clone the playground repo* -> RUNS
git clone git@gitlab.lrz.de:dsc/2023/playground.git

*Build env* -> RUNS
mamba env update -f environment.yml --prune

*Configure notebook* -> RUNS

*Database* -> RUNS
Does lecture_notes/0_introduction/2_exercise.ipynb run?
The first version of the database is until 2019-12-31

*Get data* -> RUNS
Login as spanhelhm@gmail.com into Google.
dvc pull

*Start notebook from dsc environment and check whether it runs*
0_introduction -> RUNS
1_collaboration_and_project_management -> RUNS
2_version_control -> dvc chapter not checked, but RUNS otherwise. Maybe split 1_git.ipynb into several notebooks?
