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
#     display_name: Python [conda env:dsc]
#     language: python
#     name: conda-env-dsc-py
# ---

# %% [markdown]
# # setup

# %%
import sys, os
from datetime import datetime
import sqlite3

# import sqlalchemy
import pyexasol
import pandas as pd
import numpy as np

from credentials import Credentials
from helper import SimulateID, analyze_sim_kpi
import config

# %%
assert os.getcwd().rsplit("/", 1)[-1] == '_create'

# %%
sys.path.append("./sql")
import sql.broadcast, sql.target_group, sql.cdm, sql.broadcast_target_group_cdm

# %%
print(sql.broadcast_target_group_cdm.query)

# %%
credentials = Credentials(path="/mnt/c/Users/spa0001f/.hasselhoff")

# %%
not_connected = True
count = 0
while not_connected:
    try:
        connection = pyexasol.connect(dsn=credentials.exasol.dsn,
                             user=credentials.exasol.write.user,
                             password=credentials.exasol.write.key, compression=True)
    except:
        count = count + 1
        print(f"connection attempt {count} to exasol was not succesful")
    else:
        print("connected to exasol")
        not_connected = False

# %%
# df = connection.export_to_pandas("SELECT DISTINCT sender FROM bids_universe_source_gfk.ausstrahlungen")

# %%
# full_.columns()

# %% [markdown]
# # directly export to pandas -> full
# - not advise because I get pandas warning of mixed types, the reason is that pyexsol.connect().export_to_pandas exports to a csv and then uses pd.read_csv -> update: it works now

# %%
print(sql.broadcast_target_group_cdm.query)

# %%
connection.execute(sql.cdm.query).columns()

# %%
full = connection.export_to_pandas(sql.broadcast_target_group_cdm.query)

# %%
full.info()

# %% [markdown]
# ## lower case columns -> oder sollen das die studenten machen? sie sollen dann ein mapping erstellen, die spalte an dieser stelle nicht verändern sondern konsistent mit quelle lassen

# %% [markdown]
# ## compute market share

# %%
full = full.assign(MARKET_SHARE = lambda x: (x['SEHB'] / x['TVG']) * 100)

# %% [markdown]
# ## new keys: full -> df: INPUT REQUIRED
# - run_id
# - title_id
# - a_id
# - c_id
# - l_id

# %%
if False:
    import importlib
    import helper
    importlib.reload(helper)
    from helper import SimulateID, analyze_sim_kpi

# %%
simulate_id = (
    SimulateID(full)
    .assign_sim_id('RUN_KEY', 100000)
    .assign_sim_id('TITELID', 30000)
    .assign_sim_id('A_ID', 5000)
    .assign_sim_id('C_ID', 7000)
    .assign_sim_id('C_SERIE_ID', 4000)
    # .assign_sim_id('L_ID', 3000)
)

# %%
df = simulate_id.df

# %%
df.columns

# %%
IDS = ['RUN_KEY', 'TITELID', 'A_ID', 'C_ID'] # , 'L_ID']

(
    df
    [IDS + [f"{k}_SIM" for k in IDS]]
    .dropna()
    .head(10))

# %% [markdown]
# ## simulate sehb, tvg, kinobesucher

# %% [markdown]
# ### no grouping w.r.t. movies and series: obsolete (?)

# %% code_folding=[0]
if False:
    import numpy as np
    from numpy.random import default_rng
    rng = default_rng()

    scale = 0.25
    rnd = lambda x: rng.beta(0.5, 0.5, len(df))
    """
    a_ = rng.random(len(df)) * scale - scale / 2
    w_ = rng.random(len(df)) * scale * a_ - (scale * a_) / 2
    (w_/a_).min()

    a = 1 + a_
    w = 1 + w_
    """
    a = 1 + rnd(0) * scale - scale / 2
    w_a = 1 + rnd(0) * scale - scale / 2  #  = df['MARKET_SHARE']/df['MARKET_SHARE_SIM']
    w = a / w_a
    print(f"{(w_a).max()=}, {(w_a).min()=}")
    print(f"{w.min()=}, {w.max()=}")



# %% code_folding=[0]
if False:
    df['TVG_SIM'] = df['TVG'] * a
    df['SEHB_SIM'] = df['SEHB'] * w  # SEHB_SIM darf nicht größer als tvg sein, kann passieren
    cond = df['SEHB_SIM'] > df['TVG_SIM']
    df.loc[cond, 'SEHB_SIM'] = df.loc[cond, 'TVG_SIM']
    df['MARKET_SHARE_SIM'] = (df['SEHB_SIM'] / df['TVG_SIM']) * 100

# %%
# analyze_sim_kpi(df, 'MARKET_SHARE')

# %%
# analyze_sim_kpi(df, 'SEHB', round_ = 3)

# %%
# analyze_sim_kpi(df, 'TVG', round_ = 3)

# %% [markdown]
# ### group w.r.t. TITELID

# %%
from typing import Callable
from numpy.random import default_rng

rng = default_rng()
scale = 0.25  # determines the spread of the random data around the true data
rnd = lambda n: (1 + rng.beta(0.5, 0.5, 1) * scale - scale / 2).squeeze()
multiply_sehb = 0.9  # decrease sehb sim and ma sim

def get_sim_kpis(df, rnd: Callable[int, float], scale: int = 1.74):  # rnd returns a random number
    a = rnd(1) * scale
    w_a = rnd(1)
    w = w_a * a
    
    df = df.copy() # do not mutate within apply https://pandas.pydata.org/docs/user_guide/gotchas.html#mutating-with-user-defined-function-udf-methods
    df['TVG_SIM'] = df['TVG'] * a 

    df['SEHB_SIM'] = df['SEHB'] * w  * multiply_sehb # SEHB_SIM darf nicht größer als tvg sein, kann passieren
    cond = df['SEHB_SIM'] > df['TVG_SIM']
    df.loc[cond, 'SEHB_SIM'] = df.loc[cond, 'TVG_SIM']

    df['MARKET_SHARE_SIM'] = (df['SEHB_SIM'] / df['TVG_SIM']) * 100
    df['C_HOECHSTE_BESUCHERZAHL_D_SIM'] = df['C_HOECHSTE_BESUCHERZAHL_D'] * w_a
    df['a'] = a
    df['w_a'] = w_a
    df['w'] = w
    
    return df


# %%
df = (
    df
    .groupby(['TITELID'])  # do not group w.r.t TARGET_GROUP here, not necessary (?)
    .apply(lambda x: get_sim_kpis(x, rnd)))

# %%
# df.iloc[:, -20:].head(10)

# %%
# df[df['TITELID'] == 1024716]['C_ID']

# %%
if False:
    cond_movies_and_series = df['GENRE_1'].isin(['Spielfilm', 'Serie', 'Animation'])
    movies_and_series = df[cond_movies_and_series].copy() # 37%
    other = df[~cond_movies_and_series].copy() # 63%

# %%
analyze_sim_kpi(df, 'SEHB', round_ = 3)

# %%
analyze_sim_kpi(df, 'TVG', round_ = 3)

# %%
analyze_sim_kpi(df, 'MARKET_SHARE', round_ = 3)

# %%
analyze_sim_kpi(df, 'C_HOECHSTE_BESUCHERZAHL_D', round_ = 3)

# %% [markdown]
# # NEW: Simulate licenses

# %%
# df['L_BEGINN'] = pd.to_datetime(df['L_BEGINN'])
# df['L_ENDE'] = pd.to_datetime(df['L_ENDE'])
# df['STARTZEIT_TS_DR'] = pd.to_datetime(df['STARTZEIT_TS_DR'])

# %% [markdown]
# ## current

# %%
_df = df

# %%
max_ld_id_sim = df['L_ID'].max()
max_runs = _df['L_IST_AUS'].drop_duplicates().squeeze()
cols = ['L_ID', 'A_WIEVIELTER_RUN', 'L_BEGINN', 'L_ENDE', 'L_IST_AUS']


def first_runs(_df):
    max_runs = _df['A_WIEVIELTER_RUN'].max()
    one_run = max_runs == 1
    first_runs = _df['A_WIEVIELTER_RUN'] < max_runs
    if one_run:
        _df1 = _df.assign(L_IST_AUS_SIM = 1, L_STATUS = 'one_run')
    else:
        _df1 = (
            _df
            [first_runs]
            .assign(
                L_IST_AUS_SIM = max_runs - 1, L_STATUS = 'first_runs'))
    return _df1

def last_runs(_df):
    max_runs = _df['A_WIEVIELTER_RUN'].max()
    one_run = max_runs == 1
    last_run = _df['A_WIEVIELTER_RUN'] == _df['A_WIEVIELTER_RUN'].max()
    if one_run:
        return pd.DataFrame(columns=_df.columns)
    else:
        _df2 = _df[last_run].assign(L_IST_AUS_SIM = 1, L_STATUS = 'last_run')
        return _df2


_temp = ( # for each unique run_key get first_runs and last_runs
    _df
    .dropna(subset=['L_ID'])
    .drop_duplicates(['RUN_KEY'])  # [L_ID, A_WIEVIELTER_RUN, A_WH] statt RUN_KEY? -> eher nicht
    .sort_values(['A_WIEVIELTER_RUN']))
_grouped = _temp.groupby(['L_ID'])

_df1 = _grouped.apply(first_runs).reset_index(level=0, drop=True)  # drop index 'L_ID' so that the index is the old index
_df2 = _grouped.apply(last_runs).reset_index(level=0, drop=True)  # drop index 'L_ID' so that the index is the old index

assert _temp.shape[0] == _df1.shape[0] + _df2.shape[0]


# %%
# _df1

# %% code_folding=[0]
def transform_l_ende(col: pd.Series):
    col = col.copy()
    cond1 = col.str.startswith('9999-12-31')
    cond2 = col.isna()
    cond = cond1 | cond2
    col[~cond] = (pd.to_datetime(col[~cond]) + pd.to_timedelta(rng.integers(1, 33) + 17, unit='D')).astype(str)
    return col

# after groupby
_df1 = _df1.assign(
        # L_STATUS = 'first_runs',
        L_ID_NEW = lambda x: x['L_ID'],
        L_BEGINN_SIM = lambda x: (pd.to_datetime(x['L_BEGINN']) - pd.to_timedelta(rng.geometric(0.2, x.shape[0]) + 63, unit='D')).astype(str),  
        L_ENDE_SIM = lambda x: transform_l_ende(x['L_ENDE']),
        A_WIEVIELTER_RUN_SIM = lambda x: x['A_WIEVIELTER_RUN'])
_df2 = _df2.assign(
        # L_STATUS = 'last_run',
        L_ID_NEW = lambda x: x['L_ID'] + max_ld_id_sim, # need new ld_id_sim
        L_BEGINN_SIM = lambda x: (pd.to_datetime(x['STARTZEIT_TS_DR']) - pd.to_timedelta(rng.geometric(0.2, x.shape[0]) + 72, unit='D')).dt.floor('D').astype(str),
        L_ENDE_SIM = lambda x: (pd.to_datetime(x['STARTZEIT_TS_DR']) + pd.to_timedelta(rng.geometric(0.2, x.shape[0]) + 13, unit='D')).dt.floor('D').astype(str), # need to this this here because L_ENDE has values that are too large to be converted into a pd.Timestamp
        A_WIEVIELTER_RUN_SIM = 1)
    
