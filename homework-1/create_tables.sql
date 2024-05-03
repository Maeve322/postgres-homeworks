
-- Использование базы данных "north"
\c north;

-- Создание таблицы "employees"
CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    notes VARCHAR(500) NOT NULL
);

-- Создание таблицы "customers"
CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    company_name VARCHAR(50) NOT NULL,
    contact_name VARCHAR(50) NOT NULL
);

-- Создание таблицы "orders"
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id VARCHAR REFERENCES customers(customer_id),
    employee_id INT REFERENCES employees(employee_id),
    order_date DATE,
    ship_city VARCHAR(255)
);-- SQL-команды для создания таблиц
