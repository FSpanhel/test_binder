# Ablauf

Maximal 10 Minutes questions from me and students: Also during the presentation short questions if something is not clear

Evtl. werde ich dann Fragen/Antworten abwürgen aus Zeitgründen

AM Ende werde ich erst alle meine Fragen stellen, dann ihr

Wenn ihr eine Frage währenddessnen habt, bitte sagen, ich entscheide ob wir die jetzt beantworten oder nicht bzw. sage ggf später

Ihr solltet die 10 Minuten pro Person einhalten


- Ausweiskontrolle
- Bitte auch VS Code öffnen um ggf durch den Code zu führen


# Benotungskritieren:
- Zeit eingehalten (10 +-/2): Gewichtungsfaktor = 40%
    - Abstand >=2 Min -> Note 2
    - Abstand >=4 Min -> Note 3
- Struktur: Gewicht = 20%
- Flüßigkeit: Gewicht = 20%
- Antwort auf Fragen = 20%

# Benotung
Nicklas: 2 (4+10 = 14), vll. 1.7
Lina: 2.7 weil wenig Redeanteil (4 = 4)
Sebastian: 2 (5+7 = 12), vll. 1.7

Luisa 1.7 (eigentlich 1.3 aber halt nur 6.5 , wäre dann konsistent zu den anderen) (1.5 + 5)
Vincent 2, war eigentlich gut, aber wenig Redezeit (5.5 + )
Rami 2 (oder 1.7 weil gute Performance), wenig Redezeit 1.3 (3+3)
Mario 1.3 (13)

Suki 1.3 (8.5)
Max 1.0 (14)
Moritz: 2 (6)

Ivo 1.0 (11 + 2)
Quirin 1.3 (7 + 7)
Max 1.3 (4+ 8)
Giang: 3.3 (3)

Catherine 1.0 (9)
Gregor 1.7 (7)
Mohammed: 2.7 (9) Präsi echt nicht so gut

# Gruppen
## DataFreakz:
Ein Student kam zu spät

Byte Me If U Can:
Ein Student zu spät

## Annormal Distribution:
Nicklas: 2 (4+10 = 14)
Lina: 2.7 weil wenig Redeanteil (4 = 4)
Sebastian: 2 (5+7 = 12)



Schwächste Präsentation aber ingesamt ok

Nicklas: 0-4 Min,
Beginnt mit Einführung. Wie Projekt aufgebaut. Issues labels. Verwenden pre-commit und black. Wollten CI einsetzen, geht drauf ein, deshalb verworfen.
Präsentation etwas holprig, weil nicht vom Redefluss aber vom Browser hin- und herspringen.

Lina: 4-8
SIe hat Organisation gemacht.
Sie hat die README.md gemacht.
-> wenig Redeanteil

Sebastian: 8-13
Hat TVG Verlauf gezeigt. Auf Rückfrage wieso das relevant ist, keine überzeugende Antwort aber okay

Repeat Spalte aus broadcast genommen -> sinnvoll

PT 20-22, sie haben das einfach so entschieden ohne mit mir abzusprechen.

Niklas: 13-23
Führt durch das Notebook mit deskriptiven Analysen durch
Schon wieder MA vor Feiertag oder nach Feiertag angeschaut, habe gesagt, dass das nur bei TVG sinnvoll wäre

Wieso 2 Modelle? Weil sie die Zeit hatten beiden mal auszuprobieren

Führt durch Notebook durch was NN trainiert
Kommt auf MSE von 5

Führt durch Script durch
Validierung zufällig gewählt, auch wenn das besprochen wurde, hat das hier auch noch mal bestätigt
Prediction funktioniert nicht in der Live Demo

Sebastian: 23 -
Hat ein lineares Modell gewählt
Man kann das Fitten nicht über mehrere Jahre machen, siehe iPhone bild
Ohne Cross Validation ist eigentlich auch Cross Validation, konnte er nicht begründen wieso sie das so nennen
Erklärt Patsy
1. Foto: -2 weil ein Jahr test und val
MAE von 2
Auswahl der Feature: Stepwise forward. Einmal im Notebook gemacht worden

Kein Fazit am Ende
Fußnotentitel teilweise Nachhaltigkeit und KI

Questions: Review
According to the presentation they consider E 14-49 as target group.
Train and predict: Why inner join of tables?
PT 20-21 bei neural net
PT 20-22: Anmerkung dass hier dann bei P7 nur den 1. Film

## Fantasticans
Luisa 1.7 (eigentlich 1.3 aber halt nur 6.5 , wäre dann konsistent zu den anderen) (1.5 + 5)
Vincent 2, war eigentlich gut, aber wenig Redezeit (5.5 + )
Rami 2 (oder 1.7 weil gute Performance), wenig Redezeit 1.3 (3+3)
Mario 1.3 (13)

Präsentationsslides schön

Luisa: 0-1:30
Zackig in der Präsentation

Vincent: 1:30-7
Zacking in der Präsentation
Erklärt das Problem mit pyscaffold und dvc. Erklärt schön, dass sie Git-LFS ausprobiert haben und dann verworfen
Auch cool: Weil für das nächste Mal Punkte die man besser machen könnte erwähnt

Rami: 7-10
Gut gemacht
Issue #3
Erst im Notebook ausgetobt,

Mario: 10-23
Issue #10
Erklärt dass Zeitreihenmodell adäquat ist für den Fall
Auch Ausblick was man noch hätte machen können

