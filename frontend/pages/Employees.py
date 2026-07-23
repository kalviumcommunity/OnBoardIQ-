import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Employees",
    page_icon="👥",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Main app */
html, body, [class*="css"]{
    font-size:18px;
}

/* Page Title */
h1{
    font-size:48px !important;
    font-weight:700 !important;
}

/* Section Titles */
h2,h3{
    font-size:32px !important;
    font-weight:600 !important;
}

/* Paragraphs */
p{
    font-size:20px !important;
}

/* Metric Values */
[data-testid="stMetricValue"]{
    font-size:42px !important;
    font-weight:bold;
}

/* Metric Labels */
[data-testid="stMetricLabel"]{
    font-size:18px !important;
}

/* DataFrame */
[data-testid="stDataFrame"]{
    font-size:18px !important;
}

/* Table Header */
thead tr th{
    font-size:18px !important;
}

/* Table Body */
tbody tr td{
    font-size:17px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] *{
    font-size:18px !important;
}

/* Search Box */
input{
    font-size:18px !important;
}

/* Selectbox */
[data-baseweb="select"]{
    font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Load Data ----------------

employees = pd.read_csv("backend/data/employees.csv")

# ---------------- Header ----------------

st.markdown("<h1>👥 Employee Directory</h1>", unsafe_allow_html=True)
st.markdown(
    "<p>View and search employee information.</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- Filters ----------------

col1, col2 = st.columns([2, 1])

with col1:
    search = st.text_input("🔍 Search Employee")

with col2:
    departments = ["All"] + sorted(
        employees["Department"].unique().tolist()
    )

    selected_department = st.selectbox(
        "🏢 Filter by Department",
        departments
    )

filtered = employees.copy()

if search:
    filtered = filtered[
        filtered["Name"].str.contains(search, case=False)
    ]

if selected_department != "All":
    filtered = filtered[
        filtered["Department"] == selected_department
    ]

st.divider()

# ---------------- KPI Cards ----------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "👥 Total Employees",
        len(filtered)
    )

with c2:
    st.metric(
        "🏢 Departments",
        filtered["Department"].nunique()
    )

with c3:
    st.metric(
        "👨‍💼 Managers",
        filtered["Manager"].nunique()
    )

st.divider()

# ---------------- Employee Table ----------------

st.subheader("📋 Employee List")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True,
    height=350
)

st.divider()

# ---------------- Charts ----------------

left, right = st.columns(2)

with left:

    st.subheader("📊 Employees by Department")

    dept = (
        filtered["Department"]
        .value_counts()
        .reset_index()
    )

    dept.columns = [
        "Department",
        "Employees"
    ]

    fig = px.bar(
        dept,
        x="Department",
        y="Employees",
        color="Department",
        text="Employees"
    )

    fig.update_layout(
        title="Department-wise Employees",
        title_font_size=26,
        font=dict(size=18),
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.subheader("🥧 Department Distribution")

    fig = px.pie(
        filtered,
        names="Department",
        hole=0.55
    )

    fig.update_traces(
        textinfo="percent+label",
        textfont_size=18
    )

    fig.update_layout(
        title="Department Distribution",
        title_font_size=26,
        font=dict(size=18),
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )