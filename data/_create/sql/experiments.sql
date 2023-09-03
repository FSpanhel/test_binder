SELECT SENDER, ROUND((SUM(SEHB) / SUM(TVG)) * 100, 2) as MARKET_SHARE
FROM (
	SELECT a.SENDER, SEHB, TVG, ZIELGRUPPE FROM
	(SELECT * FROM BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN WHERE DATUM >= '2012-01-01' AND DATUM <= '2019-12-31') a
	LEFT JOIN
	(SELECT * FROM BIDS_UNIVERSE_SOURCE_GFK.ZIELGRUPPEN WHERE DATUM >= '2012-01-01' AND DATUM <= '2019-12-31') z
	ON z.RUN_KEY = a.RUN_KEY
)
WHERE ZIELGRUPPE = 'Erw. 14-49'
GROUP BY SENDER
ORDER BY SENDER DESC;

SELECT C_SERIE_ID, C_SERIE, C_ID, C_CONTENT, C_PRODUKTIONSSTAFFEL_STAFFEL_NR, C_AUFLISTREIHENF, A_BESTSELLER_WIEVIELTE
FROM BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V dcdv
-- WHERE C_ID = 286433
WHERE C_SERIE = 'FUTURAMA'
ORDER BY C_PRODUKTIONSSTAFFEL_STAFFEL_NR, C_AUFLISTREIHENF, A_BESTSELLER_WIEVIELTE
;


-- do we need C_SERIE_ID? ja weil manche serien den gleichen namen haben?
SELECT C_SERIE_ID, COUNT(*)
FROM BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V dcdv
-- WHERE C_ID = 286433
WHERE A_BESTSELLER_WIEVIELTE = 1 AND C_AUFLISTREIHENF = 1 AND A_WIEVIELTE = 1
GROUP BY C_SERIE_ID
;


SELECT C_SERIE_ID, C_SERIE, C_ORIGINALTITEL, C_ID, C_CONTENT, C_PRODUKTIONSSTAFFEL_STAFFEL_NR, C_AUFLISTREIHENF, A_BESTSELLER_WIEVIELTE, A_WIEVIELTE, A_WH, A_DATUM
FROM BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V dcdv
-- WHERE C_ID = 286433
WHERE C_SERIE_ID = 8939
AND A_BESTSELLER_WIEVIELTE = 1 AND C_AUFLISTREIHENF = 1;



/*
#########################################################################
basis abfrage für dsc: aufgebaut auf C:\Users\spa0001f\Documents\personal\3_work\4_p7s1\projekte\business_intelligence\sql\exasol_tests.sql
#########################################################################
*/

SELECT * FROM BIDS_UNIVERSE_SOURCE_MANUELL.FEIERTAGE f;

select
	sender,
	min(datum) as start_ausstrahlung_sender,
	-- date_trunc('MONTH', min(datum)) as first_day_next_month
	-- ADD_MONTHS(DATE date_trunc('MONTH', min(datum)), 1)
from bids_universe_source_gfk.slot_gfk
where
	sehb > 0
group by
    sender


SELECT DISTINCT A_GENRE_1 FROM BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V cdm
SELECT DISTINCT sender FROM bids_universe_source_gfk.ausstrahlungen


-- unterschied datum und datum_real: wenn der sendetag der 13.11 ist und der film nach mitternacht anfängt dann ist datum immer noch der 13.11 aber datum_real der 14.11
SELECT
	DATUM, STARTZEIT, ENDEZEIT, DATUM_REAL, STARTZEIT_TS, STARTZEIT_TS_DR, ENDEZEIT, ENDEZEIT_TS_DR
FROM bids_universe_source_gfk.ausstrahlungen
	WHERE EXTRACT(HOUR FROM STARTZEIT_TS_DR) = 2
	AND EXTRACT(HOUR FROM ENDEZEIT_TS_DR) > 1;

SELECT
	DATUM, STARTZEIT, ENDEZEIT, DATUM_REAL, STARTZEIT_TS, STARTZEIT_TS_DR, ENDEZEIT, ENDEZEIT_TS_DR,
	SUBSTR(STARTZEIT, 10, 10) || '1' time
FROM bids_universe_source_gfk.ausstrahlungen
	WHERE EXTRACT(HOUR FROM STARTZEIT_TS_DR) = 2
	AND EXTRACT(HOUR FROM ENDEZEIT_TS_DR) > 1;

