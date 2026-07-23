import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from backend.database.database_utils import fetch_data

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- PAGE STYLE ----------------

st.markdown("""
<style>

/* Background */
.main{
    background:#F5F7FB;
}

/* Page spacing */
.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
    padding-bottom:2rem;
}

/* Main Title */
h1{
    font-size:64px !important;
    font-weight:900 !important;
    color:#111827 !important;
}

/* Section Titles */
h2{
    font-size:42px !important;
    font-weight:900 !important;
    color:#111827 !important;
}

h3{
    font-size:36px !important;
    font-weight:800 !important;
    color:#111827 !important;
}

/* Subtitle */
.subtitle{
    color:#4B5563 !important;
    font-size:24px !important;
    font-weight:600 !important;
}

/* Normal text */
p,label,span{
    font-size:22px !important;
    color:#1F2937 !important;
}

/* Button */
.stButton button{
    font-size:22px !important;
    font-weight:700 !important;
    padding:12px 30px !important;
    border-radius:12px !important;
}

/* KPI Cards */
[data-testid="metric-container"]{
    background:white;
    border-radius:18px;
    padding:30px;
    border:1px solid #D1D5DB;
    box-shadow:0 5px 18px rgba(0,0,0,.08);
}

/* KPI Label */
[data-testid="stMetricLabel"]{
    font-size:24px !important;
    font-weight:800 !important;
    color:#111827 !important;
}

/* KPI Value */
[data-testid="stMetricValue"]{
    font-size:48px !important;
    font-weight:900 !important;
    color:#111827 !important;
}

/* KPI Delta */
[data-testid="stMetricDelta"]{
    font-size:22px !important;
    font-weight:700 !important;
}

/* Charts */
.stPlotlyChart{
    background:white;
    border-radius:18px;
    padding:20px;
    border:1px solid #E5E7EB;
}

/* DataFrame */
thead tr th{
    font-size:24px !important;
    font-weight:900 !important;
    color:#111827 !important;
}

tbody tr td{
    font-size:22px !important;
    font-weight:600 !important;
    color:#374151 !important;
    padding-top:16px !important;
    padding-bottom:16px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

left, right = st.columns([5,1])

with left:
    st.title("Onboarding Insights")
    st.markdown(
        """
        <p class="subtitle">
        Welcome back, Sarah. Here's what's happening with your new hires today.
        </p>
        """,
        unsafe_allow_html=True
    )

with right:
    st.button("➕ New Hire")

st.write("")


# ---------------- DATABASE ----------------

# Total Employees
total_df = fetch_data("""
SELECT COUNT(*) AS total_employees
FROM employees;
""")

# Onboarding Completion
completion_df = fetch_data("""
SELECT ROUND(
    COUNT(*) FILTER (WHERE onboarding_status = 'Completed') * 100.0 /
    COUNT(*),
    1
) AS completion_rate
FROM employees;
""")

# Open Support Tickets
tickets_df = fetch_data("""
SELECT COUNT(*) AS open_tickets
FROM support_tickets
WHERE status IN ('Open', 'In Progress');
""")

# Tool Adoption Rate
tool_df = fetch_data("""
SELECT ROUND(
    COUNT(DISTINCT employee_id) * 100.0 /
    (SELECT COUNT(*) FROM employees),
    1
) AS tool_adoption_rate
FROM tool_usage;
""")

# Extract values
total_employees = int(total_df.iloc[0]["total_employees"])
completion_rate = float(completion_df.iloc[0]["completion_rate"])
open_tickets = int(tickets_df.iloc[0]["open_tickets"])
tool_adoption_rate = float(tool_df.iloc[0]["tool_adoption_rate"])

# Completed Employees
completed_df = fetch_data("""
SELECT COUNT(*) AS completed
FROM employees
WHERE onboarding_status = 'Completed';
""")

# Pending Employees
pending_df = fetch_data("""
SELECT COUNT(*) AS pending
FROM employees
WHERE onboarding_status <> 'Completed';
""")

completed = int(completed_df.iloc[0]["completed"])
pending = int(pending_df.iloc[0]["pending"])

department_df = fetch_data("""
SELECT
    d.dept_name AS "Department",
    ROUND(
        COUNT(*) FILTER (WHERE e.onboarding_status = 'Completed') * 100.0 /
        COUNT(*),
        1
    ) AS "Completion"
FROM departments d
JOIN employees e
    ON d.dept_id = e.department_id
GROUP BY d.dept_name
ORDER BY "Completion" DESC;
""")


tool_usage_df = fetch_data("""
SELECT
    tool_name AS "Tool",
    COUNT(*) AS "Usage"
FROM tool_usage
GROUP BY tool_name
ORDER BY "Usage" DESC;
""")

tickets_df = fetch_data("""
SELECT
    u.name AS "Employee",
    s.category AS "Category",
    s.priority AS "Priority",
    s.status AS "Status",
    CASE
        WHEN s.resolved_at IS NOT NULL THEN
            CONCAT(
                ROUND(EXTRACT(EPOCH FROM (s.resolved_at - s.created_at))/3600,1),
                ' hrs'
            )
        ELSE 'Pending'
    END AS "Resolution Time"
FROM support_tickets s
JOIN employees e
    ON s.employee_id = e.emp_id
JOIN users u
    ON e.user_id = u.user_id
ORDER BY s.created_at DESC
LIMIT 10;
""")


task_status_df = fetch_data("""
SELECT
    status AS "Status",
    COUNT(*) AS "Count"
FROM onboarding_tasks
GROUP BY status
ORDER BY "Count" DESC;
""")

# ---------------- KPI ----------------

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric(
        "TOTAL EMPLOYEES",
        total_employees
    )

with c2:
    st.metric(
        "ONBOARDING\nCOMPLETION",
        f"{completion_rate}%"
    )

with c3:
    st.metric(
        "AVG. COMPLETION\nTIME",
        "17 Days"
    )

with c4:
    st.metric(
        "OPEN SUPPORT\nTICKETS",
        open_tickets
    )

with c5:
    st.metric(
        "TOOL ADOPTION\nRATE",
        f"{tool_adoption_rate}%"
    )

st.write("")

# ---------------- ROW 2 ----------------

left,right = st.columns([1,2])

# -------- Progress Circle --------

with left:

    st.subheader("Onboarding Progress")

    fig = go.Figure(
        go.Pie(
            values=[completed, pending],
            hole=0.78,
            marker_colors=["#2563EB","#E5E7EB"],
            textinfo="none"
        )
    )

    fig.update_layout(
        height=340,
        margin=dict(t=20,b=20,l=50,r=20),
        annotations=[
            dict(
                text=f"<b style='font-size:52px'>{completion_rate}%</b><br><span style='font-size:24px'>Completion</span>",
                showarrow=False
            )
        ],
        font=dict(
            family="Arial Black",
            size=24,
            color="#111827"
        )
    )

    st.plotly_chart(fig,use_container_width=True)

    a,b=st.columns(2)

    st.metric("Completed", completed)
    st.metric("Pending", pending)

# -------- Department Chart --------

with right:

    dept = department_df

    fig=px.bar(
        dept,
        x="Completion",
        y="Department",
        orientation="h",
        text="Completion"
    )

    fig.update_traces(
        marker_color="#2563EB",
        texttemplate="%{text}%",
        textposition="outside",
        textfont_size=22
    )

    fig.update_layout(
        title="Department Comparison",
        title_font=dict(
            size=36,
            family="Arial Black",
            color="#111827"
        ),
        height=480,
        xaxis=dict(
            range=[0,100],
            visible=False
        ),
        yaxis=dict(
            categoryorder="total ascending",
            tickfont=dict(
                size=24,
                family="Arial Black",
                color="#111827"
            )
        ),
        font=dict(
            family="Arial Black",
            size=22,
            color="#111827"
        )
    )

    st.plotly_chart(fig,use_container_width=True)
# ---------------- ROW 3 ----------------

left, right = st.columns(2)

# -------- Tool Adoption --------

with left:

    tools = tool_usage_df

    fig = px.bar(
        tools,
        x="Tool",
        y="Usage",
        color="Tool",
        text="Usage"
    )

    fig.update_traces(
        texttemplate="%{text}%",
        textposition="outside",
        textfont_size=22
    )

    fig.update_layout(
        title="Tool Adoption Rate",
        title_font=dict(
            size=36,
            family="Arial Black",
            color="#111827"
        ),
        height=450,
        showlegend=False,
        font=dict(
            family="Arial Black",
            size=22,
            color="#111827"
        ),
        xaxis=dict(
            tickfont=dict(size=22)
        ),
        yaxis=dict(
            tickfont=dict(size=22),
            range=[0,100]
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------- Task Completion Status --------

with right:

    fig = px.bar(
        task_status_df,
        x="Status",
        y="Count",
        color="Status",
        text="Count"
    )

    fig.update_traces(
        textposition="outside",
        textfont_size=20
    )

    fig.update_layout(
        title="Task Completion Status",
        title_font=dict(
            size=36,
            family="Arial Black",
            color="#111827"
        ),
        height=450,
        showlegend=False,
        font=dict(
            family="Arial Black",
            size=22,
            color="#111827"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------- TABLE ----------------

st.markdown("## Recent Support Tickets")

tickets = tickets_df

styled_table = (
    tickets.style
    .set_properties(**{
        "font-size": "22px",
        "font-weight": "600",
        "text-align": "left",
        "padding": "16px"
    })
    .set_table_styles([
        {
            "selector": "th",
            "props": [
                ("font-size", "24px"),
                ("font-weight", "900"),
                ("background-color", "#F3F4F6"),
                ("color", "#111827"),
                ("text-align", "left"),
                ("padding", "18px")
            ]
        }
    ])
)

st.dataframe(
    styled_table,
    use_container_width=True,
    hide_index=True,
    height=280
)