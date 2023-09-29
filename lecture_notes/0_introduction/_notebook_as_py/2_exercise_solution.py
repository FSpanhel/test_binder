# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# # Questions regarding the next topic (version control)
#
# Please use https://partici.fi/30119096, or scan the QR code below, to answer the questions about version control.

# %% [markdown] slideshow={"slide_type": "-"}
# <div align="center">
# <img src="./figures/2_p.png" alt="drawing" width="1200"/>
# </div>
#
# <div align="left" style="font-size:16px;">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# [//]: <> (s)
# # Connecting to the database

# %% slideshow={"slide_type": "-"} tags=["s"]
import sqlite3
import pandas as pd

connection = sqlite3.connect("../../data/dsc.db")
cursor = connection.cursor()

def execute_query(query: str):
    return pd.read_sql_query(query, connection)


# %% [markdown] slideshow={"slide_type": "slide"}
# # Tasks
# Use DBeaver, or a Python interface, to anwer the following questions. 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Warm-up

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Count the number of rows in the tables 
#     - Broadcast
#     - Target_group
#     - Cdm
#     - Mapping_gfk_cdm
#     - Event
#     - Holiday

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT
	(SELECT COUNT(*) from broadcast) as n_broadcast,
	(SELECT COUNT(*) from target_group) as n_target_group,
	(SELECT COUNT(*) from cdm) as n_cdm,
	(SELECT COUNT(*) from mapping_gfk_cdm) as n_mapping_agf_cdm,
	(SELECT COUNT(*) from event) as n_event,
	(SELECT COUNT(*) from holiday) as n_holiday;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the unique channels of the broadcast table.

# %% slideshow={"slide_type": "-"}
execute_query("SELECT DISTINCT channel FROM broadcast;").squeeze().tolist()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the unique genres of the broadcast table.

# %% slideshow={"slide_type": "-"}
execute_query("SELECT DISTINCT genre FROM broadcast;")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the unique target groups of the target_group table.

# %% slideshow={"slide_type": "-"}
execute_query("SELECT DISTINCT target_group FROM target_group;")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the C_SERIES with the highest number of seasons from the cdm table.

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT DISTINCT c_series, c_season_number
FROM cdm
WHERE c_season_number = (SELECT MAX(c_season_number) from cdm);
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Use the cdm table to get the minimal and maximum number of runs that are available for a license. 

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT 
	MIN(l_number_of_runs) as min_run,
	MAX(l_number_of_runs) as max_run
FROM
	cdm c;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the name of the 100th episode of the series FUTURAMA.

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT c_series, c_content, c_season_number, c_episode_number, 
       l_id, b_license_run, b_quick_repeat, b_internal_repetition_number
FROM cdm
WHERE c_series = 'FUTURAMA' and c_episode_number = 100; 
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Broadcast data
# Note: You can find [here](https://www.sqlite.org/lang_datefunc.html) information about SQLite time and date functions.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### When does the data in the broadcast table start and end?

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT 
    MIN(start_time_agf) as min_time, 
    MAX(end_time_agf) as max_time 
FROM broadcast;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### What is the title with the longest duration?

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT title, (duration / 3600) as hours
FROM broadcast 
WHERE duration = (SELECT MAX(duration) FROM broadcast);
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Count the number of genres and sort them in ascending order.

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT genre, COUNT(*) as n
FROM broadcast
GROUP BY genre
ORDER BY n;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Show the 10 most frequent start times of broadcasts. Can you explain why the most frequent start time is at the top?

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT TIME(start_time_agf) as start_time, COUNT(*) as n
FROM broadcast b
GROUP BY TIME(start_time_agf)
ORDER BY n DESC
LIMIT 10;
""")

# %% [markdown] slideshow={"slide_type": "-"}
# [//]: <> (s)
# 03:00:00 ist the most frequent start time because a new broadcast day starts at 03:00:00.

# %% slideshow={"slide_type": "subslide"}
execute_query(
"""
SELECT TIME(end_time_agf) as end_time, COUNT(*) as n
FROM broadcast
GROUP BY TIME(end_time_agf)
ORDER BY n DESC
LIMIT 3;
""")

# %% [markdown] slideshow={"slide_type": "-"}
# [//]: <> (s)
# 02:55:00 ist the most frequent end time because a new broadcast day ends at 02:55:59

# %% [markdown] slideshow={"slide_type": "slide"}
# ### On which days are feature movies ("Spielfilm") broadcasted most frequently?

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT weekday, COUNT(*) as n
FROM broadcast
WHERE genre = 'Spielfilm'
GROUP BY weekday
ORDER BY n DESC;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Target group data
# Note: You can create a temporary table using
# ```
# CREATE TEMPORARY TABLE table_name AS 
# SELECT ... FROM ...
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Create a temporay table that contains for each run the corresponding KIPs of each target group.

# %% slideshow={"slide_type": "-"}
cursor.execute(
"""
DROP TABLE IF EXISTS btg;
""")

# %% slideshow={"slide_type": "-"}
cursor.execute(
"""
CREATE TEMPORARY TABLE btg AS
SELECT *
FROM broadcast b
LEFT JOIN
target_group tg 
on
b.RUN_ID = tg.RUN_ID;
""")

# %% [markdown] slideshow={"slide_type": "subslide"}
# [//]: <> (s)
# The following query confirms that we have created the temporary table btg.

# %% slideshow={"slide_type": "-"}
execute_query("SELECT * FROM sqlite_temp_master")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### According to Sehb, what was the most successful broadcast for the target group 'Erw. 14-49'?

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT 
    title, channel, start_time_agf,
    btg.sehb / 1e6 'Sehb in Millions', btg.target_group
FROM btg
JOIN
(
    SELECT MAX(sehb) as sehb 
    FROM btg 
    WHERE target_group = 'Erw. 14-49'
) agg
ON 
btg.sehb = agg.sehb;
""")

