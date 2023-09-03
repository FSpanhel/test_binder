# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python [conda env:dsc_2022] *
#     language: python
#     name: conda-env-dsc_2022-py
# ---

# %% slideshow={"slide_type": "notes"}
import pandas as pd

from dsc.notebook import embed_website
from dsc.introduction.data import example_pin, viewing_duration, potential

# %% [markdown] slideshow={"slide_type": "slide"}
# <div align="center" style="font-size:70px;">
# DATA AND PROJECTS
# <div/>
#     
# <div align="left" style="font-size:16px;">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# # Data description
# In this course, we will be working with german (free) **linear TV data**. 
#
# Linear TV broadcasts scheduled programs, over the air or through satellite/cable, but not streamed to a specific user. 
#
# Almost all broadcast television services count as linear TV.

# %% [markdown] hide_input=false slideshow={"slide_type": "slide"}
# The **TV program** lists the title and start time of all broadcasts for each day and channel.

# %% hide_input=false slideshow={"slide_type": "-"}
embed_website("https://www.hoerzu.de/tv-programm/", width=1200)

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# In Germany, there are two different types of broadcasters which broadcast linear TV. 
# - **Public broadcasters** like the ARD or ZDF whose primary mission is public service. Public broadcasters receive their funding primarily from a licence fee which every household, company and public institution are required to pay by law.
# - **Private/commercial broadcasters** like the RTL group or ProSiebenSat.1 are privately owned corporate media. 
#     - **free**: Commercial broadcasting primarily uses the airing of advertisements for profit.
#     - **paid**: Some servies are paid for by local subscribers, e.g. Sky. 

# %% [markdown] slideshow={"slide_type": "slide"}
# # How broadcast data is collected

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# The TV program can be used to infer the title and duration of all broadcasts for each channel and day and is freely available. 
# For private broadcasting the success, i.e., the **audience rating**, of a broadcast is crucial for the price of corresponding advertisements. 
# Audience ratings are **not publicly available and measured by the AGF**. 
#
# The AGF is the **association of TV and streaming providers in Germany** on whose behalf audience ratings in the German motion picture market are measured since April 1st, 1963 (!). The AGF further develops the continuous quantitative recording of the use of motion picture content in Germany, including the collection and evaluation of the data.

# %% [markdown] cell_style="split" hide_input=false slideshow={"slide_type": "-"}
# <div align="center" style="font-size:16px;">
# AGF members
# <img src="./figures/1_agf.png" alt="AGF members" width=800/>
# <div/>
# <div align="left" style="font-size:14px;">
# <div/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## The AGF panel

# %% [markdown] slideshow={"slide_type": "-"}
# At the core of AGF's audience research is the **AGF Panel**, which AGF operates in cooperation with **GfK**.
# - The AGF Panel is a **representative sample** of “the resident population of the Federal Republic of Germany in private households with at least one TV set in use and a German-speaking Main Income Earner.”
# - This universe represents the television usage of approximately **38 million TV households with up to 75 million individuals** over age 3 (as of January 1, 2022).
# - Moreover, once a year, panel households are surveyed with a questionnaire covering **demographic and consumer behaviour** from which target groups for analyses and pricing of advertisements can be constructed.
#
# Source: https://www.agf.de/en/audience-measurement/method/tv

# %% [markdown] slideshow={"slide_type": "slide"}
# **Relation between the panel and the population**
# <br>
# <br>
# <img src="./figures/1_agf_gfk_panel.png" alt="AGF/GFK Panel" width=1800/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Audio matching

# %% [markdown] slideshow={"slide_type": "-"}
# - TV usage is measured exclusively with an **audio matching** measurement technique.
# - The measurement devices generate audio samples at the TV set and compare them against broadcasters’ audio samples generated at central referencing sites. The matched signals are assigned to a broadcaster.

# %% [markdown] slideshow={"slide_type": "-"}
# <img src="./figures/1_audio_match.png" alt="AGF/GFK Panel" width=1200/>

