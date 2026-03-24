import ssl
import seaborn as sns
import pandas as pd

# SSL 인증 비활성화
ssl._create_default_https_context = ssl._create_unverified_context

mpg = sns.load_dataset('mpg')
group_mpg = pd.DataFrame(mpg.groupby('origin'))
print(group_mpg)