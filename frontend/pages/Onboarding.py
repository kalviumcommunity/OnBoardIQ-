import streamlit as st

st.set_page_config(page_title="Onboarding", layout="wide")

# -----------------------------
# Dummy Data
# -----------------------------
not_started = [
    {
        "department": "Engineering",
        "name": "Alex Rivera",
        "role": "Full Stack Engineer",
        "manager": "David K.",
        "progress": 0,
        "status": "Joined Today"
    },
    {
        "department": "Product",
        "name": "Jamie Chen",
        "role": "Product Manager",
        "manager": "Sarah J.",
        "progress": 0,
        "status": "Starts in 2 Days"
    }
]

in_progress = [
    {
        "department": "Marketing",
        "name": "Marcus Thompson",
        "role": "Growth Strategist",
        "manager": "Elena V.",
        "progress": 45,
        "status": "Day 14"
    },
    {
        "department": "Engineering",
        "name": "Sophia Zhang",
        "role": "Senior DevOps Engineer",
        "manager": "Robert L.",
        "progress": 78,
        "status": "Day 42"
    }
]

completed = [
    {
        "department": "Sales",
        "name": "Jordan Miller",
        "role": "Account Executive",
        "manager": "Lisa W.",
        "progress": 100,
        "status": "Finished"
    }
]

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