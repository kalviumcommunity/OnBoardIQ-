# Power BI Development Documentation

## Project

**OnBoardIQ – Employee Onboarding Insights Dashboard**

This document tracks the development progress of the Power BI dashboard for the OnBoardIQ project.

---

# Objective

The objective of the Power BI dashboard is to provide HR teams and management with interactive visualizations to monitor employee onboarding, support tickets, workforce distribution, and operational insights.

---

# Environment

| Component | Details |
|-----------|---------|
| Power BI Desktop | June 2026 Version |
| Database | PostgreSQL |
| Connection Type | Direct Database Connection |
| Data Source | employee_onboarding_dashboard |
| Status | Connected Successfully |

---

# Database Connection

Completed

- Connected Power BI to PostgreSQL.
- Imported project tables.
- Verified successful data loading.
- Auto-detected relationships between tables.

Imported Tables

- departments
- employees
- users
- tool_usage
- support_tickets
- onboarding_tasks
- onboarding_checklist

Status

Completed

---

# Data Model

Verified relationships between tables.

Relationships include:

- Departments → Employees
- Employees → Users
- Employees → Support Tickets
- Employees → Tool Usage
- Employees → Onboarding Tasks
- Employees → Onboarding Checklist

Status

Completed

---

# Dashboard Development

## KPI Cards

### 1. Total Employees

Description

Displays the total number of employees.

Field Used

employees → emp_id

Aggregation

Count

Status
Completed

---

### 2. Completed Onboarding

Description

Displays the number of employees who have completed onboarding.

Field Used

employees → emp_id

Filter Applied

onboarding_status = Completed

Aggregation

Count

Status

Completed

---

### 3. Active Tickets

Description

Displays the number of active support tickets.

Field Used

support_tickets → ticket_id

Filter Applied

status = Open OR In Progress

Aggregation

Count

Status

Completed

---

### 4. Average Resolution Time

Description

Displays the average number of days required to resolve support tickets.

Calculated Column

Resolution Days

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

Field Used

Resolution Days

Aggregation

Average

Visual Filter

- Closed
- Resolved

Status

Completed

---

# Charts

## Employees by Department

Visual

Clustered Bar Chart

Fields

Y-Axis

departments → dept_name

X-Axis

employees → emp_id (Count)

Purpose

Shows workforce distribution across departments.

Status

Completed

---

## Onboarding Status Distribution

Visual

Donut Chart

Fields

Legend

employees → onboarding_status

Values

employees → emp_id (Count)

Purpose

Displays the distribution of employees based on onboarding progress.

Status

Completed

---

Added New Visualizations
Support Tickets by Category
Created a clustered column chart to visualize support tickets grouped by category.
Configured Category on the X-axis and Count of Ticket ID on the Y-axis.
Added an appropriate chart title for better readability.
Tool Usage Distribution
Created a donut chart to visualize employee tool adoption.
Used Tool Name as the legend and Count of Usage ID as the value.
Enabled percentage and count labels for easier interpretation.

---

# DAX

Created Calculated Column

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

Calculates the number of days taken to resolve a support ticket.

Status

Completed

---

# Concepts Learned

During development, the following Power BI concepts were explored:

- Connecting PostgreSQL to Power BI
- Importing relational datasets
- Understanding the Data Model
- Table Relationships
- Card Visuals
- Clustered Bar Charts
- Donut Charts
- Visual-Level Filters
- Count vs Sum vs Average Aggregations
- Calculated Columns
- DAX Basics
- Dashboard Layout

---

# Current Dashboard Progress

## Completed

- PostgreSQL Connection
- Data Import
- Relationship Validation
- KPI Cards
- Employees by Department Chart
- Onboarding Status Distribution Chart
- Resolution Days Calculated Column

Overall Completion

Approximately **60–65%**

---

# Pending Development

## Charts

- Hiring Trend
- Support Ticket Categories
- Tool Usage Distribution
- Employment Type Distribution (if required)

---

## Dashboard Features

- Slicers
- Interactive Filtering
- Cross Filtering
- Final Layout Optimization
- Dashboard Formatting
- Color Consistency
- Alignment and Spacing

---

## DAX

Planned

- Additional Measures
- Advanced KPIs (if required)

---

# Challenges Faced

- Understanding the new Power BI interface.
- Learning the difference between calculated columns and measures.
- Applying visual-level filters correctly.
- Using appropriate aggregations (Count, Sum, Average).
- Creating DAX expressions for calculated values.

---

# Next Steps

The next development session will focus on:

1. Hiring Trend Line Chart
2. Support Ticket Category Analysis
3. Tool Usage Dashboard
4. Interactive Slicers
5. Final Dashboard Layout
6. Dashboard Formatting
7. Final Review and Testing

---

# Development Status

| Module | Status |
|----------|--------|
| PostgreSQL Connection | Completed |
| Data Model | Completed |
| KPI Cards | Completed |
| DAX Basics | Completed |
| Department Chart | Completed |
| Onboarding Chart | Completed |
| Remaining Charts | In Progress |
| Dashboard Formatting | Pending |
| Final Dashboard | Pending |

---

**Last Updated:** Sprint 3

**Current Progress:** ~65% Complete