# %% [markdown] slideshow={"slide_type": "subslide"}
# <div align="center" style="font-size:30px;">
# On the next website, scroll below for the 'TAM METER'! :D
# <div/>
# <div align="left" style="font-size:30px;">
# <div/>

# %% hide_input=false slideshow={"slide_type": "-"}
embed_website("https://www.agf.de/en/about-agf/history", height=800, width=1400)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### PIN data

# %% [markdown] slideshow={"slide_type": "-"}
# The AGF collects so called **PIN data**.
# - PIN data are **person-specific data on television usage** (measured in seconds)
# - It measures  the number of seconds that a person has spent watching a programme, commercial break or pre-defined time interval.
# - PIN data is measured each day **from 3 a.m. in the morning until 3 a.m. the next day**.
# - For instance, the date "2020-01-01" corresponds to the interval [2020-01-01 03:00:00, 2020-01-02 02:59:59].
# - Preliminary data for the previous AGF day (until 3 a.m. today) is then available from 8 a.m.
# - Final data is available 2 day later

# %% hide_input=true slideshow={"slide_type": "-"}
example_pin

# %% [markdown] slideshow={"slide_type": "slide"}
# ## KPIs

# %% [markdown]
# PIN data can be used to compute aggreated **KPIS for target groups, time intervals and channels**.
#
# - The most relevant target group for commercial broadcasters are Adults who are between 14 and 49 years old (**Erw. 14-49**).
# - Z3+ is another target group which includes all members of the panel.
#
# For simplicity, let's assume for the remainder of this section that there are only two channels ARD and P7.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Sehdauer (sehd)

# %% [markdown] cell_style="center" slideshow={"slide_type": "-"}
# For a given channel, time interval and target group:
# - The viewing duration of a corresponding panel member is the number of seconds viewed.
# - The **sehd** for a channel and target group is the corresponding (weighted) average of all individual viewing durations.

# %% [markdown] slideshow={"slide_type": "-"}
# Viewing duration for the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]

# %% cell_style="center" code_folding=[] hide_input=false slideshow={"slide_type": "-"}
viewing_duration

# %% cell_style="center" hide_input=false slideshow={"slide_type": "-"}
sehd = (
    viewing_duration
    [viewing_duration['channel'] != 'No-TV']
    .groupby(['channel'])
    .apply(lambda x: (x['viewing_duration'] @ x['weight']) / potential))  # potential is the sum of the member_id weights

# %% [markdown] slideshow={"slide_type": "-"}
# Sehd for each channel and the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]

# %% slideshow={"slide_type": "-"}
sehd.to_frame().T

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Sehbeteiligung (sehb)

# %% [markdown] slideshow={"slide_type": "-"}
# **Sehbeteiligung (Sehb)** is a measure of average viewing participation. When we talk about reach we often mean Sehb.
# - For a given channel, time interval and target group, the relative Sehb is the ratio of the viewing duration (Sehd) and the corresponding time interval.
# - The (absolute) Sehb is the relative Sehb scaled to the population of people that should be represented. 
# - Note that Sehb is not the number of viewers. 
#

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# Relative Sehb for the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# (Absolute) Sehb for the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]

# %% cell_style="split" slideshow={"slide_type": "-"}
rsehb = sehd / pd.Timedelta(hours=2)
round(rsehb, 2).to_frame().T

# %% cell_style="split" slideshow={"slide_type": "-"}
sehb = rsehb * potential
sehb.to_frame().T 

# %% [markdown] slideshow={"slide_type": "subslide"}
# **Sehb vs. number of viewers**
#   - In the digital world, e.g., streaming, the number of viewers are often the people who started to watch a program, independent of their viewing time. 
#   - Thus, if one people watches 1 one-second of a one-hour programm, the relative reach is 100% in the digital world. 
#   - However, the corresponding Sehb (= relative "reach") in the TV world is only 1/3600 = 0.028 %.
#   - Comparing reach of TV and digital formats should take this into account (!)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### TV-Gesamt (TVG)

# %% [markdown] slideshow={"slide_type": "-"}
# For a given target group and time interval, TVG is the Sehb of all channels.

