# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Final Project

# %%
import sys
sys.executable

# %% [markdown]
# ## Group 11: 
#
# | MSSV     | Họ tên         | Github                                        |
# |----------|----------------|-----------------------------------------------|
# | 19127535 | Trần Kiến Quốc | [grevyarlesp](https://github.com/grevyarlesp) |
# | 19127637 | Nguyễn Khắc Vỹ | [Khacvy1707](https://github.com/Khacvy1707)   |
#
# ## Dependencies

# %%
import pandas as pd
import os
import numpy as np

# %% [markdown]
# ## Collecting Data
#
# 1. What subject is your data about? What is the source of your data?
#
# Answers to StackOverflow Developer Survey 2021
#
# 2. Do authors of this data allow you to use like this? You can check the data license
#
# https://stackoverflow.blog/2021/08/30/the-full-data-set-for-the-2021-developer-survey-now-available/
#
# > Note you are free to share, adapt, and create derivative works from the public 2021 Stack Overflow Developer Survey results as long as you attribute them to Stack Overflow, keep the database open (if you redistribute it), and continue to share-alike any adapted database under the ODbL.
#
# 3.  How did authors collect data?
#
# Data are collected by survey

# %% [markdown]
# ## Exploring Data

# %% [markdown]
# Checking the data folder

# %%
DATA_DIR = './data/stack-overflow-developer-survey-2021/'
# files = !ls $DATA_DIR 
files = [file for file in files if '.csv' in file]
files

# %% [markdown]
# Reading data

# %%
df1 = pd.read_csv(os.path.join(DATA_DIR, files[0]))

# %%
df1

# %% [markdown]
# 1. How many rows and columns?

# %%
num_rows, num_cols = df1.shape
num_rows, num_cols

# %% [markdown]
# 2. What is the meaning of each row?

# %%
df1.columns

# %% [markdown]
# Là các câu trả lời cho các câu hỏi

# %% [markdown]
# 3. Are there duplicated rows?
#

# %%
have_duplicated_rows = df1.duplicated()
have_duplicated_rows = have_duplicated_rows.any()
have_duplicated_rows

# %% [markdown]
# So there are no duplicated rows

# %% [markdown]
# 5. What is the current data type of each column? Are there columns having inappropriate data types?

# %%
df1.dtypes

# %% [markdown]
# There are quite many rows with inapproriate data types...

# %% [markdown]
# 6.  With each numerical column, how are values distributed?
#
# -  What is the percentage of missing values?
# -  Min? max? Are they abnormal?

# %%
df1.min(),df1.max()

# %% [markdown]
# There are many rows with missing values.

# %% [markdown]
# 7. With each categorical column, how are values distributed?
#
# - What is the percentage of missing values?
# - How many different values? Show a few. Are they abnormal?

# %%
df1.nunique()

# %% [markdown]
# ## Ask meaningful questions

# %% [markdown]
# - Top 5 countries with the highest average salaries. 
# - Top 5 programming language.
# - Are salaries dependence on programming level?
# - Ratio of male and female working professionally.
# - 

# %% [markdown]
# ## Preprocessing data to answer the questions

# %% [markdown]
# Dropping columns with high misisng value rates 

# %%
temp_series = df1.isna().sum() / len(df1)
temp_series = list(temp_series[temp_series < 0.6].index)
df1 = df1[temp_series]
df1

# %% [markdown] tags=[]
# ## Reflection

# %% [markdown]
# ## References

# %% [markdown]
#
#
