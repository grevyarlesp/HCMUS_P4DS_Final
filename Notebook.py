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
# | MSSV     | Họ tên         | Github                                        |Email                         | 
# |----------|----------------|-----------------------------------------------|------------------------------|
# | 19127535 | Trần Kiến Quốc | [grevyarlesp](https://github.com/grevyarlesp) |19127535@student.hcmus.edu.vn | 
# | 19127637 | Nguyễn Khắc Vỹ | [Khacvy1707](https://github.com/Khacvy1707)   |nkvy19@clc.fitus.edu.vn       |
#
# Github Link: https://github.com/grevyarlesp/HCMUS_P4DS_Final/ 
#
# ## Dependencies

# %%
import pandas as pd
import os
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
plt.style.use('classic')

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

# %%
# unzip data
DATA_DIR = './data/stack-overflow-developer-survey-2021/'
try:
    os.makedirs(DATA_DIR)
    link = 'https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip'
    # !wget $link -P $DATA_DIR
    datafile = os.path.join(DATA_DIR, 'stack-overflow-developer-survey-2021.zip')
    # !unzip $datafile -d $DATA_DIR
    # !rm $datafile -f
except:
    pass

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
# - MainBranch: type of developer (self employed, professional, ...) 
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
# - NEWCollabToolsHaveWorkedWith: development environment (Vim,PyCharm, Notepad, Sublime,...)
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
df1[categorical_cols].head(10)

# %%

cate_cols_info = df1[categorical_cols].agg([missing_rate, pd.Series.unique, pd.Series.nunique])
cate_cols_info

# %% [markdown]
# ## Ask meaningful questions

# %% [markdown]
# 1. Top 10 countries with the highest average salaries.     
# 2. Top 10 programming language.
# 3. Most commonly used text editor / IDE for each operating system.
# 4. Most common type of developer in Vietnam?
# 5. How long does it take for a programmer to become a pro?

# %% [markdown]
# ## Preprocessing data to answer the questions

# %% [markdown]
# ### Answering questions

# %% [markdown]
# #### 1. Top 10 countries with the highest average salaries. 
#
# Salary is something that most working people are interested in and choosing the Top 10 countries with the highest average salaries will help a lot in choosing a programmer's working environment.
#
# To answer this, we only consider countries with more than 1000 respondents. 
#
# Countries with too low number of respondents might cause bias in the data.

# %%
salary_df = df1[['Country', 'ConvertedCompYearly']]
s = salary_df.groupby('Country').agg({'count', 'mean'})
s.columns = ['Average', 'Count']
s = s.loc[s['Count'] >= 1000]
s = s.sort_values(by = ['Average'], ascending = False)
s = s.head(10)

# %%
plt.figure()
plt.title("Top 10 countries with the highest average salaries")
s['Average'].plot.barh(color = 'green')

# %% [markdown]
# As expected, the US seems to have the highest compensation.
#
# The only representative of Asia is India, which proves that the resources for this industry in other Asian countries are still quite weak.
#
# European countries make up the majority of this ranking.
#
# If you intend to find another working environment abroad, the above countries are the top salary countries for you to choose.

# %% [markdown]
# #### 2. Top 10 programming language in 2021
#
# Programming languages are something that a programmer must know and the statistics of the Top 10 programming languages will help those who are in the learning process can choose to learn the most popular programming languages.

# %%
lang_df = pd.DataFrame(df1['LanguageHaveWorkedWith'].str.split(';').explode().reset_index()).groupby('LanguageHaveWorkedWith').count()
lang_df = lang_df.sort_values('index', ascending = False)
lang_df.columns = ['count']
display(lang_df.head(10))

# %% [markdown]
# The programming languages in the top 10 are all quite familiar and are used in popular industries such as software, AI, databases,...

# %% [markdown]
# Let's find out which language is the most popular amongst each type of developers. 

# %%
cols = ['MainBranch', 'LanguageHaveWorkedWith' ]
lang_df2 = df1[cols]
lang_df2.loc[:, cols[1]] = lang_df2[cols[1]].str.split(';').explode('LanguageHaveWorkedWith').dropna()
ans_lang_df = lang_df2.groupby(cols).size().to_frame('Size').reset_index().pivot(index = cols[0], columns = cols[1], values = 'Size').fillna(0)
display(ans_lang_df)

for idx in ans_lang_df.index:
    plt.figure()
    plt.title(idx)
    ans_lang_df.loc[idx].sort_values().plot.barh(color = 'lightblue')

# %% [markdown]
# Remarks: the histogram is quite similar in all categories, with JavaScript being a web scripting language at the top.
#
# Python is popular amongst students for its versatility.
#
# Most people know how to code Javascript, so if you want a job, then learn Javascript.