_combined = pd.concat([_df1, _df2])  # drop index 'L_ID'
_index = _combined.index
# 
_out = (
    SimulateID(
        _combined.sort_values(by=['STARTZEIT_TS_DR', 'SENDER', 'ZIELGRUPPE']))
    .assign_sim_id('L_ID_NEW', 3000)
    .df
)
assert _out['L_ID_NEW_SIM'].notna().all() # important, otherwise the following merge explodes because L_ID has missings

# %%
license_cols2collect = [
    'L_ID_NEW', 'L_ID_NEW_SIM', 'L_STATUS', 'L_BEGINN_SIM', 'L_ENDE_SIM', 'A_WIEVIELTER_RUN_SIM', 'L_IST_AUS_SIM']
license_cols = ['RUN_KEY', 'TITEL', 'SENDER', 'ZIELGRUPPE', 'STARTZEIT_TS_DR',
    'L_ID', 'A_REDAKTION_BESTOF', 'L_BEGINN', 'L_ENDE', 'L_IST_AUS', 'A_WIEVIELTE', 'A_WIEVIELTER_RUN', 'A_WH',
]

# %%
_out[license_cols + license_cols2collect].head()

# %% code_folding=[0]
if False:
    license_sim = (
         _df.dropna(subset=['L_ID'])
        .join(
            _out[license_cols2collect],
        ))
    license_sim.index.name = None
    assert license_sim.shape[0] == _df.loc[_df['L_ID'].notna()].shape[0]
    license_sim

# %% code_folding=[]
if True:
    license_sim = (
     _df.dropna(subset=['L_ID'])[['RUN_KEY']].reset_index()
    .merge(
        _out[['RUN_KEY'] + license_cols2collect],
        how='left',
        on=['RUN_KEY'])
    .set_index('index'))
    license_sim.index.name = None
    assert license_sim.shape[0] == _df.loc[_df['L_ID'].notna()].shape[0]
    license_sim

# %%
fully_merged = df.join(
    license_sim,
    rsuffix="_")
assert fully_merged.shape[0] == df.shape[0]

# %%
if False:
    fully_merged = df.join(
    _out[['L_ID_NEW', 'RUN_KEY'] + license_cols2collect],
    rsuffix="_")
    assert fully_merged.shape[0] == df.shape[0]

# %%
_check = fully_merged.dropna(subset=['L_ID'])
pd.testing.assert_series_equal(
    _check['RUN_KEY'],
    _check['RUN_KEY_'],
    check_names=False)

# %%
df = fully_merged

# %%
if False:
    _check[license_cols + license_cols2collect].drop_duplicates('RUN_KEY')

# %%
if False:
    _a = _check[license_cols + license_cols2collect].drop_duplicates('RUN_KEY')
    _a[_a['L_ID'] == 2330030.0]

# %%
if False:
    cond = _a['A_WIEVIELTER_RUN'] > _a['L_IST_AUS']
    cond.sum() / cond.shape[0]  # knapp 5%

# %%
if False:
    cond = _a['A_WIEVIELTER_RUN'] != _a['A_WIEVIELTE'] 
    cond.sum() / cond.shape[0]

# %%
if False:
    _a.set_index('L_ID').loc[3073513.0]

# %%
if False:
    _a[cond][_a[cond]['L_ID'].duplicated(keep=False)].sort_values(['L_ID']).set_index('L_ID') # .loc[1654681.0]

# %%
if False:
    cond = _a['A_WIEVIELTE'] > _a['L_IST_AUS']
    cond.sum() / cond.shape[0]  # 0 

# %% [markdown]
# # save full tables as csv:df -> df_export -> table_dc

# %%
# df.columns

# %% code_folding=[0]
if False:
    mapping = {
        'RUN_KEY': 'RUN_KEY_SIM',
        'TITELID': 'TITELID_SIM',
        'C_ID': 'C_ID_SIM'
    }

# %% code_folding=[]
# tables = ['broadcast', 'target_group', 'cdm', 'mapping', 'joined']
today = datetime.now().strftime("%Y_%m_%d")

# %% code_folding=[0]
if False:
    format_ = 'csv'
    tables = ['broadcast', 'target_group', 'cdm', 'mapping', 'joined']
    today = datetime.now().strftime("%Y_%m_%d")
    for table in tables:
        if table == 'joined':
            cols = df.columns
        elif table == 'mapping':
            cols = list(mapping.values())
        else:
            cols = list(connection.execute(getattr(sql, table).query).columns().keys())
            for k, v in mapping.items():
                if k in cols:
                    cols = cols + [v]
        path = f"./csv/{today}/{table}.{format_}"
        os.makedirs(f"./csv/{today}", exist_ok=True) 
        df.to_csv(path, columns=cols, sep=";", index=False, compression=format_)

# %% code_folding=[0]
if False:
    # zip
    format_ = 'zip'
    tables = ['broadcast', 'target_group', 'cdm', 'mapping_gfk_cdm', 'joined']
    today = datetime.now().strftime("%Y_%m_%d")
    for table in tables:
        if table == 'joined':
            cols = df.columns
        elif table == 'mapping':
            cols = list(mapping.values())
        else:
            cols = list(connection.execute(getattr(sql, table).query).columns().keys())
            for k, v in mapping.items():
                if k in cols:
                    cols = cols + [v]
        path = f"./csv/{today}/{table}.{format_}"
        os.makedirs(f"./csv/{today}", exist_ok=True) 
        df.to_csv(path, columns=cols, sep=";", index=False, compression=format_)