Q: Trend? Unklar, ob ein deterministischer Trend bei SARIMA modelliert wird. Nur stochastischer Trend über Differenzen
Immer ein Differenzierungsparameter von 2 für alle Modelle

Luisa: 23-28
Sie präsentiert bis jetzt am besten
Issue # 13
Hat gut reagiert auf die Frage was ich bei target_variable denn eingeben kann
Schöne Erklärung des script Workflows
Auch schöne Antwort auf die Frage bzgl. Code Duplizierung in fit.py and predict.py

Rami: 28-31
Erklärt plot script

Questions:
Warum keine Type hints?
So you did use plain START_TIME_AGF for aggregating?
https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/4#note_2198059
https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/4#note_2198046
Model tuning https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/4#note_2198035
Model fiting: https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/4#note_2198024
Config values https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/4#note_2198023
Implicit https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/4#note_2198017

Remarks:
SARIMA Deterministischer Trend wäre gut
Nullkommastellen 1. 2 Stellen okay.

## DataFreakz
Suki 1.3 (8.5)
Max 1.0 (14)
Moritz: 1.3, doch eher nur 2 geben wegen der Zeit (6)


Suki Hong Ngoc Nguyen 0-8:30
Führt schön die Diskussion auf Gitlab auf (am Anfang hat Max mehr mit sich selbst geredert, das hat sich aber dann geändert, von Discord weg)

Max: 8:30- 22:30
Sehr gut, weil er sich die Daten genauer angeschaut hat Fllme ab 20:00 genommen hat und nicht 20:15 wie in Bild 3 von mir genannt
Er hat sich die Daten echt sehr genau angeschaut, was ich gut finde
Keiner hat sich die Daten so genau angeschaut wie er glaube ich
Führt sehr schön über die Schritte durch

Moritz: 22:28
Hat sich um die Doku gekümmert
Wiki nur teilweise fertig
Schließt mit Reflexion ab, sehr gut
Wegen Zeitproblemen wurden fehlenden Zeilen rausgelöscht, sie sind sich dem bewusst

Q:
Könnt ihr das Wiki mal zeigen?
Why do you save the model in /scripts? -> Altlast
You consider all target groups? https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/3#note_2197951
Main script https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/3#note_2197960 -> auch altlast
Ignore loc warning https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/3#note_2197991
Dropping rows of data because on na in kinobesucher https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/3#note_2197992 -> ist sich dem bewusst, Zeitdruck

## We get it right + 2 Minuten
Hier viele Fragen schon während der Präsi von mir
Ivo 1 (11 + 2)
Quirin 1.3 (7 + 7)
Max 1.3 (4+ 8)
Giang: (3) Die schlechtestes bis jetzt, eher so 2.7


Ivo 0-11
EInführung was gemacht wurde und Executive

black wurde eigentlich angewandt, sah aber nicht so aus

Quirin 11- 18
Zeigt Analyse auf

Max: 18 - 22
Start mit seinem Projektverlauf

Ivo: 24 - 26 (+ 2 für Frage)

Quirin: 28
Fehlende Werte werden ausgetauscht -> unklar wie genau

IVo beantwortet alle Fragen:
Wieso Skalierung auf 0/1 -> besserer Vergleich und weil Best Pratice im ML Bereich

Max: 35-43
BAcktest: 1 Jahr Prognose, dann Update
Hat Cross Validation programmiert
Coole Plots
SIe haben auch mehrere Modelle (ARIMA etc) ausprobiert

Giang Pham: 43-46


Q:
Methodenfrage: Was könnte das Problem bei exp Smoothing sein wenn ich einen monotonen Trend habe?
Different signatures https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/5#note_2198406 -> Atrefakt
https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/5#note_2198483
No direct prediction https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/5#note_2198512 -> weiß er nicht, aber okay,


hacky way https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/5#note_2198527 -> wenn man str übergibt
cursor https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/5#note_2198528 -> weil kein pd.DataFrame zurück gegeben sollte

## byte me if you can + 5 Min
Catherine 1.0 (9)
Gregor 1.7 (7)
Mohammed: 2.7 (9) Präsi echt nicht so gut


Catherine 0 - 9
Erzählt von den Anfangschwierigkeiten mit den MR mit 76 Commits
Haben sich dann mehr am Zeitplan orientiert

Gregor hat das initiale große NOtebook mit 3421 Zeilen angelegt was dann das Fundament wurde

Sie haben am Anfang über WhatsApp kommuniziert

Gregor: 9 - 16
nichts zu erwähnen

Sie wollte eigentlich 20 - 23 Uhr festsetzen

Mohammed: 16 - 25
Er ist über den Code drüber gerutscht



Q:
- Movies starting only at 20 https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/2#note_2197839 and
- score https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/2#note_2197908 and https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/2#note_2197916 -> haben sie vergesssen rauszunehmen
- Features https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/2#note_2197924 and below
- Format of time range https://gitlab.lrz.de/fspanhel/dsc_private/-/merge_requests/2#note_2197896
-

Fazit:
- Aussprache Review/Time Series:
- Anmerkung: dt.date statt string
- Git commit history eher wild
- Klassen sollen kein workflow sein, wenn etwas sequentiell gemacht wird dann eher eine Folge von Funktionen
- Modellwahl/tuning automatisiert im Skript, nicht manuell im Notebook
- Generell methodisch noch viel zu machen, lernt man vll. in der Praxis oder später
- Mehr Code Reviews und Diskussion auf Gitlab
- Aufgabe genau lesen und nachfragen (nicht alle Teams haben die Aufgabe bearbeitet)
-
