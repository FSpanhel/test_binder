# 1. git
## setup
### set user and email
```bash
git config user.name "fspanhel";
git config user.email "spanhel@hm.edu";
```
### set remotes
https://jigarius.com/blog/multiple-git-remote-repositories
#### origin: fetchtes from and pushes to dsc and pushes to dsc_private
```
git remote add origin git@github.com:FSpanhel/dsc.git;
git remote set-url --add --push origin git@github.com:FSpanhel/dsc.git;
git remote set-url --add --push origin git@gitlab.lrz.de:fspanhel/dsc_private.git;
```
#### hm
```
git remote add hm git@gitlab.lrz.de:dsc/2023/course.git
# git push -f {remote} {target_branch}:main
```

#### p7
```
git remote add p7 git@gitlab.p7s1.io:ent-bi-data-science/dsc_2022.git;
# git fetch && git co p7/p7
```

Note:
- did not succeed to use GitLab for mirroring
    - https://stackoverflow.com/questions/30268549/mirroring-from-gitlab-to-github
    - https://docs.gitlab.com/ee/user/project/repository/mirror/
- use git clone -- mirror can be problematic (there are different suggestions on how to use it)
    - https://www.edwardthomson.com/blog/mirroring_git_repositories.html
    - http://blog.plataformatec.com.br/2013/05/how-to-properly-mirror-a-git-repository/
    - http://web.archive.org/web/20130326122719/http://jefferai.org/2013/03/24/screw-the-mirrors/
-> the best option seems to just add another remote and then push my local stuff (?) using https://jigarius.com/blog/multiple-git-remote-repositories

## view a file from another branch
```bash
git show main:README.md # > readme_from_main.md is also possible
```

## checkout a file from another branch
```
git checkout <branch_name> -- <file_path>
```

## push changes to the remote with the same name you are working on
```bash
git push origin HEAD

git branch -a # List both remote-tracking branches and local branches.
```

## contributors ordered by number of merges:
```bash
git config --global alias.sc 'git shortlog -sn --no-merges'
```

## nice log
https://stackoverflow.com/questions/7853332/how-to-change-git-log-date-formats
https://stackoverflow.com/a/34778736
```bash
git log -n1 --pretty='format:%cd' --date=format:'%a %Y-%m-%d %H:%M:%S'
```

## search in file: you can search in Git even if you aren't sure which commit—or even branch—you made your changes.
```bash
git config --global alias.sf '!git rev-list --all | xargs git grep -F';  # e.g. git sf 'abc'
```

## backup untracked files: https://opensource.com/article/20/10/advanced-git-tips
```bash
git config --global alias.backup '!git ls-files --others --exclude-standard -z |\ xargs -0 tar rvf ./backup-untracked.zip';
```
## interactive add
https://stackoverflow.com/questions/1085162/commit-only-part-of-a-file-in-git?rq=1

# github
- added ssh key https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

-> can not protect branch with free version

# gitlab
https://stackoverflow.com/questions/41782553/meaning-of-allowed-to-push-and-allowed-to-merge-in-gitlab

protect -> https://gitlab.p7s1.io/fspanhel/git_tests/-/settings/repository
https://gitlab.p7s1.io/fspanhel/git_tests/-/settings/repository

main:
- allowed to merge: maintainer (default)  d.h., wenn es kein ff-merge gibt
- allowed to push: maintainer (default) d.h., wenn es ff-merge gibt
-> studenten sollten developer sein, damit sie merge requests erstellen können

für die projekte dann merge approval ändern:
With merge request approval rules, you can set the minimum number of
required approvals before work can merge into your project. You can also extend these
rules to define what types of users can approve work
- 2 approver für dev machen (After a merge request receives the number and type of approvals you configure, it can merge)
- bei main nichts verändern: nur ich kann wieder mergen wenn die branch main protected ist
Settings > Merge requests.

Users with at least the Developer role can create a protected branch.

Ich habe keine Gruppe gemacht damit Studenten nicht später den Code
der anderen sehen können. Projekte sollten deshalb immer geheim sein.


## approval rules
https://gitlab.lrz.de/fspanhel/dsc_private/edit -> add approval rule
https://cityofaustin.github.io/ctm-dev-workflow/protected-branches.html

# git-lfs
sudo apt install git-lfs

# 2. env
conda create -y -n dsc python nb_conda numpy pandas scipy flake8 jupyter jupytext jupyter_contrib_nbextensions mypy rise pyexasol matplotlib

mamba create -y -n dsc python\
numpy pandas scipy matplotlib\
nb_conda jupyter jupytext jupyter_contrib_nbextensions rise pyexasol
flake8 black mypy\
pyscaffold pyscaffoldext-dsproject


% conda requirements non portable over operating systems