# %% [markdown]
# ## column_mapping: INPUT REQUIRED

# %% code_folding=[]
column_mapping = {
    # broadcast
    'RUN_KEY': 'RUN_ID_TRUE',
    'RUN_KEY_SIM': 'RUN_ID',
    'TITELID': 'TITLE_ID_TRUE',
    'TITELID_SIM': 'TITLE_ID',
    'TITEL': 'TITLE',
    'SENDER': 'CHANNEL',
    'STARTZEIT_TS_DR': 'START_TIME',
    'ENDEZEIT_TS_DR': 'END_TIME',
    'STARTZEIT_TS': 'START_TIME_AGF',
    'ENDEZEIT_TS': 'END_TIME_AGF',
    'WOCHENTAG': 'WEEKDAY',
    'DAUER': 'DURATION',
    'GENRE_1': 'GENRE',
    # 'GENRE_2': 'GENRE_2',
    # 'GENRE_3': 'GENRE_3',
    'WIEDERHOLUNG': 'REPETITION',
    # target_group
    'ZIELGRUPPE': 'TARGET_GROUP',
    'SEHB': 'SEHB_TRUE',
    'TVG': 'TVG_TRUE',
    'MARKET_SHARE': 'MARKET_TRUE',
    'SEHB_SIM': 'SEHB',
    'TVG_SIM': 'TVG',
    'MARKET_SHARE_SIM': 'MARKET_SHARE',
    # cdm
    'A_ID': 'A_ID_TRUE',
    'A_ID_SIM': 'A_ID',
    'A_BESTSELLER_WIEVIELTE': 'A_INTERNAL_REPETITION_NUMBER',
    'C_ID': 'C_ID_TRUE',
    'C_ID_SIM': 'C_ID',
    'C_CONTENT': 'C_CONTENT',
    'C_SERIE_ID': 'C_SERIES_ID_TRUE',
    'C_SERIE_ID_SIM': 'C_SERIES_ID',
    'C_SERIE': 'C_SERIES',
    'C_ORIGINALTITEL': 'C_ORIGINAL_TITLE',
    'C_AUFLISTREIHENF': 'C_EPISODE_NUMBER',
    'C_PRODUKTIONSSTAFFEL_STAFFEL_NR': 'C_SEASON_NUMBER',
    'C_PRODJAHR_VON': 'C_YEAR_OF_PRODUCTION',
    'C_SERIE_KATEGORIE': 'C_SERIES_CATEGORY_1',
    'C_SERIE_VERWENDBARKEIT': 'C_SERIES_CATEGORY_2',
    'C_ERSTESPRODUKTIONSLAND': 'C_COUNTRY_OF_PRODUCTION',
    'C_HOECHSTE_BESUCHERZAHL_D': 'C_HIGHEST_NUMBER_OF_VISITORS_GERMANY_TRUE',
    'C_HOECHSTE_BESUCHERZAHL_D_SIM': 'C_HIGHEST_NUMBER_OF_VISITORS_GERMANY',
    'L_ID': 'L_ID_TRUE',
    'L_BEGINN': 'L_START_TRUE',
    'L_ENDE': 'L_END_TRUE',
    'A_WIEVIELTER_RUN': 'A_WIEVIELTER_RUN_TRUE',
    'A_WIEVIELTE': 'A_WIEVIELTE',
    'A_REDAKTION_BESTOF': 'A_REDAKTION_BESTOF',
    'L_IST_AUS': 'L_IST_AUS_TRUE',
    'L_ID_NEW_SIM': 'L_ID',
    'L_BEGINN_SIM' : 'L_START',
    'L_ENDE_SIM': 'L_END',
    'A_WIEVIELTER_RUN_SIM': 'A_LICENSE_RUN',
    'L_IST_AUS_SIM': 'L_NUMBER_OF_RUNS',
    'A_WH': 'A_WH',
    #
    'a': 'WEIGHT_SEHB',
    'w': 'WEIGHT_TVG',
    'w_a': 'WEIGHT_MA'
}

# %% code_folding=[0]
if False:
    flat_table_columns = {}
    for k, v in column_mapping.items():
        if 'TRUE' in v:
            continue
        else:
            flat_table_columns[k] = v
    flat_table_columns

# %%
df_export = df.rename(columns=column_mapping)
df_export.columns

# %%
df_export.info()

# %% code_folding=[0]
if False:
    table = {}
    table['flat_table'] = df_export[flat_table_columns.values()]
    table['mapping_gfk_cdm'] = df[['RUN_KEY_SIM', 'A_ID_SIM']].rename(columns=column_mapping)
    table['mapping_sim'] = df_export[IDS + [f"{k}_TRUE" for k in IDS] + ['WEIGHT_SEHB', 'WEIGHT_TVG', 'WEIGHT_MA']]

    temp = list(connection.execute(getattr(sql, table).query).columns().keys())
    table['broadcast'] = df[temp + ['RUN_KEY_SIM', 'TITELID_SIM']].rename(columns=column_mapping)

    table_columns['target_group'] = list(connection.execute(getattr(sql, table).query).columns().keys())

# %% [markdown]
# ## table_columns mapping: INPUT REQUIRED

# %%
table_columns = {}
table_columns['broadcast'] = ['RUN_ID', 'TITLE_ID', 'TITLE', 'CHANNEL', 'START_TIME', 'END_TIME',
                              'START_TIME_AGF', 'END_TIME_AGF',
       'WEEKDAY', 'DURATION', 'GENRE', 
                              # 'GENRE_2', 'GENRE_3', 
                              'REPETITION']
