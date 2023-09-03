```python
import pandas as pd

from dsc.notebook import embed_website
from dsc.introduction.data import (
    path2db, channels, potential, example_pin, viewing_duration)
```

# Data description
In this course, we will be working with german (free) **linear TV data**.

Linear TV broadcasts scheduled programs, over the air or through satellite/cable, but not streamed to a specific user.
Almost all broadcast television services count as linear TV.

The **TV program** lists the title and start time of all broadcasts for each day and channel.


```python
embed_website("https://www.hoerzu.de/tv-programm/")
```





<iframe
    width="900"
    height="500"
    src="https://www.hoerzu.de/tv-programm/"
    frameborder="0"
    allowfullscreen

></iframe>




In Germany, there are two different types of broadcasters which broadcast linear TV.
- **Public broadcasters** like the ARD or ZDF whose primary mission is public service. Public broadcasters receive their funding primarily from a licence fee which every household, company and public institution are required to pay by law.
- **Private/commercial broadcasters** like the RTL group or ProSiebenSat.1 are privately owned corporate media.
    - **free**: Commercial broadcasting primarily uses the airing of advertisements for profit.
    - **paid**: Some servies are paid for by local subscribers, e.g. Sky.

# How broadcast data is collected

The TV program can be used to infer the title and duration of all broadcasts for each channel and day and is freely available.
For private broadcasting the success, i.e., the **audience rating**, of a broadcast is crucial for the price of corresponding advertisements.
Audience ratings are **not publicly available and measured by the AGF**.

The AGF is the **association of TV and streaming providers in Germany** on whose behalf audience ratings in the German motion picture market are measured since April 1st, 1963 (!). The AGF further develops the continuous quantitative recording of the use of motion picture content in Germany, including the collection and evaluation of the data.

<div align="center" style="font-size:16px;">
AGF members
<img src="./figures/1_agf.png" alt="AGF members" width=800/>
<div/>
<div align="left" style="font-size:14px;">
<div/>

## The AGF panel

At the core of AGF's audience research is the **AGF Panel**, which AGF operates in cooperation with **GfK**.
- The AGF Panel is a **representative sample** of “the resident population of the Federal Republic of Germany in private households with at least one TV set in use and a German-speaking Main Income Earner.”
- This universe represents the television usage of approximately **38 million TV households with up to 75 million individuals** over age 3 (as of January 1, 2022).
- Moreover, once a year, panel households are surveyed with a questionnaire covering **demographic and consumer behaviour** from which target groups for analyses and pricing of advertisements can be constructed.

Source: https://www.agf.de/en/audience-measurement/method/tv

**Relation between the panel and the population**
<br>
<br>
<img src="./figures/1_agf_gfk_panel.png" alt="AGF/GFK Panel" width=1800/>

### Audio matching

- TV usage is measured exclusively with an **audio matching** measurement technique.
- The measurement devices generate audio samples at the TV set and compare them against broadcasters’ audio samples generated at central referencing sites. The matched signals are assigned to a broadcaster.

<img src="./figures/1_audio_match.png" alt="AGF/GFK Panel" width=1200/>

<div align="center" style="font-size:14px;">
On the next website, scroll below for the 'TAM METER'! :D
<div/>
<div align="left" style="font-size:14px;">
<div/>


```python
embed_website("https://www.agf.de/en/about-agf/history", height=800, width=1400)
```





<iframe
    width="1400"
    height="800"
    src="https://www.agf.de/en/about-agf/history"
    frameborder="0"
    allowfullscreen

></iframe>




### PIN data

The AGF collects so called **PIN data**.
- PIN data are **person-specific data on television usage** (measured in seconds)
- It measures  the number of seconds that a person has spent watching a programme, commercial break or pre-defined time interval.
- PIN data is measured each day **from 3 a.m. in the morning until 3 a.m. the next day**, e.g., the date "2020-01-01" corresponds to the interval [2020-01-01 03:00:00, 2020-01-02 02:59:59]
- Preliminary data for the previous AGF day (until 3 a.m. today) is then available from 8 a.m.
- Final data is available 2 day later


