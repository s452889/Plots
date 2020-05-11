import pandas as pd
import matplotlib.pyplot as plt

# pd options (display settings)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 1000)
# read csv
df_schema = pd.read_csv('survey_results_schema.csv')
df_survey = pd.read_csv('survey_results_public.csv',
                        usecols=['Respondent', 'Age', 'WorkWeekHrs'],
                        index_col=['Respondent'])
# filter data (it is impossible to work more than 168 hours per week)
df_survey = df_survey[df_survey['WorkWeekHrs'] < float(168)]
df_survey = df_survey[(df_survey['Age'] < float(80)) & (df_survey['Age'] > float(10))]
# plot settings
plt.plot(df_survey['Age'], df_survey['WorkWeekHrs'], 'ro', markersize=1)
plt.xlabel('Age')
plt.ylabel('WorkWeekHrs')
# show plot
print(plt.show())