table_columns['target_group'] = ['RUN_ID'] + ['TARGET_GROUP', 'SEHB', 'TVG']
table_columns['cdm'] = [
        'A_ID', 'A_INTERNAL_REPETITION_NUMBER', 'A_LICENSE_RUN', 'A_WH',
        # 'B_ID', 'B_INTERNAL_REPETITION_NUMBER', 
        'C_ID', 'C_CONTENT', 
        'C_SERIES_ID', 'C_SERIES',
                        # 'C_ORIGINAL_TITLE', 
                        'C_EPISODE_NUMBER',
       'C_SEASON_NUMBER', 'C_YEAR_OF_PRODUCTION', 'C_SERIES_CATEGORY_1',
       'C_SERIES_CATEGORY_2', 'C_COUNTRY_OF_PRODUCTION',
       'C_HIGHEST_NUMBER_OF_VISITORS_GERMANY',
       'L_ID', 'L_START', 'L_END', 'L_NUMBER_OF_RUNS']
new_ids = ['RUN_ID', 'TITLE_ID', 'A_ID', 'C_ID', 'C_SERIES_ID']
table_columns['mapping_gfk_cdm'] = ['RUN_ID', 'A_ID']
table_columns['mapping_sim'] = ['RUN_ID'] + [f"{k}_TRUE" for k in new_ids] + ['WEIGHT_SEHB', 'WEIGHT_TVG', 'WEIGHT_MA']
table_columns['flat_table'] = df_export.columns  # list(flat_table_columns.values())

# %%
(
    df_export[table_columns['broadcast']].drop_duplicates('RUN_ID').shape[0]
    / df_export[table_columns['broadcast']].shape[0])  # 0.199

# %%
df_export[table_columns['broadcast']].drop_duplicates('RUN_ID').shape[0]  # 688124

# %%
df_export[table_columns['target_group']].shape[0]  # 3448515

# %%
(
    df_export.dropna(subset='A_ID').drop_duplicates('A_ID').shape[0]
    / df_export.dropna(subset='A_ID').shape[0])  # 0.197

# %%
df_export.dropna(subset='A_ID').drop_duplicates('A_ID').shape[0]  # 151834

# %%
(
    df_export.dropna(subset='A_ID').drop_duplicates('A_ID').shape[0]
    / df_export.dropna(subset='A_ID').shape[0])  # 0.19732

# %% [markdown]
# ## drop duplicates and missings: (df_export, table_columns) -> table_dc

# %%
table_dc = {}

# %%
# 688124*5

# %%
# df_export.shape[0] / 5

# %%
# table_dc['broadcast'].shape[0]

# %%
# df_export.drop_duplicates(subset=['RUN_ID']).shape

# %%
# df_export.drop_duplicates(subset=['RUN_ID', 'A_ID']).shape

# %%
# unique_a_id = (df_export.groupby(['RUN_ID'])['A_ID'].size() == 5)

# %%
# unique_a_id[~unique_a_id]

# %%
# full[full['RUN_KEY'] == '202012072347421072110641319']

# %%
# df_export[df_export['RUN_ID'] == 637116]

# %%
# c_ = df_export.drop_duplicates(subset=['RUN_ID', 'A_ID']).duplicated(keep=False, subset=['RUN_ID'])

# %%
# df_export.drop_duplicates(subset=['RUN_ID', 'A_ID'])[c_]

# %%
table_dc['broadcast'] =  (
    df_export
    .drop_duplicates('RUN_ID')  # duplicates because left join with target group
    [table_columns['broadcast']])
assert table_dc['broadcast']['RUN_ID'].notna().all()

# %%
# new
if False:
    table_dc['broadcast'] =  (
        df_export
        .drop_duplicates(['RUN_ID', 'A_ID'])  # duplicates because left join with target group
        [table_columns['broadcast']])
    assert table_dc['broadcast']['RUN_ID'].notna().all()

# %%
table_dc['target_group'] = df_export[table_columns['target_group']]

# %%
table_dc['mapping_gfk_cdm'] = (
    df_export
    .dropna(subset=['A_ID']) # missing because broadcast is left joined with cdm and cdm is filtered for spielfilm, serie & animation
    .drop_duplicates('RUN_ID')
    [table_columns['mapping_gfk_cdm']])

# %%
# new
if False:
    table_dc['mapping_gfk_cdm'] = (
    df_export
    .dropna(subset=['A_ID']) # missing because broadcast is left joined with cdm and cdm is filtered for spielfilm, serie & animation
    .drop_duplicates(['RUN_ID', 'A_ID'])
    [table_columns['mapping_gfk_cdm']])

# %%
table_dc['cdm'] = (
    df_export
    .dropna(subset=['A_ID']) # missing because broadcast is left joined with cdm and cdm is filtered for spielfilm, serie & animation
    .drop_duplicates('A_ID') # we could have duplicate A_IDs if a run contains 3 a.m.
    [table_columns['cdm']])

# %%
table_dc['mapping_sim'] = (
    df_export
    .drop_duplicates('RUN_ID')
    [table_columns['mapping_sim']])

# %%
# table_dc['flat_table'] = df_export[table_columns['flat_table']]  # no need to save flat table because I can reproduce ft below

# %%
# table_dc['flat_table'].shape

