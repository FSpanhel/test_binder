- [Purpose](#purpose)
- [Roadmap](#roadmap)
- [Appointments](#appointments)
  - [1. Termin praktischer Teil](#1-termin-praktischer-teil)
  - [2. Termin praktischer Teil](#2-termin-praktischer-teil)
  - [Practical part: 3th Meeting](#practical-part-3th-meeting)
  - [Presentation](#presentation)
- [General remarks](#general-remarks)
- [Issues](#issues)
  - [First issue](#first-issue)
  - [Second issue](#second-issue)


# Purpose
Everything about the project flow and what I should tell the students in each appointment.

# Roadmap
  - November 24 and December 1: Setup, data import and basic feature building.
  - December 8: Setting up cross-validation for a benchmark model and estimating the prediction error.
  - December 15: Optimization of feature creation, model fitting, and cross-validation.
  - December 22: Code modularization and creation of scripts.
  - January 12: Final discussion of open points.

# Appointments
## 1. Termin praktischer Teil
1. In Gruppen zusammengesetzt schon?
2. Ansage dass jetzt der Zeitpunkt ist nicht mitzumachen, eine Person ist schon ausgetreten. Das ist den anderen gegenüber nicht sehr sozial.
   - Data Freakz hat nur 2 Leute (Austritt Cornelius Rottmair), Moritz Kick wäre noch frei
   - Müsst schauen, dass ihr den Zeitplan, den ich empfohlen, habe auch einhaltet. Sonst wird es sehr stressig werden.
3. Workflow besprechen anhand we_get_it_right
  - MR1 und MR2 zeigen
    - MR1:
      - Atomic commits
    - MR2:
      - Wenn MR2 sich auf MR1 bezieht, dann das in der Description benennen
    - Git und GitLab user name sollte der gleiche sein
    - And please add a picture of yourself or an avatar to your GitLab profile

## 2. Termin praktischer Teil
- Nicht overengineeren (Klassen/Test)
- Lieber im Notebook erstmal Skripten, ich hab noch keinen Code im Package gesehen der vermutlich so bestehend bleibt
- Mehr Interaktion auf Gitlab
- Die Hälfte der Leute hat noch gar nichts da aktiv gemacht
- Nicht vergessen MR auf submission zu machen. Wenn ihr das nicht macht und es dann irgendwelche Probleme geben sollte beim MR auf submission, dann ist das nicht mein Problem (ich musste schon manuell was fixen  (force push auf submission, hätte ich auch nicht machen muss aber dann wäre die history sehr viel aufgebläht geworden) weil man sich nicht den workflow gehalten hat)


## Practical part: 3th Meeting
<!-- - Die Studies müssen mehr Speed aufholen -->

## Presentation
Upfront, some information about the presentation that will take place on January 20th.

The presentation of your project should be based on the Git commit history and GitLab issues and merge requests. That is, show (essential) Git commits and GitLab isses/merge requests in the presentation and use them to present the evolution (discussions, decisions, merge requests) of your project.

To explain decisions, e.g., we use feature X but not feature Z, that are not obvious from merge requests or issues, you should use notebooks or snapshots from notebooks.

During the presentation, it should become clear to everyone how the package and the scripts work and what they do.
For instance,
    - What features do you create and how is the training done?
    - How do you predict?
    - How can the workflow of the script be changed? In particular, the time range for training and prediction.


# General remarks
1. If you write "Closes #4 (closed)" in the corresponding MR, then this issue is closed when the branch is merged to the default branch.
   - I would suggest to do this because otherwise it is not clear why this issue has been closed.
   - Moreover, you don't have to close manually.
2. If you want to have a discussion do not just add a comment but start a thread because
   1. A thread can be resolved.
   2. If a thread is resolved, the thread is collapsed and it is clear that the discussion has ended.
   3. Moreover, on the top right you can see how many threads are unresolved.
   4. Before a MR is approved all threads should be resolved.
3. If a MR replaces another MR, refer to the old MR.
4. If there is something for me to see, open a MR or an issue. I can't see if you create a new branch. -> improve formulation


# Issues

## First issue
  - 3 Stufen:
    - Basismodell ohne Formatqualität und Konkurrenz
    - Baismodell mit Formatqualität
    - Konkurrenz
- Rating Landscape:
  - Aggregation der Werte
  - Multistep forecast
  - MA rekursiv erklären
  - Sehb durch Prophet?

## Second issue
As a stakeholder I want descriptive analysis to see how the target variable behaves and its relation to possible features
(pandas report tool as tip)