SELECT
	SUBSTR(STARTZEIT, 12, 15),
	DATUM,
	STARTZEIT,
	(DATUM || '-' || SUBSTR(ENDEZEIT,12, 15)) AS ENDEZEIT_TS,
	ENDEZEIT_TS_DR,
	STARTZEIT_TS
FROM bids_universe_source_gfk.ausstrahlungen;

SELECT SUBSTR('abcdef',2, 2) S1,
       SUBSTRING('abcdef' FROM 4 FOR 2) S2
       ;

SELECT 'abc' || 'DEF';


SELECT * FROM BIDS_UNIVERSE_SOURCE_MANUELL.EVENTS e -- bis 2018, könnten studenten dann selbst auffüllen
SELECT * FROM BIDS_UNIVERSE_SOURCE_MANUELL.FEIERTAGE f -- bis 2025
-- SELECT * FROM BIDS_UNIVERSE_SOURCE_MANUELL.SCHULFERIEN s


-- (RUN_KEY; ID_PROMAMS) DUPLIKATE im matching, sollte eigentlich nicht passieren dürfen
SELECT
    run_key,
    ID_PROMAMS
FROM
    BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH
WHERE RUN_KEY = 202012072347421072110641319

---

SELECT COUNT(*)
FROM (SELECT * FROM bids_universe_source_gfk.ausstrahlungen aus
	WHERE
	    aus.datum >= '2015-01-01' AND aus.datum <= '2022-08-31'
	    AND aus.sender IN ('ProSieben', 'SAT.1', 'Kabel Eins', 'VOX', 'RTL', 'RTL_ZWEI', 'ARD Das Erste', 'ZDF')
) aus
LEFT JOIN (SELECT * FROM BIDS_UNIVERSE_SOURCE_GFK.ZIELGRUPPEN
	WHERE
	    ZIELGRUPPE IN ('Erw. 14-49', 'Männer 14-29', 'Männer 30-49', 'Frauen 14-29', 'Frauen 30-49')
) zg
ON
    aus.run_key = zg.run_key
LEFT JOIN (SELECT * FROM BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH) g2c
ON
    aus.run_key = g2c.run_key
LEFT JOIN BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V dcdv
ON
	g2c.ID_PROMAMS = dcdv.A_ID



/*
##########
#########
#########
 */

SELECT
    -- ## broadcast
    aus.run_key,  -- need to transform this
    titel,
    sender,
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
    cdm.C_ORIGINALTITEL, -- ORIGINAL_TITLE Ist der Contenttitel der ersten bekannten Aufführung (Format: Artikel nachgestellt, außer bei Episoden). Außerdem Titel in der Originalsprache der Produktion. Titel, den der Lizenzgeber als Originaltitel definiert.
    cdm.C_AUFLISTREIHENF,  -- EPISODE_NUMBER Einordnung einer Episode innerhalb einer Serie mit Hilfe einer aufsteigenden Nummer; UJ: Festgelegte Reihenfolge von Episoden innerhalb einer Serie
      -- ## staffel-ebene
    cdm.C_PRODUKTIONSSTAFFEL_STAFFEL_NR, -- SEASON_NUMBER Beschreibt numerisch um welche Staffel es sich handelt. Bei Redaktion Info & Magazine und Nachrichten werden hier die Jahreszahlen hinterlegt
    cdm.C_PRODJAHR_VON,  -- YEAR_OF_PRODUCTION Jahr des Produktionsbeginns
    cdm.C_SERIE_KATEGORIE, -- SERIES_CATEGORY_1 Die Serien Kategorie ist die strukturelle Bezeichnung einer Content Serie.  Für den Content Datamart sind folgende Werte enthalten "Gameshow"; "Aktuelles"; "TV Movie Reihe"; "News-Magazin"; "Magazin"; "Talkshow"; "Nachrichten-Serie"; "Sport"; "Reportage"; "Nachrichten"; "Lizenzprogramm-Neutral-Serie"; "TV Movie"; "Dokumentation"; "Dauerwerbesendung"; "Spielfilm"; "Zeichentrick", "Serie"; "Show"; "Sondersendung-Serie"; "Teleshopping".
    cdm.C_ERSTESPRODUKTIONSLAND, -- COUNTRY_OF_PRODUCTION Land/Staat, in dem sich der Sitz der Produktionsfirma befindet.
    cdm.C_SERIE_VERWENDBARKEIT, -- SERIES_CATEGORY_2 Kategorisierung von Serien in Serial/Procedural/High Concept/Sitcom. Feld befindet sich auf der Ebene Content/Serie.Die Kategorisierung, ob Serie einen durchgehenden Handlungsstrang (serial) hat oder nicht, beeinflusst die Aufteilung der Anschaffungskosten auf die Anzahl der Runs. Rückfragen zu Einteilung oder fehlenden Einteilung Martin Mötsch oder Asset Valuation Team.
    cdm.C_FSK, -- Einstufung eines Content in eine altersmäßige Freigabe gemäß Einstufung des Verbandes „Freiwillige Selbstkontrolle".
    cdm.C_HOECHSTE_BESUCHERZAHL_D -- highest number of visitors germany

