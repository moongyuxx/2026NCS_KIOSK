import ssl
import seaborn as sns

# SSL 인증 비활성화
ssl._create_default_https_context = ssl._create_unverified_context

mpg = sns.load_dataset('mpg')

print(
    mpg[['origin', 'name', 'mpg']]
    .query('origin == "europe" and mpg >= 30.0')
    .sort_values('mpg', ascending=False)
)

print(mpg)