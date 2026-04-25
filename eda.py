import pandas as pd

# -----------------------
# STEP 1: LOAD DATA
# -----------------------
df = pd.read_csv("data/poll_data.csv")

print("✅ Data Loaded Successfully!\n")

# -----------------------
# STEP 2: PREVIEW DATA
# -----------------------
print("🔍 First 5 Rows:")
print(df.head())

# -----------------------
# STEP 3: DATA INFO
# -----------------------
print("\n📊 Dataset Info:")
print(df.info())

# -----------------------
# 📅 DATE RANGE (ADD HERE)
# -----------------------
print("\n📅 Date Range:", df['Date'].min(), "to", df['Date'].max())

# -----------------------
# STEP 4: MISSING VALUES
# -----------------------
print("\n❓ Missing Values:")
print(df.isnull().sum())

# -----------------------
# STEP 5: UNIQUE VALUES
# -----------------------
print("\n🧾 Unique Categories:")

print("Age Groups:", df['Age_Group'].unique())
print("Gender:", df['Gender'].unique())
print("Region:", df['Region'].unique())
print("Candidates:", df['Candidate'].unique())

# -----------------------
# STEP 6: BASIC STATS
# -----------------------
print("\n📈 Basic Statistics:")
print(df.describe())

# -----------------------
# STEP 7: QUICK INSIGHT
# -----------------------
print("\n🔥 Quick Vote Count:")
print(df['Candidate'].value_counts())

print("\n📊 Vote Percentage:")
print(df['Candidate'].value_counts(normalize=True) * 100)