-- A) Broadcasts
SELECT *
FROM (
SELECT
    aus.run_key, --  as RUN_ID,  -- need to transform this
    titel, -- AS title,
    aus.sender, -- AS channel,
    -- aus.datum, -- evtl. nicht den studenten geben da aus start_time extraierbar
    -- startzeit, -- jahr passt hier nicht
    aus.startzeit_ts_dr, --  AS start_time,
    endezeit_ts_dr, -- AS end_time,
    wochentag, -- AS weekday,
    dauer, -- AS duration,  -- in seconds (?)
    titelid, -- as title_id, -- need to tranform this!
    genre_1,
    genre_2,
    genre_3,
    WIEDERHOLUNG -- ?
FROM bids_universe_source_gfk.ausstrahlungen aus
WHERE
    aus.datum >= '2015-01-01'
    -- AND aus.datum <= '2020-12-31'
    AND aus.datum <= '2022-08-31'
    AND aus.sender IN ('ProSieben', 'SAT.1', 'Kabel Eins', 'VOX', 'RTL', 'RTL_ZWEI', 'ARD Das Erste', 'ZDF')

) aus

-- B) Target Groups
LEFT JOIN (
SELECT
    run_key,
    zielgruppe,
    sehb,
    tvg
    -- sender,
    -- datum,
    -- sehd
    -- , startzeit_ts_dr
FROM
    BIDS_UNIVERSE_SOURCE_GFK.ZIELGRUPPEN
WHERE
    ZIELGRUPPE IN ('Erw. 14-49', 'Männer 14-29', 'Männer 30-49', 'Frauen 14-29', 'Frauen 30-49')

) zg
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
WHERE aus.RUN_KEY = 202012072347421072110641319





