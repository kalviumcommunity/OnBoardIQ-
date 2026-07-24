import streamlit as st
from backend.database.database_utils import fetch_data

st.set_page_config(page_title="Onboarding", layout="wide")

# -----------------------------
# Database Data
# -----------------------------
not_started = fetch_data("""
SELECT
    d.dept_name AS department,
    u.name,
    e.designation AS role,
    COALESCE(m.name,'Not Assigned') AS manager,
    0 AS progress,
    'Pending' AS status
FROM employees e
JOIN users u
ON e.user_id = u.user_id
JOIN departments d
ON e.department_id = d.dept_id
LEFT JOIN employees me
ON e.manager_id = me.emp_id
LEFT JOIN users m
ON me.user_id = m.user_id
WHERE e.onboarding_status='Pending';
""").to_dict("records")


in_progress = fetch_data("""
SELECT
    d.dept_name AS department,
    u.name,
    e.designation AS role,
    COALESCE(m.name,'Not Assigned') AS manager,
    50 AS progress,
    'In Progress' AS status
FROM employees e
JOIN users u
ON e.user_id = u.user_id
JOIN departments d
ON e.department_id = d.dept_id
LEFT JOIN employees me
ON e.manager_id = me.emp_id
LEFT JOIN users m
ON me.user_id = m.user_id
WHERE e.onboarding_status='In Progress';
""").to_dict("records")


completed = fetch_data("""
SELECT
    d.dept_name AS department,
    u.name,
    e.designation AS role,
    COALESCE(m.name,'Not Assigned') AS manager,
    100 AS progress,
    'Completed' AS status
FROM employees e
JOIN users u
ON e.user_id = u.user_id
JOIN departments d
ON e.department_id = d.dept_id
LEFT JOIN employees me
ON e.manager_id = me.emp_id
LEFT JOIN users m
ON me.user_id = m.user_id
WHERE e.onboarding_status='Completed';
""").to_dict("records")

# -----------------------------
# Header
# -----------------------------

left, right = st.columns([5,1])

with left:
    st.title("Onboarding Tracker")
    st.caption(
        "Track and manage the progress of new hires through their first 90 days."
    )

with right:
    st.write("")
    st.button("➕ New Onboarding", use_container_width=True)

st.divider()

# -----------------------------
# DATABASE KPI
# -----------------------------

# Total Employees
total_df = fetch_data("""
SELECT COUNT(*) AS total_employees
FROM employees;
""")

# Completed Onboarding
completed_df = fetch_data("""
SELECT COUNT(*) AS completed
FROM employees
WHERE onboarding_status = 'Completed';
""")

# In Progress
progress_df = fetch_data("""
SELECT COUNT(*) AS in_progress
FROM employees
WHERE onboarding_status = 'In Progress';
""")

# Pending
pending_df = fetch_data("""
SELECT COUNT(*) AS pending
FROM employees
WHERE onboarding_status = 'Pending';
""")

# Extract KPI values
total_employees = int(total_df.iloc[0]["total_employees"])
completed_count = int(completed_df.iloc[0]["completed"])
in_progress_count = int(progress_df.iloc[0]["in_progress"])
pending_count = int(pending_df.iloc[0]["pending"])
# -----------------------------
# KPI Cards
# -----------------------------

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "👥 Total Employees",
        total_employees
    )

with k2:
    st.metric(
        "✅ Completed",
        completed_count
    )

with k3:
    st.metric(
        "⏳ In Progress",
        in_progress_count
    )

with k4:
    st.metric(
        "📝 Pending",
        pending_count
    )

st.divider()

# -----------------------------
# Card
# -----------------------------

def employee_card(emp):

    with st.container(border=True):

        st.caption(emp["department"].upper())

        st.subheader(emp["name"])

        st.write(emp["role"])

        st.write("Progress")

        st.progress(emp["progress"]/100)

        st.write(f"**{emp['progress']}%**")

        st.write(f"👤 Manager: {emp['manager']}")

        st.caption(emp["status"])

# -----------------------------
# Columns
# -----------------------------

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("### NOT STARTED")

    for emp in not_started:
        employee_card(emp)

with c2:

    st.markdown("### IN PROGRESS")

    for emp in in_progress:
        employee_card(emp)

with c3:

    st.markdown("### COMPLETED")

    for emp in completed:
        employee_card(emp)