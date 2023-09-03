query = """
SELECT
    g2c.datum_gfk,
    g2c.run_key,
    g2c.ID_PROMAMS AS A_ID, -- A_ID = ID_PROMAMS
    g2c.CONTENT_ID_PROMAMS AS C_ID
FROM BIDS_UNIVERSE_MAPPING.GFK2CUBE_MATCH g2c
"""