```python
example_pin
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>member_id</th>
      <th>channel</th>
      <th>start</th>
      <th>end</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>No-TV</td>
      <td>2020-01-01 03:00:00</td>
      <td>2020-01-01 14:11:59</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>ARD</td>
      <td>2020-01-01 14:12:00</td>
      <td>2020-01-01 17:59:59</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>P7</td>
      <td>2020-01-01 18:00:00</td>
      <td>2020-01-01 20:00:00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>RTL</td>
      <td>2020-01-01 20:00:01</td>
      <td>2020-01-01 23:30:01</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>No-TV</td>
      <td>2020-01-01 23:30:00</td>
      <td>2020-01-02 02:59:59</td>
    </tr>
  </tbody>
</table>
</div>



## KPIs

PIN data can be used to compute aggreated **KPIS for target groups, time intervals and channels**.

- The most relevant target group for commercial broadcasters are Adults who are between 14 and 49 years old (**Erw. 14-49**).
- Z3+ is another target group which includes all members of the panel.

For simplicity, let's assume for the remainder of this section that there are only two channels ARD and P7.

### Sehdauer (sehd)

For a given channel, time interval and target group:
- The viewing duration of a corresponding panel member is the number of seconds viewed.
- The **sehd** is the (weighted) average of all individual viewing durations.

Viewing duration for the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]


```python
viewing_duration
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>member_id</th>
      <th>weight</th>
      <th>target_group</th>
      <th>channel</th>
      <th>start</th>
      <th>end</th>
      <th>viewing_duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>50</td>
      <td>Erw. 14-49</td>
      <td>ARD</td>
      <td>2020-01-01 15:00:00</td>
      <td>2020-01-01 16:29:59</td>
      <td>0 days 01:30:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>50</td>
      <td>Erw. 14-49</td>
      <td>P7</td>
      <td>2020-01-01 16:30:00</td>
      <td>2020-01-01 16:59:59</td>
      <td>0 days 00:30:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>25</td>
      <td>Erw. 14-49</td>
      <td>No-TV</td>
      <td>2020-01-01 15:00:00</td>
      <td>2020-01-01 15:59:59</td>
      <td>0 days 01:00:00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>25</td>
      <td>Erw. 14-49</td>
      <td>ARD</td>
      <td>2020-01-01 16:00:00</td>
      <td>2020-01-01 16:59:59</td>
      <td>0 days 01:00:00</td>
    </tr>
  </tbody>
</table>
</div>




```python
sehd = (
    viewing_duration
    [viewing_duration['channel'] != 'No-TV']
    .groupby(['channel'])
    .apply(lambda x:
           (x['viewing_duration'] @ x['weight'])
           / potential))  # potential is the sum of the member_id weights
```

Sehd for the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]


```python
sehd
```




    channel
    ARD   0 days 01:20:00
    P7    0 days 00:20:00
    dtype: timedelta64[ns]



### Sehbeteiligung (sehb)

**Sehbeteiligung (sehb)** is a measure of average viewing participation. When we talk about reach we often mean sehb.
- For a given channel, time interval and target group, the relative Sehb is the ratio of the viewing duration (sehd) and the corresponding time interval.
- The (absolute) Sehb is the relative Sehb scaled to the population of people that should be represented.
- Note that Sehb is not the number of viewers.


Sehb (in millions) the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]

Relative sehb for the time interval [2020-01-01 15:00:00, 2020-01-01 16:59:59]


```python
rsehb = sehd / pd.Timedelta(hours=2)
round(rsehb, 2)
```




    channel
    ARD    0.67
    P7     0.17
    dtype: float64




```python
sehb = rsehb * potential
sehb
```




    channel
    ARD    50.0
    P7     12.5
    dtype: float64



**Sehb vs. number of viewers**
  - In the digital world, e.g., streaming, the number of viewers are often the people who started to watch a program, independent of their viewing time.
  - Thus, if all people watch 1 one-second of a one-hour programm, the relative reach is 100% in the digital world.
  - However, the corresponding Sehb (= relative "reach") in the TV world is only 1/3600 = 0.028 %.
  - Comparing reach of TV and digital formats should take this into account (!)