# %% [markdown] slideshow={"slide_type": "-"}
# TVG

# %% slideshow={"slide_type": "-"}
tvg = sehb.sum()
tvg

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Market share (ms)

# %% [markdown] slideshow={"slide_type": "-"}
# The **market share** is the most relevant KPI for measuring the (relative) performance of a program. 
# - (Short-term) pricing of advertisements is based on the market share
# - The renewal or cancellation of a TV series is based on the market share 
#
# The market share is given by the ratio of Sehb and TVG.

# %% slideshow={"slide_type": "-"}
market_share = (sehb / tvg) * 100
market_share.to_frame().T

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Actual numbers
# The following website displays sehb (VP) and market shares (MS) of today.

# %% hide_input=false slideshow={"slide_type": "-"}
embed_website("https://www.agf.de/en/data/tv-data", width=1600, height=700)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Concluding remarks

# %% [markdown] slideshow={"slide_type": "-"}
# - Among other things, **the AGF is responsible for measuring the audience of linear TV and operates the AGF panel in cooperation with the GFK**.
# - As a result, linear TV broadcast performance data are often referred to as AGF/GFK data.
# - The established KPIs are recognized as the **market standard** for the media and advertising industry.
# - The most important KPIs are **Sehb**, **TVG** and the **market share**.
# - Although the number of measurement units is far smaller than in the digitial world, AGF/GFK data contains the exact viewing duration and detailed information about demographics and consumer behavio
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # Internal data

# %% [markdown]
# Besides AGF/GFK data KPI each broadcaster has internal data that is **not accessible to other broadcasters or agencies**.
# - Internal data which includes **further information** about programs, e.g., costs, availability, ..., or whether it is an
#     - In-house production (e.g., taff, red)
#     - Commissioned production (e.g., GNTM)
#     - Licensed program (Big bang theory)
# - Purchased additional broadcast meta data
#     - DMB
#     - Gracenote
# - Other data

# %% [markdown] slideshow={"slide_type": "slide"}
# # Accessing the data

# %% [markdown] slideshow={"slide_type": "fragment"}
# - Unfortunately, KPI data provided by the AGF can not be used in this course due to copyright reasons. 
# - Similarly, we can not use internal data.
# - Thereore, **KPI data about television usage has been simulated** with a focus on capturing the main features of the real data.
# - In addition, **internal data has been generated** with the idea to represent a possible scenario.
# - Moreover, the database only contains the subset of tables and columns that are relevant for this course.
# - Like real data, the synthetic **data is not perfect and has inconsistencies to a small degree**.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Database
#
# - The data is stored in an **sqlite database** which can be downloaded [here](https://syncandshare.lrz.de/getlink/fiVWchss6RorJVL3LDR47D/dsc.db).
# - I recommend to store the database in /data/dsc.db.
# - The database will be **updated each month** with more data (!).
# - The data can be accessed using the command-line shell https://www.sqlite.org/cli.html, an sql client software, or a python interface (sqlite3, sqlalchemy, pandas...).
#
# For now, let's use an **sql client software**.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Using an SQL client software like DBeaver

# %% [markdown] slideshow={"slide_type": "-"}
# **DBeaver** is a multi-platform database tool for all people who need to work with databases.
#
# The free **community edition** (CE) of DBeaver is an open source software and supports all common SQL Databases (https://dbeaver.io/).
#
# A closed-source **enterprise edition** of DBeaver is distributed under a commercial license has support of NoSQL databases and cloud (https://dbeaver.com/edition/).
#
# Comparison of DBeaver Community 22.2.0 vs. DBeaver PRO 22.1: https://dbeaver.com/edition/.
#
# Some **useful features**:
# - SQL queries execution
# - Data browser/editor with a huge number of features
# - Syntax highlighting and SQL auto-completion
# - Database structure (metadata) browse and edit

# %% [markdown] slideshow={"slide_type": "slide"}
# **Please install the DBeaver community version**

# %% hide_input=false slideshow={"slide_type": "-"}
embed_website("https://dbeaver.io/", width=1600, height=700)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Database tables

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Broadcast

# %% [markdown] slideshow={"slide_type": "-"}
# The **broadcast table** represents the actual TV program. It has the following columns:
# - RUN_ID: identifier of a broadcast that is unique for each datetime, title and channel. This is a primary key.
# - TITLE_ID: unique id of a title.
# - TITLE: title of the broadcast.
# - CHANNEL: channel on which the broadcast was aired.
# - START_TIME_AGF: starting time (5 minutes frequency) of the broadcast in terms of the [AGF/GFK terminology](#pin-data).
# - END_TIME_AGF: ending time (5 minutes frequency) of the broadcast in terms of the [AGF/GFK terminology](#pin-data).
# - WEEKDAY: weekday of the broadcast.
# - DURATION: duration of the broadcast (excluding advertisements).
# - GENRE: the genre of the broadcast.
# - REPEAT: 'ja' if the broadcast is a repetition, 'no' if it is a first-run.
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Target group

# %% [markdown]
# The table **target_group** contains the following metrics related to the success of a broadcast:
# - RUN_ID: unique id of a broadcast that is unique for each datetime, title and channel. This is a primary key.
# - Target group: target group for which an KPI is measure for a RUN_ID.
# - Sehb: the Sehb of this record.
# - TVG: the TVG of this record.
#
# Note that:
# - All KPIs have been simulated and differ from the actual KPIs.
# - The measured KPIs exclude advertisements, e.g., the Sehb is the Sehb of the program without the Sehb of
# the advertisements and thus likely to be higher than the Sehb with advertisements

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Content data mart (cdm)
# Information is available for the genres Spielfilm, Serie and Animation.

# %% [markdown] slideshow={"slide_type": "-"}
# - **Broadcast level**
#     - B_ID: Identifier of a broadcast. This is a primary key.
#     - B_INTERNAL_REPETITION_NUMBER: Counts through the internal chronological broadcast order of the Content ID.
#     - B_QUICK_REPEAT: 1 if the broadcast is a repeat of a recent broadcast (usually within 24 hours), B_LICENSE_RUN is then not increased.
#     - B_LICENSE_RUN: The run number of the corresponding license. For instance, if a license has three runs (L_NUMBER_OF_RUNS = 3), then the first run of this license has B_LICENSE_RUN = 1.
#     
# - **Content level**
#     - C_ID: Unique identifier of a content. In cases of a feature film this identifies the feature film, in cases of a series this identifies the episode. A content can be broadcastet several times.
#     - C_CONTENT: the (current) title of a content.
#     - C_SERIES_ID: identifies a series.
#     - C_SERIES: the title of the corresponding series of an episode.
#     - C_SEASON_NUMBER: The season of a series.
#     - C_EPISODE_NUMBER: The running episode number of a series (counting over all seasons). 
#     - C_YEAR_OF_PRODUCTION: Year of production.
#     - C_SERIES_CATEGORY_1: Structural designation of a series.
#     - C_SERIES_CATEGORY_2: Categorization of a series into Serial/Procedural/High Concept/Sitcom.
#     - C_FSK: Classification of a content into an age-related release according to the classification of the FSK association.
#     - C_HIGHEST_NUMBER_OF_VISITORS_GERMANY: Number of cinema visits in Germany.
# - **License level**
#     - L_ID: Unique identifier for a license. A license is required to broadcasts licensed feature movies or series.
#     - L_START: The start of a license. A run must not be broadcasted before L_START.
#     - L_END: The end of a license. A run must not be broadcasted after L_END.
#     - L_NUMBER_OF_RUNS: The number of available runs of a license. If L_NUMBER_OF_RUNS have been broadcasted, a new license is required to broadcast further runs.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Mapping_gfk_cdm