LEFT JOIN (
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
    -- cdm.C_SERIE, -- Brauch ich vermutlich nicht aus.titel die Info schon hat (?) Dies ist der Serientitel wie er von ProMams für die Ausstrahlung des Contents ausgewiesen wird. Entspricht dem Serientitel der Ausstrahlung.
    -- cdm.C_SERIE_ID, -- Brauch ich vermutlich nicht da aus.titleid die Info schon hat (?) Eindeutige Nummer der Serie. Fasst Episoden, Staffeln, Piloten oder Serienspecials zusammen.

    cdm.C_PRODUKTIONSSTAFFEL_STAFFEL_NR, -- Beschreibt numerisch um welche Staffel es sich handelt. Bei Redaktion Info & Magazine und Nachrichten werden hier die Jahreszahlen hinterlegt
    cdm.C_PRODJAHR_VON,  -- Jahr des Produktionsbeginns
    cdm.C_SERIE_KATEGORIE, -- Die Serien Kategorie ist die strukturelle Bezeichnung einer Content Serie.  Für den Content Datamart sind folgende Werte enthalten "Gameshow"; "Aktuelles"; "TV Movie Reihe"; "News-Magazin"; "Magazin"; "Talkshow"; "Nachrichten-Serie"; "Sport"; "Reportage"; "Nachrichten"; "Lizenzprogramm-Neutral-Serie"; "TV Movie"; "Dokumentation"; "Dauerwerbesendung"; "Spielfilm"; "Zeichentrick", "Serie"; "Show"; "Sondersendung-Serie"; "Teleshopping".
    -- cdm.C_Produktionsstaffel_ID, -- Brauch ich vermutlich nicht, da ich mir diese id auch zusammenbauen kann -- Eindeutige ID für Staffeln in ProMams. In der Contenthierarchie Serien ID - Staffel ID - Content ID.
    -- cdm.C_SERIE_A_NUMMER, -- In diesem Feld wird seit 2017 die Qualität einer Serie beschrieben um daraus die Kategorisierung von Lizenzserien abzuleiten (z.B. Drama A, Sitcom C, etc.)
    cdm.C_ERSTESPRODUKTIONSLAND, -- Land/Staat, in dem sich der Sitz der Produktionsfirma befindet.
    cdm.C_SERIE_VERWENDBARKEIT, -- Kategorisierung von Serien in Serial/Procedural/High Concept/Sitcom. Feld befindet sich auf der Ebene Content/Serie.Die Kategorisierung, ob Serie einen durchgehenden Handlungsstrang (serial) hat oder nicht, beeinflusst die Aufteilung der Anschaffungskosten auf die Anzahl der Runs. Rückfragen zu Einteilung oder fehlenden Einteilung Martin Mötsch oder Asset Valuation Team.
    cdm.C_FSK, -- Einstufung eines Content in eine altersmäßige Freigabe gemäß Einstufung des Verbandes „Freiwillige Selbstkontrolle".
    cdm.C_HOECHSTE_BESUCHERZAHL_D

/*
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
*/

FROM
    BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V cdm
WHERE
    cdm.A_PERSPEKTIVE_VERBRAUCH = 1
    -- AND cdm.A_ID IS NOT NULL -- no effect if uses at this place
    AND cdm.A_GENRE_1 IN ('Serie', 'Animation', 'Spielfilm')
) cdm
ON
    g2c.ID_PROMAMS = cdm.A_ID


ORDER BY aus.startzeit_ts_dr, aus.sender, zg.zielgruppe

/*
#########################################################################
1) full query (broadcasts, target groups, cube)
#########################################################################
*/


SELECT
	WIEDERHOLUNG, -- ?
	aus.run_key,  -- need to transform this
	title,
	channel,
	aus.datum, -- evtl. nicht den studenten geben da aus start_time extraierbar
	-- startzeit, -- jahr passt hier nicht
	start_time,
	end_time,
	weekday,
	duration,  -- in seconds (?)
	titelid, -- need to tranform this!
	genre_1,
	genre_2,
	genre_3
	,
	zg.target_group AS target_group,
	zg.sehb AS sehb,
	zg.tvg AS tvg,
	zg.sehd AS sehd
	-- zg.sehd / dauer AS bla

-- A) Broadcasts
FROM (
	SELECT
		WIEDERHOLUNG, -- ?
		aus.run_key,  -- need to transform this
		titel AS title,
		aus.sender AS channel,
		aus.datum, -- evtl. nicht den studenten geben da aus start_time extraierbar
		-- startzeit, -- jahr passt hier nicht
		aus.startzeit_ts_dr AS start_time,
		endezeit_ts_dr AS end_time,
		wochentag AS weekday,
		dauer AS duration,  -- in seconds (?)
		titelid, -- need to tranform this!
		genre_1,
		genre_2,
		genre_3
	FROM bids_universe_source_gfk.ausstrahlungen aus
	WHERE
		aus.datum >= '2015-01-01'
		AND aus.datum <= '2020-12-31'
		AND aus.sender IN ('ProSieben', 'SAT.1', 'Kabel Eins', 'VOX', 'RTL', 'RTL_ZWEI', 'ARD Das Erste', 'ZDF')
		-- 'sixx', 'Kabel Eins Doku', 'ProSieben MAXX'
) aus

-- B) Target Groups
LEFT JOIN (
    SELECT
    	zg.run_key,
    	zg.zielgruppe AS target_group,
    	zg.sehb,
    	zg.tvg,
    	zg.sender,
    	zg.datum,
    	zg.sehd,
    	zg.startzeit_ts_dr
    FROM BIDS_UNIVERSE_SOURCE_GFK.ZIELGRUPPEN zg
    WHERE zg.ZIELGRUPPE IN ('Erw. 14-49', 'Männer 14-29', 'Männer 30-49', 'Frauen 14-29', 'Frauen 30-49')
) zg
ON
	aus.run_key = zg.run_key

