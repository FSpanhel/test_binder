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

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the unique channels of the broadcast table.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the unique genres of the broadcast table.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the unique target groups of the target_group table.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the C_SERIES with the highest number of seasons from the cdm table.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Use the cdm table to get the minimal and maximum number of runs that are available for a license. 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Get the name of the 100th episode of the series FUTURAMA.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Broadcast data
# Note: You can find [here](https://www.sqlite.org/lang_datefunc.html) information about SQLite time and date functions.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### When does the data in the broadcast table start and end?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### What is the title with the longest duration?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Count the number of genres and sort them in ascending order.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Show the 10 most frequent start times of broadcasts. Can you explain why the most frequent start time is at the top?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### On which days are feature movies ("Spielfilm") broadcasted most frequently?

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Target group data
# Note: You can create a temporary table using
# ```
# CREATE TEMPORARY TABLE table_name AS 
# SELECT ... FROM ...
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Create a temporay table that contains for each run the corresponding KIPs of each target group.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### According to Sehb, what was the most successful broadcast for the target group 'Erw. 14-49'?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Investigate the yearly and monthly seasonality of TVG for the target group 'Erw. 14-49' and the channel 'ARD Das Erste'. What patterns do you observe?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Compute the market share for each run and target group.

# %% [markdown] slideshow={"slide_type": "slide"}
# ###  For each channel, compute the market share for the target group 'Erw. 14-49'.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Internal data

# %% [markdown] slideshow={"slide_type": "slide"}
# ### What is the average number of available runs per license?

# %% [markdown] slideshow={"slide_type": "slide"}
# ###  Find the C_CONTENT of the license with the maximal numbers of run.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Which C_CONTENT has the highest number of cinema visitors?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Join the cdm table to the broadcast table and store it as temporary table.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Count the number of broadcast genres that are available in the cdm table. Hint: A genre is only available in the cdm table if L_ID is not null.
