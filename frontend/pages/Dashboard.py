import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

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

# ---------------- KPI ----------------

c1,c2,c3,c4,c5 = st.columns(5)

with c1:
    st.metric("TOTAL EMPLOYEES","248","+12%")

with c2:
    st.metric("ONBOARDING\nCOMPLETION","87%","+3%")

with c3:
    st.metric("AVG. COMPLETION\nTIME","17d","-2d")

with c4:
    st.metric("OPEN SUPPORT\nTICKETS","19","-4")

with c5:
    st.metric("TOOL ADOPTION\nRATE","82%","+5%")

st.write("")

# ---------------- ROW 2 ----------------

left,right = st.columns([1,2])

# -------- Progress Circle --------

with left:

    st.subheader("Onboarding Progress")

    fig = go.Figure(
        go.Pie(
            values=[87,13],
            hole=0.78,
            marker_colors=["#2563EB","#E5E7EB"],
            textinfo="none"
        )
    )

    fig.update_layout(
        height=380,
        margin=dict(t=20,b=20,l=20,r=20),
        annotations=[
            dict(
                text="<b style='font-size:52px'>87%</b><br><span style='font-size:24px'>Completion</span>",
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

    with a:
        st.metric("Completed","216")

    with b:
        st.metric("Pending","32")

# -------- Department Chart --------

with right:

    dept=pd.DataFrame({
        "Department":["Engineering","HR","Marketing","Finance","Sales"],
        "Completion":[94,82,76,91,68]
    })

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

    tools = pd.DataFrame({
        "Tool": [
            "Slack",
            "Jira",
            "GitHub",
            "Confluence",
            "Google",
            "Notion"
        ],
        "Usage": [
            88,
            75,
            91,
            67,
            84,
            61
        ]
    })

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

# -------- Employee Productivity --------

with right:

    months = [
        "Jan",
        "Mar",
        "May",
        "Jul",
        "Sep",
        "Nov"
    ]

    productivity = [
        35,
        55,
        48,
        82,
        36,
        78
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=months,
            y=productivity,
            mode="lines+markers",
            line=dict(
                color="#2563EB",
                width=5
            ),
            marker=dict(
                size=10
            ),
            fill="tozeroy"
        )
    )

    fig.update_layout(
        title="Employee Productivity",
        title_font=dict(
            size=36,
            family="Arial Black",
            color="#111827"
        ),
        height=450,
        font=dict(
            family="Arial Black",
            size=22,
            color="#111827"
        ),
        xaxis=dict(
            tickfont=dict(size=22)
        ),
        yaxis=dict(
            tickfont=dict(size=22)
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------- TABLE ----------------

st.markdown("## Recent Support Tickets")

tickets = pd.DataFrame({

    "Employee": [
        "Alex Chen",
        "Mia Thompson",
        "David Wilson",
        "Elena Rodriguez"
    ],

    "Category": [
        "IT Setup",
        "Benefits",
        "Security Policy",
        "Tool Access"
    ],

    "Priority": [
        "HIGH",
        "MEDIUM",
        "CRITICAL",
        "LOW"
    ],

    "Status": [
        "In Progress",
        "Resolved",
        "Pending",
        "Resolved"
    ],

    "Resolution Time": [
        "2.5h",
        "18.0h",
        "0.5h",
        "4.2h"
    ]

})

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