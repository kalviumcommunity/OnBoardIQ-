# 👨‍💻 OnBoardIQ - Developer README

> Internal documentation for developers working on the OnBoardIQ project.

---

# Project Information

| Property | Value |
|----------|-------|
| Project Name | OnBoardIQ |
| Project Type | Employee Onboarding Insights Dashboard |
| Domain | HR Analytics |
| Development Status | In Progress |
| Current Sprint | Sprint 3 |
| Database | PostgreSQL |
| Backend | Python |
| Frontend | Streamlit |
| Visualization | Plotly, Power BI |

---

# Project Objective

OnBoardIQ is an HR analytics platform that provides actionable insights into employee onboarding, tool adoption, support requests, and workforce trends.

The project aims to help HR teams and management monitor onboarding progress, identify bottlenecks, and improve employee experience using interactive dashboards.

---

# Technology Stack

## Frontend
- Streamlit
- Plotly Express

## Backend
- Python

## Database
- PostgreSQL

## Analytics
- SQL
- Power BI
- DAX

---

# Current Folder Structure

```
OnBoardIQ
│
├── backend
│   ├── config.py
│   ├── db_connection.py
│   └── database
│       └── database_utils.py
│
├── frontend
│   ├── app.py
│   └── pages
│       ├── Dashboard.py
│       ├── ToolUsage.py
│       └── Analytics.py
│
├── docs
│   └── DEVELOPER_README.md
│
└── requirements.txt
```

---

# Database Tables

Current database contains the following tables:

- departments
- employees
- users
- tool_usage
- support_tickets
- onboarding_tasks
- onboarding_checklist

---

# Development Progress

## Database

### Completed

- PostgreSQL database created
- CSV datasets imported
- Table relationships verified
- Foreign keys implemented
- Database connectivity established
- Streamlit connected with PostgreSQL

Status

✅ Completed

---

## Backend Development

Completed

- Database configuration
- Database connection utility
- Generic SQL fetch function
- Dynamic SQL query execution
- PostgreSQL integration

Files

```
config.py

db_connection.py

database_utils.py
```

Status

✅ Completed

---

# Streamlit Development

## Dashboard Page

Completed

Implemented

- Total Employees KPI
- Completed Onboarding KPI
- Open Tickets KPI
- Tool Adoption KPI
- Department Comparison
- Task Completion Chart
- Tool Adoption Chart
- Support Ticket Overview

Status

✅ Completed

---

## Tool Usage Page

Completed

Implemented

- Tool Adoption Percentage
- Most Used Tool
- Average Usage
- Inactive Employees
- Daily Login Trend
- Tool Usage Distribution

Status

✅ Completed

---

## Analytics Page

Completed

Implemented

Filters

- Department
- Employment Type
- Onboarding Status

Charts

- Hiring Trend
- Department Performance
- Support Categories
- Tool Usage Distribution
- Employment Type Distribution

KPIs

- Average Resolution Time
- Average Usage
- Most Used Tool

Status

✅ Completed

Pending

- UI polish
- Additional filter improvements

---

# SQL Development

Created SQL queries for

- Employee Count
- Hiring Trend
- Department Performance
- Tool Usage
- Average Resolution Time
- Support Categories
- Employment Type
- Most Used Tool
- Average Usage

Implemented dynamic filtering using SQL WHERE clauses.

Status

✅ Completed

---

# Power BI Development

## Current Progress

### Database Integration

Completed

- Installed Power BI Desktop
- Connected PostgreSQL database
- Imported all project tables
- Verified relationships between tables
- Understood the Power BI interface and data model

---

## KPI Dashboard

Completed

Created executive KPI cards for:

- Total Employees
- Completed Onboarding
- Active Tickets
- Average Resolution Time

---

## Visualizations

Completed

- Employees by Department (Clustered Bar Chart)
- Onboarding Status Distribution (Donut Chart)

---

## DAX

Implemented a calculated column:

```DAX
Resolution Days =
IF(
    ISBLANK('public support_tickets'[resolved_at]),
    BLANK(),
    DATEDIFF(
        'public support_tickets'[created_at],
        'public support_tickets'[resolved_at],
        DAY
    )
)
```

Purpose

Calculates the number of days required to resolve a support ticket.

---

## Remaining Work

- Hiring Trend
- Support Ticket Category Analysis
- Tool Usage Dashboard
- Slicers
- Dashboard Formatting
- Advanced DAX Measures (if required)

Status

🟡 Approximately 65% Complete
---

# Challenges Faced

## Streamlit

- Dynamic SQL filtering
- PostgreSQL integration
- Analytics page filtering
- Dashboard layout optimization

## Power BI

- Understanding new June 2026 interface
- Learning visual interactions
- KPI card configuration
- Visual filtering

---

# Bugs Fixed

- PostgreSQL connection issues
- SQL query corrections
- Analytics filter logic
- Dashboard chart rendering
- KPI integration

---

# Current Project Status

| Module | Progress |
|---------|----------|
| Database | 100% |
| Backend | 90% |
| Streamlit Dashboard | 85% |
| SQL Analytics | 100% |
| Power BI | 65% |
| Documentation | In Progress |

Overall Progress

Approximately **85% Complete**

---

# Next Sprint Goals

## Streamlit

- Final UI improvements
- Dashboard polishing

## Power BI

- Complete KPI cards
- Hiring Trend
- Department Charts
- Support Ticket Charts
- Tool Usage Dashboard
- Slicers
- Dashboard formatting
- Advanced DAX

---

# Lessons Learned

During this sprint, the following concepts were explored:

- PostgreSQL integration with Streamlit
- SQL-based analytics
- Dynamic query generation
- Plotly visualizations
- Power BI data modeling
- KPI creation
- Visual filtering
- Introduction to DAX
- Dashboard design principles

---

# Development Notes

- PostgreSQL serves as the single source of truth for all dashboards.
- Streamlit dashboards use live SQL queries.
- Power BI is directly connected to PostgreSQL for interactive reporting.
- SQL queries are reused across multiple dashboard components where possible.
- Dashboard development follows a modular approach to simplify maintenance and future enhancements.

---

# Future Enhancements

- Role-based authentication
- Real-time dashboard refresh
- Predictive onboarding analytics
- Employee churn prediction
- Export reports (PDF/Excel)
- Email notifications
- AI-powered HR insights
- Cloud deployment

---

# Sprint Summary

**Sprint Goal:** Complete analytics integration and begin Power BI dashboard development.

### Achievements

- PostgreSQL fully integrated with Streamlit
- Analytics dashboard completed
- SQL analytics finalized
- Power BI environment configured
- Initial KPI cards created
- Project documentation initiated

**Sprint Status:** 85% completion