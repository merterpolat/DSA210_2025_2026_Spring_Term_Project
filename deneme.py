import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


df_fights = pd.read_csv('C:\\Users\\merte\\PycharmProjects\\DSA210_2025_2026_Spring_Term_Project\\data.csv', encoding='latin1')
df_details = pd.read_csv('C:\\Users\\merte\\PycharmProjects\\DSA210_2025_2026_Spring_Term_Project\\raw_fighter_details.csv', encoding='latin1')

print("Data loaded successfully.")
print(f"Total number of fights: {len(df_fights)}")



all_fighters = pd.concat([df_fights['R_fighter'], df_fights['B_fighter']])
experience_counts = all_fighters.value_counts().reset_index()
experience_counts.columns = ['fighter_name', 'total_fights']
experience_counts['Experience_Level'] = experience_counts['total_fights'].apply(
    lambda x: 'Veteran' if x > 10 else 'Prospect'
)

df_details = df_details.merge(experience_counts, on='fighter_name', how='left')
print("Enrichment complete: Experience levels have been added.")


df_clean = df_fights[['Winner', 'B_avg_TD_pct', 'B_avg_SIG_STR_pct']].dropna().copy()
df_clean['is_Blue_Winner'] = df_clean['Winner'].apply(lambda x: 1 if x == 'Blue' else 0)


print("\nSummary Statistics")
print(df_clean.describe())


plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df_clean['B_avg_TD_pct'], kde=True, color='blue')
plt.title('Distribution of Takedown Accuracy')

plt.subplot(1, 2, 2)
sns.histplot(df_clean['B_avg_SIG_STR_pct'], kde=True, color='red')
plt.title('Distribution of Striking Accuracy')
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x='B_avg_SIG_STR_pct', y='B_avg_TD_pct', hue='Winner', data=df_clean, alpha=0.5)
plt.title('Striking Accuracy vs. Takedown Accuracy')
plt.xlabel('Striking Accuracy (%)')
plt.ylabel('Takedown Accuracy (%)')
plt.show()


plt.figure(figsize=(7, 5))
sns.countplot(x='Experience_Level', data=df_details, palette='viridis')
plt.title('Count of Veteran vs. Prospect Fighters (Enriched Data)')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Winner', y='B_avg_TD_pct', data=df_clean, palette='pastel')
plt.title('Takedown Accuracy Comparison by Winner')
plt.show()


print("\nHypothesis Testing")
threshold = df_clean['B_avg_TD_pct'].median()

high_grappling = df_clean[df_clean['B_avg_TD_pct'] >= threshold]['is_Blue_Winner']
low_grappling = df_clean[df_clean['B_avg_TD_pct'] < threshold]['is_Blue_Winner']

t_stat, p_val = stats.ttest_ind(high_grappling, low_grappling)

print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < 0.05:
    print("Result: There is a statistically significant difference (Reject H0).")
else:
    print("Result: No significant difference found (Fail to reject H0).")

df_details.to_csv('enriched_fighter_details.csv', index=False)