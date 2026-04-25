import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_poll_data.csv")

print("🧠 Generating Insights...\n")

# -----------------------
# 1. OVERALL LEADER
# -----------------------
vote_counts = df['Candidate'].value_counts()
leader = vote_counts.idxmax()
leader_percent = (vote_counts.max() / len(df)) * 100

print(f"🏆 Leading Candidate: {leader} ({leader_percent:.2f}%)")

# -----------------------
# 2. REGION INSIGHT
# -----------------------
region = pd.crosstab(df['Region'], df['Candidate'])

print("\n🌍 Region-wise Leader:")
for r in region.index:
    top_candidate = region.loc[r].idxmax()
    print(f"{r}: {top_candidate}")

# -----------------------
# 3. AGE GROUP INSIGHT
# -----------------------
age = pd.crosstab(df['Age_Group'], df['Candidate'])

print("\n👥 Age Group Preference:")
for a in age.index:
    top_candidate = age.loc[a].idxmax()
    print(f"{a}: {top_candidate}")

# -----------------------
# 4. CONFIDENCE ANALYSIS
# -----------------------
confidence_avg = df.groupby('Candidate')['Confidence_Level'].mean()

print("\n📊 Average Confidence Level:")
print(confidence_avg)

# -----------------------
# 5. TREND INSIGHT
# -----------------------
df['Date'] = pd.to_datetime(df['Date'])
trend = df.groupby(['Date', 'Candidate']).size().unstack()

print("\n📈 Trend Insight:")
print("Polling trend shows variation across dates. Analyze chart for pattern.")

# -----------------------
# FINAL SUMMARY
# -----------------------
print("\n🧾 FINAL SUMMARY:")
print(f"- {leader} is currently leading the poll.")
print("- Voting patterns vary across regions and demographics.")
print("- Confidence levels indicate voter certainty.")
print("- Time-based trends show how preferences evolve.")