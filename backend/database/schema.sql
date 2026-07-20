-- ==========================
-- USERS TABLE
-- ==========================
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('Admin', 'HR', 'Manager', 'Employee')),
    contact_no VARCHAR(15),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- ==========================
-- DEPARTMENTS TABLE
-- ==========================
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100) UNIQUE NOT NULL
);

-- ==========================
-- EMPLOYEES TABLE
-- ==========================
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,

    user_id INTEGER UNIQUE NOT NULL,
    department_id INTEGER,

    manager_id INTEGER,
    team_lead_id INTEGER,

    designation VARCHAR(100) NOT NULL,
    joining_date DATE NOT NULL,
    probation_end_date DATE,
    employment_type VARCHAR(20)
        CHECK (employment_type IN ('Full-Time','Part-Time','Intern','Contract')),

    onboarding_status VARCHAR(20)
        CHECK (onboarding_status IN ('Pending','In Progress','Completed')),

    CONSTRAINT fk_employee_user
        FOREIGN KEY(user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_department
        FOREIGN KEY(department_id)
        REFERENCES departments(dept_id),

    CONSTRAINT fk_manager
        FOREIGN KEY(manager_id)
        REFERENCES employees(emp_id),

    CONSTRAINT fk_team_lead
        FOREIGN KEY(team_lead_id)
        REFERENCES employees(emp_id)
);

-- ==========================
-- ONBOARDING CHECKLIST
-- ==========================
CREATE TABLE onboarding_checklist (

    checklist_id SERIAL PRIMARY KEY,

    employee_id INTEGER NOT NULL,

    title VARCHAR(150) NOT NULL,
    description TEXT,

    status VARCHAR(20)
        CHECK(status IN ('Pending','Completed')),

    due_date DATE,
    completed_date DATE,

    CONSTRAINT fk_checklist_employee
        FOREIGN KEY(employee_id)
        REFERENCES employees(emp_id)
        ON DELETE CASCADE
);

-- ==========================
-- ONBOARDING TASKS
-- ==========================
CREATE TABLE onboarding_tasks (

    task_id SERIAL PRIMARY KEY,

    employee_id INTEGER NOT NULL,

    assigned_by_user_id INTEGER NOT NULL,

    task_name VARCHAR(150) NOT NULL,

    description TEXT,

    status VARCHAR(20)
        CHECK(status IN ('Pending','In Progress','Completed')),

    due_date DATE,

    completion_date DATE,

    CONSTRAINT fk_task_employee
        FOREIGN KEY(employee_id)
        REFERENCES employees(emp_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_task_assignedby
        FOREIGN KEY(assigned_by_user_id)
        REFERENCES users(user_id)
);

-- ==========================
-- TOOL USAGE
-- ==========================
CREATE TABLE tool_usage (

    usage_id SERIAL PRIMARY KEY,

    employee_id INTEGER NOT NULL,

    tool_name VARCHAR(100) NOT NULL,

    login_count INTEGER DEFAULT 0,

    last_used TIMESTAMP,

    total_usage_minutes INTEGER DEFAULT 0,

    CONSTRAINT fk_usage_employee
        FOREIGN KEY(employee_id)
        REFERENCES employees(emp_id)
        ON DELETE CASCADE
);

-- ==========================
-- SUPPORT TICKETS
-- ==========================
CREATE TABLE support_tickets (

    ticket_id SERIAL PRIMARY KEY,

    employee_id INTEGER NOT NULL,

    assigned_to_user_id INTEGER,

    category VARCHAR(50),

    priority VARCHAR(20)
        CHECK(priority IN ('Low','Medium','High','Critical')),

    status VARCHAR(20)
        CHECK(status IN ('Open','In Progress','Resolved','Closed')),

    title VARCHAR(200) NOT NULL,

    description TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    resolved_at TIMESTAMP,

    CONSTRAINT fk_ticket_employee
        FOREIGN KEY(employee_id)
        REFERENCES employees(emp_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_ticket_assigned
        FOREIGN KEY(assigned_to_user_id)
        REFERENCES users(user_id)
);