# %%
ft = (
    table_dc['broadcast']
    .merge(table_dc['target_group'], on=['RUN_ID'], how='left')  # passt
    .merge(table_dc['mapping_gfk_cdm'], on=['RUN_ID'], how='left') # passt
    .merge(table_dc['cdm'], on='A_ID', how='left') # passt
    .merge(table_dc['mapping_sim'], on='RUN_ID', how='left')
    .sort_values(['START_TIME', 'CHANNEL', 'TARGET_GROUP'])
)

# %%
assert ft.shape[0] == df_export.shape[0]

# %%
assert (ft['RUN_ID'] == df_export['RUN_ID']).all()

# %%
# assert (ft['A_ID'] == df_export['A_ID']).all()  # does not hold because of duplicates in matching_gfk_cdm

# %%
# c_ = df_export['A_ID'].isin(ft['A_ID'])

# %%
# c_ = ft['A_ID'].fillna(0) == df_export['A_ID'].fillna(0)

# %%
# df_export[~c_]

# %%
# df_export.dropna(subset=['A_ID']).head()

# %% [markdown]
# ## export

# %%
# path_csv = "/home/spa0001f/github/dsc/data/create/csv"
# today = lambda: datetime.now().strftime("%Y_%m_%d")

# %%
# config.save_csv = False

# %%
# table_dc.keys()

# %%
today

# %%
# format_ = 'zip'  # compression
format_ = config.format_
if config.save_csv:
    os.makedirs(os.path.join(config.path_csv, today), exist_ok=True) 
for name, df_ in table_dc.items():
    path_ = os.path.join(config.path_csv, today, f"{name}.{format_}")
    if config.save_csv:
        df_.to_csv(path_, sep=";", index=False, compression=format_)
        print(f"{path_} created")
    else:
        print(f"{path_} is not created")

# %% [markdown]
# # Load data

# %%
load_data = False  # set this only manually to True

# %%
# load_data = True
# config.path_load_csv = '/home/spa0001f/github/teach/dsc/data/_create/csv/2022_10_11'

# %%
if load_data:
    table_dc = {}
    for _file in os.listdir(config.path_load_csv):
        _name = _file.rsplit(".", maxsplit=1)[0]
        _path = os.path.join(config.path_load_csv, _file)
        print("loading", _name, _path)
        table_dc[_name] = pd.read_csv(_path, sep=";", compression=config.format_)

# %%
print(
table_dc['broadcast']['START_TIME'].min(),"\n",
table_dc['broadcast']['START_TIME_AGF'].min())

# %%
print(
table_dc['broadcast']['START_TIME'].max(),"\n",
table_dc['broadcast']['START_TIME_AGF'].max())

# %%
table_dc['broadcast'].drop_duplicates('RUN_ID')[['START_TIME', 'START_TIME_AGF']]

# %%
# table_dc['broadcast']['START_TIME'].min()

# %% [markdown]
# # Quick fix: Remove rows from CDM where L_ID is missing

# %%
table_dc['cdm'] = table_dc['cdm'].dropna(subset=['L_ID'])

# %%
assert table_dc['cdm']['L_ID'].notna().all()
assert table_dc['broadcast']['RUN_ID'].notna().all()

# %% [markdown]
# # filter broadcast, target_group, mapping_gfk_cdm, cdm w.r.t. date: table_dc -> table_filtered

# %%
table_dc['broadcast']['START_TIME'] = (
    pd.to_datetime(table_dc['broadcast']['START_TIME']))  # do not use .dt.date because this becomes an object dtyp

table_dc['broadcast']['END_TIME'] = (
    pd.to_datetime(table_dc['broadcast']['END_TIME']))  # do not use .dt.date because this becomes an object dtype

# %%
bounds = [
    table_dc['broadcast']['START_TIME'].min() - pd.Timedelta(seconds=1), # should start at 02:59:59
    pd.Timestamp('2019-12-31 23:59:59') + pd.Timedelta(hours=3),
    pd.Timestamp('2020-12-31 23:59:59') + pd.Timedelta(hours=3),
    pd.Timestamp('2021-12-31 23:59:59') + pd.Timedelta(hours=3),
    table_dc['broadcast']['END_TIME'].max(),  # this end at 02:59:59
]

# %%
lower_upper = list(zip(bounds[:-1], bounds[1:]))
lower_upper

# %% [markdown]
# ## table_filtered

# %%
table_filtered = {}
a_id = []
for lb, ub in lower_upper:
    bound_str = ub.date().strftime("%Y_%m_%d")
    bound_str = (ub - pd.Timedelta(days=1)).date().strftime("%Y_%m_%d")  # data goes until this day and 3 a.m.
    cond_lb = table_dc['broadcast']['START_TIME'] > lb
    cond_ub = table_dc['broadcast']['END_TIME'] <= ub
    cond = cond_lb & cond_ub

    table_filtered[bound_str] = {}
    table_filtered[bound_str]['broadcast'] = table_dc['broadcast'][cond].copy()
    filtered_run_ids = table_filtered[bound_str]['broadcast']['RUN_ID']

    table_filtered[bound_str]['target_group'] = (
        table_dc['target_group']
        [table_dc['target_group']['RUN_ID'].isin(filtered_run_ids)]).copy()
    table_filtered[bound_str]['mapping_gfk_cdm'] = (
        table_dc['mapping_gfk_cdm']
        [table_dc['mapping_gfk_cdm']['RUN_ID'].isin(filtered_run_ids)]).copy()
    table_filtered[bound_str]['cdm'] = (
        table_dc['cdm']
        [table_dc['cdm']['A_ID'].isin(table_filtered[bound_str]['mapping_gfk_cdm']['A_ID'])]).copy()
    a_id.extend(table_filtered[bound_str]['cdm']['A_ID'].tolist())

# %% [markdown]
# ## checks

