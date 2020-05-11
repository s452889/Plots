import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd options (display settings)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 1000)
# read csv
df_schema = pd.read_csv('survey_results_schema.csv')
df_survey = pd.read_csv('survey_results_public.csv',
                        usecols=['Respondent', 'OpSys', 'Age', 'WorkWeekHrs'],
                        index_col=['Respondent'])
df_survey = df_survey.dropna()
# filter data (it is impossible to work more than 168 hours per week)
df_survey = df_survey[(df_survey['WorkWeekHrs'] < float(168)) & (df_survey['Age'] < float(80)) &
                      (df_survey['Age'] > float(10))]
# unique values in column as list
unique_values = df_survey.OpSys.unique()
# show plot for every unique value in 'OpSys' column
for i in unique_values:
    # filter data
    x = df_survey[df_survey['OpSys'] == i]
    # plot settings
    plt.plot(x['Age'], x['WorkWeekHrs'], 'ro', markersize=1)
    plt.xlabel('Age')
    plt.ylabel('WorkWeekHrs')
    plt.title(i)
    plt.show()

