import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="OnBoardIQ Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Main page */
.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

/* Dashboard Title */
h1{
    font-size:48px !important;
    font-weight:700 !important;
    color:#1F2937;
}

/* Section Headings */
h2{
    font-size:34px !important;
    font-weight:700 !important;
    color:#1F2937;
}

/* Normal text */
p{
    font-size:20px !important;
}

/* Metric Labels */
[data-testid="stMetricLabel"]{
    font-size:18px !important;
    font-weight:600;
}

/* Metric Values */
[data-testid="stMetricValue"]{
    font-size:42px !important;
    font-weight:700;
}

/* Sidebar */
section[data-testid="stSidebar"] *{
    font-size:18px !important;
}

/* Dataframe */
[data-testid="stDataFrame"]{
    font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
employees = pd.read_csv("data/employees.csv")
onboarding = pd.read_csv("data/onboarding.csv")
tickets = pd.read_csv("data/tickets.csv")
tool_usage = pd.read_csv("data/tool_usage.csv")

# ---------------- TITLE ----------------
st.markdown(
    "<h1>📊 OnBoardIQ Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p>Welcome to the Employee Onboarding Insights Dashboard</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- KPI CARDS ----------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Total Employees",
        len(employees)
    )

with col2:
    completed = onboarding[
        onboarding["Status"] == "Completed"
    ].shape[0]

    st.metric(
        "✅ Completed",
        completed
    )

with col3:
    st.metric(
        "💻 Active Users",
        len(tool_usage)
    )

with col4:
    open_tickets = tickets[
        tickets["Status"] == "Open"
    ].shape[0]

    st.metric(
        "🎫 Open Tickets",
        open_tickets
    )

st.divider()

# ---------------- TABLE ----------------
st.markdown("<h2>Employee Data</h2>", unsafe_allow_html=True)

st.dataframe(
    employees,
    use_container_width=True,
    height=280
)

# ---------------- BAR CHART ----------------
st.markdown("<h2>📊 Employees by Department</h2>", unsafe_allow_html=True)

dept_count = employees["Department"].value_counts().reset_index()
dept_count.columns = ["Department", "Employees"]

fig = px.bar(
    dept_count,
    x="Department",
    y="Employees",
    color="Department",
    title="Employees in Each Department"
)

fig.update_layout(
    title_font_size=24,
    font=dict(size=18),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- PIE CHART ----------------
st.markdown("<h2>🥧 Onboarding Status</h2>", unsafe_allow_html=True)

status_count = onboarding["Status"].value_counts().reset_index()
status_count.columns = ["Status", "Count"]

fig = px.pie(
    status_count,
    names="Status",
    values="Count",
    title="Onboarding Status"
)

fig.update_layout(
    title_font_size=24,
    font=dict(size=18),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- SUPPORT TICKETS ----------------
st.markdown("<h2>🎫 Support Ticket Categories</h2>", unsafe_allow_html=True)

ticket_count = tickets["Category"].value_counts().reset_index()
ticket_count.columns = ["Category", "Count"]

fig = px.bar(
    ticket_count,
    x="Category",
    y="Count",
    color="Category",
    title="Support Tickets"
)

fig.update_layout(
    title_font_size=24,
    font=dict(size=18),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- TOOL USAGE ----------------
st.markdown("<h2>💻 Tool Usage</h2>", unsafe_allow_html=True)

fig = px.bar(
    tool_usage,
    x="Tool",
    y="LoginCount",
    color="Tool",
    title="Tool Login Count"
)

fig.update_layout(
    title_font_size=24,
    font=dict(size=18),
    height=500
)

st.plotly_chart(fig, use_container_width=True)