# %% [markdown] slideshow={"slide_type": "-"}
# The table **mapping_gfk_cdm** only contains the columns RUN_ID and B_ID.
# - AGF/GFK data uses the RUN_ID to identify a broadcast whereas the content data mart uses the B_ID to identify a broadcast.
# - For each B_ID there is usually one RUN_ID and vice versa. 
#     - An exception occurs when a broadcast starts before 03:00:00 a.m. and ends after 03:00:00 a.m. 
#     - In this case, this broadcast gets different RUN_IDs for the first and second day because, among other things, the AGF date determines the RUN_ID.
# - Since the AGF/GFK data is not internal data, there is no natural mapping between the AGF/GFK data and the content data mart.
# - A mapping has been established using **fuzzy title and datetime matching**.
# - Keep in mind that the mapping is mostly correct (in > 98% of the cases) but not always.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Events & holidays

# %% [markdown] slideshow={"slide_type": "-"}
# - The table **events** contains public information about events that might influence TV audience behavior.
# - The table **holidays** contains public information about German holidays.

# %% [markdown] slideshow={"slide_type": "slide"}
# # Projects

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Project 1: Forecasting the market shares of movies or series

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# <div align="center">
# <img src="./figures/1_project_1.png" alt="Project 2" width=700 height=700/>
# </div>
# <div align="left">
# </div>

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# - **Objective**: Forecast the market share of feature movies or series broadcasted during prime time in the next 6 weeks for the channels ProSieben, Sat.1 and Kabel eins.
#     - You can choose whether you want to model movies or series (or both).
#     - Group size: 3-4 people. 
# - **What will you do?**
#     - Learn how to start with a simple model that already does quite well and how to improve it
#     - Lots of feature engineering
#     - Implement a custom split for cross validation
#     - Optionally construct sophisticated features to approximate complex facts of the TV market

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Project 2: Forecasting monthly KPIs per channel

# %% [markdown] cell_style="split" hide_input=false slideshow={"slide_type": "-"}
# <div align="center">
# <img src="./figures/1_project_2.png" alt="Project 2" width=1000/>
# <div/>
# <div align="left">
# </div>

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# - **Objective**: Forecast of monthly market shares and sehb for the channels ProSieben, Sat.1 and Kabel eins up to 12 months
#     - Group size: 3 people
# - **What will you do**?
#     - Learn how to do time series forecasting
#     - Learn how to do multi-step-ahead forecasting
#     - Learn how to deal with seasonal patterns
#     - Learn how to set up cross validation if the data has a temporal dimension

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Project 3: Forecasting the usage time of licenses

# %% [markdown] cell_style="center" hide_input=true slideshow={"slide_type": "-"}
# <img src="./figures/1_project_3.png" alt="Project 3" width=1700 height=800/>

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# <div align="left" style="font-weight:bold;">
# Project 3: Forecasting the usage time of licenses
# <div/>
# <div align="left" style="font-weight:normal">
# <div/>
# <br>
#
# - **Objective**: Forecast the usage times of movies and series licenses
#     - Although more abstract than the other proejcts, this forecast is useful for a handful of optimizations
#     - Group size: 3 people
# - **What will you do**?
#     - Learn how to tackle a non-standard problem
#     - Learn how to set up cross validation if the data is no completely observable
#     - Learn how to impose further assumptions that might be required to model the data
#     - Learn how to justify your assumptions
#     

# %% [markdown] slideshow={"slide_type": "slide"}
# ## General remarks on the project work
# - **Groups**
#     - The groups will be randomly assigned. 
#     - You will determine how you will work together as a team. 
# - **Grading**
#     - Grades are based primarily on how well you apply the **best practices** learned in this course.
#         - It should be understandable what you did and why.
#         - No [Spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code).
#         - The code should run on other machines without the need for manual adjustements.
#         - The code should not break down if prediction should be done for new data.
#     - Moreover, the **methodological soundness** of your forecast will be evaluated.
#         - How well does your cross validation mimic the real use case? 
#         - Did you consider relevant features?
#     - It is not necessary that your forecast could win a [kaggle](https://www.kaggle.com/) competition.
# - The **best practices** that I suggest are suggestions. 
#     - You are free to apply other/further best practices. 
#     - You can also use additional data.
#
#
# **I recommend that every student use the first part of the course to familiarize themselves with the data so that they can make an informed decision about their project preferences**
