import pandas as pd
import numpy as np
import os

np.random.seed(42)

n = 1000

states = [
    "Maharashtra", "Karnataka", "Gujarat", "Rajasthan", "Madhya Pradesh",
    "Uttar Pradesh", "Bihar", "West Bengal", "Tamil Nadu", "Kerala",
    "Telangana", "Andhra Pradesh", "Punjab", "Haryana", "Odisha"
]

state_coordinates = {
    "Maharashtra": (19.7515, 75.7139),
    "Karnataka": (15.3173, 75.7139),
    "Gujarat": (22.2587, 71.1924),
    "Rajasthan": (27.0238, 74.2179),
    "Madhya Pradesh": (22.9734, 78.6569),
    "Uttar Pradesh": (26.8467, 80.9462),
    "Bihar": (25.0961, 85.3131),
    "West Bengal": (22.9868, 87.8550),
    "Tamil Nadu": (11.1271, 78.6569),
    "Kerala": (10.8505, 76.2711),
    "Telangana": (18.1124, 79.0193),
    "Andhra Pradesh": (15.9129, 79.7400),
    "Punjab": (31.1471, 75.3412),
    "Haryana": (29.0588, 76.0856),
    "Odisha": (20.9517, 85.0985),
}

selected_states = np.random.choice(states, n)

data = {
    "Respondent_ID": range(1, n + 1),
    "Date": pd.date_range(start="2024-04-01", periods=n, freq="h"),
    "State": selected_states,
    "Region": np.random.choice(["Urban", "Rural"], n, p=[0.58, 0.42]),
    "Age_Group": np.random.choice(["18-24", "25-34", "35-44", "45+"], n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "Candidate": np.random.choice(
        ["Candidate A", "Candidate B", "Candidate C", "NOTA"],
        n,
        p=[0.43, 0.31, 0.17, 0.09]
    ),
    "Voting_Issue": np.random.choice(
        ["Jobs", "Education", "Healthcare", "Inflation", "Infrastructure"],
        n
    ),
    "Confidence_Level": np.random.randint(1, 6, n)
}

df = pd.DataFrame(data)

df["Latitude"] = df["State"].map(lambda x: state_coordinates[x][0])
df["Longitude"] = df["State"].map(lambda x: state_coordinates[x][1])

os.makedirs("data", exist_ok=True)
df.to_csv("data/poll_data.csv", index=False)

print("✅ Synthetic election poll data created successfully!")
print("📁 Saved as data/poll_data.csv")