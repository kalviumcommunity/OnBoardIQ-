-- ============================================================
-- EMPLOYEE ONBOARDING INSIGHTS DASHBOARD
-- ANALYTICS QUERIES
-- ============================================================

-- ============================================================
-- EMPLOYEE ANALYTICS
-- ============================================================

-- Total Employees
SELECT COUNT(*) AS total_employees
FROM employees;

------------------------------------------------------------

-- Employees by Department
SELECT
    d.dept_name,
    COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.dept_id = e.department_id
GROUP BY d.dept_name
ORDER BY employee_count DESC, d.dept_name;

------------------------------------------------------------

-- Employees by Designation
SELECT
    designation,
    COUNT(*) AS employee_count
FROM employees
GROUP BY designation
ORDER BY employee_count DESC;

------------------------------------------------------------

-- Employees by Employment Type
SELECT
    employment_type,
    COUNT(*) AS employee_count
FROM employees
GROUP BY employment_type
ORDER BY employee_count DESC;

------------------------------------------------------------

-- Employees by Onboarding Status
SELECT
    onboarding_status,
    COUNT(*) AS employee_count
FROM employees
GROUP BY onboarding_status
ORDER BY employee_count DESC;

------------------------------------------------------------

-- Employees Currently on Probation
SELECT
    COUNT(*) AS employees_on_probation
FROM employees
WHERE probation_end_date IS NOT NULL
AND probation_end_date >= CURRENT_DATE;

------------------------------------------------------------

-- New Employees Joined in Last 30 Days
SELECT
    COUNT(*) AS new_hires_last_30_days
FROM employees
WHERE joining_date >= CURRENT_DATE - INTERVAL '30 days';

------------------------------------------------------------

-- Department-wise Onboarding Completion
SELECT
    d.dept_name,
    ROUND(
        COUNT(*) FILTER (WHERE onboarding_status = 'Completed') * 100.0 /
        COUNT(*),
        2
    ) AS completion_percentage
FROM employees e
JOIN departments d
ON e.department_id = d.dept_id
GROUP BY d.dept_name
ORDER BY completion_percentage DESC;

------------------------------------------------------------

-- Employees Under Each Manager
SELECT
    u.name AS manager_name,
    COUNT(e.emp_id) AS team_size
FROM employees e
JOIN employees m
ON e.manager_id = m.emp_id
JOIN users u
ON m.user_id = u.user_id
GROUP BY u.name
ORDER BY team_size DESC;

------------------------------------------------------------

-- Employees Under Each Team Lead
SELECT
    u.name AS team_lead_name,
    COUNT(e.emp_id) AS team_size
FROM employees e
JOIN employees t
ON e.team_lead_id = t.emp_id
JOIN users u
ON t.user_id = u.user_id
GROUP BY u.name
ORDER BY team_size DESC;

------------------------------------------------------------

-- Top 5 Departments by Employee Count
SELECT
    d.dept_name,
    COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.dept_id = e.department_id
GROUP BY d.dept_name
ORDER BY employee_count DESC
LIMIT 5;


-- ============================================================
-- ONBOARDING ANALYTICS
-- ============================================================

-- Overall Onboarding Completion Percentage
SELECT
    ROUND(
        COUNT(*) FILTER (WHERE onboarding_status = 'Completed') * 100.0 /
        COUNT(*),
        2
    ) AS onboarding_completion_percentage
FROM employees;

------------------------------------------------------------

-- Pending Checklist Items
SELECT
    COUNT(*) AS pending_checklist_items
FROM onboarding_checklist
WHERE status = 'Pending';

------------------------------------------------------------

-- Completed Checklist Items
SELECT
    COUNT(*) AS completed_checklist_items
FROM onboarding_checklist
WHERE status = 'Completed';

------------------------------------------------------------

-- Pending Tasks
SELECT
    COUNT(*) AS pending_tasks
FROM onboarding_tasks
WHERE status = 'Pending';

------------------------------------------------------------

-- Tasks In Progress
SELECT
    COUNT(*) AS tasks_in_progress
FROM onboarding_tasks
WHERE status = 'In Progress';

------------------------------------------------------------

-- Completed Tasks
SELECT
    COUNT(*) AS completed_tasks
FROM onboarding_tasks
WHERE status = 'Completed';

------------------------------------------------------------

-- Overdue Tasks
SELECT
    COUNT(*) AS overdue_tasks
FROM onboarding_tasks
WHERE due_date < CURRENT_DATE
AND status <> 'Completed';

------------------------------------------------------------

-- Average Tasks Per Employee
SELECT
    ROUND(
        COUNT(*) * 1.0 /
        (SELECT COUNT(*) FROM employees),
        2
    ) AS avg_tasks_per_employee
