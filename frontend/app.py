import streamlit as st
from streamlit_option_menu import option_menu
import runpy
import sys
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.auth.login import login_user
from backend.auth.signup import register_user

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="OnboardIQ",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SESSION STATE ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

BASE_DIR = os.path.dirname(__file__)
PAGES_DIR = os.path.join(BASE_DIR, "pages")

# ---------------- LOGIN / SIGNUP ----------------

if not st.session_state.logged_in:

    # ---------- LOGIN ----------
    if not st.session_state.show_signup:

        st.title("🚀 OnboardIQ")
        st.subheader("Welcome Back")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):

            user = login_user(email, password)

            if user:

                st.session_state.logged_in = True
                st.session_state.user = user

                st.success("Login Successful")
                st.rerun()

            else:

                st.error("Invalid email or password")

        col1, col2 = st.columns([4, 1])

        with col1:
            st.write("Don't have an account?")

        with col2:
            if st.button("Sign Up"):
                st.session_state.show_signup = True
                st.rerun()

    # ---------- SIGNUP ----------
    else:

        st.title("🚀 OnboardIQ")
        st.subheader("Create Your Account")

        full_name = st.text_input("Full Name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )
        confirm = st.text_input(
            "Confirm Password",
            type="password",
            key="confirm_password"
        )

        if st.button("Create Account", use_container_width=True):

            if password != confirm:
                st.error("Passwords do not match.")
            elif full_name == "" or email == "" or password == "":
                st.warning("Please fill all the fields.")
            else:

                success, message = register_user(
                    full_name,
                    email,
                    password
                )

                if success:

                    st.success(message)

                    st.session_state.show_signup = False

                    st.info("Please login.")

                    st.rerun()

                else:

                    st.error(message)

        if st.button("← Back to Login"):
            st.session_state.show_signup = False
            st.rerun()

    st.stop()

# ---------------- CSS ----------------

st.markdown("""
<style>

[data-testid="stSidebarNav"]{
    display:none;
}

[data-testid="stSidebar"] > div:first-child{
    padding-top:20px;
    padding-left:10px;
    padding-right:10px;
}

/* Hide the collapse/expand arrow */
[data-testid="stSidebarCollapseButton"]{
    display:none;
}

/* Older Streamlit versions */
[data-testid="collapsedControl"]{
    display:none;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

with st.sidebar:
    if st.session_state.user:

        st.write(f"👋 Welcome, {st.session_state.user['name']}")
        st.caption(st.session_state.user["role"])
        st.caption(
        f"Last Login: {st.session_state.user['last_login']}"
        )
        st.divider()

    st.markdown("""
<div style="padding:8px 0 20px 8px;">
<span style="
font-family:Inter,Arial,sans-serif;
font-size:32px;
font-weight:700;
color:#2563EB;
letter-spacing:-0.5px;
">
OnboardIQ
</span>
</div>
""", unsafe_allow_html=True)

    st.divider()

    selected = option_menu(
        menu_title=None,

        options=[
            "Dashboard",
            "Employees",
            "Onboarding",
            "Tool Usage",
            "Support Tickets",
            "Analytics",
            "Settings"
        ],

        icons=[
            "house-fill",
            "people-fill",
            "person-check-fill",
            "tools",
            "ticket-fill",
            "bar-chart-fill",
            "gear-fill"
        ],

        default_index=0,

        styles={

            "container":{
                "padding":"0px",
                "background-color":"white",
            },

            "icon":{
                "color":"#2563EB",
                "font-size":"16px",
            },

            "nav-link":{
                "font-size":"18px",
                "font-weight":"600",
                "text-align":"left",
                "padding":"10px 12px",
                "margin":"6px 0",
                "border-radius":"12px",
                "color":"#111827",
                "--hover-color":"#F3F4F6",
            },

            "nav-link-selected":{
                "background-color":"#EAF2FF",
                "color":"#2563EB",
                "font-weight":"700",
            }

        }
    )
    st.divider()

    if st.button("Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

# ---------------- PAGE ROUTING ----------------

if selected == "Dashboard":
    runpy.run_path(os.path.join(PAGES_DIR, "Dashboard.py"))

elif selected == "Employees":
    runpy.run_path(os.path.join(PAGES_DIR, "Employees.py"))

elif selected == "Onboarding":
    runpy.run_path(os.path.join(PAGES_DIR, "Onboarding.py"))

elif selected == "Tool Usage":
    runpy.run_path(os.path.join(PAGES_DIR, "Tool_Usage.py"))

elif selected == "Support Tickets":
    runpy.run_path(os.path.join(PAGES_DIR, "Support_Tickets.py"))

elif selected == "Analytics":
    runpy.run_path(os.path.join(PAGES_DIR, "Analytics.py"))

elif selected == "Settings":
    runpy.run_path(os.path.join(PAGES_DIR, "Settings.py"))