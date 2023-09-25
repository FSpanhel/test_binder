- [x] lecture_notes/1_version_control/exercise_solution.ipynb -> should the students make a merge request? the should add their initial at the beginning of an issue? and do everything in their name folder? -> For now, let's only do this for the first exercise because it gets too annoying if I do this for each exercise. But maybe for 2.4./ 2.5 it makes sense?
- [x] build lecture_notes/1_version_control/exercise_3.ipynb



- [x] finish ecture_notes/1_version_control/1_git.ipynb
  - [x] Atomit commit exercise
  - [x] Branches
  - [x] Other stuff in Word Doc
- [ ] Update commit_to_hm_branch.py
- [x] Push first initial commit to course and playground
  - [x] Set up GitLab repos
    - [x] Main protected, only I can push


- [x] first_task.md should become 1_exercise.ipynb
- [x] build pdoc -> run this later on the branch that is pushed for the students
- [ ] Try software install with Isabella  
- [ ] Check binder
- [ ] Presenter kaufen
- [ ] Whiteboard + Studierende den Gruppen zuordnen

- [x] rename lecture_notes/1_version_control to lecture_notes/2_version_control
- [x] Rename lecture_notes/3_code/0_python_guidelines_and_tools.ipynb to lecture_notes/3_code/0_python_standards_and_tools.ipynb
- [x] Put lecture_notes/4_collaboration_and_project_management to archive



- [x] conda install windows, path not found
- [x] how to activate the environment
- [x] add style for rise
- [x] update 0.0 use wsl!
- [x] Add more to versioning Jupyter notebooks
- [x] exercise 2.4 is not that good
- [x] 3_exercise_with_solution.ipynb
- [x] dsc.db auf .gitignore

- [x] evtl noch script für 3.2.3 exercise
- [x] vorlesung durchsprechen und check
- [x] commit und dann dvc notebook laufen lassen und commit
- [x] push
- [x] browser aufräumen
- [ ] presenter holen
- [ ] studenten sollen PATH="" mal setzen

# optional
- [ ] md aus lecture machen und auf gitlab verfügbar machen
- [ ] figures verkleinern bzw width entfernen bevor zu markdown konvertieren

# Learnings:
- I need to set toc:sideBar to false in the notebook meta data so that the toc is displayed correcty!
      "toc_position": {
        "height": "734px",
        "width": "360px",
        "left": "0px",
        "top": "200px"
      },
- I can add a custom nb configuration to a repo as described in nbconfig/_README.md
- https://stackoverflow.com/a/76956283

conda vars:
in der lock env file:
variables:
  JUPYTER_CONFIG_DIR: /home/spa0001f/github/teach/dsc_new/.jupyter
but not in environment.yml -> can not specify here



lecture_notes/intro_and_setup
# Einführung -> branch 1-revise-intro
- [x] Sheldon Bild raus und was ich so mache (fachlich ausbilden)
- Update von intro.pynb
- [x] Kurze Einführung in VS Code (install)
- [x] WSL für Windows Nutzer
- Shell Einführung -> Nö
- [x] env installieren -> DONE
- [x] Notebook starten -> TOC wird nicht richtig angezeigt, Browser Problem? -> fixed
- [x] Umstellen des Repos auf Gruppenrepo damit kein Projektlimit, siehe https://doku.lrz.de/gitlab-10332895.html#GitLab-Projektlimit
- [ ] Evtl. sagen dass ChatGPT NLP Leute vertreibt? + Slide einfügen nach Slide 5. DS is very competitive (Bootcamps, Masters), fancy shit, viele Unternehmen sind nicht so weit, Überangebot an Leute die das wollen.
- [x] Add dvc for data:
  - [x] Add to environment.yml
  - [x] Add dvc remotes:
    - Deleted ~/.cache/pydrive2fs/710796635688-iivsgbgsb6uv1fap6635dhvuei09o66c.apps.googleusercontent.com/default.json to reauthenticate, see https://discuss.dvc.org/t/manually-prompt-gdrive-authentication-step/858/4
    - Remote origin is for public data: https://drive.google.com/drive/u/0/folders/15vLYuJslaBGh2ZA_oSYk1lKxqKqiZfgt
    - Remote private is for private data: https://drive.google.com/drive/u/0/folders/1R2vF3ajbP50jOvIyEVwAcISdM68ZcjBJ
    - Consider https://stackoverflow.com/a/76956283 to separate push/pull/status of the remotes



- ES IST echt wichtig das nächste Mal wenn ich den Kurs halte dafür zu sorgen dass alle das notebook im browser mit den table of contents öffnen können
- Viele kennen auch nicht .. oder ., am besten kurz intro zu shell geben
- Studenten kannten ipython nicht, eventuell auch ipython und jupyter console erklären wenn man skripten laufen lässt<p>


# Environments
- Virtual envs zuerst durchnehmen! - why envs in der 1. veranstaltung bzw klonen und conda env mit allen durchgehe + Bei Intro Übersicht über die Kapitel hinzufügen (1. Block Env, Git, Folder) **was ist damit gemeint**
- Evtl. gleich mit mamba durchstarten und nicht mit conda?
- Aufgabe:
- Erstelle Verzeichnis names my_project
- Environment erstellen mit package pandas
- environment.yml erstellen
- Neue Verzeichnis my_project_clone
- Installiere dort environment
- Immer mamba benutzen wenn mamba env create/update benutzt wird. Ansonsten conda (ggf. geht auch mamba, aber nicht immer)

Setup gitlab projects: protect main and MRs for course and playground

# Projects
- Sachen rausschmeißen die ich nicht brauch
  - [ ] 0.1: Audio matching kürzen
  - clustered_answers_1st_quizzie nicht mit den studenten besprechen (nur für mich)
  - 1.0:

lecture_notes/version_control_and_project_management
# Version Control -> branch 2-revise-vc
- 1.0
  - Wieso Git Git heißt weglassen
  - Git-LFS in der Vorlesung überspringen, nur sagen dass wir es nich nutzen weil es mitm remote storage etc. schwierig wird
- Explain jupytext.toml


lecture_notes/code
# Setup Python project


- Rename lecture_notes/introduction into lecture_notes/data_and_projects?
- In der Vorlesung sollen die Studenten die Aufgaben auch schon machen (d.h., bei Git dann gemeinsam rebasen und nicht erst in der Übung)

- Ende with Rebase in the second lecture, continue with interactive Rebase and show how one can edit the notebook and then rebase


- pandas groupby categorical example (bad design choices)
- rename pyscaffold_test to test_project? -> erstmal so lassen, vll. beim nächsten mal
- change requirements for grading and add that a report should be created? or should this be optional?
- [x] rename package to fs_package
- [x] tidy up __main__ of pyscaffold_test
- [ ] does it run when files are not pushed?
  - also report.py -> next time
- - Should Using PyScaffold for setting up your Project be a subsectionn of Structuring your code? Or should I rename this chapter
to code_structure?
- package downgrade so dass nicht read and load schon da sind? -> nicht unbedingt nötig




Bei der Verteilung der Projektgruppen auch nach einer Selbsteinschätzung fragen damit die Gruppen ausgeglichen sind


- In jedes Notebook einen code reference machen mit den commands die man in diesem Kapitel gelernt hat,
das ist gut damit die Studenten sich zurecht finden
- Note: if your script does not run you can use python3 -m pdb [<script>] to debug the script or use vscode
    - https://www.codementor.io/@stevek/advanced-python-debugging-with-pdb-g56gvmpfa
    -  In Jupyter notebooks you can use the magic command %debug



presentation:
**Gut wäre es wenn die Studenten auf die Präsi auch draufschreiben wer welche Folie präsentiert, so dass es für mich klarer ist, wer was vorgestellt hat**

 Improvements:
 - Evtl. Sehb für all channels geben? Und nicht auch TVG für Ausstrahlung?
 - Das nächste mal direkt von Anfang an mit Issues arbeiten wenn es Updates gibt?
 - Evaluation beachtet: Mit der Projektarbeit schon früher anfangen
 - Quatro statt Notebooks benutzen?
 - Bewertung Studenten: Es hat fast nie jemand was zu MRs gesagt, außer Niklas
 - Vll. sollten die Studenten nur mit scikit-learn arbeiten dürfen? Dann lernen sie mehr basics
 - Im DVC Kapitel müssen sie gdrive mit hm.dvc2022@gmail.com teilen und nicht mit spanhel@hm.edu
 - Da es mit Windows Probleme gibt, WSL empfehlen!
 - Evaluation direkt im Kurs machen und nicht online um die Antwortrate zu erhöhen
