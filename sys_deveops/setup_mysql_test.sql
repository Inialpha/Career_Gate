-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS career_gate_test_db;
CREATE USER IF NOT EXISTS 'career_gate_test'@'localhost' IDENTIFIED BY 'career_gate_test_pwd';
GRANT ALL PRIVILEGES ON `career_gate_test_db`.* TO 'career_gate_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'career_gate_test'@'localhost';
FLUSH PRIVILEGES;
