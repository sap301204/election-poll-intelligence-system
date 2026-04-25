import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("data/cleaned_poll_data.csv")

# Style
sns.set(style="whitegrid")

print("📊 Visualization Started...")

# -----------------------
# 1. CANDIDATE VOTE COUNT
# -----------------------
plt.figure(figsize=(8,5))
sns.countplot(x='Candidate', data=df, palette='Set2')
plt.title("Vote Count per Candidate")
plt.savefig("images/candidate_count.png")
plt.show()

# -----------------------
# 2. VOTE SHARE (PIE)
# -----------------------
vote_counts = df['Candidate'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(vote_counts, labels=vote_counts.index, autopct='%1.1f%%')
plt.title("Vote Share")
plt.savefig("images/vote_share.png")
plt.show()

# -----------------------
# 3. REGION-WISE ANALYSIS
# -----------------------
region_data = pd.crosstab(df['Region'], df['Candidate'])

region_data.plot(kind='bar', stacked=True, figsize=(8,5))
plt.title("Region-wise Candidate Preference")
plt.ylabel("Votes")
plt.savefig("images/region_analysis.png")
plt.show()

# -----------------------
# 4. AGE GROUP ANALYSIS
# -----------------------
age_data = pd.crosstab(df['Age_Group'], df['Candidate'])

age_data.plot(kind='bar', stacked=True, figsize=(8,5))
plt.title("Age Group vs Candidate")
plt.savefig("images/age_analysis.png")
plt.show()

# -----------------------
# 5. TREND OVER TIME
# -----------------------
df['Date'] = pd.to_datetime(df['Date'])
trend = df.groupby(['Date', 'Candidate']).size().unstack()

trend.plot(figsize=(10,5))
plt.title("Polling Trend Over Time")
plt.savefig("images/trend.png")
plt.show()

# -----------------------
# 6. CONFIDENCE ANALYSIS
# -----------------------
plt.figure(figsize=(7,5))
sns.boxplot(x='Candidate', y='Confidence_Level', data=df)
plt.title("Confidence Level per Candidate")
plt.savefig("images/confidence.png")
plt.show()

print("✅ All charts saved in /images folder")