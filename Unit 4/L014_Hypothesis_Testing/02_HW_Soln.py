## Imports
import pandas as pd
from numpy import sqrt
from scipy import stats as st

## Load DF
file_path = r'''https://raw.githubusercontent.com/
                the-codingschool/datascience/master/
                Unit%204/L014_Hypothesis_Testing/
                01_HW_SocialMedia_Data.csv''' #link to .csv file
for x in ['\n', '\t', ' ']:
        file_path = file_path.replace(x, '') #clean up the file path link
df = pd.read_csv(file_path) #read the csv
print(df.head()) #print the dataframe (optional)
print()

app_list = (list(df.columns))[1:] #list of social media app

## Analysis (Loop Through Each App)
for app in app_list:
    app_name = app.capitalize() #name of the app
    print(app_name)

    df_app = df[app] #data for the specific app

    ## Sample Statistics
    sample_mean = df_app.mean()
    sample_std = df_app.std()
    sample_n = df_app.count()

    ## Optional Print Statements 
    print('Sample Mean: {:.2f}'.format(sample_mean))
    print('Sample Standard Deviation: {:.2f}'.format(sample_std))
    print('Sample n: {}'.format(sample_n))

    ## Calculate Z Score
    null_mean = 5 #null hypothesis mean
    z = (sample_mean - null_mean)/(sample_std/sqrt(sample_n))
    print('Z Score: {:.2f}'.format(z))

    ## Calculate P Value
    z_use = -(abs(z))
    p_val = st.norm.cdf(z_use)
    print('p-value: {:.2f}'.format(p_val))

    ## Draw Conclusion
    alpha = 0.05
    if p_val < 0.05:
        print('We can reject the null hypothesis.')
    else:
        print('We fail to reject the null hypothesis.')
    
    print()