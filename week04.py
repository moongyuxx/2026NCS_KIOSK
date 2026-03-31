import ssl
import seaborn as sns
import pandas as pd

# SSL 인증 비활성화
# ssl._create_default_https_context = ssl._create_unverified_context

mpg = sns.load_dataset('mpg')
print(mpg.info())
hp_median = mpg['horsepower'].median()
mpg_filed = mpg.copy()
mpg_filled['horsepower'] = mpg_filled['horsepower'].fillna(hp_median)
print(mpg_filled.info())