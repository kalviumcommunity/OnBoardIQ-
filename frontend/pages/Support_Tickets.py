import streamlit as st
from backend.database.database_utils import fetch_data

st.set_page_config(page_title="Support Tickets", layout="wide")

# ----------------------------
# PAGE STYLE
# ----------------------------

st.markdown("""
<style>

.main{
    background:#F5F7FB;
}

.block-container{
    padding-top:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

div[data-testid="stVerticalBlock"]>div:has(div.ticket-box){
    background:#F8FAFC;
}

.ticket{
    background:white;
    border-radius:12px;
    padding:18px;
    border:1px solid #E5E7EB;
    margin-bottom:15px;
}

.small{
    font-size:12px;
    color:#6B7280;
}

.high{
    color:#EF4444;
    font-weight:700;
}

.medium{
    color:#F59E0B;
    font-weight:700;
}

.low{
    color:#2563EB;
    font-weight:700;
}

.resolved{
    color:#22C55E;
    font-weight:700;
}

.title{
    font-size:20px;
    font-weight:700;
    color:#111827;
}

.desc{
    color:#6B7280;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# DATABASE DATA
# ----------------------------

open_tickets = fetch_data("""
SELECT
    st.ticket_id AS id,
    UPPER(st.priority) AS priority,
    st.title,
    st.description,
    u.name AS employee,
    d.dept_name AS team
FROM support_tickets st
JOIN employees e
ON st.employee_id = e.emp_id
JOIN users u
ON e.user_id = u.user_id
JOIN departments d
ON e.department_id = d.dept_id
WHERE st.status = 'Open';
""").to_dict("records")


progress_tickets = fetch_data("""
SELECT
    st.ticket_id AS id,
    UPPER(st.priority) AS priority,
    st.assigned_to_user_id,
    st.title,
    st.description,
    u.name AS employee,
    d.dept_name AS team
FROM support_tickets st
JOIN employees e
ON st.employee_id = e.emp_id
JOIN users u
ON e.user_id = u.user_id
JOIN departments d
ON e.department_id = d.dept_id
WHERE st.status='In Progress';
""").to_dict("records")


resolved_tickets = fetch_data("""
SELECT
    st.ticket_id AS id,
    'RESOLVED' AS priority,
    st.resolved_at,
    st.title,
    st.description,
    u.name AS employee,
    d.dept_name AS team
FROM support_tickets st
JOIN employees e
ON st.employee_id = e.emp_id
JOIN users u
ON e.user_id = u.user_id
JOIN departments d
ON e.department_id = d.dept_id
WHERE st.status IN ('Resolved','Closed');
""").to_dict("records")

# ----------------------------
# HEADER
# ----------------------------

left,right = st.columns([5,1])

with left:

    st.title("Support Tickets")

    st.caption(
        "Manage and monitor employee technical hurdles during onboarding."
    )

with right:

    st.write("")
    st.button("➕ Create Ticket",use_container_width=True)

st.divider()

# ----------------------------
# KPI
# ----------------------------

total_df = fetch_data("""
SELECT COUNT(*) AS total
FROM support_tickets;
""")

open_df = fetch_data("""
SELECT COUNT(*) AS total
FROM support_tickets
WHERE status='Open';
""")

progress_df = fetch_data("""
SELECT COUNT(*) AS total
FROM support_tickets
WHERE status='In Progress';
""")

resolved_df = fetch_data("""
SELECT COUNT(*) AS total
FROM support_tickets
WHERE status IN ('Resolved','Closed');
""")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "🎫 Total Tickets",
        int(total_df.iloc[0]["total"])
    )

with k2:
    st.metric(
        "🟠 Open",
        int(open_df.iloc[0]["total"])
    )

with k3:
    st.metric(
        "🟡 In Progress",
        int(progress_df.iloc[0]["total"])
    )

with k4:
    st.metric(
        "🟢 Resolved",
        int(resolved_df.iloc[0]["total"])
    )

st.divider()

# ----------------------------
# CARD
# ----------------------------

def ticket_card(ticket,column_type):

    color = {
        "HIGH":"high",
        "MEDIUM":"medium",
        "LOW":"low",
        "CRITICAL": "high",
        "RESOLVED":"resolved"
    }

    with st.container(border=True):

        c1,c2 = st.columns([3,1])

        with c1:
            st.markdown(
                f"<span class='{color[ticket['priority']]}'>{ticket['priority']} PRIORITY</span>",
                unsafe_allow_html=True
            )

        with c2:
            if column_type == "open":
                st.caption(f"#TK-{ticket['id']}")

            elif column_type == "progress":
                st.caption(f"User {ticket['assigned_to_user_id']}")

            elif column_type == "resolved":

                if ticket["resolved_at"] is not None:
                    st.caption(str(ticket["resolved_at"]).split(" ")[0])
                else:
                    st.caption("-")
        st.markdown(
            f"<div class='title'>{ticket['title']}</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='desc'>{ticket['description']}</div>",
            unsafe_allow_html=True
        )

        st.write("")

        b1,b2 = st.columns([2,1])

        with b1:
            st.caption("👤 "+ticket["employee"])

        with b2:
            st.caption(ticket["team"])

# ----------------------------
# KANBAN
# ----------------------------

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown("### 🟠 OPEN")

    for ticket in open_tickets:
        ticket_card(ticket,"open")

with col2:

    st.markdown("### 🟡 IN PROGRESS")

    for ticket in progress_tickets:
        ticket_card(ticket,"progress")

with col3:

    st.markdown("### 🟢 RESOLVED")

    for ticket in resolved_tickets:
        ticket_card(ticket,"resolved")