# %%
ls_ = []
for k, v in table_filtered.items():
    ls_.append(pd.Series(list(map(lambda x: x.shape[0], v.values()))))
check_ = pd.concat(ls_, axis=1)
check_.index = ['broadcast', 'target_group', 'mapping_gfk_cdm', 'cdm']
check_.columns = table_filtered.keys()
check_

# %%
if False:
    ls_ = []
    for k, v in table_filtered.items():
        ls_.append(pd.Series(list(map(lambda x: x.shape[0], v.values()))))
    check_ = pd.concat(ls_, axis=1)
    check_.index = ['broadcast', 'target_group', 'mapping_gfk_cdm', 'cdm']
    check_.columns = table_filtered.keys()
    check_

# %%
if False:
    check_ = check_.assign(
    sum=check_.sum(axis=1),
    true=[table_dc[k].shape[0] for k in check_.index],
    diff=lambda x: x['true'] - x['sum'],
    rel_diff=lambda x: x['diff']/x['true'])
    check_

# %%
check_ = check_.assign(
    sum=check_.sum(axis=1),
    true=[table_dc[k].shape[0] for k in check_.index],
    diff=lambda x: x['true'] - x['sum'],
    rel_diff=lambda x: x['diff']/x['true'])
check_

# %%
assert (abs(check_['rel_diff']) < 0.01).all()

# %%
table_filtered['2019_12_31']['broadcast'].describe(include='all', datetime_is_numeric=True)[['START_TIME', 'END_TIME']]

# %%
table_filtered['2021_12_31']['broadcast'].describe(include='all', datetime_is_numeric=True)[['START_TIME', 'END_TIME']]

# %% [markdown]
# ## quick fixes

# %% [markdown]
# ### remove start_time and end_time from broacasts

# %%
for key in table_filtered.keys():
    table_filtered[key]['broadcast'] = table_filtered[key]['broadcast'].drop(columns = ['START_TIME', 'END_TIME'])

# %% [markdown]
# ### rename A_ID to B_ID and A_INTERNAL_REPETITION_NUMBER, REPETITION, A_WH, A_LICENSE_RUN

# %%
for key in table_filtered.keys():
    table_filtered[key]['cdm'] = table_filtered[key]['cdm'].rename(
        columns = {
            'A_ID': 'B_ID',
            'A_INTERNAL_REPETITION_NUMBER': 'B_INTERNAL_REPETITION_NUMBER',
            'A_LICENSE_RUN': 'B_LICENSE_RUN',
            'A_WH': 'B_QUICK_REPEAT'})
    table_filtered[key]['mapping_gfk_cdm'] = table_filtered[key]['mapping_gfk_cdm'].rename(
        columns = {'A_ID': 'B_ID'})
    table_filtered[key]['broadcast'] = table_filtered[key]['broadcast'].rename(
        columns = {'REPETITION': 'REPEAT'})

# %% [markdown]
# ## add event & holiday

# %%
first_date = list(table_filtered.keys())[0]

# %%
table_filtered[first_date]['event'] = connection.export_to_pandas("SELECT * FROM BIDS_UNIVERSE_SOURCE_MANUELL.EVENTS")
table_filtered[first_date]['holiday'] = connection.export_to_pandas("SELECT * FROM BIDS_UNIVERSE_SOURCE_MANUELL.FEIERTAGE")

# %% [markdown]
# ## NEW: round datetime column downwards to 5 minutes

# %%
for key in table_filtered.keys():
    table_filtered[key]['broadcast']['START_TIME_AGF_5MIN'] = (
        pd.to_datetime(table_filtered[key]['broadcast']['START_TIME_AGF']).dt.floor('5min').astype(str))
    table_filtered[key]['broadcast']['END_TIME_AGF_5MIN'] = (
        pd.to_datetime(table_filtered[key]['broadcast']['END_TIME_AGF']).dt.floor('5min').astype(str))

# %%
table_filtered[key]['broadcast'][['END_TIME_AGF', 'END_TIME_AGF_5MIN']]

# %%
for key in table_filtered.keys():
    table_filtered[key]['broadcast']['START_TIME_AGF'] = table_filtered[key]['broadcast']['START_TIME_AGF_5MIN'].copy()
    table_filtered[key]['broadcast']['END_TIME_AGF'] = table_filtered[key]['broadcast']['END_TIME_AGF_5MIN'].copy()
    table_filtered[key]['broadcast'] = table_filtered[key]['broadcast'].drop(columns = ['START_TIME_AGF_5MIN', 'END_TIME_AGF_5MIN'])
    # table_filtered[key]['broadcast'] = table_filtered[key]['broadcast'].drop(columns = ['START_TIME_AGF', 'END_TIME_AGF'])

# %% [markdown]
# ## NEW: Multiply Sehb & TVG and cast to int
# - Note: since SEHB and TVG is simulated the number of decimal places is not 7 but more

# %%
for key in table_filtered.keys():
    table_filtered[key]['target_group']['SEHB_'] = (table_filtered[key]['target_group']['SEHB'] * 1e6).round()
    table_filtered[key]['target_group']['TVG_'] = (table_filtered[key]['target_group']['TVG'] * 1e6).round()

# %%
for key in table_filtered.keys():
    table_filtered[key]['target_group']['SEHB'] = table_filtered[key]['target_group']['SEHB_']
    table_filtered[key]['target_group']['TVG'] = table_filtered[key]['target_group']['TVG_']
    table_filtered[key]['target_group'] = table_filtered[key]['target_group'].drop(columns = ['SEHB_', 'TVG_'])

# %% [markdown]
# ## NEW: ROUND Kinobesucher

