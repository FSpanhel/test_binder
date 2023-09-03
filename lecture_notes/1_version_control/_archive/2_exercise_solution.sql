-- ####################### WARM-UP #######################

/*
1. Count the number of rows in the tables
    - broadcast
    - target_group
    - cdm
    - mapping_gfk_cdm
    - event
    - holidy
1. Get the unique channels of the broadcast table.
1. Get the unique genres of the broadcast table.
1. Get the unique target groups of the target_group table.
1. Get the unique genres of the cdm table.
1. Use the cdm table to get the minimal and maxium number of runs that is available for a license.
1. Which title has been broadcasted the most according to the cdm table?
*/

SELECT
	(SELECT COUNT(*) from broadcast) as n_broacast,
	(SELECT COUNT(*) from target_group) as n_target_group,
	(SELECT COUNT(*) from cdm) as n_cdm,
	(SELECT COUNT(*) from mapping_gfk_cdm) as n_mapping_agf_cdm,
	(SELECT COUNT(*) from event) as n_event,
	(SELECT COUNT(*) from holiday) as n_holiday ;


-- 1. Get the unique channels of the broadcast table.


SELECT DISTINCT(CHANNEL) FROM broadcast b ;


-- 1. Get the unique genres of the broadcast table.


SELECT DISTINCT(GENRE) FROM broadcast b ;

-- 1. Get the unique target groups of the target_group table.


SELECT DISTINCT(TARGET_GROUP) from target_group tg;

-- 1. FIX: Get the content with the maximal number of episodes from the cdm table.


SELECT C_CONTENT, C_SEASON_NUMBER, C_EPISODE_NUMBER, C_ID
from cdm c
WHERE C_SEASON_NUMBER = (SELECt MAX(C_SEASON_NUMBER) from cdm);
-- WHERE C_EPISODE_NUMBER = (SELECt MAX(C_EPISODE_NUMBER) from cdm);

SELECT C_SERIES
from cdm c
WHERE C_SEASON_NUMBER = (SELECt MAX(C_SEASON_NUMBER) from cdm);

-- 1. Use the cdm table to get the minimal and maxium number of runs that is available for a license.


SELECT
	MIN(L_NUMBER_OF_RUNS) as MIN_RUN,
	MAX(L_NUMBER_OF_RUNS) as MAX_RUN
FROM
	cdm c;


1. Which title has been broadcasted the most according to the cdm table?

SELECT C_CONTENT, B_INTERNAL_REPETITION_NUMBER
FROM cdm c
WHERE B_INTERNAL_REPETITION_NUMBER = (SELECT MAX(B_INTERNAL_REPETITION_NUMBER) from cdm);


-- ####################### BROADCAST DATA #######################
-- 1. When does the data in the broadcast table start and end?


SELECT MIN(START_TIME_AGF), MAX(END_TIME_AGF) FROM broadcast b;


-- 1. What is the title with the longest duration?


SELECT TITLE, (DURATION / 3600) as HOURS
FROM broadcast b
WHERE DURATION = (SELECT MAX(DURATION) FROM broadcast);

/*
SELECT TITLE, (DURATION / 3600) as HOURS
FROM broadcast b
ORDER BY DURATION DESC
LIMIT 10;
*/

-- 1. Count the number of genres and sort them in ascending order.


SELECT GENRE, COUNT(*) as n
FROM broadcast b
GROUP BY GENRE
ORDER BY n;

-- 1. 1. Show the 10 most frequent starting times of broadcasts.

SELECT TIME(START_TIME_AGF), COUNT(*) as n
FROM broadcast b
GROUP BY TIME(START_TIME_AGF)
ORDER BY n DESC
LIMIT 10;

/*
03:00:00 ist the most frequent start time because a new broadcast day starts at 03:00:00
*/


/*
SELECT TIME(END_TIME_AGF), COUNT(*) as n
FROM broadcast b
GROUP BY TIME(END_TIME_AGF)
ORDER BY n DESC
LIMIT 50;
*/

/*
02:55:00 ist the most frequent end time because a new broadcast day ends at 02:55:59
*/


-- 1. On which days are feature movies ("Spielfilm") broadcasted most frequently?


SELECT WEEKDAY, COUNT(*) as n
FROM broadcast b
WHERE GENRE = 'Spielfilm'
GROUP BY WEEKDAY
ORDER BY n DESC;


-- ####################### TARGET GROUP DATA #######################

-- 1. For each run, join the KIPs of each target group.
DROP TABLE IF EXISTS btg;
CREATE TEMPORARY TABLE btg AS
SELECT *
FROM broadcast b
LEFT JOIN
target_group tg
on
b.RUN_ID = tg.RUN_ID;

/*
SELECT * FROM btg;
SELECT * FROM sqlite_master;
*/

-- 1. According to SEHB, what was the most successful broadcast for each target group?

/*
SELECT TARGET_GROUP, TITLE, CHANNEL, SEHB, START_TIME_AGF, END_TIME_AGF
FROM btg
WHERE SEHB = (SELECT MAX(SEHB) FROM btg);
*/

SELECT btg.TARGET_GROUP, TITLE, CHANNEL, btg.SEHB, START_TIME_AGF, END_TIME_AGF
FROM btg
JOIN
(SELECT MAX(SEHB) as sehb, TARGET_GROUP FROM btg GROUP BY TARGET_GROUP) max_sehb
ON
btg.target_group = max_sehb.target_group and btg.sehb = max_sehb.sehb;

-- 1. Find an explanation why the most successful broadcasts was so successful at this day.
-- https://www.youtube.com/watch?v=a7IMPsyQg6k&t=108s

