query = """
SELECT
    -- ########
    -- ausstrahlungs-ebene
    -- ########
    -- aus.run_key,
    -- g2c.ID_PROMAMS,  -- entspricht A_ID
    cdm.A_ID, -- Eindeutige Nummer (Primärschlüssel) der Datenbank AnalyticsCube. Die Ausstrahlung ist die unterste für uns relevante Ebene einer in ProMams angelegten Plan- bzw. Ist-Lizenz oder eines Plan- bzw. Ist-Contents. Beispielsweise ist es im Falle eines Spielfilms ein Run/Ausstrahlung des Films selbst, bei einer Serie ist es ein Run/Ausstrahlung der Episode.
    cdm.A_BESTSELLER_WIEVIELTE, -- Dieses Feld zählt die interne chronologische Ausstrahlungsreihenfolge der Content-ID innerhalb der aktuellen TVD Free-TV Sender durch, unabhängig von den Verträgen
    cdm.A_CONTENTAUSSTRAHLUNG_WIEVIELTE_FREE_TV, -- Sollen die Studenten das selbst erstellen? Erfassung die wievielte Free TV Ausstrahlung des Contents es ist. Die Erfassung erfolgt inkl. Konkurrenzdaten, aber unterschiedliche Erfassungskriterien (z.B. Erfassung nur gewisser Sender, bei RTL II wird nur Content in der PrimeTime erfasst etc.)

    -- ########
    -- content/episoden-ebene (ein content kann mehrmals ausgestrahlt erden), diese ebene gibt es nicht in der bidb
    -- ########
    cdm.C_ID, -- eindeutige Nummer des Content; UJ: ProMams hat eine Dimension Content. Content ist die unterste für uns relevante Ebene eines Formats. Im Falle eines Spielsfilms ist es der Film selbst, bei einer Serie ist es die Episode
    -- g2c.CONTENT_ID_PROMAMS,  -- entspricht C_ID
    cdm.C_CONTENT,  -- ist der jeweils aktuelle Haupttitel eines Content, am Schluss dann der Titel, unter dem die Produktion gesendet wird (Format: Artikel nachgestellt, außer bei Episoden). Der Haupttitel kann sich ändern, es gibt aber zu jedem Zeitpunkt senderübergreifend nur einen eindeutigen Haupttitel pro Content.
    cdm.C_ORIGINALTITEL, -- Ist der Contenttitel der ersten bekannten Aufführung (Format: Artikel nachgestellt, außer bei Episoden). Außerdem Titel in der Originalsprache der Produktion. Titel, den der Lizenzgeber als Originaltitel definiert.
    cdm.C_AUFLISTREIHENF,  -- Einordnung einer Episode innerhalb einer Serie mit Hilfe einer aufsteigenden Nummer; UJ: Festgelegte Reihenfolge von Episoden innerhalb einer Serie

    -- #########
    -- staffel-ebene
    -- #########
    -- aus.titel,  -- raus weil aus
    -- aus.TITELID,  - raus weil aus
    cdm.C_SERIE, -- Brauch ich vermutlich nicht aus.titel die Info schon hat (?) Dies ist der Serientitel wie er von ProMams für die Ausstrahlung des Contents ausgewiesen wird. Entspricht dem Serientitel der Ausstrahlung.
    cdm.C_SERIE_ID, -- Brauch ich vermutlich nicht da aus.titleid die Info schon hat (?) Eindeutige Nummer der Serie. Fasst Episoden, Staffeln, Piloten oder Serienspecials zusammen.

    cdm.C_PRODUKTIONSSTAFFEL_STAFFEL_NR, -- Beschreibt numerisch um welche Staffel es sich handelt. Bei Redaktion Info & Magazine und Nachrichten werden hier die Jahreszahlen hinterlegt
    cdm.C_PRODJAHR_VON,  -- Jahr des Produktionsbeginns
    cdm.C_SERIE_KATEGORIE, -- Die Serien Kategorie ist die strukturelle Bezeichnung einer Content Serie.  Für den Content Datamart sind folgende Werte enthalten "Gameshow"; "Aktuelles"; "TV Movie Reihe"; "News-Magazin"; "Magazin"; "Talkshow"; "Nachrichten-Serie"; "Sport"; "Reportage"; "Nachrichten"; "Lizenzprogramm-Neutral-Serie"; "TV Movie"; "Dokumentation"; "Dauerwerbesendung"; "Spielfilm"; "Zeichentrick", "Serie"; "Show"; "Sondersendung-Serie"; "Teleshopping".
    -- cdm.C_Produktionsstaffel_ID, -- Brauch ich vermutlich nicht, da ich mir diese id auch zusammenbauen kann -- Eindeutige ID für Staffeln in ProMams. In der Contenthierarchie Serien ID - Staffel ID - Content ID.
    -- cdm.C_SERIE_A_NUMMER, -- In diesem Feld wird seit 2017 die Qualität einer Serie beschrieben um daraus die Kategorisierung von Lizenzserien abzuleiten (z.B. Drama A, Sitcom C, etc.)
    cdm.C_ERSTESPRODUKTIONSLAND, -- Land/Staat, in dem sich der Sitz der Produktionsfirma befindet.
    cdm.C_SERIE_VERWENDBARKEIT, -- Kategorisierung von Serien in Serial/Procedural/High Concept/Sitcom. Feld befindet sich auf der Ebene Content/Serie.Die Kategorisierung, ob Serie einen durchgehenden Handlungsstrang (serial) hat oder nicht, beeinflusst die Aufteilung der Anschaffungskosten auf die Anzahl der Runs. Rückfragen zu Einteilung oder fehlenden Einteilung Martin Mötsch oder Asset Valuation Team.
    cdm.C_FSK, -- Einstufung eines Content in eine altersmäßige Freigabe gemäß Einstufung des Verbandes „Freiwillige Selbstkontrolle".
    cdm.C_HOECHSTE_BESUCHERZAHL_D,

    -- #########
    -- LIZENZ-ebene
    -- #########
    cdm.L_ID,
    cdm.A_REDAKTION_BESTOF, -- für nutzungsdauer
    cdm.L_BEGINN, -- simulate
    cdm.L_ENDE, -- simulate
    cdm.L_IST_AUS, -- simulate
    cdm.A_WIEVIELTE, -- Gibt an, um die wievielte Ausstrahlung lt. Abschreibungsgrid innerhalb einer Lizenz es sich handelt. Die wievielte zählt pro Vertrag und beginnt bei einem neuen Vertrag wieder mit 1
    cdm.A_WIEVIELTER_RUN, -- Feld gibt die ausstrahlungsfolge innerhalb einer Lizenz wieder. In der Regel sollte die wievielte und der wievielte Run übereinstimmen, jedoch gibt es bei den kleinen Sendern Ausnahmen, bei denen die Ausstrahlungen "von hinten" abgespielt werden können. Das Feld wird auf der Verbrauchsebene gepflegt und bei Weitergaben fängt die Zählung von vorne an.
    cdm.A_WH -- Ist war A Feld, aber nur für Lizenzbetrachtung relevant und sensibel, deshalb zu Lizenz gepackt: Kurzfristige und kostenfreie Wiederholung im Rahmen der jeweiligen vertraglichen Möglichkeiten

    -- wenn A_WH == 1, dann haben A_WIEVIELE und A_WIEVIELTER_RUN, duplikate (also den gleichen Wert für 2 verschiedene A_IDs), bestseller wievielte is dann Missing für die A_ID wo A_WH == 1 und ansonsten gefüllt


FROM
    BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V cdm
WHERE
    cdm.A_PERSPEKTIVE_VERBRAUCH = 1
    -- AND cdm.A_ID IS NOT NULL -- no effect if used at this place
    AND cdm.A_GENRE_1 IN ('Serie', 'Animation', 'Spielfilm')
"""  # noqa