# 3. bash
## symbolic link to windows : https://apple.stackexchange.com/questions/2991/whats-the-difference-between-alias-and-link?rq=1
```bash
ln -s /mnt/c/Users/spa0001f/Documents/personal/3_work/5_nebentaetigkeit/fh_muenchen /home/spa0001f/github/dsc/_windows
```
## change permissions
```bash
chmod 755 -R ./data/create/sql
```
## run the program as subprocess
% & to put the program into the background, && to join https://stackoverflow.com/questions/4510640/what-is-the-purpose-of-in-a-shell-command
https://askubuntu.com/questions/1107124/what-is-the-meaning-of-at-the-end-of-a-command

## python -m
https://stackoverflow.com/questions/7610001/what-is-the-purpose-of-the-m-switch

# 3. jupyter notebook
## commands
jupyter notebook list
jupyter notebook stop [port number]

## jupytext
jupytext:
- can open .py files as notebook
- jupytext -diff
- can filter cells by metadata

https://jupytext.readthedocs.io/en/latest/faq.html#i-have-modified-a-text-file-but-git-reports-no-diff-for-the-paired-ipynb-file
The synchronization between the two files happens when you reload and save the notebook in Jupyter, or when you explicitly run jupytext --sync.

automatically save notebook in notebook_as_py subfolder
https://jupytext.readthedocs.io/en/latest/config.html#configuring-paired-notebooks-globally,
echo 'formats = "ipynb,notebook_as_py//py:percent"' >> juptext.toml

## rise
https://www.youtube.com/watch?v=Gx2TnIdt0hw
    - https://youtu.be/Gx2TnIdt0hw?t=1299 -> how to customize rise using css
    - https://youtu.be/Gx2TnIdt0hw?t=2258 -> deck tape might be better for exporting

customization:
    - reveal.js themes:
      - sky, serif (sehr edel), solarized,
      - beige (nicht so cool)
      - moon (too dark)
    - transition: linear, slide
    - slidenumber: h.v (default), c.t.
    - Automatically launch RISE
    - "rise": {"theme": "sky"}
    - "rise": {"autolaunch": true}
    - "rise": {"scroll": true}
    - "rise": {"enable_chalkboard": true}

# vscode
% select python interpreter in vs code


# dbeaver
- formatting: dbeaver/window/preferences/editors/formatting -> formatters, keywords upper case, everthing else lower case
- code folding: https://stackoverflow.com/questions/58886533/how-do-i-enable-or-configure-code-folding-and-side-by-side-text-compare-in-dbe (right click enables line numbers)
- export data: right-click anywhere in the results



# already setup
git clone % insert link here

# hm stuff
## lrz synch and share
- files should not be located in the base folder but a subfolder
- download a client to synchronize files https://syncandshare.lrz.de/download_client




datamart: bis HOECHTEBESUCHERZAHL_D alles drin, erlöse oder kosten nicht, das wäre auch zu sensibel, selbst mit simulation
-
% requirements

# confluence:
- es gibt eduvote (brauche lizenz, bleibe bei patricify)
- es gibt rocketchat statt slack

## prüfung https://conwiki.cc.hm.edu/confluence/pages/viewpage.action?pageId=32645636
- anscheind brauche ich noch einen beisitzer für die mündliche prüfung?

## https://conwiki.cc.hm.edu/confluence/pages/viewpage.action?pageId=184292933
Wo ist der Aufenthaltsraum?
Das sogenannte »Café« im Raum R3.047 dient als eine Art Aufenthaltsraum für die an der Fakultät Beschäftigten. Dort können Sie sich mit Kollegen und Kolleginnen auf ein Gespräch und auf einen Kaffee (oder Tee) treffen.

**Wo ist der Raum für Lehrbeauftragte?**
Da Lehrbeauftragte kein eigenes Büro zugewiesen bekommen, gibt es für sie im 3. Stock einen Arbeitsraum (R3.029) mit zwei Fakultätsrechnern (Anmeldung mit der HM-Kennung). Dort befinden sich auch freie Stromanschlüsse sowie WLAN über eduroam (dazu später mehr), sodass Lehrbeauftragte alternativ auch mit ihrem eigenen Gerät arbeiten können.

Wo ist das Sekretariat?
In R3.045 und R3.046. Die E-Mail-Adresse des Sekretariats lautet: sek-fk07@hm.edu. Telefonisch erreichen Sie das Sekretariat über die Durchwahlen -3700 beziehungsweise -3701.

