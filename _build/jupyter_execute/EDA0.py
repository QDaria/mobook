#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
file_path = '/Users/mo/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/MoNAVbucopy/data/181_nov1.csv'
df = pd.read_csv(file_path);df.head()


# In[14]:


df.apply(pd.Series.nunique)


# In[15]:


df.columns


# In[18]:


df = df[['PID', 'ARENA_TILTAKDELTAKER_ID', 'ARENA_TILTAKGJENNOMFORING_ID', 'TILTAKGJENNOMFORINGHIST_ID', 'KJONN', 
        'FODSEL_AAR', 'FODSEL_MND', 'DATO_FRA', 'DATO_TIL', 'DELTAKERSTATUSKODE', 'REG_DATO', 'DELTAKERTYPEKODE',
        'PERSON_ORG_ENHET_AFNR', 'ARENA_ENHET_KODE', 'ARENA_ENHET_NAVN','PERSON_GEOGRAFI_ID', 'KOMMUNENAVN',
        'FYLKESNAVN','PM_BEGIN_DATE','PM_END_DATE']]


# In[19]:


df.head()


# In[20]:


df.apply(pd.Series.nunique)


# In[21]:


df.dtypes


# In[26]:


min(df['PM_END_DATE']), max(df['PM_END_DATE'])


# In[28]:


df['PM_END_DATE'] = pd.to_datetime(df['PM_END_DATE'], errors = 'coerce')
df.dtypes


# In[29]:


df['PM_BEGIN_DATE'] = pd.to_datetime(df['PM_END_DATE'], errors = 'coerce')
df['DATO_FRA'] = pd.to_datetime(df['DATO_FRA'], errors = 'coerce')
df['DATO_TIL'] = pd.to_datetime(df['DATO_TIL'], errors = 'coerce')
df['REG_DATO'] = pd.to_datetime(df['REG_DATO'], errors = 'coerce')
df.dtypes


# In[30]:


from faker import Faker
fake = Faker()


random_date = fake.date_between_dates(min(df['PM_END_DATE']), max(df['PM_END_DATE']))
random_date


# In[46]:


df.dtypes


# In[47]:


df['PM_END_DATE'] = pd.to_datetime(df['PM_END_DATE'], errors = 'coerce')
df.dtypes


# In[ ]:


for column in df.select_dtypes(include=['object']).columns:
    df[column] = df[column].astype(pd.StringDtype())
df.dtypes


# In[31]:


# Count how many rows in df with NaT
df['PM_END_DATE'].isnull().sum()


# In[39]:


df['PM_BEGIN_DATE'].isnull().sum()


# In[ ]:


# replace every NaT rows in df['PM_END_DATE'] with random_date converted to pandas.core.series.Series 
df['PM_END_DATE'] = df['PM_END_DATE'].fillna(random_date)
df['PM_END_DATE']

df['PM_END_DATE'].isnull().sum()


# In[ ]:


d.open_browser()
dtale.instances() 


# In[48]:


ilename = ""
    sep = ","
    dft = AV.AutoViz(
          filename,
          sep=",",
          depVar="",
          dfte=df,
          cheader=0,
          verbose=1,
          lowess=True,
          bchart_format="bokeh",
          max_rows_analyzed=150000,
          max_cols_analyzed=30,
          save_plot_dir=None
    )    


# In[ ]:


def main():
    dtale.show(df, subprocess=False)
    ######## Autoviz ###########
    data_cleaning_suggestions(df)
    #autoviz = AutoViz_Class().AutoViz('train.csv')
    filename = ""
    sep = ","
    dft = AV.AutoViz(
        filename,
        sep=",",
        depVar="",
        dfte=df,
        header=0,
        verbose=1,
        lowess=True,
        chart_format="bokeh",
        max_rows_analyzed=150000,
        max_cols_analyzed=30,
        save_plot_dir=None
    )    


# In[45]:


import dtale
import dtale.app as dtale_app
from pandas_profiling import ProfileReport
import sweetviz as sv
from autoviz.AutoViz_Class import AutoViz_Class
from autoviz import data_cleaning_suggestions
#from dataprep.datasets import load_dataset
#from dataprep.eda import create_report
import klib
import dabl
from datatile.summary.df import DataFrameSummary

dfs = DataFrameSummary(df)
dfs.summary()

if __name__ == '__main__':
    
    ######## dtale ###########
    dtale.show(df, subprocess=False)
    #dtale_app.JUPYTER_SERVER_PROXY = True
    
    ######## pandas-profiling #########
    profile = ProfileReport(df, explorative=True)
    profile.to_file("181.html")                              #Saving results to a HTML file
                              
    ######## Sweetviz ##########
    sweet_report = sv.analyze(df)
    #Saving results to HTML file
    sweet_report.show_html('sweet_181_report.html')
    
    ######## dataprep #########
    #create_report(df).show_browser()
    
    ######## Klib ###########
    klib.missingval_plot(df)
    df= klib.data_cleaning(df)
    klib.corr_plot(df, annot=False)
    klib.corr_plot(df, split='pos', annot=False)
    klib.corr_plot(df, split='neg', annot=False)
    klib.corr_plot(df, target='DELTAKERSTATUSKODE')
    klib.corr_mat(df)
    klib.dist_plot(df['DELTAKERTYPEKODE'])
    klib.cat_plot(df, figsize=(50,15))
    plot = klib.corr_plot(df, annot=False, figsize=(12,10))
    plot.figure.savefig('figure.pdf')
    
    ########## dabl ###########
    dabl.plot(df, target_col="Survived")
    
    ######### datatile
    dfs = DataFrameSummary(df)
    dfs.summary()


# In[ ]:





# In[ ]:




