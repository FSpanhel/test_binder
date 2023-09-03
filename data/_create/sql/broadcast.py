query = """
SELECT
    aus.run_key, --  as RUN_ID,  -- need to transform this
    titel, -- AS title,
    aus.sender, -- AS channel,
    aus.datum, -- gut für filtern, da tag hier um 3 Uhr früh endet
    aus.startzeit_ts,
    (aus.DATUM || '-' || SUBSTR(aus.ENDEZEIT, 12, 15)) AS endezeit_ts,  -- gibt es nicht in der bidb (wieso auch immer)
    -- startzeit, -- jahr passt hier nicht
    aus.startzeit_ts_dr, --  AS start_time,  -- tag endet um 12 a.m.
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
    aus.datum >= '2012-01-01'  -- hier nicht datum_real benutzen, war zuerst 2015-01-01
    -- AND aus.datum <= '2020-12-31'
    AND aus.datum <= '2022-08-31'
    AND aus.sender IN ('ProSieben', 'SAT.1', 'Kabel Eins', 'VOX', 'RTL', 'RTL_ZWEI', 'ARD Das Erste', 'ZDF')
"""  # noqa