Wo gibt's Kaffee, Wasser?
Die Küche im Raum R3.048 darf gerne von Ihnen mitgenutzt werden. Dort finden Sie eine Kaffeemaschine, Wasserflaschen sowie Geschirr, einen Kühlschrank, eine Mikrowelle, einen Wasserkocher und einen Geschirrspüler. Der Kaffee sowie das Wasser (aus den Flaschen) werden nicht von der Fakultät gestellt, sondern privat finanziert. Tragen Sie daher bitte ihre entnommenen Mengen an Kaffee (in Tassen) und Wasserflaschen in Liste im Ordner auf dem Sideboard gegenüber der Kaffeemaschine ein. Ihre Einzahlungen (mindestens 5 Euro) tätigen Sie bitte im Vorfeld im Sekretariat. Denn ist die Kasse leer, können kein Kaffee, kein Wasser und keine Milch (und erst recht keine Kekse) nachgekauft werden (traurig).

Büromaterial
Allgemeines Büromaterial (Klebefilm, Stifte, Notizblöcke, ...), das Sie für Ihre Arbeit an der Hochschule benötigen, können Sie sich selbstständig aus den Schränken in R3.047 nehmen. Bitte melden Sie dem Sekretariat, wenn Artikel zur Neige gehen.

Allgemeine Kopier-, Scann- und Druckmöglichkeit
Der R3.042 ist unser Drucker- und Kopierer-Raum. Dort können Sie Drucken, Scannen und Kopieren (auch mit Zusammenheften). Mehr Informationen dazu im Abschnitt Drucker einrichten.

Zugang zur Hochschule außerhalb der Öffnungszeiten
Halten Sie Ausschau nach einem quadratischen Kästchen in der Nähe der Tür und halten Sie Ihre Zugangskarte dagegen – die Tür wird entriegelt. Wenn Sie das bereits abgesperrte Gebäude wieder verlassen wollen, drücken Sie beim Rausgehen am Buchungsterminal zuerst die F1-Taste und halten Sie dann Ihre Karte gegen das Buchungsterminal – die Tür wird entriegelt.

**WLAN**
eduoram: meier55@hm.edu
Besucher, die keinen eduroam-Account haben, können das kostenlose Bayern WLAN nutze
Möglichkeit: Wenn am Dozentenpult eine LAN-Buchse zur Verfügung steht, können Sie auch kabelgebunden eine Verbindung ins Netz herstellen. Voraussetzung dafür ist, dass Sie VPN nutzen (zur Einrichtungsanleitung).



# to do
- I need to add TV-Gesamt to the channels? -> no!
- [x] Should I remove GENRE_2 and GENRE_3 because it is GFK Data? -> yes
- [x] Remove C_ORIGINALTITEL
- [x] Rename C_ID and C_INTERNAL_REPETITION_NUMBER to B_ID and B_INTERNAL_REPETITION_NUMBER
- Simulate license data
- [x] add gfk date and replace start and end time by it
- [ ] do a check for the sql tasks
- [ ] finish project description

- [x] check Ludwigs tools
    - particify
        - https://particify.de/manual/
    - mural (like miro)
- [x] read jupter notebook presentation links
- [x] sqlite tabs abarbeiten -> erstmal beibehalten, werden später noch relevant
- read logging
- check data science mails
- [x] "finish" 0_intro
- version control lecture
    - [x] add quizzie in previous exercise
    - read git links in word doc
    - [x] check out mamba
    - [x] add .zips of dsc to dvc
- gitlab: create group and do them not allow to push -> habe nicht die rechte dazu,
wie kann ich das bei der hm machen? https://docs.gitlab.com/ee/user/group/manage.html
    - generell überlegen ob studis ihre projekte dann auf eine branch hauen oder unter dsc/projects/project_name_aaa usw als git submodule?

- [x] push to gitlab arbeit und dann clonen und gucken ob conda/das package läuft
- [x] was für sachen brauche ich um pip install -e nutzen zu können -> gar nichts anscheinend außer setup.py

- [ ] gitlab:
    - [x] create project + roles + push rules
    - create group for students (?)
    - create project group for project work? use glab
- [ ] moodle -> eher nicht benutzen

- daten
    - [x] Zeit auf 5 Min runden
        - [x] check correctness
    - [x] Sehb mal 1.37 nehmen
    - [x] Check Summe Sehb <= TVG -> Summe Sehb nicht relevant da wir nicht auf Zeitslots agieren, aber vll. ein Problem bei Aggregation auf Monat und Jahr? Vll. Sehb stauchen?
    - x] Sehb und TVG in int casten
        - [x] check correctness
        - [x] adjust 1_data.ipynb
    - [x] als parquet abspeichern? -> hat nicht viel gebracht vom speicherplatz
    - [x] Lizenzdaten simulieren
    - [x] Daten ab 2010? + noch mal laufen lassen für A_ID = B_ID in mapping

TODO:
- evtl. Markdown in die Docu einfügen, vll. in den Ordner Docu nur die Docu reinpacken aber nicht die source files
    - Ich darf dann aber keine Bilder zentieren! -> need to use
    <div align="left" style="font-size:14px;">
    <div/>
    after I used a centering or other stuff!
    - Wie bekomme ich Code Ouput in Markdown? -> use nb_convert
    - Inactive cells does not work with md https://github.com/mwouts/jupytext/issues/688
    - height sollte auf 0 sein wenn ich zu markdown konvertiere weil embed_website nicht geht

