import broadcast
import cdm
import target_group

query = f"""
SELECT
    -- ## broadcast
    aus.run_key,  -- need to transform this
    titel,
    sender,
    startzeit_ts,
    endezeit_ts,
    startzeit_ts_dr,
    endezeit_ts_dr,
    wochentag,
    dauer,  -- in seconds (?)
    titelid, -- need to tranform this!
    genre_1,
    genre_2,
    genre_3,
    WIEDERHOLUNG -- ?
    ,

    -- ## target group
    zg.zielgruppe,
    zg.sehb,
    zg.tvg
    -- zg.sehd
    ,

    g2c.ID_PROMAMS,

    -- ## cdm
      -- ## ausstrahlungs-ebene
    cdm.A_ID, -- Eindeutige Nummer (Primärschlüssel) der Datenbank AnalyticsCube. Die Ausstrahlung ist die unterste für uns relevante Ebene einer in ProMams angelegten Plan- bzw. Ist-Lizenz oder eines Plan- bzw. Ist-Contents. Beispielsweise ist es im Falle eines Spielfilms ein Run/Ausstrahlung des Films selbst, bei einer Serie ist es ein Run/Ausstrahlung der Episode.
    cdm.A_BESTSELLER_WIEVIELTE, -- A_INTERNAL_REPETITION_NUMBER Dieses Feld zählt die interne chronologische Ausstrahlungsreihenfolge der Content-ID innerhalb der aktuellen TVD Free-TV Sender durch, unabhängig von den Verträgen
    -- cdm.A_CONTENTAUSSTRAHLUNG_WIEVIELTE_FREE_TV, -- A_REPETITION_NUMBER Sollen die Studenten das selbst erstellen? Erfassung die wievielte Free TV Ausstrahlung des Contents es ist. Die Erfassung erfolgt inkl. Konkurrenzdaten, aber unterschiedliche Erfassungskriterien (z.B. Erfassung nur gewisser Sender, bei RTL II wird nur Content in der PrimeTime erfasst etc.)
    -- ## content/episoden-ebene (ein content kann mehrmals ausgestrahlt erden), diese ebene gibt es nicht in der bidb
    cdm.C_ID, -- eindeutige Nummer des Content; UJ: ProMams hat eine Dimension Content. Content ist die unterste für uns relevante Ebene eines Formats. Im Falle eines Spielsfilms ist es der Film selbst, bei einer Serie ist es die Episode
    cdm.C_CONTENT,  -- ist der jeweils aktuelle Haupttitel eines Content, am Schluss dann der Titel, unter dem die Produktion gesendet wird (Format: Artikel nachgestellt, außer bei Episoden). Der Haupttitel kann sich ändern, es gibt aber zu jedem Zeitpunkt senderübergreifend nur einen eindeutigen Haupttitel pro Content.
    cdm.C_SERIE_ID,
    cdm.C_SERIE,
    cdm.C_ORIGINALTITEL, -- ORIGINAL_TITLE Ist der Contenttitel der ersten bekannten Aufführung (Format: Artikel nachgestellt, außer bei Episoden). Außerdem Titel in der Originalsprache der Produktion. Titel, den der Lizenzgeber als Originaltitel definiert.
    cdm.C_AUFLISTREIHENF,  -- EPISODE_NUMBER Einordnung einer Episode innerhalb einer Serie mit Hilfe einer aufsteigenden Nummer; UJ: Festgelegte Reihenfolge von Episoden innerhalb einer Serie
      -- ## staffel-ebene
    cdm.C_PRODUKTIONSSTAFFEL_STAFFEL_NR, -- SEASON_NUMBER Beschreibt numerisch um welche Staffel es sich handelt. Bei Redaktion Info & Magazine und Nachrichten werden hier die Jahreszahlen hinterlegt
    cdm.C_PRODJAHR_VON,  -- YEAR_OF_PRODUCTION Jahr des Produktionsbeginns
    cdm.C_SERIE_KATEGORIE, -- SERIES_CATEGORY_1 Die Serien Kategorie ist die strukturelle Bezeichnung einer Content Serie.  Für den Content Datamart sind folgende Werte enthalten "Gameshow"; "Aktuelles"; "TV Movie Reihe"; "News-Magazin"; "Magazin"; "Talkshow"; "Nachrichten-Serie"; "Sport"; "Reportage"; "Nachrichten"; "Lizenzprogramm-Neutral-Serie"; "TV Movie"; "Dokumentation"; "Dauerwerbesendung"; "Spielfilm"; "Zeichentrick", "Serie"; "Show"; "Sondersendung-Serie"; "Teleshopping".
    cdm.C_ERSTESPRODUKTIONSLAND, -- COUNTRY_OF_PRODUCTION Land/Staat, in dem sich der Sitz der Produktionsfirma befindet.
    cdm.C_SERIE_VERWENDBARKEIT, -- SERIES_CATEGORY_2 Kategorisierung von Serien in Serial/Procedural/High Concept/Sitcom. Feld befindet sich auf der Ebene Content/Serie.Die Kategorisierung, ob Serie einen durchgehenden Handlungsstrang (serial) hat oder nicht, beeinflusst die Aufteilung der Anschaffungskosten auf die Anzahl der Runs. Rückfragen zu Einteilung oder fehlenden Einteilung Martin Mötsch oder Asset Valuation Team.
    cdm.C_FSK, -- Einstufung eines Content in eine altersmäßige Freigabe gemäß Einstufung des Verbandes „Freiwillige Selbstkontrolle".
    cdm.C_HOECHSTE_BESUCHERZAHL_D, -- highest number of visitors germany
      -- ## lizenz-ebene
    cdm.L_ID,
    cdm.A_REDAKTION_BESTOF, -- für nutzungsdauer -> brauche ich nicht?
    cdm.L_BEGINN, -- simulate
    cdm.L_ENDE, -- simulate
    cdm.L_IST_AUS, -- simulate
    cdm.A_WIEVIELTE, -- Gibt an, um die wievielte Ausstrahlung lt. Abschreibungsgrid innerhalb einer Lizenz es sich handelt. Die wievielte zählt pro Vertrag und beginnt bei einem neuen Vertrag wieder mit 1
    cdm.A_WIEVIELTER_RUN, -- Feld gibt die ausstrahlungsfolge innerhalb einer Lizenz wieder. In der Regel sollte die wievielte und der wievielte Run übereinstimmen, jedoch gibt es bei den kleinen Sendern Ausnahmen, bei denen die Ausstrahlungen "von hinten" abgespielt werden können. Das Feld wird auf der Verbrauchsebene gepflegt und bei Weitergaben fängt die Zählung von vorne an.
    cdm.A_WH -- Ist war A Feld, aber nur für Lizenzbetrachtung relevant und sensibel, deshalb zu Lizenz gepackt: Kurzfristige und kostenfreie Wiederholung im Rahmen der jeweiligen vertraglichen Möglichkeiten

    -- wenn A_WH == 1, dann haben A_WIEVIELE und A_WIEVIELTER_RUN, duplikate (also den gleichen Wert für 2 verschiedene A_IDs), bestseller wievielte is dann Missing für die A_ID wo A_WH == 1 und ansonsten gefüllt

-- A) Broadcasts
FROM ({broadcast.query}) aus

-- B) Target Groups
LEFT JOIN ({target_group.query}) zg
ON
    aus.run_key = zg.run_key

-- C) Content Data Mart
LEFT JOIN (
    SELECT
        run_key, -- alias required because otherwise pyexasol.connect().execute complains because of duplicate columns when I use select * at the beginning
        ID_PROMAMS
    FROM
        BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH
) g2c
ON
    aus.run_key = g2c.run_key
LEFT JOIN ({cdm.query}) cdm
ON
    g2c.ID_PROMAMS = cdm.A_ID

ORDER BY aus.startzeit_ts_dr, aus.sender, zg.zielgruppe
"""  # noqa
