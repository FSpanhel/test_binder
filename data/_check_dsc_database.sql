SELECT *
FROM mapping_gfk_cdm mgc ;

SELECT COUNT(*) FROM broadcast b;  -- 688,124 wie source :)
SELECT COUNT(*) FROM target_group tg; -- source: 3,440,520, hier: 3,448,515 -> okay


-- source: 3,440,520, hier: 3,448,515 -> okay
SELECT COUNT(*)
FROM broadcast aus
LEFT JOIN target_group zg
ON
    aus.run_id = zg.run_id;

/*
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
 */


-- hier: 3,448,515 : source 3,448,515 -> okay
SELECT COUNT(*)
FROM broadcast aus
LEFT JOIN target_group zg
ON
    aus.run_id = zg.run_id
LEFt JOIN mapping_gfk_cdm mgc
ON
	aus.run_id = mgc.run_id;
/*
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
*/

-- hier: 3,448,565, source: 3,448,515 -> okay
SELECT COUNT(*)
FROM broadcast aus
LEFT JOIN target_group zg
ON
    aus.run_id = zg.run_id
LEFt JOIN mapping_gfk_cdm mgc
ON
	aus.run_id = mgc.run_id
LEFT JOIN cdm c
ON
	mgc.B_ID = c.B_ID;

/*
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
*/


SELECT DISTINCT(GENRE) FROM broadcast b ;
-- SELECT DISTINCT(GENRE_2) FROM broadcast b ;
-- SELECT DISTINCT(GENRE_3) FROM broadcast b ;
SELECT DISTINCT(REPEAT) FROM broadcast b ;
SELECT MIN(START_TIME_AGF)  FROM broadcast b ;
SELECT MAX(START_TIME_AGF)  FROM broadcast b ;
SELECT DISTINCT(CHANNEL) from broadcast b;










-- 8. Which movie has the highest number of cinema visitors?



-- 9. What is the title of the license which has the oldest license start?


SELECT
cdm.B_ID, MIN(L_START), b.TITLE
FROM cdm
LEFT JOIN
mapping_gfk_cdm mgc
on cdm.B_ID = mgc.B_ID
LEFT JOIN
broadcast b
on b.RUN_ID = mgc.RUN_ID;

-- 10. What is the relation between RUN_ID and B_ID?


/*
For one B_ID there can be two R_IDs if the run starts before 2:59:99 a.m. and ends after 3 a.m.
That is because a "GFK day" starts at at 3 a.m. and ends at 2:59:99 a.m.
*/



SELECT START_TIME_AGF from broadcast b ORDER BY START_TIME_AGF;

--
