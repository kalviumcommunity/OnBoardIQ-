import streamlit as st

st.markdown("""
<style>

/* ===== PAGE ===== */
.stApp{
    background-color:#F5F7FB;
}

/* Remove top padding */
.block-container{
    padding-top:1.5rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* ===== PAGE TITLE ===== */
.page-title{
    font-size:46px;
    font-weight:700;
    color:#111827;
    margin-bottom:5px;
}

.page-subtitle{
    font-size:18px;
    color:#6B7280;
    margin-bottom:30px;
}

/* ===== SEARCH BOX ===== */
input{
    border-radius:12px !important;
}

/* ===== BUTTON ===== */
.stButton>button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
    padding:10px 18px;
    font-weight:600;
    font-size:16px;
    width:100%;
}

.stButton>button:hover{
    background:#1D4ED8;
    color:white;
}

/* ===== COLUMN BOX ===== */
.column-box{
    background:#EEF2F7;
    border-radius:18px;
    padding:18px;
    min-height:700px;
}

/* ===== COLUMN TITLE ===== */
.column-title{
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-size:13px;
    font-weight:700;
    color:#6B7280;
    letter-spacing:1px;
    margin-bottom:18px;
    text-transform:uppercase;
}

/* ===== COUNT BADGE ===== */
.count-badge{
    background:white;
    border-radius:50%;
    width:24px;
    height:24px;
    display:flex;
    justify-content:center;
    align-items:center;
    font-size:12px;
    font-weight:700;
    color:#374151;
}

/* ===== EMPLOYEE CARD ===== */
.employee-card{
    background:white;
    border-radius:14px;
    padding:18px;
    margin-bottom:18px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    border:1px solid #E5E7EB;
}

/* ===== DEPARTMENT BADGE ===== */
.badge{
    display:inline-block;
    padding:5px 10px;
    border-radius:8px;
    font-size:11px;
    font-weight:700;
    text-transform:uppercase;
}

.badge-engineering{
    background:#DBEAFE;
    color:#2563EB;
}

.badge-marketing{
    background:#EDE9FE;
    color:#7C3AED;
}

.badge-sales{
    background:#FDE68A;
    color:#92400E;
}

.badge-product{
    background:#FEE2E2;
    color:#DC2626;
}

/* ===== STATUS TEXT ===== */
.status{
    float:right;
    font-size:12px;
    color:#6B7280;
}

/* ===== EMPLOYEE NAME ===== */
.emp-name{
    font-size:22px;
    font-weight:700;
    color:#111827;
    margin-top:14px;
}

/* ===== ROLE ===== */
.role{
    font-size:15px;
    color:#6B7280;
    margin-bottom:18px;
}

/* ===== PROGRESS ===== */
.progress-label{
    font-size:13px;
    color:#6B7280;
    margin-bottom:6px;
}

.progress-value{
    float:right;
    font-weight:700;
    color:#111827;
}

/* ===== FOOTER ===== */
.manager{
    border-top:1px solid #E5E7EB;
    margin-top:18px;
    padding-top:14px;
    color:#6B7280;
    font-size:13px;
}

/* ===== ARROW ===== */
.arrow{
    float:right;
    font-size:20px;
    color:#6B7280;
}

/* ===== HR ===== */
hr{
    border:none;
    border-top:1px solid #E5E7EB;
    margin-top:14px;
    margin-bottom:14px;
}

</style>
""", unsafe_allow_html=True)