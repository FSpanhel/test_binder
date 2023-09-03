# I could also just use one repo by using git checkout main file


# copy files to dsc_2022: wd = dsc

# ---- 0
# yes | cp -r lecture_notes/0_introduction/figures ../dsc_2022/lecture_notes/0_introduction/;
python3 -m dsc.notebook_parser lecture_notes/0_introduction/2_exercise_solution.ipynb
yes | cp lecture_notes/0_introduction/0_intro.ipynb ../dsc_2022/lecture_notes/0_introduction;
yes | cp lecture_notes/0_introduction/1_data_and_projects.ipynb ../dsc_2022/lecture_notes/0_introduction;
yes | cp lecture_notes/0_introduction/2_exercise.ipynb ../dsc_2022/lecture_notes/0_introduction;
yes | cp lecture_notes/0_introduction/rise.css ../dsc_2022/lecture_notes/0_introduction;

yes | cp data/dsc.db ../dsc_2022/data;

yes | cp lecture_notes/0_introduction/2_exercise_solution.ipynb ../dsc_2022/lecture_notes/0_introduction;


# ---- 1
# exercise without solution
python3 -m dsc.notebook_parser lecture_notes/1_version_control/3_exercise_solution.ipynb False;
#
yes | cp -r lecture_notes/1_version_control/figures ../dsc_2022/lecture_notes/1_version_control/ &&
yes | cp lecture_notes/1_version_control/0_intro.ipynb ../dsc_2022/lecture_notes/1_version_control &&
yes | cp lecture_notes/1_version_control/1_git.ipynb ../dsc_2022/lecture_notes/1_version_control &&
yes | cp lecture_notes/1_version_control/2_dvc.ipynb ../dsc_2022/lecture_notes/1_version_control &&
yes | cp lecture_notes/1_version_control/3_exercise.ipynb ../dsc_2022/lecture_notes/1_version_control &&
yes | cp lecture_notes/1_version_control/rise.css ../dsc_2022/lecture_notes/1_version_control

# package
yes | cp src/dsc/version_control/git.py ../dsc_2022/src/dsc/version_control/ &&
yes | cp src/dsc/version_control/exercise_git.py ../dsc_2022/src/dsc/version_control/

# solution
yes | cp src/dsc/version_control/exercise_dvc.py ../dsc_2022/src/dsc/version_control/
yes | cp lecture_notes/1_version_control/3_exercise_solution.ipynb ../dsc_2022/lecture_notes/1_version_control


# copy files to dsc: wd = dsc_2022
# yes | cp -r ../dsc_2022/lecture_notes/ .;

# ----- 2
yes | cp -r lecture_notes/2_setup_python_project/figures ../dsc_2022/lecture_notes/2_setup_python_project/ &&
yes | cp lecture_notes/2_setup_python_project/0_intro.ipynb ../dsc_2022/lecture_notes/2_setup_python_project &&
yes | cp lecture_notes/2_setup_python_project/1_virtual_envs_and_packages.ipynb ../dsc_2022/lecture_notes/2_setup_python_project &&
yes | cp lecture_notes/2_setup_python_project/2_python_project.ipynb ../dsc_2022/lecture_notes/2_setup_python_project &&
yes | cp lecture_notes/2_setup_python_project/rise.css ../dsc_2022/lecture_notes/2_setup_python_project

# code structure
yes | cp -r lecture_notes/2_setup_python_project/code_structure/* ../dsc_2022/lecture_notes/2_setup_python_project/code_structure

# dsc package
# yes | cp -r src/dsc/setup_python_project/* ../dsc_2022/src/dsc/setup_python_project/
yes | cp src/dsc/setup_python_project/virtual_environment.py ../dsc_2022/src/dsc/setup_python_project/ &&
yes | cp src/dsc/setup_python_project/sys_path.py ../dsc_2022/src/dsc/setup_python_project/

# pyscaffold_test package
yes | cp -r src/dsc/setup_python_project/pyscaffold_test ../dsc_2022/src/dsc/setup_python_project

# scripts
yes | cp -r lecture_notes/2_setup_python_project/scripts/* ../dsc_2022/lecture_notes/2_setup_python_project/scripts

# solution -> do not copy notebook_as_script
# package: data, model, plot
# code_structure: 1, 2, 3 companion_module
yes | cp -r lecture_notes/2_setup_python_project/code_structure ../dsc_2022/lecture_notes/2_setup_python_project

# pyscaffold_test
# cp -r lecture_notes/2_setup_python_project/code_structure ../pyscaffold_test/notebooks

python3 -m dsc.setup_python_project.pyscaffold_test

tox -e docs && rm -r ../dsc/_windows/pyscaffold_test && cp -r docs/_build/html ../dsc/_windows/pyscaffold_test

# ---------3
yes | cp -r lecture_notes/3_code/1_python_guidelines_and_tools.ipynb ../dsc_2022/lecture_notes/3_code

# ------ 4
yes | cp -r lecture_notes/4_collaboration_and_project_management/collaboration_and_project_management.ipynb ../dsc_2022/lecture_notes/4_collaboration_and_project_management
yes | cp -r lecture_notes/4_collaboration_and_project_management/figures ../dsc_2022/lecture_notes/4_collaboration_and_project_management
