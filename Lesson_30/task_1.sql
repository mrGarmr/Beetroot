
-- Create a table
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    department TEXT NOT NULL
);

-- Rename the table
ALTER TABLE employees RENAME TO staff;

-- Add a new column
ALTER TABLE staff ADD COLUMN salary REAL;

-- Insert rows
INSERT INTO staff (name, age, department, salary) VALUES ('Oles Poderevlnskiy', 55, 'StandUper', 55000);
INSERT INTO staff (name, age, department, salary) VALUES ('Taras Shevchenko', 35, 'Poet', 70000);

-- Update a row
UPDATE staff SET salary = 60000 WHERE name = 'Taras Shevchenko';

-- Delete a row
DELETE FROM staff WHERE name = 'Oles Poderevlnskiy';

