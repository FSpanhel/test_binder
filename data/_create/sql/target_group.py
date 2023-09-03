query = """
SELECT
    datum,
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
"""  # noqa
