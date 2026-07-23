import streamlit as st
from backend.database.database_utils import fetch_data

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

employees = fetch_data("""
SELECT
    e.emp_id,
    u.name,
    d.dept_name AS department,
    m.name AS manager,
    e.designation,
    e.employment_type,
    e.onboarding_status
FROM employees e
LEFT JOIN users u
ON e.user_id = u.user_id
LEFT JOIN departments d
ON e.department_id = d.dept_id
LEFT JOIN employees me
ON e.manager_id = me.emp_id
LEFT JOIN users m
ON me.user_id = m.user_id;
""")

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
        employees["department"].dropna().unique().tolist()

    )

    selected_department = st.selectbox(
        "🏢 Filter by Department",
        departments
    )

filtered = employees.copy()

if search:
    filtered = filtered[
        filtered["name"].str.contains(search, case=False)
    ]

if selected_department != "All":
    filtered = filtered[
        filtered["department"] == selected_department
    ]

st.divider()

# ---------------- DATABASE ----------------

# Total Employees
total_df = fetch_data("""
SELECT COUNT(*) AS total_employees
FROM employees;
""")

# Total Departments
department_df = fetch_data("""
SELECT COUNT(*) AS total_departments
FROM departments;
""")

# Total Managers
manager_df = fetch_data("""
SELECT COUNT(DISTINCT manager_id) AS total_managers
FROM employees
WHERE manager_id IS NOT NULL;
""")

# Extract values
total_employees = int(total_df.iloc[0]["total_employees"])
total_departments = int(department_df.iloc[0]["total_departments"])
total_managers = int(manager_df.iloc[0]["total_managers"])

# ---------------- KPI Cards ----------------

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "👥 Total Employees",
        total_employees
    )

with c2:
    st.metric(
        "🏢 Departments",
        total_departments
    )

with c3:
    st.metric(
        "👨‍💼 Managers",
        total_managers
    )

st.divider()

# ---------------- Employee Table ----------------

st.subheader("📋 Employee List")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True,
    height=450
)

st.divider()