SELECT TARGET_GROUP, TITLE, CHANNEL, SEHB, START_TIME_AGF, END_TIME_AGF
FROM btg
WHERE
START_TIME_AGF > '2014-07-08 20:00:00'
AND START_TIME_AGF <= '2014-07-08 23:59:59'
AND CHANNEL = 'ZDF'
AND TARGET_GROUP = 'Erw. 14-49';


-- 1. Investigate the yearly and monthly seasonality of TVG for the target group 'Erw. 14-49' and the channel 'ARD Das Erste'. What patterns do you observe?


-- yearly
SELECT SUM(TVG) AS TVG, CHANNEL, strftime('%Y', START_TIME_AGF) as YEAR
FROM btg
WHERE CHANNEL = 'ARD Das Erste' AND TARGET_GROUP = 'Erw. 14-49'
GROUP BY
strftime('%Y', START_TIME_AGF);

/*
We see that the tv usage is continously decreasing over the years.
Note that the broadcast table has no information about viewing behavior during advertisement.
Consequently, summing the corresponding TVG of all broadcasts over a channel, target group and time interval (e.g., a year)
yields different results depending on the advertisement behavior of channels.

SELECT SUM(TVG) AS TVG, CHANNEL, strftime('%Y', START_TIME_AGF) as YEAR
FROM btg
WHERE CHANNEL IN ('ZDF', 'ARD Das Erste', 'ZDF', 'ProSieben', 'SAT.1', 'RTL')
AND TARGET_GROUP = 'Erw. 14-49'
GROUP BY
CHANNEL, strftime('%Y', START_TIME_AGF);
*/


SELECT SUM(TVG) as TVG, strftime('%m', START_TIME_AGF) as MONTH
FROM btg
WHERE CHANNEL = 'ARD Das Erste' AND TARGET_GROUP = 'Erw. 14-49'
GROUP BY
strftime('%m', START_TIME_AGF)
ORDER BY TVG DESC;

/*
We see that TVG is higher in the winter and lower in the summer.
*/

-- 1. Compute the market share for each run and target group.


SELECT TITLE, START_TIME_AGF, TARGET_GROUP, SEHB, TVG,
ROUND((SEHB / TVG) * 100, 2) as MARKET_SHARE
FROM btg;


-- 1. Compute the market share of the target group 'Erw. 14-49' for each channel.


SELECT CHANNEL, ROUND((SUM(SEHB) / SUM(TVG)) * 100, 2) as MARKET_SHARE_E1449
from BTG
WHERE TARGET_GROUP = 'Erw. 14-49'
GROUP BY CHANNEL
ORDER BY MARKET_SHARE_E1449 DESC;



-- ####################### INTERNAL #######################
-- 1. What is the average number of available runs per license?
DROP TABLE IF EXISTS btg;
SELECT AVG(L_NUMBER_OF_RUNS) FROM CDM;

-- 1. Find the C_CONTENT of the license with the maximal numbers of run.


SELECT C_CONTENT, B_INTERNAL_REPETITION_NUMBER, L_ID
FROM cdm
WHERE B_INTERNAL_REPETITION_NUMBER = (SELECT MAX(B_INTERNAL_REPETITION_NUMBER) from cdm);

-- 1. Which C_CONTENT has the highest number of cinema visitors?


SELECT DISTINCT C_CONTENT, C_HIGHEST_NUMBER_OF_VISITORS_GERMANY
from cdm
WHERE C_HIGHEST_NUMBER_OF_VISITORS_GERMANY = (SELECT MAX(C_HIGHEST_NUMBER_OF_VISITORS_GERMANY) from cdm);


-- 1. Join the cdm table to the broadcast table.


CREATE TEMPORARY TABLE btgcdm AS
SELECT * FROM broadcast b
JOIN mapping_gfk_cdm mgc
on b.RUN_ID = mgc.RUN_ID
JOIN cdm
on mgc.B_ID = cdm.B_ID;


-- 1. Count the number of broadcast genres that are available in the cdm table. Hint: A genre is only available in the cdm table if L_ID is not null.


SELECT COUNT(*), GENRE
FROM btgcdm
WHERE L_ID is not NULL
GROUP BY GENRE;

-- 1. What is the broadcast title of the license which has the oldest license start?


SELECT TITLE, L_START, L_END, START_TIME_AGF, L_NUMBER_OF_RUNS, B_LICENSE_RUN
FROM
btgcdm
WHERE L_START = (SELECT MIN(L_START) FROM cdm);

/*
This license has three runs and three last was broadcasted on 2012-04-01.
The value of L_END should indicate that there is no license end.
 */


-- ####################### GEEK QUESTIONS #######################
-- 1. Compute START_TIME_REAL which is the start time of a broadcast such that the date refers to the actual date of this day (but not the AGF/GFK date).
-- Use this column to list the RUN_IDs of the broadcast which are broadcasted in the first 4 hours of 2021-01-02.
SELECT RUN_ID, CHANNEL, START_TIME_AGF,
CASE
	WHEN TIME(START_TIME_AGF) >= '00:00:00' and TIME(START_TIME_AGF) < '03:00:00' THEN DATETIME(START_TIME_AGF, '+1 days')
	ELSE START_TIME_AGF
END as START_TIME_REAL
FROM broadcast b
WHERE START_TIME_REAL BETWEEN '2012-01-02 00:00:00' AND '2012-01-02 04:00:00' AND CHANNEL = 'ProSieben' -- > '23:30:00' and TIME(START_TIME_AGF) < '03:00:00' ;
ORDER BY START_TIME_REAL;


--  Wie viel Ausstrahlungen durchschnittlich auf jedem Sender pro Tag?
SELECT COUNT(GENRE), CHANNEL, WEEKDAY
FROM broadcast b
GROUP BY CHANNEL, WEEKDAY;