ORDER BY aus.start_time, aus.channel, zg.target_group

/*
#########################################################################
2) cube/content datamart
#########################################################################
*/
SELECT
    -- ########
    -- ausstrahlungs-ebene
    -- ########
    aus.run_key,
    g2c.ID_PROMAMS,  -- entspricht A_ID
    cdm.A_ID, -- Eindeutige Nummer (Primärschlüssel) der Datenbank AnalyticsCube. Die Ausstrahlung ist die unterste für uns relevante Ebene einer in ProMams angelegten Plan- bzw. Ist-Lizenz oder eines Plan- bzw. Ist-Contents. Beispielsweise ist es im Falle eines Spielfilms ein Run/Ausstrahlung des Films selbst, bei einer Serie ist es ein Run/Ausstrahlung der Episode.
    cdm.A_BESTSELLER_WIEVIELTE, -- Dieses Feld zählt die interne chronologische Ausstrahlungsreihenfolge der Content-ID innerhalb der aktuellen TVD Free-TV Sender durch, unabhängig von den Verträgen
    cdm.A_CONTENTAUSSTRAHLUNG_WIEVIELTE_FREE_TV, -- Sollen die Studenten das selbst erstellen? Erfassung die wievielte Free TV Ausstrahlung des Contents es ist. Die Erfassung erfolgt inkl. Konkurrenzdaten, aber unterschiedliche Erfassungskriterien (z.B. Erfassung nur gewisser Sender, bei RTL II wird nur Content in der PrimeTime erfasst etc.)

    -- ########
    -- content/episoden-ebene (ein content kann mehrmals ausgestrahlt erden), diese ebene gibt es nicht in der bidb
    -- ########
    cdm.C_ID, -- eindeutige Nummer des Content; UJ: ProMams hat eine Dimension Content. Content ist die unterste für uns relevante Ebene eines Formats. Im Falle eines Spielsfilms ist es der Film selbst, bei einer Serie ist es die Episode
    g2c.CONTENT_ID_PROMAMS,  -- entspricht C_ID
    cdm.C_CONTENT,  -- ist der jeweils aktuelle Haupttitel eines Content, am Schluss dann der Titel, unter dem die Produktion gesendet wird (Format: Artikel nachgestellt, außer bei Episoden). Der Haupttitel kann sich ändern, es gibt aber zu jedem Zeitpunkt senderübergreifend nur einen eindeutigen Haupttitel pro Content.
    cdm.C_ORIGINALTITEL, -- Ist der Contenttitel der ersten bekannten Aufführung (Format: Artikel nachgestellt, außer bei Episoden). Außerdem Titel in der Originalsprache der Produktion. Titel, den der Lizenzgeber als Originaltitel definiert.
    cdm.C_AUFLISTREIHENF,  -- Einordnung einer Episode innerhalb einer Serie mit Hilfe einer aufsteigenden Nummer; UJ: Festgelegte Reihenfolge von Episoden innerhalb einer Serie

    -- #########
    -- staffel-ebene
    -- #########
    aus.titel,
    aus.TITELID,
    -- cdm.C_SERIE, -- Brauch ich vermutlich nicht aus.titel die Info schon hat (?) Dies ist der Serientitel wie er von ProMams für die Ausstrahlung des Contents ausgewiesen wird. Entspricht dem Serientitel der Ausstrahlung.
    -- cdm.C_SERIE_ID, -- Brauch ich vermutlich nicht da aus.titleid die Info schon hat (?) Eindeutige Nummer der Serie. Fasst Episoden, Staffeln, Piloten oder Serienspecials zusammen.

    cdm.C_PRODJAHR_VON,  -- Jahr des Produktionsbeginns
    cdm.C_SERIE_KATEGORIE, -- Die Serien Kategorie ist die strukturelle Bezeichnung einer Content Serie.  Für den Content Datamart sind folgende Werte enthalten "Gameshow"; "Aktuelles"; "TV Movie Reihe"; "News-Magazin"; "Magazin"; "Talkshow"; "Nachrichten-Serie"; "Sport"; "Reportage"; "Nachrichten"; "Lizenzprogramm-Neutral-Serie"; "TV Movie"; "Dokumentation"; "Dauerwerbesendung"; "Spielfilm"; "Zeichentrick", "Serie"; "Show"; "Sondersendung-Serie"; "Teleshopping".
    cdm.C_PRODUKTIONSSTAFFEL_STAFFEL_NR, -- Beschreibt numerisch um welche Staffel es sich handelt. Bei Redaktion Info & Magazine und Nachrichten werden hier die Jahreszahlen hinterlegt
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
    -- cdm.A_WIEVIELTER_RUN, -- Feld gibt die ausstrahlungsfolge innerhalb einer Lizenz wieder. In der Regel sollte die wievielte und der wievielte Run übereinstimmen, jedoch gibt es bei den kleinen Sendern Ausnahmen, bei denen die Ausstrahlungen "von hinten" abgespielt werden können. Das Feld wird auf der Verbrauchsebene gepflegt und bei Weitergaben fängt die Zählung von vorne an.
    cdm.A_WH -- Ist war A Feld, aber nur für Lizenzbetrachtung relevant und sensibel, deshalb zu Lizenz gepackt: Kurzfristige und kostenfreie Wiederholung im Rahmen der jeweiligen vertraglichen Möglichkeiten
    /*
    wenn A_WH == 1
    dann haben A_WIEVIELE und A_WIEVIELTER_RUN
    duplikate (also den gleichen Wert für 2 verschiedene A_IDs)
    bestseller wievielte is dann Missing für die A_ID wo A_WH == 1 und ansonsten gefüllt
        */