FROM onboarding_tasks;


-- ============================================================
-- SUPPORT TICKET ANALYTICS
-- ============================================================

-- Total Support Tickets
SELECT
    COUNT(*) AS total_tickets
FROM support_tickets;

------------------------------------------------------------

-- Open Tickets
SELECT
    COUNT(*) AS open_tickets
FROM support_tickets
WHERE status = 'Open';

------------------------------------------------------------

-- Tickets by Status
SELECT
    status,
    COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY status
ORDER BY ticket_count DESC;

------------------------------------------------------------

-- Tickets by Priority
SELECT
    priority,
    COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY priority
ORDER BY ticket_count DESC;

------------------------------------------------------------

-- Tickets by Category
SELECT
    category,
    COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY category
ORDER BY ticket_count DESC;

------------------------------------------------------------

-- Department-wise Support Tickets
SELECT
    d.dept_name,
    COUNT(st.ticket_id) AS total_tickets
FROM support_tickets st
JOIN employees e
ON st.employee_id = e.emp_id
JOIN departments d
ON e.department_id = d.dept_id
GROUP BY d.dept_name
ORDER BY total_tickets DESC;

------------------------------------------------------------

-- Average Resolution Time (Hours)
SELECT
    ROUND(
        AVG(EXTRACT(EPOCH FROM (resolved_at - created_at)) / 3600),
        2
    ) AS avg_resolution_hours
FROM support_tickets
WHERE resolved_at IS NOT NULL;


-- ============================================================
-- TOOL USAGE ANALYTICS
-- ============================================================

-- Tool Usage Records
SELECT
    tool_name,
    COUNT(*) AS usage_records
FROM tool_usage
GROUP BY tool_name
ORDER BY usage_records DESC;

------------------------------------------------------------

-- Total Logins by Tool
SELECT
    tool_name,
    SUM(login_count) AS total_logins
FROM tool_usage
GROUP BY tool_name
ORDER BY total_logins DESC;

------------------------------------------------------------

-- Most Used Tool
SELECT
    tool_name,
    SUM(login_count) AS total_logins
FROM tool_usage
GROUP BY tool_name
ORDER BY total_logins DESC
LIMIT 1;

------------------------------------------------------------

-- Average Login Count
SELECT
    ROUND(AVG(login_count),2) AS avg_login_count
FROM tool_usage;

------------------------------------------------------------

-- Average Usage Minutes
SELECT
    ROUND(AVG(total_usage_minutes),2) AS avg_usage_minutes
FROM tool_usage;

------------------------------------------------------------

-- Total Usage Minutes by Tool
SELECT
    tool_name,
    SUM(total_usage_minutes) AS total_minutes
FROM tool_usage
GROUP BY tool_name
ORDER BY total_minutes DESC;

------------------------------------------------------------

-- Top 5 Employees by Tool Usage
SELECT
    u.name,
    SUM(t.total_usage_minutes) AS usage_minutes
FROM tool_usage t
JOIN employees e
ON t.employee_id = e.emp_id
JOIN users u
ON e.user_id = u.user_id
GROUP BY u.name
ORDER BY usage_minutes DESC
LIMIT 5;


-- ============================================================
-- USER ANALYTICS
-- ============================================================

-- Users by Role
SELECT
    role,
    COUNT(*) AS total_users
FROM users
GROUP BY role
ORDER BY total_users DESC;

------------------------------------------------------------

-- Active Users
SELECT
    COUNT(*) AS active_users
FROM users
WHERE is_active = TRUE;

------------------------------------------------------------

-- Inactive Users
SELECT
    COUNT(*) AS inactive_users
FROM users
WHERE is_active = FALSE;


-- ============================================================
-- DASHBOARD KPI QUERIES
-- ============================================================

-- KPI 1 - Total Employees
SELECT
    COUNT(*) AS total_employees
FROM employees;

------------------------------------------------------------

-- KPI 2 - Pending Tasks
SELECT
    COUNT(*) AS pending_tasks
FROM onboarding_tasks
WHERE status = 'Pending';

------------------------------------------------------------

-- KPI 3 - Open Support Tickets
SELECT
    COUNT(*) AS open_support_tickets
FROM support_tickets
WHERE status = 'Open';

------------------------------------------------------------

-- KPI 4 - Onboarding Completion Percentage
SELECT
    ROUND(
        COUNT(*) FILTER (WHERE onboarding_status = 'Completed') * 100.0 /
        COUNT(*),
        2
    ) AS onboarding_completion_percentage
FROM employees;

------------------------------------------------------------

-- KPI 5 - Active Users
SELECT
    COUNT(*) AS active_users
FROM users
WHERE is_active = TRUE;