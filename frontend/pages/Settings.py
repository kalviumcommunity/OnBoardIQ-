import streamlit as st

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="OnboardIQ | Settings",
    page_icon="⚙️",
    layout="wide"
)

# -------------------------------------------------
# CSS
# -------------------------------------------------
st.markdown("""
<style>

.main{
    background:#F8FAFC;
}

.block-container{
    padding-top:30px;
    padding-left:35px;
    padding-right:35px;
}

.title{
    font-size:34px;
    font-weight:700;
    color:#1E293B;
    margin-bottom:20px;
}

/* Card */
div[data-testid="stVerticalBlockBorderWrapper"]{
    background:white;
    border:1px solid #E5E7EB;
    border-radius:18px;
    padding:22px;
    margin-bottom:22px;
    box-shadow:0 2px 8px rgba(15,23,42,.05);
}

/* Blue Button */
div.stButton > button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
    height:44px;
    font-weight:600;
}

div.stButton > button:hover{
    background:#1D4ED8;
    color:white;
}

/* Text Inputs */

div[data-baseweb="input"]{
    border-radius:10px;
}

/* Upload */

div[data-testid="stFileUploader"]{
    border:none;
}

/* Small text */

.small{
    color:#64748B;
    font-size:13px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Title
# -------------------------------------------------

st.markdown('<p class="title">Settings</p>', unsafe_allow_html=True)

# -------------------------------------------------
# SETTINGS MENU + PROFILE
# -------------------------------------------------

left, right = st.columns([1,4])

# ===========================
# Left Menu
# ===========================

with left:
    menu = [
        "👤 Profile Settings",
        "🔔 Notifications",
        "👥 Role Management",
        "🔒 Security",
        "🎨 Theme"
        ]

    for i, item in enumerate(menu):

        if i == 0:
            st.markdown(f"""
            <div style="
                border:2px solid #2563EB;
                border-radius:12px;
                padding:14px;
                margin-bottom:10px;
                font-weight:600;
                color:#2563EB;
                background:white;
            ">
                {item}
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown(f"""
            <div style="
                border:1px solid #E5E7EB;
                border-radius:12px;
                padding:14px;
                margin-bottom:10px;
                font-weight:600;
                color:#374151;
                background:white;
            ">
                {item}
            </div>
            """, unsafe_allow_html=True)

# ===========================
# Profile Card
# ===========================

with right:

    with st.container(border=True):

        head1, head2 = st.columns([5,2])

        with head1:

            st.markdown("### Profile Settings")

            st.markdown(
                '<p class="small">Manage your public profile and account details.</p>',
                unsafe_allow_html=True
            )

        with head2:

            st.write("")
            st.write("")

            st.button(
                "Save Changes",
                type="primary",
                use_container_width=True
            )

        st.write("")

        img, form = st.columns([1,3])

        # ---------------- Avatar ----------------

        with img:
            st.markdown("""
                <div style="
                width:100px;
                height:100px;
                border-radius:50%;
                background:#F1F5F9;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:48px;
                color:#64748B;
                margin:auto;
                border:3px solid #E5E7EB;
            ">
            👤
            </div>
            """, unsafe_allow_html=True)
                    width:100px;
                    height:100px;
                    border-radius:50%;
                    background:#F1F5F9;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:48px;
                    color:#64748B;
                    margin:auto;
                    border:3px solid #E5E7EB;
                ">
                👤
                </div>
                """, unsafe_allow_html=True)


            st.markdown(
                "<center><b></b></center>",
                unsafe_allow_html=True
       
            st.markdown(
                "<center><span style='color:#2563EB;font-size:13px;'>Remove photo</span></center>",
                unsafe_allow_html=True
            )

        # ---------------- Form ----------------

        with form:

            c1, c2 = st.columns(2)

            with c1:

                full_name = st.text_input(
                    "Full Name",
                    value="Sarah Johnson"
                )

            with c2:

                email = st.text_input(
                    "Email Address",
                    value="sarah.johnson@onboardiqinsights.io"
                )

            job = st.text_input(
                "Job Title",
                value="HR Manager & Data Strategist"
            )
# =====================================================
# SECURITY & PASSWORD CARD
# =====================================================

    with st.container(border=True):

        st.markdown("### 🔒 Security & Password")

        st.markdown(
            '<p class="small">Update your password to keep your account secure.</p>',
            unsafe_allow_html=True
        )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:
            current_password = st.text_input(
                "Current Password",
                type="password",
                placeholder="Enter current password"
            )

        with col2:
            new_password = st.text_input(
                "New Password",
                type="password",
                placeholder="Enter new password"
            )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Re-enter new password"
        )

        st.write("")

        # Password Requirements Box
        st.info("""
**Password Requirements**

• Minimum **8 characters**

• Include at least **one uppercase letter**

• Include at least **one lowercase letter**

• Include at least **one number**

• Include at least **one special character**
""")

        st.write("")

        if st.button(
            "Update Password",
            use_container_width=True,
            type="primary"
        ):

            if current_password == "":
                st.error("Please enter your current password.")

            elif new_password == "":
                st.error("Please enter a new password.")

            elif confirm_password == "":
                st.error("Please confirm your new password.")

            elif new_password != confirm_password:
                st.error("Passwords do not match.")

            else:
                st.success("Password updated successfully!")

# =====================================================
# DELETE ACCOUNT CARD
# =====================================================

    with st.container(border=True):

        left_col, right_col = st.columns([5, 1.5])

        with left_col:

            st.markdown("""
            <h3 style="color:#DC2626; margin-bottom:0px;">
            🗑 Delete Account
            </h3>
            """, unsafe_allow_html=True)

            st.markdown("""
            <p class="small">
            Permanently delete your account and all associated data.
            This action cannot be undone.
            </p>
            """, unsafe_allow_html=True)

        with right_col:

            st.write("")
            st.write("")

            delete = st.button(
                "Delete Account",
                type="primary",
                use_container_width=True,
                key="delete_account"
            )

        if delete:

            st.warning(
                "⚠️ This feature is disabled in the demo version."
            )