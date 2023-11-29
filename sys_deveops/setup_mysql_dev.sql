-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS career_gate_dev_db;
CREATE USER IF NOT EXISTS 'career_gate_dev'@'localhost' IDENTIFIED BY 'career_gate_dev_pwd';
GRANT ALL PRIVILEGES ON `career_gate_dev_db`.* TO 'career_gate_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'career_gate_dev'@'localhost';
FLUSH PRIVILEGES;
