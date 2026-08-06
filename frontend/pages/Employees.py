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

/* ---------------- Background ---------------- */

.stApp{
    background:#F5F7FB;
}

.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
    max-width:1400px;
}

/* ---------------- Headers ---------------- */

h1{
    color:#111827;
    font-size:48px !important;
    font-weight:700 !important;
    margin-bottom:0px;
}

h2,h3{
    color:#111827;
    font-weight:600;
}

p{
    color:#6B7280;
    font-size:18px;
}
label{
    font-size:18px !important;
    font-weight:600 !important;
    color:#374151 !important;
}

/* ---------------- KPI Cards ---------------- */

[data-testid="stMetric"]{
    background:#FFFFFF;
    border:1px solid #E5E7EB;
    border-radius:18px;
    padding:20px;
    box-shadow:0 8px 18px rgba(15,23,42,.08);
    transition:0.3s;
}

[data-testid="stMetric"]:hover{
    transform:translateY(-3px);
    box-shadow:0 14px 30px rgba(15,23,42,.12);
}

[data-testid="stMetricLabel"]{
    color:#6B7280;
    font-size:16px !important;
}

[data-testid="stMetricValue"]{
    color:#1E3A8A;
    font-size:38px !important;
    font-weight:700;
}

/* ---------------- DataFrame ---------------- */

[data-testid="stDataFrame"]{
    background:white;
    border-radius:16px;
    border:1px solid #E5E7EB;
    overflow:hidden;
}

/* ---------------- Inputs ---------------- */

input{
    border-radius:12px !important;
}

[data-baseweb="select"]{
    border-radius:12px;
}

/* ---------------- Buttons ---------------- */

.stButton>button{
    border-radius:10px;
    border:none;
    background:#2563EB;
    color:white;
}

/* ---------------- Horizontal Line ---------------- */

hr{
    margin-top:25px;
    margin-bottom:25px;
    border:0;
    border-top:1px solid #E5E7EB;
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

title1, title2 = st.columns([5, 1])

st.markdown("""
<h1 style="
font-size:56px;
font-weight:800;
color:#173F73;
margin-bottom:0;
">
👥 Employee Directory
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
font-size:22px;
color:#4B5563;
margin-top:8px;
margin-bottom:28px;
">
Manage, search and monitor employee information across the organization.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- Filters ----------------

f1, f2, f3 = st.columns([3, 1.5, 1.5])

with f1:
    search = st.text_input(
        "Search Employee",
        placeholder="Search by employee name..."
    )

with f2:
    departments = ["All"] + sorted(
        employees["department"].dropna().unique().tolist()
    )

    selected_department = st.selectbox(
        "Department",
        departments
    )

with f3:
    statuses = ["All"] + sorted(
        employees["onboarding_status"].dropna().unique().tolist()
    )

    selected_status = st.selectbox(
        "Status",
        statuses
    )

filtered = employees.copy()

if search:
    filtered = filtered[
        filtered["name"].str.contains(search, case=False, na=False)
    ]

if selected_department != "All":
    filtered = filtered[
        filtered["department"] == selected_department
    ]

if selected_status != "All":
    filtered = filtered[
        filtered["onboarding_status"] == selected_status
    ]

st.markdown("<br>", unsafe_allow_html=True)

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

st.markdown("## Employee Directory")

display_df = filtered.rename(columns={
    "emp_id": "Employee ID",
    "name": "Employee Name",
    "department": "Department",
    "manager": "Manager",
    "designation": "Designation",
    "employment_type": "Employment Type",
    "onboarding_status": "Onboarding Status"
})

st.data_editor(
    display_df,
    use_container_width=True,
    hide_index=True,
    disabled=True,
    height=500
)

st.caption(f"Showing {len(display_df)} employee(s)")