### TV-Gesamt (TVG)

For a given target group and time interval, TVG is the Sehb of all channels.

TVG (in millionns)


```python
tvg = sehb.sum()
tvg
```




    62.5



### Market share (ms)

The **market share** is the most relevant KPI for measuring the (relative) performance of a program.
- (Short-term) pricing of advertisements is based on the market share
- The renewal or cancellation of a TV series is based on the market share

The market share is given by the ratio of Sehb and TVG.


```python
market_share = (sehb / tvg) * 100
market_share
```




    channel
    ARD    80.0
    P7     20.0
    dtype: float64



### Actual numbers
The following website displays sehb (VP) and market shares (MS) of today.


```python
embed_website("https://www.agf.de/en/data/tv-data", width=1600, height=700)
```





<iframe
    width="1600"
    height="700"
    src="https://www.agf.de/en/data/tv-data"
    frameborder="0"
    allowfullscreen

></iframe>




## Concluding remarks

- Among other things, the AGF is responsible for measuring the audience of linear TV and operates the AGF panel in cooperation with the GFK.
- As a result, linear TV broadcast performance data are often referred to as AGF/GFK data.
- The established KPIs are recognized as the market standard for the media and advertising industry.
- The most important KPIs are Sehb, TVG and the market share.
- Although the number of measurement units is far smaller than in the digitial world, AGF/GFK data contains the exact viewing duration and detailed information about demographics and consumer behavio


# Internal data

Besides AGF/GFK data KPI each broadcaster has internal data that is not accessible to other broadcasters or agencies.
- Internal data which includes further information about programs, e.g., costs, availability, ..., or whether it is an
    - In-house production (e.g., taff, red)
    - Commissioned production (e.g., GNTM)
    - Licensed program (Big bang theory)
- Purchased additional brodcast meta data
    - DMB
    - Gracenote
- Other data

# Accessing the data

- Unfortunately, KPI data provided by the AGF can not be used in this course due to copyright reasons.
- Similarly, we can not use internal data.
- However, KPI data about television usage has been simulated with a focus on capturing the main features of the real data.
- In addition, internal data has been generated with the idea to represent a possible scenario.
- Moreover, the database only contains the subset of tables and columns that are relevant for this course.
- Like real data, the synthetic data is not perfect and has inconsistencies to a small degree.

## Database: UNFINISHED

- The data is stored in an sqlite database located in {{path2db}}.
- The database will be updated each month with more data (!).
- The data can be accessed using the command-line shell https://www.sqlite.org/cli.html, an sql client software, or a python interface (sqlite3, sqlalchemy, pandas...).

For now, let's use an sql client software.

## Using an SQL client software like DBeaver

DBeaver is a multi-platform database tool for all people who need to work with databases.

