import streamlit as st
from streamlit_option_menu import option_menu
import runpy

st.set_page_config(
    page_title="OnboardIQ",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

/* Hide Streamlit default multipage navigation */
[data-testid="stSidebarNav"]{
    display:none;
}

/* Sidebar */
st.set_page_config(
    page_title="OnboardIQ",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

/* Sidebar padding */
[data-testid="stSidebar"] > div:first-child{
    padding-top:20px;
    padding-left:10px;
    padding-right:10px;
}

/* Hide Streamlit menu/footer */
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

    st.markdown("""
<div style="padding:8px 0 20px 8px;">
    <span style="
        font-family: Inter, Arial, sans-serif;
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

# ---------------- PAGE ROUTING ----------------

if selected == "Dashboard":
    runpy.run_path("pages/Dashboard.py")

elif selected == "Employees":
    runpy.run_path("pages/Employees.py")

elif selected == "Onboarding":
    runpy.run_path("pages/Onboarding.py")

elif selected == "Tool Usage":
    runpy.run_path("pages/Tool_Usage.py")

elif selected == "Support Tickets":
    runpy.run_path("pages/Support_Tickets.py")

elif selected == "Analytics":
    runpy.run_path("pages/Analytics.py")

elif selected == "Settings":
    st.title("⚙️ Settings")
    st.info("Coming Soon...")