import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="India Election Poll Dashboard",
    page_icon="🗳️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at 20% 10%, rgba(37, 99, 235, 0.35), transparent 25%),
        radial-gradient(circle at 80% 20%, rgba(168, 85, 247, 0.25), transparent 30%),
        linear-gradient(135deg, #020617 0%, #070b1f 45%, #000000 100%);
    color: #ffffff;
}

.block-container {
    padding-top: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* Sidebar Cyber Pattern */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, rgba(2,6,23,0.96), rgba(15,23,42,0.98)),
        repeating-linear-gradient(
            135deg,
            rgba(56,189,248,0.08) 0px,
            rgba(56,189,248,0.08) 1px,
            transparent 1px,
            transparent 12px
        );
    border-right: 2px solid #22d3ee;
    box-shadow: 6px 0 30px rgba(34,211,238,0.25);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4 {
    color: #22d3ee;
    text-shadow: 0 0 10px rgba(34,211,238,0.8);
}

section[data-testid="stSidebar"] label {
    color: #e0f2fe !important;
    font-weight: 700;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(34,211,238,0.35);
    border-radius: 14px;
    box-shadow: inset 0 0 12px rgba(34,211,238,0.12);
}

section[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background: linear-gradient(90deg, #ec4899, #8b5cf6) !important;
    border-radius: 999px !important;
    color: white !important;
    font-weight: 800;
}

/* Title */
.neon-title {
    text-align: center;
    font-size: 44px;
    font-weight: 950;
    color: #67e8f9;
    text-shadow: 0 0 10px #22d3ee, 0 0 22px #3b82f6, 0 0 38px #a855f7;
    letter-spacing: 1px;
}

.neon-subtitle {
    text-align: center;
    color: #dbeafe;
    font-size: 16px;
    margin-bottom: 28px;
}

/* KPI Cards */
.kpi-card {
    background:
        linear-gradient(145deg, rgba(15,23,42,0.96), rgba(30,41,59,0.72));
    border: 1px solid rgba(34,211,238,0.9);
    border-radius: 24px;
    padding: 24px;
    text-align: center;
    box-shadow:
        0 0 20px rgba(34,211,238,0.35),
        inset 0 0 18px rgba(168,85,247,0.12);
    min-height: 135px;
}

.kpi-card h4 {
    color: #a5f3fc;
    font-size: 14px;
    margin-bottom: 12px;
}

.kpi-card h2 {
    color: #ffffff;
    font-size: 32px;
    margin: 0;
    text-shadow: 0 0 10px rgba(255,255,255,0.4);
}

/* Section Styling */
.zone-title {
    color: #67e8f9;
    font-size: 27px;
    font-weight: 950;
    text-shadow: 0 0 12px rgba(34,211,238,0.75);
    margin-top: 30px;
    margin-bottom: 18px;
    padding-left: 8px;
    border-left: 5px solid #22d3ee;
}

.glow-line {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, #22d3ee, #a855f7, transparent);
    margin: 34px 0;
}

.chart-card {
    background: rgba(2, 6, 23, 0.55);
    border: 1px solid rgba(34,211,238,0.25);
    border-radius: 22px;
    padding: 16px;
    box-shadow: 0 0 18px rgba(34,211,238,0.14);
}

.insight-card {
    background:
        linear-gradient(135deg, rgba(15,23,42,0.95), rgba(30,41,59,0.75));
    border: 1px solid rgba(34,211,238,0.6);
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 0 18px rgba(34,211,238,0.25);
    font-size: 17px;
}

/* Download Button */
.stDownloadButton button {
    background: linear-gradient(90deg, #06b6d4, #8b5cf6, #ec4899);
    color: white;
    border-radius: 999px;
    border: none;
    padding: 11px 24px;
    font-weight: 800;
    box-shadow: 0 0 14px rgba(139,92,246,0.6);
}

.stDataFrame {
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned_poll_data.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df

df = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 🎛️ Control Panel")

st.sidebar.markdown("#### 🌍 Geography Filters")
selected_state = st.sidebar.multiselect(
    "Select States",
    options=sorted(df["State"].unique()),
    default=sorted(df["State"].unique())
)

selected_region = st.sidebar.multiselect(
    "Select Region Type",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

st.sidebar.markdown("---")

st.sidebar.markdown("#### 👥 Demographic Filters")
selected_age = st.sidebar.multiselect(
    "Select Age Group",
    options=sorted(df["Age_Group"].unique()),
    default=sorted(df["Age_Group"].unique())
)

selected_gender = st.sidebar.multiselect(
    "Select Gender",
    options=sorted(df["Gender"].unique()),
    default=sorted(df["Gender"].unique())
)

st.sidebar.markdown("---")

st.sidebar.markdown("#### 🗳️ Election Data")
selected_candidate = st.sidebar.multiselect(
    "Select Candidate",
    options=sorted(df["Candidate"].unique()),
    default=sorted(df["Candidate"].unique())
)

filtered_df = df[
    (df["State"].isin(selected_state)) &
    (df["Region"].isin(selected_region)) &
    (df["Age_Group"].isin(selected_age)) &
    (df["Gender"].isin(selected_gender)) &
    (df["Candidate"].isin(selected_candidate))
]

if filtered_df.empty:
    st.warning("No data available for selected filters.")
    st.stop()

# ---------------- CHART STYLE FUNCTION ----------------
def style_fig(fig, height=430):
    fig.update_layout(
        template="plotly_dark",
        height=height,
        title_x=0.5,
        title_font=dict(size=18, color="#e0f2fe"),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(2,6,23,0.82)",
        font=dict(color="#e5e7eb", size=13),
        margin=dict(l=25, r=25, t=60, b=35),
        legend=dict(
            bgcolor="rgba(2,6,23,0.75)",
            bordercolor="rgba(34,211,238,0.45)",
            borderwidth=1,
            font=dict(size=12)
        )
    )
    fig.update_xaxes(
        gridcolor="rgba(148,163,184,0.16)",
        zeroline=False,
        showline=True,
        linecolor="rgba(34,211,238,0.35)"
    )
    fig.update_yaxes(
        gridcolor="rgba(148,163,184,0.16)",
        zeroline=False,
        showline=True,
        linecolor="rgba(34,211,238,0.35)"
    )
    return fig

# ---------------- HEADER ----------------
st.markdown('<div class="neon-title">🇮🇳 INDIA ELECTION POLL ANALYTICS DASHBOARD</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="neon-subtitle">Premium Synthetic Poll Intelligence | State-wise, Region-wise & Demographic Analysis</div>',
    unsafe_allow_html=True
)

# ---------------- KPI CALCULATIONS ----------------
total_votes = len(filtered_df)

vote_counts = filtered_df["Candidate"].value_counts().reset_index()
vote_counts.columns = ["Candidate", "Votes"]
vote_counts["Vote Share (%)"] = (vote_counts["Votes"] / total_votes * 100).round(2)

leader = vote_counts.iloc[0]["Candidate"]
leader_votes = vote_counts.iloc[0]["Votes"]
leader_share = vote_counts.iloc[0]["Vote Share (%)"]

total_states = filtered_df["State"].nunique()
avg_confidence = filtered_df["Confidence_Level"].mean()

# ---------------- KPI CARDS ----------------
k1, k2, k3, k4 = st.columns(4)

k1.markdown(f"""
<div class="kpi-card">
<h4>📊 Total Responses</h4>
<h2>{total_votes}</h2>
</div>
""", unsafe_allow_html=True)

k2.markdown(f"""
<div class="kpi-card">
<h4>🏆 Leading Candidate</h4>
<h2>{leader}</h2>
</div>
""", unsafe_allow_html=True)

k3.markdown(f"""
<div class="kpi-card">
<h4>📈 Leader Vote Share</h4>
<h2>{leader_share}%</h2>
</div>
""", unsafe_allow_html=True)

k4.markdown(f"""
<div class="kpi-card">
<h4>🗺️ States Covered</h4>
<h2>{total_states}</h2>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="glow-line">', unsafe_allow_html=True)

# ---------------- SECTION 1 ----------------
st.markdown('<div class="zone-title">🏆 Election Result Command Center</div>', unsafe_allow_html=True)

left, mid, right = st.columns([1.1, 1.4, 1.4])

with left:
    st.subheader("🏆 Result Table")
    st.dataframe(vote_counts, use_container_width=True, hide_index=True)

    st.subheader("⚡ Quick Insight")
    st.success(f"{leader} is leading with {leader_votes} votes and {leader_share}% vote share.")
    st.info(f"Average confidence level: {avg_confidence:.2f}/5")

with mid:
    fig_donut = px.pie(
        vote_counts,
        names="Candidate",
        values="Votes",
        hole=0.58,
        title="Vote Share Donut",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_donut.update_traces(
        textinfo="percent+label",
        marker=dict(line=dict(color="#020617", width=3)),
        pull=[0.04 if c == leader else 0 for c in vote_counts["Candidate"]]
    )
    fig_donut = style_fig(fig_donut, height=440)
    st.plotly_chart(fig_donut, use_container_width=True)

with right:
    fig_bar = px.bar(
        vote_counts,
        x="Candidate",
        y="Votes",
        text="Votes",
        title="Candidate-wise Vote Count",
        color="Candidate",
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    fig_bar.update_traces(
        textposition="outside",
        marker_line_color="#ffffff",
        marker_line_width=1.2,
        opacity=0.92
    )
    fig_bar = style_fig(fig_bar, height=440)
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown('<hr class="glow-line">', unsafe_allow_html=True)

# ---------------- SECTION 2 MAP ----------------
st.markdown('<div class="zone-title">🗺️ State Intelligence Zone</div>', unsafe_allow_html=True)

state_votes = (
    filtered_df.groupby(["State", "Latitude", "Longitude"])
    .size()
    .reset_index(name="Votes")
)

fig_map = px.scatter_geo(
    state_votes,
    lat="Latitude",
    lon="Longitude",
    size="Votes",
    hover_name="State",
    hover_data={"Votes": True, "Latitude": False, "Longitude": False},
    title="India State-wise Poll Response Bubble Map",
    projection="natural earth",
    color="Votes",
    color_continuous_scale="Turbo",
    size_max=38
)

fig_map.update_traces(
    marker=dict(
        line=dict(width=1.5, color="white"),
        opacity=0.86
    )
)

fig_map.update_geos(
    visible=True,
    showcountries=True,
    countrycolor="rgba(56,189,248,0.65)",
    showland=True,
    landcolor="rgba(15,23,42,0.85)",
    showocean=True,
    oceancolor="rgba(2,6,23,1)",
    showlakes=False,
    lataxis_range=[5, 38],
    lonaxis_range=[65, 100]
)

fig_map = style_fig(fig_map, height=520)
st.plotly_chart(fig_map, use_container_width=True)

state_result = (
    filtered_df.groupby(["State", "Candidate"])
    .size()
    .reset_index(name="Votes")
)

state_leader = (
    state_result.sort_values(["State", "Votes"], ascending=[True, False])
    .drop_duplicates("State")
    .reset_index(drop=True)
)

state_left, state_right = st.columns([1.2, 2])

with state_left:
    st.subheader("📍 State-wise Leaders")
    st.dataframe(state_leader, use_container_width=True, hide_index=True)

with state_right:
    fig_state = px.bar(
        state_result,
        x="State",
        y="Votes",
        color="Candidate",
        title="State-wise Candidate Performance",
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig_state.update_traces(
        marker_line_color="#ffffff",
        marker_line_width=0.8,
        opacity=0.9
    )
    fig_state.update_layout(xaxis_tickangle=-45)
    fig_state = style_fig(fig_state, height=480)
    st.plotly_chart(fig_state, use_container_width=True)

st.markdown('<hr class="glow-line">', unsafe_allow_html=True)

# ---------------- SECTION 3 DEMOGRAPHICS ----------------
st.markdown('<div class="zone-title">👥 Demographic Breakdown Zone</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    region_chart = (
        filtered_df.groupby(["Region", "Candidate"])
        .size()
        .reset_index(name="Votes")
    )

    fig_region = px.bar(
        region_chart,
        x="Region",
        y="Votes",
        color="Candidate",
        title="Urban vs Rural Candidate Preference",
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig_region.update_traces(
        marker_line_color="#ffffff",
        marker_line_width=0.8,
        opacity=0.9
    )
    fig_region = style_fig(fig_region, height=450)
    st.plotly_chart(fig_region, use_container_width=True)

with c2:
    age_chart = (
        filtered_df.groupby(["Age_Group", "Candidate"])
        .size()
        .reset_index(name="Votes")
    )

    fig_age = px.bar(
        age_chart,
        x="Age_Group",
        y="Votes",
        color="Candidate",
        title="Age Group-wise Voting Pattern",
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    fig_age.update_traces(
        marker_line_color="#ffffff",
        marker_line_width=0.8,
        opacity=0.9
    )
    fig_age = style_fig(fig_age, height=450)
    st.plotly_chart(fig_age, use_container_width=True)

st.markdown('<hr class="glow-line">', unsafe_allow_html=True)

# ---------------- SECTION 4 ISSUE ANALYSIS ----------------
st.markdown('<div class="zone-title">📌 Voting Issue Impact Zone</div>', unsafe_allow_html=True)

issue_chart = (
    filtered_df.groupby(["Voting_Issue", "Candidate"])
    .size()
    .reset_index(name="Votes")
)

fig_issue = px.bar(
    issue_chart,
    x="Voting_Issue",
    y="Votes",
    color="Candidate",
    title="Voting Issue-wise Candidate Preference",
    barmode="group",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig_issue.update_traces(
    marker_line_color="#ffffff",
    marker_line_width=0.8,
    opacity=0.92
)
fig_issue = style_fig(fig_issue, height=500)
st.plotly_chart(fig_issue, use_container_width=True)

st.markdown('<hr class="glow-line">', unsafe_allow_html=True)

# ---------------- SECTION 5 TREND ----------------
st.markdown('<div class="zone-title">📈 Polling Momentum Zone</div>', unsafe_allow_html=True)

trend = (
    filtered_df.groupby([filtered_df["Date"].dt.date, "Candidate"])
    .size()
    .reset_index(name="Votes")
)

trend.columns = ["Date", "Candidate", "Votes"]

fig_trend = px.line(
    trend,
    x="Date",
    y="Votes",
    color="Candidate",
    markers=True,
    title="Polling Trend Over Time",
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig_trend.update_traces(
    line=dict(width=3),
    marker=dict(size=7, line=dict(width=1, color="white"))
)
fig_trend = style_fig(fig_trend, height=500)
st.plotly_chart(fig_trend, use_container_width=True)

st.markdown('<hr class="glow-line">', unsafe_allow_html=True)

# ---------------- SECTION 6 INSIGHTS ----------------
st.markdown('<div class="zone-title">🧠 Executive Insight Panel</div>', unsafe_allow_html=True)

top_state = state_votes.sort_values("Votes", ascending=False).iloc[0]["State"]
top_issue = filtered_df["Voting_Issue"].value_counts().idxmax()

st.markdown(f"""
<div class="insight-card">
<ul>
<li><b>{leader}</b> is currently leading with <b>{leader_share}%</b> vote share.</li>
<li>The dashboard analyzes <b>{total_votes}</b> synthetic poll responses across <b>{total_states}</b> Indian states.</li>
<li><b>{top_state}</b> has the highest number of responses in the selected filters.</li>
<li>The most discussed voting issue is <b>{top_issue}</b>.</li>
<li>Region, age group, and issue-wise charts help understand deeper voter behavior patterns.</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.write("")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_election_poll_data.csv",
    mime="text/csv"
)

with st.expander("📄 View Filtered Dataset"):
    st.dataframe(filtered_df, use_container_width=True)