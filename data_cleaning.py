#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:54:08 2020

@author: vigneshshenbagarajan
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

#salary estimate

df.columns

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

salary = salary.apply(lambda x: x.replace('$',''))

df['Salary'] = salary

df['Hourly'] = df['Salary'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

df['employer_provided'] = df['Salary'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']    

df['salary_minuskd'] = df['Salary'].apply(lambda x: x.replace('K',''))

df['salary_final'] = df['salary_minuskd'].apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['salary_final'] = df['salary_final'].str.strip()

df['min_salary'] = df['salary_final'].apply(lambda x: x.split('-')[0])

df['max_salary'] = df['salary_final'].apply(lambda x: x.split('-')[1])

df['min_salary'] = df['min_salary'].astype(int)
df['max_salary'] = df['max_salary'].astype(int)

df['avg_salary'] = (df['min_salary']+df['max_salary'])/2


#company name

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)


#age

df['age'] = df['Founded'].apply(lambda x: x if x<1 else 2020-x)

# Job state and headquarters

df['state'] = df.Location.apply(lambda x: x.split(',')[1])

df['state'] = df.state.apply(lambda x: x.replace('Los Angeles','CA'))

df.state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis=1)


#parsing of job description (python, etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark 
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws 
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()


df_final = df.drop(['Unnamed: 0'], axis =1)


df_final.columns

df_final.to_csv('data_cleaned.csv',index = False)