- [x] nicht alle daten schon hochladen!
- [x] csv hochladen als backup
- [x] 2 Stunden im ZPA und Gitlab noch hinzufügen
- [x] link für dsc.db sharen und einfügen in präsi
- [x] dsc.db hochladen
- [x] fußnote data_1
    - davor py_script umbenennen weil es sonst probleme gibt oder metadata direkt in notebook bearbeiten
- [x] exercise
- [x] repo pushen
- [x] tabs abspeichern



- [x] Daten neu erzeugen
    - [x] ROUND C_HIGHEST_NUMBER_OF_VISITORS_GERMANY
    - [x] Wieso fangen die Daten nicht um 3 Uhr früh an? -> doch machen sie, es ist nur so dass 01.01.2012 0:00 ja dann schon der 2. Januar ist!
        - Komisch, weil ich auch mit Datum abrufe
        - START_TIME = STARTZEIT_TS_DR
        - START_TIME_AGF = STARTZEIT_TS
    - [x] Evtl. brauche ich noch Season title -> habe SERIE_ID und SERIES_ID hinzugefügt
    - [x] rename mapping_gfk_cdm to mapping_agf_cdm -> ein anderes mal
    - [x] zu data_1 hinzufügen dass AGF TIME auf 5 Minuten gerundet
- [x] exercise fertig machen
    - [x] auch mit python drauf zugreifen?
    - [x] In blöcke aufspalten
    - [ ] Optionale Aufgaben für die Nerds (werden wir hier nicht besprechen, lösung gibt es trotzdem)
        - recode START_TIME_AFG in the true START_TIME
        - What is the first broadcast in the data set?
- [x] Quizzie aufbereiten

- [ ] Evtl. noch Marktanteile eines Senders nach Zielgruppe anzeigen lassen?


https://stackoverflow.com/a/61537392
It is important to note that pip uninstall can not uninstall a module that has been installed with pip install -e


- [ ] render doc on gitlab https://stackoverflow.com/questions/55595323/can-i-render-html-on-gitlab


1. Updates (pulled das repo), Fragen, Agenda,
2. http://localhost:8888/notebooks/dsc/lecture_notes/0_introduction/clustered_answers_to_1st_quizzie.ipynb
3. Runterladen der neuen Datei! -> in 1_data updaten
4. Review http://localhost:8888/notebooks/dsc/lecture_notes/0_introduction/1_data.ipynb

# Exercise
6. http://localhost:8888/notebooks/dsc/lecture_notes/0_introduction/2_exercise.ipynb
7. http://localhost:8888/notebooks/dsc/lecture_notes/0_introduction/2_exercise_solution.ipynb

# VC
8. http://localhost:8888/notebooks/dsc/lecture_notes/1_version_control/0_intro.ipynb
9. http://localhost:8888/notebooks/dsc/lecture_notes/1_version_control/1_git.ipynb




# copy from windows to dsc


[x] MATCH intro_0 dsc und dsc22!!!!!!!

conda env export -n my_ds_project -f environment.lock.yml

Idee: jedes team erzeugt eine branch mit dem team_namen und dort einen
ordner dsc/projects/team_name.
Ich werde die branch protected so dass dort nur mittels PR etwas gemerged werden kann.
Für die Entwicklung nutzt die branch team_name/dev. Von dieser branch sollte hier
dann PRs auf die branch team_name machen.
Ihr könnt euch sonst so viele lokale oder remote branches (z.B. team_name/member_name) erstellen wie ihr wollt.

Für die Code bewertung ist die branch mit eurem team_namen und der entspreched ordner
dsc/projects/team_name relevant.


2 approvals bei gruppe

branch names:
main
dev - your currently best model, should be runnable
issue_number

fork a repo = copy a repo with a different namespace on github

sagen, dass ich keine sprechstunde habe, bzw. nach der übung
dafür auch bitte mail schreiben damit ich das einrichten kann



2 approvals bei gruppe

branch names:
main
dev - your currently best model, should be runnable
issue_number

fork a repo = copy a repo with a different namespace on github

sagen, dass ich keine sprechstunde habe, bzw. nach der übung
dafür auch bitte mail schreiben damit ich das einrichten kann


jupytext --to md *.ipynb

docs are ignored

4 weg?

Schreiben wie man die Präsi anzeigen kann?
7: auf Markdown verweisen? und documentation read the docs?
repo installieren

https://w3-mediapool.hm.edu/mediapool/media/intranet/lokal/qm_2/formulare_und_vorlagen_1/2018-11-08_Glossar_intern_final.pdf