The free **community edition** (CE) of DBeaver is an open source software and supports all common SQL Databases (https://dbeaver.io/).

A closed-source **enterprise edition** of DBeaver is distributed under a commercial license has support of NoSQL databases and cloud (https://dbeaver.com/edition/).

Comparison of DBeaver Community 22.2.0 vs. DBeaver PRO 22.1: https://dbeaver.com/edition/.

Some **useful features**:
- SQL queries execution
- Data browser/editor with a huge number of features
- Syntax highlighting and SQL auto-completion
- Database structure (metadata) browse and edit

**Please install the DBeaver community version**


```python
embed_website("https://dbeaver.io/", width=1600, height=700)
```





<iframe
    width="1600"
    height="700"
    src="https://dbeaver.io/"
    frameborder="0"
    allowfullscreen

></iframe>




## Database tables

### broadcast

The broadcast table represents the actual TV program. It has the following columns:
- RUN_ID: unique id of a broadcast that is unique for each datetime, title and channel. This is a primary key.
- TITLE_ID: unique id of a title.
- TITLE: title of the broadcast.
- CHANNEL: channel on which the broadcast was aired.
- START_TIME: starting time of the broadcast in terms of the AGF/GFK terminology.
- END_TIME: ending time of the broadcast in terms of the AGF/GFK terminology.
- WEEKDAY: weekday of the broadcast.
- DURATION: duration of the broadcast (excluding advertisements).
- GENRE: the genre of the broadcast.
- REPETITION: 'ja' if the broadcast is a repetition, 'no' if it is a first-run.



### target group

The table target group contains the following metrics related to the success of a broadcast:
- RUN_ID: unique id of a broadcast that is unique for each datetime, title and channel. This is a primary key.
- Target group: target group for which an KPI is measure for a RUN_ID.
- Sehb: the Sehb of this record.
- TVG: the TVG of this record.

Note that:
- All KPIs have been simulated and differ from the actual KPIs.
- The measured KPIs exclude advertisements, e.g., the Sehb is the Sehb of the program without the Sehb of
the advertisements and thus likely to be higher than the Sehb with advertisements

### content data mart (cdm): UNFINISHED


- Broadcast level
    - B_ID: unique identifier of a broadcast.
    - B_INTERNAL_REPETITION_NUMBER: Counts through the internal chronological broadcast order of the Content ID.

- Content/episode level
    - C_ID: unique identifier of a content. In cases of a feature film this identifies the feature film, in cases of a series this identifies the episode. A content can be broadcastet several times.
    - C_CONTENT: the (current) title of a content.
    - C_SEASON_NUMBER: The season of a series.
    - C_EPISODE_NUMBER: The episode number of a series.
    - C_YEAR_OF_PRODUCTION: Year of production.
    - C_SERIES_CATEGORY_1: Structural designation of a series.
    - C_SERIES_CATEGORY_2: Categorization of a series into Serial/Procedural/High Concept/Sitcom.
    - C_FSK: Classification of a content into an age-related release according to the classification of the FSK association.
    - C_HIGHEST_NUMBER_OF_VISITORS_GERMANY: Number of cinema visits in Germany.


### mapping_gfk_cdm

The table mapping_gfk_cdm only contains the columns RUN_ID and A_ID.
- AGF/GFK data uses the RUN_ID to identify a unique broadcast whereas the content data mart uses the A_ID to identify a broadcast.
- Since the AGF/GFK data is not internal data, there is no natural mapping between the AGF/GFK data and the content data mart.
- A mapping has been established using fuzzy title and datetime matching.
- Keep in mind that the mapping is mostly correct (in > 98% of the cases) but not always.

### events & holidays

- The table events contains public information about events that might influence TV audience behavior.
- The table holidays contains public information about German holidays.

# Projects

## Project 1: Forecasting the market shares of movies or series

<div align="center">
<img src="./figures/1_project_1.png" alt="Project 2" width=500 height=500/>
</div>
<div align="left">
</div>

- **Objective**: Forecast the market share of feature movies or series broadcasted during prime time in the next 6 weeks for the channels ProSieben, Sat.1 and Kabel eins.
    - You can choose whether you want to model movies or series (or both).
    - Group size: 3-4 people.
- **What will you do?**
    - Learn how to start with a simple model that already does quite well and how to improve it
    - Lots of feature engineering
    - Implement a custom split for cross validation
    - Optionally construct sophisticated features to approximate complex facts of the TV market

## Project 2: Forecasting monthly and annual KPIs per channel: UNFINISHED, evtl. nur monthly prognose? Weil ich die Daten nur ab 2015 bereitstelle, monatlich sollte ja auch passen, evtl. Daten für Projekt 3 auch ab 2010 bereitstellen?

<div align="center">
<img src="./figures/1_project_2.png" alt="Project 2" width=1000/>
<div/>
<div align="left">
</div>

- **Objective**: Forecast monthly and yearly market shares and sehb for the channels ProSieben, Sat.1 and Kabel eins up to 12 months and 5 years, respectively
    - Group size: 3 people
- **What will you do**?
    - Learn how to do time series forecasting
    - Learn how to do multi-step-ahead forecasting
    - Learn how to deal with seasonal patterns
    - Learn how to set up cross validation if the data has a temporal dimension

## Forecasting the usage time of licenses (UNFINISHED)

- little feature engineering
- find methods how to deal with this non-standard problem
- 2 people

<img src="./figures/1_project_3.png" alt="Project 2" width=1200 height=500/>