FROM
    BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN aus
LEFT JOIN
    BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
ON aus.run_key = g2c.run_key
LEFT JOIN
    BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V cdm
ON g2c.ID_PROMAMS = cdm.A_ID
WHERE
    cdm.A_PERSPEKTIVE_VERBRAUCH = 1
    AND cdm.A_ID IS NOT NULL -- useful because this excludes external channels
    AND cdm.A_GENRE_1 IN ('Serie', 'Animation', 'Spielfilm')
	/*
	AND cdm.C_HOECHSTE_BESUCHERZAHL_D IS NOT NULL
	AND aus.GENRE_1 = 'Serie'
	AND aus.TITELID = 1024716
	*/

LIMIT 50



/*
#########################################################################
3) mapping tabelle cube/gfk
#########################################################################
*/

SELECT
	g2c.run_key,
	g2c.ID_PROMAMS AS A_ID, -- A_ID = ID_PROMAMS
	g2c.CONTENT_ID_PROMAMS AS C_ID
FROM BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
LIMIT 100



/*
#########################################################################
OLD STUFF
#########################################################################
 */

SELECT
	s5.datum, s5.startzeit_ts as s5_slot, s5.sender, s5.run_key, s5.zielgruppe
	-- , zg.sehb, zg.tvg
	-- , aus.startzeit_ts_dr, endezeit_ts_dr, aus.wochentag, aus.titel, aus.dauer, aus.titelid, aus.genre_1, aus.genre_2, aus.genre_3
    -- , events.art as event
    -- , feiertage.feiertag
    -- , lr.run_key_lr, lr.runnr, lr.run_key_lr, zg_lr.sehb as sehb_lr, zg_lr.tvg as tvg_lr, zg_lr.startzeit_ts_dr as lr_startzeit_ts_dr
    -- , ma_plan.MA_PLAN_E1449
FROM BIDS_UNIVERSE_SOURCE_GFK.SLOT_5 as s5

-- add Zielgruppen to slot_5
LEFT JOIN (
    SELECT zg.run_key, zg.zielgruppe, zg.sehb, zg.tvg, zg.sender, zg.datum, zg.startzeit_ts_dr
    FROM BIDS_UNIVERSE_SOURCE_GFK.ZIELGRUPPEN zg
    WHERE zg.ZIELGRUPPE IN ('Erw. 14-49', 'M�nner 14-29')
) zg ON zg.run_key = s5.run_key AND zg.zielgruppe = s5.zielgruppe

-- add Ausstrahlungsinfo
LEFT JOIN (
    SELECT sender, aus.run_key, datum, startzeit_ts_dr, endezeit_ts_dr, wochentag, titel, dauer, titelid, genre_1, genre_2, genre_3
    FROM bids_universe_source_gfk.ausstrahlungen aus
    ) aus ON aus.run_key = s5.run_key