# %%
for key in table_filtered.keys():
    table_filtered[key]['cdm']['C_HIGHEST_NUMBER_OF_VISITORS_GERMANY'] = (
        table_filtered[key]['cdm']['C_HIGHEST_NUMBER_OF_VISITORS_GERMANY'].round())

# %% [markdown]
# # save partial tables as csv

# %%
path_csv_public = config.path_csv_public

# %%
# config.save_csv_public = True
config.path_csv_public = "/home/spa0001f/github/teach/dsc/data/csv/"

# %%
format_ = config.format_  # compression
for _date, _dc in table_filtered.items():
    for _name, _df in _dc.items():
        _folder = os.path.join(path_csv_public, _date)
        if config.save_csv_public:
            os.makedirs(_folder, exist_ok=True)
        _path = os.path.join(_folder, f"{_name}.{format_}")
        if config.save_csv_public:
            _df.to_csv(_path, sep=";", index=False, compression=format_)
            print(f"{_path} created")
        else:
            print(f"{_path} was not created")

# %% [markdown]
# # build database

# %%
os.getcwd()

# %%
os.chdir("/home/spa0001f/github/teach/dsc")

# %%
assert os.getcwd() =='/home/spa0001f/github/teach/dsc'

# %%
os.system("python3 ./data/create_database.py")

# %% [markdown]
# # STOP

# %%
assert False, "stop here"

# %% [markdown]
# # build databases

# %%
if False:
    import zipfile
    path = f"./csv/{today}/mapping.{format_}"
    zf = zipfile.ZipFile(path) 
    dfm = pd.read_csv(zf.open('mapping'), sep=";")

# %%
path

# %%
table_names = list(table_columns.keys())
table_names.remove('flat_table')
table_names.remove('mapping_sim')
table_names.remove('broadcast')
table_names = [broadcast_filtered] + table_names
table_names

# %% [markdown]
# ## read csv

# %%
path2csv = './csv/2022_09_12'
format_ = "zip"
tables_dc = {}
for table in table_names:
    path = f"./csv/{today}/{table}.{format_}"
    tables_dc[table] = pd.read_csv(path, sep=";", compression=format_)

# %%

# %%
# today = datetime.now().strftime("%Y_%m_%d")
s_connection = sqlite3.connect("./database/dsc.db")

# %%
# continue here, use simulated keys and kpis and drop original kpis -> do this before the csvs are created, need to create a mapping table then
# also rename columns

# %%
for table in tables:
    tables_dc[table].to_sql(table, con=s_connection, index=False)

# %%
cursor = s_connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")  # query and print all the tables in the database engine
print(cursor.fetchall())

# %% [markdown]
# # sqlite

# %%
df.columns

# %%
s_connection = sqlite3.connect("./database/dsc.db")

# %% [markdown]
# ## broadcasts

# %%
cols = connection.execute(sql.broadcast.query).columns()
list(cols.keys())
list(cols.values())

type_ = {}
for key, value in cols.items():
    type_[key] = value['type']
type_

for key, value in type_.items():
    if value in ['DECIMAL']:
        type_[key] = 'REAL'
    else:
        type_[key] = 'TEXT'
        
type_

# %%
df.columns

# %%
cursor = s_connection.cursor()

# %%
sqlite_query = """ CREATE TABLE IF NOT EXISTS TEST
    (RUN_ID INTEGER, TITLE TEXT)"""
cursor.execute(sqlite_query)
s_connection.commit()
s_connection.close()

# %%
s_values = list(df.iloc[:, :2].head().replace(np.nan, None).itertuples(index=False, name=None))
s_values

# %%
s_connection = sqlite3.connect("./database/dsc.db")
cursor = s_connection.cursor()
# cursor.execute("INSERT INTO TEST VALUES (1, 'ABC')")
cursor.executemany("INSERT INTO TEST VALUES (?, ?)", s_values)  # always need a tuple of ? here, so use (?,) if only one value should be inserted
# s_connection.commit()  # if I do not commit then the changes do not remain if the connection is closed

# %%
select_all = cursor.execute("SELECT * FROM TEST")  # this is an iterator

# %%
select_all.fetchall()

# %%
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")  # query and print all the tables in the database engine
print(cursor.fetchall())

# %%
s_connection.close()

# %% [markdown]
# # sqlalchemy

# %%
import sqlalchemy as db

# %%
engine = db.create_engine("sqlite:///database/dsc.db") #  three slashes for a relative path https://stackoverflow.com/a/70834382, can create multiple connections

# %%
a_connection = engine.connect()

# %%
metadata = db.MetaData()
test = db.Table('Test', metadata, autoload=True, autoload_with=engine)
query = db.select([test])
result_proxy = a_connection.execute(query)
result_set = result_proxy.fetchall()

# %%
result_set

# %%
query2 = test.insert().values(RUN_ID=2, TITLE='YXZ')  # see 7:30 how to insert several rows: https://www.linkedin.com/learning/advanced-python-working-with-databases/solution-create-an-sqlite-database?autoSkip=true&autoplay=true&resume=false&u=70943858
a_connection.execute(query2)
result_proxy = a_connection.execute(query)
result_set = result_proxy.fetchall()
result_set

# %%

# %%

# %% [markdown]
# # use execute and fetch

# %%
full_ = connection.execute(sql.broadcast_target_group_cdm.query)

# %%
a = full_.fetchall()

# %%
pd.DataFrame(a[0:10]).fillna(np.nan) # .dtypes

# %% [markdown]
# ## column info for each query (might be useful later on)

# %%
connection.execute(sql.broadcast.query).columns()

# %%
connection.execute(sql.target_group.query).columns()
