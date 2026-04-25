import pandas as pd
import os

df = pd.read_csv("data/poll_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

before = len(df)
df.drop_duplicates(inplace=True)
after = len(df)

print(f"🧹 Removed {before - after} duplicate rows")

df = df.dropna(subset=["Candidate", "State"])

text_columns = ["State", "Region", "Age_Group", "Gender", "Candidate", "Voting_Issue"]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip().str.title()

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Weekday"] = df["Date"].dt.day_name()

def confidence_category(value):
    if value >= 4:
        return "High"
    elif value >= 2:
        return "Medium"
    else:
        return "Low"

df["Confidence_Category"] = df["Confidence_Level"].apply(confidence_category)
df["Vote_Flag"] = 1

os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_poll_data.csv", index=False)

print("✅ Cleaned data saved successfully!")
print("📁 Saved as data/cleaned_poll_data.csv")