-- add last run info
LEFT JOIN (
    SELECT a.sender, runnr, va.run_key, LAG(va.run_key) OVER (PARTITION BY va.ROOTID ORDER BY a.STARTZEIT_TS asc) run_key_lr, a.TITEL, a.ST
        va.titelid, va.ROOTID
    FROM BIDS_UNIVERSE_MASTER.RUNNR rnr
    JOIN BIDS_UNIVERSE_INTEGRATION.V_ALLIDS va ON va.runid = rnr.runid
    JOIN BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN a ON a.run_key = va.run_key
    WHERE a.sender IN ('ProSieben', 'ZDF')
    ORDER BY va.rootid, a.startzeit_ts
) lr ON lr.run_key = s5.run_key

-- add Zielgruppen of last run
LEFT JOIN BIDS_UNIVERSE_SOURCE_GFK.ZIELGRUPPEN zg_lr ON zg_lr.run_key = run_key_lr AND s5.zielgruppe = zg_lr.zielgruppe

LEFT JOIN BIDS_UNIVERSE_SOURCE_MANUELL.EVENTS events ON events.datum = s5.datum
LEFT JOIN BIDS_UNIVERSE_SOURCE_MANUELL.FEIERTAGE feiertage ON feiertage.datum = s5.datum

LEFT JOIN BIDS_UNIVERSE_MASTER.MA_PLAN_IST_EVAL
ma_plan ON ma_plan.run_key = aus.run_key

WHERE
	s5.datum >= '2017-01-01'
	-- s5.datum >= '2019-11-18'
	AND s5.datum <= '2021-02-28'
	AND s5.sender IN ('ProSieben', 'ZDF')
	AND s5.zielgruppe IN ('Erw. 14-49', 'M�nner 14-29')
	AND EXTRACT(HOUR FROM s5.startzeit_ts) = 20
	AND EXTRACT(MINUTE FROM s5.startzeit_ts) BETWEEN 20 AND 35
ORDER BY s5.datum, s5_slot, s5.sender, s5.zielgruppe


-- SELECT * FROM BIDS_UNIVERSE_MASTER.MA_PLAN_IST_EVAL LIMIT 10
-- WHERE BIDS_UNIVERSE_MASTER.MA_PLAN_IST_EVAL.STARTZEIT_TS



/*
#########################################################################
JOIN von gfk und datamart um original titel des spielfilms zu bekommen
#########################################################################
*/

SELECT
	aus.run_key, aus.titel, g2c.ID_PROMAMS, g2c.CONTENT_ID_PROMAMS,
	cdm.A_ID, cdm.C_CONTENT, cdm.C_ORIGINALTITEL, cdm.C_HOECHSTE_BESUCHERZAHL_D
FROM
	BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN aus
LEFT JOIN
	-- SELECT mapping.run_key, id_promams
	-- FROM
	BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
ON aus.run_key = g2c.run_key
LEFT JOIN
	BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V cdm
ON g2c.ID_PROMAMS = cdm.A_ID
WHERE
	cdm.A_ID IS NOT NULL
	AND cdm.C_HOECHSTE_BESUCHERZAHL_D IS NOT NULL
LIMIT 100

/*
#########################################################################
duplikate in der mapping tabelle BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH
#########################################################################
*/
-- JOIN von gfk und datamart mittels mapping f�r black panther erzeugt 2 identische runkeys
SELECT
	aus.run_key, aus.titel, g2c.ID_PROMAMS, g2c.CONTENT_ID_PROMAMS,
	cdm.A_ID, cdm.C_CONTENT, cdm.C_ORIGINALTITEL, cdm.C_HOECHSTE_BESUCHERZAHL_D
FROM
	BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN aus
LEFT JOIN
	BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
ON aus.run_key = g2c.run_key
LEFT JOIN
	BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V cdm
ON g2c.ID_PROMAMS = cdm.A_ID
WHERE
	c_originaltitel = 'BLACK PANTHER'

-- Erkl�rung: in der mapping tabelle gibt es duplikate
	-- sowohl id_promams als run_key kommen doppelt vor, die anderen felder sind teilweise NULL
SELECT *
FROM
	BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