# %% [markdown]
# Similarly, let's look at the misc tech for each type of developer:

# %%
cols = ['MainBranch', 'MiscTechHaveWorkedWith' ]
tech_df = df1[cols]
tech_df.loc[:, cols[1]] = tech_df[cols[1]].str.split(';').explode('LanguageHaveWorkedWith').dropna()
ans_tech_df = tech_df.groupby(cols).size().to_frame('Size').reset_index().pivot(index = cols[0], columns = cols[1], values = 'Size').fillna(0)
display(ans_tech_df)

for idx in ans_lang_df.index:
    plt.figure()
    plt.title(idx)
    ans_tech_df.loc[idx].sort_values().plot.barh(color = 'lightblue')

# %% [markdown]
# NumPy is popular, because Python is popular. Pandas isn't as popular as Pandas for most cases.
#
# Despite Javascript popularity, React Native isn't more popular, surprisingly.

# %% [markdown]
# #### 3. Most commonly used text editor / IDE for each operating system.
#

# %%
temp_df = df1[['OpSys', 'NEWCollabToolsHaveWorkedWith']]
temp_df.loc[:, 'NEWCollabToolsHaveWorkedWith'] = temp_df['NEWCollabToolsHaveWorkedWith'].str.split(';')

tools_df = temp_df.explode('NEWCollabToolsHaveWorkedWith').groupby(['OpSys', 'NEWCollabToolsHaveWorkedWith']).size().to_frame('Size')
tools_df = tools_df.reset_index()
tools_df = tools_df.sort_values(['OpSys','NEWCollabToolsHaveWorkedWith'], ascending= False)
tools_df.columns = ['OpSys', 'Tools', 'Size']
tools_df = tools_df.pivot(columns = 'Tools', index = 'OpSys', values = 'Size')

for idx in tools_df.index:
    plt.figure()
    plt.title(idx)
    tools_df.loc[idx].sort_values().plot.bar(color = 'purple')

# %% [markdown]
# VSCode is the most popular on most platforms. 
#
# Vim is more popular on BSD, suprisingly. There must be a correlation between using BSD and using Vim. 
#
# Windows users tend to use VS and VSCode more. 

# %% [markdown]
# #### 4. Most common type of developer in Vietnam.
#
# Finding out the most common types of developer in Vietnam.

# %%
vn_df = df1[df1['Country'] == 'Viet Nam']
plt.figure()
plt.title("Most common type of developer in Vietnam.")
vn_df.groupby('MainBranch').size().plot.barh(color = 'lightblue')


# %% [markdown]
# The results show that, in Vietnam, there are many different types of developers and not everyone needs formal training to be able to code.

# %% [markdown]
# By education level: How many developers in VN have a Bachlelor's degree?

# %%
s = 'I am a developer by profession'
temp_df = vn_df[vn_df['MainBranch'] == s]
temp_df.groupby('EdLevel').size().plot.barh(color = 'orange')

# %% [markdown]
# So mostly they have a Bachelor's degree. 
#
# Because of the nature of this field, we can see that having a degree isn't necessary, but would make it easier. 

# %% [markdown]
# #### 5. How long does it take for a programmer to become a pro?
#
# People who are about to start learning programming are so interested in how long it will take them to become a       professional programmer and the answer to this question will help them know more about this.

# %% [markdown]
# To answer this question, we only use years for which figures are available.

# %%
year_df = df1[['YearsCode', 'YearsCodePro']]
year_df = year_df[year_df['YearsCodePro'].isna() != 1]
time_take_df = year_df['YearsCode'] - year_df['YearsCodePro']
time_take_df.mean().round(1)

# %% [markdown]
# It takes more than 5 years to become a pro programmer.
#
# The time taken is also relatively similar to the education time at universities and colleges.
#
# Statistical time shows that becoming a professional programmer does not take as long as people think. The difficulty of becoming a good programmer lies in the mindset, not the long, arduous training time.

# %% [markdown] tags=[]
# ## Reflection
# #### What difficulties have you encountered?
# Kiến Quốc: There are some challenges regarding using git to manage and version control Jupyter Notebook files. 
#
# Khắc Vỹ: Having some difficulty asking meaningful, factual questions about studying and working in the industry. Besides, collaborating on github also causes some difficulties for me.
#
# #### What have you learned?
# Kiến Quốc: Learned how to efficiently use Pandas, Numpy in this course and doing this project, and how to collaborate using git. 
#
# Khắc Vỹ: I have learned how to pose a problem and solve it with a dataset and processing steps in this course.
#
# #### If you had more time, what would you do?
# Group: We will approach more aspects of the IT industry through more meaningful questions and answers.

# %% [markdown]
# ## References

# %% [markdown]
# - Python Data Science Handbook
#
# - Lecture slides

# %% [markdown]
#
#
