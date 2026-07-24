import streamlit as st

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
# DUMMY DATA
# ----------------------------

open_tickets = [
    {
        "priority":"HIGH",
        "id":"TK-882",
        "title":"VPN Access Denied",
        "description":"Cannot connect to internal staging server from home network.",
        "employee":"Alex Rivera",
        "team":"Engineering"
    },
    {
        "priority":"LOW",
        "id":"TK-885",
        "title":"Slack Channel Invite",
        "description":"Requesting access to #proj-nexus and #team-design channels.",
        "employee":"Jasmine Wu",
        "team":"Design"
    }
]

progress_tickets = [
    {
        "priority":"MEDIUM",
        "id":"TK-883",
        "title":"Laptop Setup Delay",
        "description":"MacBook delivery delayed by courier. Tracking status pending.",
        "employee":"Marcus Thorne",
        "team":"Operations"
    }
]

resolved_tickets = [
    {
        "priority":"RESOLVED",
        "id":"TK-884",
        "title":"Adobe Suite License",
        "description":"Creative Cloud access approved for asset production.",
        "employee":"Sofia Chen",
        "team":"Marketing"
    }
]

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
# CARD
# ----------------------------

def ticket_card(ticket):

    color = {
        "HIGH":"high",
        "MEDIUM":"medium",
        "LOW":"low",
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
            st.caption(ticket["id"])

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
        ticket_card(ticket)

with col2:

    st.markdown("### 🟡 IN PROGRESS")

    for ticket in progress_tickets:
        ticket_card(ticket)

with col3:

    st.markdown("### 🟢 RESOLVED")

    for ticket in resolved_tickets:
        ticket_card(ticket)