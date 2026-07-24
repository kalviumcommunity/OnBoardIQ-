import streamlit as st
import plotly.express as px
from backend.database.database_utils import fetch_data

st.set_page_config(
    page_title="Tool Usage",
    layout="wide"
)

# ---------------- PAGE STYLE ---------------- #

st.markdown("""
<style>

.main{
    background:#F5F7FB;
}

.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

[data-testid="metric-container"]{
    background:white;
    border-radius:16px;
    padding:18px;
    border:1px solid #E5E7EB;
    box-shadow:0 2px 10px rgba(0,0,0,.05);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

left, right = st.columns([5,1])

with left:
    st.title("Tool Usage Insights")
    st.caption("Monitor software adoption and employee engagement.")

with right:
    st.button("Generate Report", use_container_width=True)

st.write("")

# ---------------- KPI DATA ---------------- #

adoption_df = fetch_data("""
SELECT
ROUND(
COUNT(DISTINCT employee_id)*100.0/
(SELECT COUNT(*) FROM employees),
1
) AS adoption
FROM tool_usage;
""")

active_tool_df = fetch_data("""
SELECT
tool_name,
SUM(login_count) AS total
FROM tool_usage
GROUP BY tool_name
ORDER BY total DESC
LIMIT 1;
""")

inactive_df = fetch_data("""
SELECT
COUNT(DISTINCT employee_id) AS inactive
FROM tool_usage
WHERE login_count=0;
""")

avg_usage_df = fetch_data("""
SELECT
ROUND(AVG(total_usage_minutes),1) AS avg_usage
FROM tool_usage;
""")

# ---------------- KPI ---------------- #

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "TOOL ADOPTION %",
        f"{adoption_df.iloc[0]['adoption']}%"
    )

with k2:
    st.metric(
        "MOST ACTIVE TOOL",
        active_tool_df.iloc[0]["tool_name"]
    )

with k3:
    st.metric(
        "INACTIVE EMPLOYEES",
        int(inactive_df.iloc[0]["inactive"])
    )

with k4:
    st.metric(
        "AVG USAGE (MIN)",
        avg_usage_df.iloc[0]["avg_usage"]
    )

st.write("")

# ---------------- ROW 1 ---------------- #

left, right = st.columns([2,1])

with left:

    st.subheader("Daily Login Frequency")

    login_df = fetch_data("""
    SELECT
    DATE(last_used) AS "Date",
    SUM(login_count) AS "Logins"
    FROM tool_usage
    GROUP BY DATE(last_used)
    ORDER BY DATE(last_used);
    """)

    fig = px.bar(
        login_df,
        x="Date",
        y="Logins"
    )

    fig.update_layout(
        height=400,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    st.subheader("Top Used Applications")

    apps_df = fetch_data("""
    SELECT
    tool_name,
    SUM(login_count) AS usage
    FROM tool_usage
    GROUP BY tool_name
    ORDER BY usage DESC;
    """)

    max_usage = apps_df["usage"].max()

    for _, row in apps_df.iterrows():

        st.write(row["tool_name"])

        st.progress(row["usage"] / max_usage)

        st.caption(f"{row['usage']} logins")

# ---------------- ROW 2 ---------------- #

st.subheader("Usage Minutes by Tool")

usage_df = fetch_data("""
SELECT
tool_name,
SUM(total_usage_minutes) AS minutes
FROM tool_usage
GROUP BY tool_name
ORDER BY minutes DESC;
""")

fig = px.bar(
    usage_df,
    x="tool_name",
    y="minutes",
    color="tool_name",
    text="minutes"
)

fig.update_traces(textposition="outside")

fig.update_layout(
    height=400,
    showlegend=False,
    xaxis_title="Tool",
    yaxis_title="Usage Minutes"
)

st.plotly_chart(
    fig,
    use_container_width=True
)