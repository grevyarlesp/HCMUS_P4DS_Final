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
# > TLDR: You are free to share, adapt, and create derivative works from The Public 2021 Stack Overflow Developer Survey Results as long as you attribute Stack Overflow, keep the database open (if you redistribute it), and continue to share-alike any adapted database under the ODbl.
#
#
# 3.  How did authors collect data?
#
# Data are collected by survey

# %% [markdown]
# ## Exploring Data

# %% [markdown]
# ### Checking the data folder

# %%
DATA_DIR = './data/stack-overflow-developer-survey-2021/'
# files = !ls $DATA_DIR 
files = [file for file in files if '.csv' in file]
files

# %% [markdown]
# ### Reading data

# %%
df1 = pd.read_csv(os.path.join(DATA_DIR, files[0]))

# %%
df1

# %% [markdown]
# ### Questions

# %% [markdown]
# #### How many rows and columns?

# %%
num_rows, num_cols = df1.shape
num_rows, num_cols

# %% [markdown]
# #### What is the meaning of each row?

# %%
df1.columns

# %%
df1['OrgSize']

# %% [markdown]
#
# Answers to the questions on stackoverflow. A few we may care about:
#
# - MainBranch
# - Employment 
# - Country 
# - EdLevel : Education level
# - Age1stCode: The age at which they first code
# - LearnCode: Where they learn code.
# - YearsCode: Number of years they have been coding
# - YearsCodePro: number of years they have been coding professionally
# - DevType:  type of developer
# - OrgSize: size of the companies they are working at
# - ConvertedCompYearly: converted yearly compensation in US dollar
# - LanguageHaveWorkedWith : languages they have worked with
# - LanguageWantToWorkWith
# - MiscTechHaveWorkedWith: NumpY, TensorFlow, Flutter, Qt
# - MiscTechWantToWorkWith
# - OpSys: Their primary operating system
# - Age: Age group they belong to
# - NEWCollabToolsWantToWorkWith: developmenet environment (Vim,PyCharm, Notepad, Sublime,...)
# - NEWCollabToolsHaveWorkedWith: developmenet environment (Vim,PyCharm, Notepad, Sublime,...)
# - Gender
#
# Refer to the questions sheet for more detail.

# %%
cols = [
    'MainBranch', 'Employment', 'Country', 'EdLevel', 'Age1stCode', 'LearnCode', 
    'YearsCode', 'YearsCodePro','DevType', 'OrgSize', 'ConvertedCompYearly', 'LanguageHaveWorkedWith',
    'LanguageWantToWorkWith', 'LanguageWantToWorkWith', 'MiscTechHaveWorkedWith',
    'MiscTechWantToWorkWith', 'NEWCollabToolsWantToWorkWith', 'NEWCollabToolsHaveWorkedWith',
    'OpSys', 'Age', 'Gender'
    
]
numerical_cols = np.array([
    'YearsCode', 'YearsCodePro', 'ConvertedCompYearly'
])

categorical_cols = np.array([
    'MainBranch', 'Employment', 'Country', 'EdLevel', 'Age1stCode',
    'DevType', 'OrgSize', 'OpSys', 'Age', 'Gender'
    
])

df1 = df1[cols]

# %% [markdown]
# #### Are there duplicated rows?

# %%
have_duplicated_rows = df1.duplicated()
have_duplicated_rows = have_duplicated_rows.any()
have_duplicated_rows, df1.duplicated().sum()

# %% [markdown]
# So there are 3 duplicated rows
#

# %% [markdown]
# #### What is the current data type of each column? Are there columns having inappropriate data types?

# %%
pd.DataFrame(df1.dtypes)

# %% [markdown]
# There are quite many rows with inapproriate data types...: YearsCode, YearsCodePro

# %% [markdown]
# ####  With each numerical column, how are values distributed?
#
# -  What is the percentage of missing values?
# -  Min? max? Are they abnormal?

# %%
numerical_cols

# %%
df1.loc[:, numerical_cols[0:2]] = df1.loc[:, numerical_cols[0:2]].replace('More than 50 years', '50.1')
df1.loc[:, numerical_cols[0:2]] = df1.loc[:, numerical_cols[0:2]].replace('Less than 1 year', '0.9')
df1.loc[:, numerical_cols[0:2]] = df1[numerical_cols[0:2]].astype(np.float64)


# %%
def missing_rate(s):
    return s.isna().sum() / len(s)
    
num_cols_info = df1[numerical_cols].agg([min, max, pd.DataFrame.mean, missing_rate])
num_cols_info

# %% [markdown]
# There are many rows with missing values.

# %% [markdown]
# #### With each categorical column, how are values distributed?
#
# - What is the percentage of missing values?
# - How many different values? Show a few. Are they abnormal?

# %%
df1[categorical_cols]

# %%

cate_cols_info = df1[categorical_cols].agg([missing_rate, pd.Series.unique, pd.Series.nunique])
cate_cols_info

# %%

# %% [markdown]
# ## Ask meaningful questions

# %% [markdown]
# - Countries with highest average salary?
# - Are salaries dependence on programming level?
# - Top 5 countries with the highest average salaries. 
# - Top 5 programming language.
# - Ratio of male and female working professionally?
# - Most commonly used text editor / IDE for each operating system.

# %% [markdown]
# ## Preprocessing data to answer the questions

# %% [markdown]
# ### Answering questions

# %% [markdown]
# #### Countries with highest average salaries

# %% [markdown] tags=[]
# ## Reflection

# %% [markdown]
# ## References

# %% [markdown]
#
#
