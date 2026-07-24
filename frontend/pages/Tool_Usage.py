import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

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

.subtitle{
    color:#6B7280;
    font-size:16px;
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

# ---------------- KPI ---------------- #

k1,k2,k3,k4 = st.columns(4)

with k1:
    st.metric(
        "TOOL ADOPTION %",
        "82%",
        "+4.2%"
    )

with k2:
    st.metric(
        "MOST ACTIVE TOOL",
        "Slack",
        "89% Team Presence"
    )

with k3:
    st.metric(
        "INACTIVE EMPLOYEES",
        "14",
        "Pending"
    )

with k4:
    st.metric(
        "PEAK USAGE TIME",
        "10 AM",
        "Daily Avg"
    )

st.write("")

# ---------------- ROW 1 ---------------- #

left,right = st.columns([2,1])

with left:

    st.subheader("Daily Login Frequency")

    days = list(range(1,31))

    values = np.random.randint(20,80,30)

    df = pd.DataFrame({
        "Day":days,
        "Logins":values
    })

    fig = px.bar(
        df,
        x="Day",
        y="Logins"
    )

    fig.update_layout(
        height=400,
        showlegend=False
    )

    st.plotly_chart(fig,use_container_width=True)

with right:

    st.subheader("Top Used Applications")

    apps = {
        "Slack":94,
        "GitHub":88,
        "Jira":72,
        "Confluence":65,
        "Notion":41
    }

    for app,percent in apps.items():

        st.write(app)

        st.progress(percent/100)

        st.caption(f"{percent}%")

# ---------------- ROW 2 ---------------- #

st.subheader("Weekly Usage Intensity")

heatmap = np.random.randint(
    0,
    100,
    size=(7,24)
)

heat = px.imshow(
    heatmap,
    labels=dict(
        x="Hour",
        y="Day"
    ),
    aspect="auto"
)

heat.update_layout(height=350)

st.plotly_chart(
    heat,
    use_container_width=True
)