WHERE
	g2c.ID_PROMAMS = 35511162
	OR g2c.run_key = 202012062015021073511125051

/*
#########################################################################
different titelids for one content: mocking jay
#########################################################################
*/

SELECT
	aus.run_key, aus.titel, aus.TITELID, g2c.ID_PROMAMS, g2c.CONTENT_ID_PROMAMS,
	cdm.A_BESTSELLER_WIEVIELTE, cdm.A_WIEVIELTER_RUN, cdm.L_BEGINN, cdm.C_LETZTE_AUSSTRAHLUNG_ID,
	cdm.A_ID, cdm.C_CONTENT, cdm.C_ORIGINALTITEL, cdm.C_HOECHSTE_BESUCHERZAHL_D
FROM
	BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN aus
LEFT JOIN
	BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
ON
	aus.run_key = g2c.run_key
LEFT JOIN
	BIDS_UNIVERSE_SOURCE_CUBE.DI_CONTENT_DATAMART_V cdm
ON
	g2c.ID_PROMAMS = cdm.A_ID
WHERE
	aus.RUN_KEY = 202002222015041072111173628
	OR aus.RUN_KEY = 201711122014321073511082251


-- verschiedene content_id_promams und titelid
-- generelle check abfrage
WITH CTE AS ( -- reihenfolge wird nicht abgespeichert? ja weil letztes order nur ausgef�hrt wird, also wenn ich von der cte selected
	SELECT
	g2c.CONTENT_ID_PROMAMS
	, aus.TITEL
	, aus.TITELID
	, LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) AS lagged_TITELID -- order by wird ben�tigt, damit das sinnvoll ist
	, aus.TITELID - LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) AS DIFF
	, CAST(aus.TITELID - LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) <> 0 AS INT) AS POS_DIFF
	FROM
		BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN aus
	LEFT JOIN
		BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
	ON aus.run_key = g2c.run_key
	WHERE
		aus.GENRE_1 = 'Spielfilm'
	ORDER BY
		g2c.CONTENT_ID_PROMAMS
)
-- POS_DIFF ist 125,710 mal 1, COUNT(DISTINCT CONTENT_ID_PROMAMS) ist 6493

-- SELECT * FROM CTE ORDER BY CONTENT_ID_PROMAMS

-- SELECT SUM(POS_DIFF), COUNT(DISTINCT CONTENT_ID_PROMAMS) FROM CTE


SELECT CONTENT_ID_PROMAMS, SUM(POS_DIFF) AS sum
FROM ( -- reihenfolge wird nicht abgespeichert? ja weil letztes order nur ausgef�hrt wird, also wenn ich von der cte selected
	SELECT
	g2c.CONTENT_ID_PROMAMS
	, aus.TITEL
	, aus.TITELID
	, LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) AS lagged_TITELID -- order by wird ben�tigt, damit das sinnvoll ist
	, aus.TITELID - LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) AS DIFF
	, CAST(aus.TITELID - LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) <> 0 AS INT) AS POS_DIFF
	FROM
		BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN aus
	LEFT JOIN
		BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
	ON aus.run_key = g2c.run_key
	WHERE
		aus.GENRE_1 = 'Spielfilm'
	ORDER BY
		g2c.CONTENT_ID_PROMAMS
)
GROUP BY CONTENT_ID_PROMAMS
HAVING SUM(POS_DIFF) <> 1


SELECT
g2c.CONTENT_ID_PROMAMS
, aus.TITEL
, aus.TITELID
, LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) AS lagged_TITELID -- order by wird ben�tigt, damit das sinnvoll ist mus
, aus.TITELID - LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) AS DIFF
, CAST(aus.TITELID - LAG(aus.TITELID, 1, 0) OVER (ORDER BY g2c.CONTENT_ID_PROMAMS ASC) <> 0 AS INT) AS POS_DIFF
FROM
	BIDS_UNIVERSE_SOURCE_GFK.AUSSTRAHLUNGEN aus
LEFT JOIN
	BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
ON aus.run_key = g2c.run_key
WHERE
	-- g2c.CONTENT_ID_PROMAMS IN (5788486, 5648303)
	aus.TITELID IN (773965, 1109465, 1083783, 1083783, 1083783)
ORDER BY
	g2c.TITELID
	-- g2c.CONTENT_ID_PROMAMS