# %% [markdown] slideshow={"slide_type": "subslide"}
# [//]: <> (s)
# Or alternatively:

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT 
    title, channel, start_time_agf,
    btg.sehb / 1e6 'Sehb in Millions', btg.target_group
FROM btg
WHERE target_group = 'Erw. 14-49'
ORDER BY btg.sehb DESC
LIMIT 1
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Investigate the yearly and monthly seasonality of TVG for the target group 'Erw. 14-49' and the channel 'ARD Das Erste'. What patterns do you observe?

# %% [markdown] slideshow={"slide_type": "-"}
# [//]: <> (s)
# Yearly TVG:

# %% slideshow={"slide_type": "-"}
yearly_tvg = execute_query(
"""
SELECT SUM(tvg) / 1e6 AS 'tvg in millions', strftime('%Y', START_TIME_AGF) as year
FROM btg
WHERE channel = 'ARD Das Erste' AND target_group = 'Erw. 14-49'
GROUP BY
strftime('%Y', START_TIME_AGF);
""")
yearly_tvg

# %% slideshow={"slide_type": "slide"} tags=["s"]
yearly_tvg.plot('year', 'tvg in millions')

# %% [markdown] slideshow={"slide_type": "-"}
# [//]: <> (s)
# - We see that the tv usage is continously decreasing over the years.
# - Note that the broadcast table has no information about viewing behavior during advertisement.
# - Consequently, summing the corresponding TVG of broadcasts over a channel, target group and time interval (e.g., a year)
# yields different results depending on the advertisement behavior of channels as can be seen in the next query.

# %% slideshow={"slide_type": "subslide"}
execute_query(
"""
SELECT SUM(TVG) / 1e6 AS 'tvg in millions', CHANNEL, strftime('%Y', START_TIME_AGF) as YEAR
FROM btg
WHERE CHANNEL IN ('ARD Das Erste', 'RTL')
AND TARGET_GROUP = 'Erw. 14-49'
GROUP BY CHANNEL, strftime('%Y', START_TIME_AGF);
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# [//]: <> (s)
# Monthly TVG:

# %% slideshow={"slide_type": "-"}
monthly_tvg = execute_query(
"""
SELECT SUM(tvg) / 1e6 as 'tvg in millions', strftime('%m', start_time_agf) as month
FROM btg
WHERE channel = 'ARD Das Erste' AND target_group = 'Erw. 14-49'
GROUP BY
strftime('%m', start_time_agf)
""")
monthly_tvg

# %% slideshow={"slide_type": "slide"} tags=["s"]
monthly_tvg.plot('month', 'tvg in millions')

# %% [markdown] slideshow={"slide_type": "-"}
# [//]: <> (s)
# We see that monthly TVG is higher in the winter and lower in the summer.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Compute the market share for each run and target group.

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT title, start_time_agf, target_group, sehb, tvg,
ROUND((sehb / tvg) * 100, 2) as market_share
FROM btg;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ###  For each channel, compute the market share for the target group 'Erw. 14-49'.

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT channel, round((SUM(sehb) / SUM(tvg)) * 100, 2) as market_share_E1449
from BTG
WHERE target_group = 'Erw. 14-49'
GROUP BY channel
ORDER BY market_share_E1449 DESC;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Internal data

# %% [markdown] slideshow={"slide_type": "slide"}
# ### What is the average number of available runs per license?

# %% slideshow={"slide_type": "-"}
execute_query("SELECT AVG(L_NUMBER_OF_RUNS) FROM CDM;")

# %% [markdown] slideshow={"slide_type": "slide"}
# ###  Find the C_CONTENT of the license with the maximal numbers of run.

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT l_id, c_content, b_internal_repetition_number
FROM cdm
WHERE b_internal_repetition_number = (SELECT MAX(b_internal_repetition_number) from cdm);
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Which C_CONTENT has the highest number of cinema visitors?

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT DISTINCT c_content, c_highest_number_of_visitors_germany / 1e6 as 'max cinema visitors in millions'
from cdm 
WHERE c_highest_number_of_visitors_germany = (SELECT MAX(c_highest_number_of_visitors_germany) from cdm);
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Join the cdm table to the broadcast table and store it as temporary table.

# %% slideshow={"slide_type": "-"}
cursor.execute(
"""
DROP TABLE IF EXISTS btgcdm;
""")

# %% slideshow={"slide_type": "-"}
cursor.execute(
"""
CREATE TEMPORARY TABLE btgcdm AS
SELECT * FROM broadcast b 
LEFT JOIN mapping_gfk_cdm mgc 
on b.RUN_ID = mgc.RUN_ID 
LEFT JOIN cdm
on mgc.B_ID = cdm.B_ID;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Count the number of broadcast genres that are available in the cdm table. Hint: A genre is only available in the cdm table if L_ID is not null.

# %% slideshow={"slide_type": "-"}
execute_query(
"""
SELECT COUNT(*), genre
FROM btgcdm
WHERE l_id is not NULL
GROUP BY genre;
""")

# %% [markdown] slideshow={"slide_type": "slide"}
# [//]: <> (s)
# # Closing the connection the database

# %% slideshow={"slide_type": "-"} tags=["s"]
connection.close()
