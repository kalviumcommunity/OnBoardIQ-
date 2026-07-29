import streamlit as st
import plotly.express as px
from backend.database.database_utils import fetch_data

st.set_page_config(
    page_title="Analytics",
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

div[data-baseweb="select"]{
    background:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

left,right = st.columns([5,1])

with left:
    st.title("Analytics & Insights")
    st.caption("Strategic workforce analytics and organizational trends.")

with right:
    st.button(
        "Export Report",
        use_container_width=True
    )

st.write("")

# ---------------- FILTERS ---------------- #

with st.container(border=True):

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        department = st.selectbox(
            "Department",
            [
                "All",
                "Engineering",
                "HR",
                "Finance",
                "Marketing",
                "Product",
                "Sales"
            ]
        )

    with c2:
        employment = st.selectbox(
            "Employment Type",
            [
                "All",
                "Full-Time",
                "Intern",
                "Contract"
            ]
        )

    with c3:
        onboarding = st.selectbox(
            "Onboarding Status",
            [
                "All",
                "Completed",
                "In Progress",
                "Pending"
            ]
        )

    with c4:
        join_date = st.date_input("Joined After")

    with c5:
        st.write("")
        st.write("")
        reset = st.button(
            "Reset Filters",
            use_container_width=True
        )

# ---------------- FILTER CONDITIONS ---------------- #

conditions = []

if department != "All":
    conditions.append(f"d.dept_name = '{department}'")

if employment != "All":
    conditions.append(f"e.employment_type = '{employment}'")

if onboarding != "All":
    conditions.append(f"e.onboarding_status = '{onboarding}'")

conditions.append(f"e.joining_date >= '{join_date}'")

where_clause = ""

if conditions:
    where_clause = "WHERE " + " AND ".join(conditions)

# ---------------- SQL QUERIES ---------------- #

conditions = []

if department != "All":
    conditions.append(f"d.dept_name = '{department}'")

if employment != "All":
    conditions.append(f"e.employment_type = '{employment}'")

if onboarding != "All":
    conditions.append(f"e.onboarding_status = '{onboarding}'")

where_clause = ""

if conditions:
    where_clause = "WHERE " + " AND ".join(conditions)

# =====================================================
# Hiring Trend
# =====================================================

query = f"""
SELECT
    TO_CHAR(e.joining_date,'Mon') AS month,
    COUNT(*) AS hires,
    EXTRACT(MONTH FROM e.joining_date) AS month_num

FROM employees e
JOIN departments d
ON e.department_id = d.dept_id

{where_clause}

GROUP BY month, month_num
ORDER BY month_num;
"""

hiring_df = fetch_data(query)

# =====================================================
# Department Performance
# =====================================================

query = f"""
SELECT
    d.dept_name,

    ROUND(
        COUNT(*) FILTER (
            WHERE e.onboarding_status='Completed'
        ) * 100.0 /
        COUNT(*),
        1
    ) AS completion

FROM employees e
JOIN departments d
ON e.department_id = d.dept_id

{where_clause}

GROUP BY d.dept_name
ORDER BY completion DESC;
"""

department_df = fetch_data(query)

# =====================================================
# Support Categories
# =====================================================

query = f"""
SELECT
    s.category,
    COUNT(*) AS total

FROM support_tickets s
JOIN employees e
ON s.employee_id = e.emp_id
JOIN departments d
ON e.department_id = d.dept_id

{where_clause}

GROUP BY s.category;
"""

support_df = fetch_data(query)

# =====================================================
# Average Resolution Time
# =====================================================

resolution_condition = where_clause

if resolution_condition:
    resolution_condition += " AND s.resolved_at IS NOT NULL"
else:
    resolution_condition = "WHERE s.resolved_at IS NOT NULL"

query = f"""
SELECT
    ROUND(
        AVG(
            EXTRACT(EPOCH FROM (s.resolved_at - s.created_at))/3600
        ),
        1
    ) AS avg_time

FROM support_tickets s
JOIN employees e
ON s.employee_id = e.emp_id
JOIN departments d
ON e.department_id = d.dept_id

{resolution_condition};
"""

resolution_df = fetch_data(query)

# =====================================================
# Most Used Tool
# =====================================================

query = f"""
SELECT
    t.tool_name

FROM tool_usage t
JOIN employees e
ON t.employee_id = e.emp_id
JOIN departments d
ON e.department_id = d.dept_id

{where_clause}

GROUP BY t.tool_name
ORDER BY SUM(t.login_count) DESC

LIMIT 1;
"""

tool_df = fetch_data(query)

# =====================================================
# Average Usage
# =====================================================

query = f"""
SELECT
    ROUND(
        AVG(t.total_usage_minutes),
        1
    ) AS avg_usage

FROM tool_usage t
JOIN employees e
ON t.employee_id = e.emp_id
JOIN departments d
ON e.department_id = d.dept_id

{where_clause};
"""

usage_df = fetch_data(query)

# =====================================================
# Tool Usage Distribution
# =====================================================

query = f"""
SELECT
    t.tool_name,
    SUM(t.login_count) AS usage

FROM tool_usage t
JOIN employees e
ON t.employee_id = e.emp_id
JOIN departments d
ON e.department_id = d.dept_id

{where_clause}

GROUP BY t.tool_name;
"""

tool_usage_df = fetch_data(query)

# =====================================================
# Employment Type Distribution
# =====================================================

query = f"""
SELECT
    e.employment_type,
    COUNT(*) AS total

FROM employees e
JOIN departments d
ON e.department_id = d.dept_id

{where_clause}

GROUP BY e.employment_type;
"""

employment_df = fetch_data(query)

# ---------------- KPI CARDS ---------------- #

k1,k2,k3 = st.columns(3)

with k1:

    st.metric(
        "Average Resolution Time",
        f"{resolution_df.iloc[0]['avg_time']} hrs"
    )

with k2:

    st.metric(
        "Most Used Tool",
        tool_df.iloc[0]["tool_name"]
    )

with k3:

    st.metric(
        "Average Usage",
        f"{usage_df.iloc[0]['avg_usage']} mins"
    )

st.write("")

# ---------------- HIRING TREND ---------------- #

st.subheader("Employee Hiring Trend")

fig = px.line(
    hiring_df,
    x="month",
    y="hires",
    markers=True
)

fig.update_traces(
    line=dict(width=4),
    marker=dict(size=10)
)

fig.update_layout(
    height=420,
    xaxis_title="Month",
    yaxis_title="Employees Joined",
    showlegend=False,
    plot_bgcolor="white",
    paper_bgcolor="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")

# ---------------- ROW 2 ---------------- #

left, right = st.columns([2,1])

# ============================================================
# Department Performance
# ============================================================

with left:

    st.subheader("Department-wise Onboarding Completion")

    fig = px.bar(
        department_df,
        x="dept_name",
        y="completion",
        color="completion",
        text="completion"
    )

    fig.update_traces(
        texttemplate="%{text}%",
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        showlegend=False,
        xaxis_title="Department",
        yaxis_title="Completion %",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ============================================================
# Support Categories
# ============================================================

with right:

    st.subheader("Support Ticket Categories")

    fig = px.pie(
        support_df,
        names="category",
        values="total",
        hole=0.55
    )

    fig.update_layout(
        height=420,
        legend_title="Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.write("")

# ---------------- ROW 3 ---------------- #

left, right = st.columns(2)

# ============================================================
# Tool Usage Distribution
# ============================================================

with left:

    st.subheader("Tool Usage Distribution")

    fig = px.pie(
        tool_usage_df,
        names="tool_name",
        values="usage",
        hole=0.45
    )

    fig.update_traces(
        textinfo="percent+label"
    )

    fig.update_layout(
        height=420,
        legend_title="Tools"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ============================================================
# Employment Type Distribution
# ============================================================

with right:

    st.subheader("Employment Type Distribution")

    fig = px.bar(
        employment_df,
        x="employment_type",
        y="total",
        color="employment_type",
        text="total"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        showlegend=False,
        xaxis_title="Employment Type",
        yaxis_title="Employees",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.write("")

# ---------------- SUMMARY ---------------- #

st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.info(
        f"""
**Top Performing Department**

{department_df.iloc[0]['dept_name']}

Completion Rate: **{department_df.iloc[0]['completion']}%**
"""
    )

with c2:
    st.success(
        f"""
**Most Used Tool**

{tool_df.iloc[0]['tool_name']}

Average Usage: **{usage_df.iloc[0]['avg_usage']} mins**
"""
    )

with c3:
    st.warning(
        f"""
**Support Categories**

{support_df.shape[0]} Categories

Monitor ticket trends regularly.
"""
    )

st.write("")
st.caption("OnBoardIQ Analytics • Live PostgreSQL Data")