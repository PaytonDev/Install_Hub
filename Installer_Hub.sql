-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/bgLYup
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

DROP DATABASE IF EXISTS install;

CREATE DATABASE install;

\c install;


CREATE TABLE Dealerships (
    DTID SERIAL NOT NULL,
    Store_Num TEXT NOT NULL,
    Ent_Code TEXT NOT NULL,    
    D_Name TEXT NOT NULL,
    D_Address TEXT NOT NULL,
    D_City TEXT NOT NULL,
    D_Phone TEXT NOT NULL,
    Services TEXT[] NOT NULL,
    Departments TEXT[] NOT NULL,
    Employees TEXT[] NOT NULL,
    CONSTRAINT pk_Dealership PRIMARY KEY (
        DTID
     )
);

CREATE TABLE Projects (
    ProjectID SERIAL NOT NULL,
    Title TEXT NOT NULL,
    Dealership INT NOT NULL,
    Users TEXT[] NOT NULL,
    Project_Date DATE NOT NULL,
    CONSTRAINT pk_Project PRIMARY KEY (
        ProjectID
     )
);

CREATE TABLE Departments (
    DepartmentID SERIAL NOT NULL,
    Department TEXT NOT NULL,
    CONSTRAINT pk_Department PRIMARY KEY (
        DepartmentID
    )
);


CREATE TABLE Employees (
    EID SERIAL NOT NULL,
    E_FirstName TEXT NOT NULL,
    E_LastName TEXT NOT NULL,
    E_Department INT NOT NULL,
    E_Title TEXT NOT NULL,
    Phone TEXT NOT NULL,
    Email TEXT NOT NULL,
    CONSTRAINT pk_Employee PRIMARY KEY (
        EID
     )
);  


CREATE TABLE Users (
    UserID SERIAL NOT NULL,
    Current_Dealership INT NOT NULL,
    I_FirstName TEXT NOT NULL,
    I_LastName TEXT NOT NULL,
    I_Department INT NOT NULL,
    I_Title TEXT NOT NULL,
    Username TEXT NOT NULL UNIQUE,
    I_Password TEXT NOT NULL UNIQUE,
    Phone TEXT NOT NULL,
    Email TEXT NOT NULL,
    CONSTRAINT pk_User PRIMARY KEY (
        UserID
     )
);


CREATE TABLE Tasks (
    TaskID SERIAL NOT NULL,
    T_Description TEXT NOT NULL,
    T_Department INT NOT NULL,
    T_Status boolean NOT NULL,
    CONSTRAINT pk_Task PRIMARY KEY (
        TaskID
    )
);


ALTER TABLE Employees ADD CONSTRAINT fk_Employees_Departments FOREIGN KEY(E_Department)
REFERENCES Departments (DepartmentID);

ALTER TABLE  Users ADD CONSTRAINT fk_Users_Departments FOREIGN KEY(I_Department)
REFERENCES Departments (DepartmentID);

ALTER TABLE Tasks ADD CONSTRAINT fk_Tasks_Departments FOREIGN KEY(T_Department)
REFERENCES Departments (DepartmentID);

ALTER TABLE Projects ADD CONSTRAINT fk_Projects_Dealerships FOREIGN KEY(Dealership)
REFERENCES Dealerships (DTID);

ALTER TABLE Users ADD CONSTRAINT fk_Users_Dealerships FOREIGN KEY(Current_Dealership)
REFERENCES Dealerships (DTID);

INSERT INTO Departments
    (Department)
VALUES
    ('Accounting'),
    ('Business Office'),
    ('Parts'),
    ('Service');
    
INSERT INTO Employees
    (E_FirstName, E_LastName, E_Department, E_Title, Phone, Email)
VALUES
    ('Jennifer', 'Finch', 1, 'Controller', '555-555-5555', 'jen.finch@janeford.com'),
    ('Thadeus', 'Gathercoal', 2, 'Sales Manager', '777-777-77777', 'thad.gathercoal@janeford.com'),
    ('Sonja', 'Pauley', 3, 'Parts Manager', '888-888-8888', 'sonja.pauley@janeford.com'),
    ('Waneta', 'Skeleton', 4, 'Service Manager', '999-999-9999', 'waneta.skeleton@janeford.com'),
    ('Cohen', 'Norton', 1, 'Controller', '963-852-8527', 'cohen.norton@johnford.com'),
    ('Loretta', 'Elwyn', 2, 'Sales Manager', '456-123-4567', 'Loretta.El@johnford.com'),
    ('Alyce', 'Greg', 3, 'Parts Manager', '789-999-7890', 'waneta.skeleton@johnford.com'),
    ('Gretchen', 'Arabella', 4, 'Service Manager', '852-963-9638', 'waneta.skeleton@johnford.com');

INSERT INTO Dealerships
    (Store_Num, Ent_Code, D_Address, D_City, D_Phone, Services, Departments, Employees, D_Name)
VALUES
    ('E17', 'JNDE', '1234 Smith St. Richmond, VA 51680', 'Richmond, VA', '123-123-1234',
    '{"VinSolutions", "Dealertrack F&I", "VAuto"}',
    '{"Accounting", "Business Office", "Parts", "Service"}',
    '{"Jennifer Finch", "Thadeus Gathercoal", "Sonja Pauley", "Waneta Skeleton"}', 'Jane Doe Ford'),

    ('A4', 'JODO', '4321 Smith St. Richmond, VA 23806', 'Richmond, VA', '321-123-4321',
    '{"VinSolutions", "Dealertrack F&I", "VAuto", "Reflections"}',
    '{"Accounting", "Business Office", "Parts", "Service"}',
    '{"Cohen Norton", "Loretta Elwyn", "Alyce Greg", "Gretchen Arabella"}', 'John Doe Nissan');


INSERT INTO Projects
    (Title, Dealership, Users, Project_Date)
VALUES
    ('Buy/Sell Jane Doe Ford', 1,
    '{"Berkie Wycliff", "Alvin Leathes", "Cory Squibbes", "Breeana Payton"}',
     '2021-01-15'),
    ('Buy/Sell John Doe Nissan', 1,
    '{"Berkie Wycliff", "Alvin Leathes", "Cory Squibbes", "Breeana Payton"}',
     '2021-01-15');

INSERT INTO Tasks
    (T_Description, T_Department, T_Status)
VALUES
    ('Trained On Standard DMS Reports', 1, false),
    ('Trained On Core Reporting', 1, false),
    ('Retail Deal Posted', 1, false),
    ('Dealer Trade Deal Posted', 1, false),
    ('Lease Deal Posted', 1, false),
    ('Credit App Submitted', 2, false),
    ('Retail Deal Created', 2, false),
    ('Lease Deal Created', 2, false),
    ('Wholesale Deal Created', 2, false),
    ('Dealer Trade Deal Created', 2, false),
    ('Trained On Creating A Return', 3, false),
    ('Trained On Cashiering and Balancing Cash Drawer', 3, false),
    ('Trained On Viewing Demand', 3, false),
    ('Manager Trained On Entering Forced Order', 3, false),
    ('Manager Trained On Part Number Replacement', 3, false),
    ('Trained On Using Tech Time Reporting', 4, false),
    ('Manager Trained On Tech Time Report', 4, false),
    ('Manager Trained On Work In Process Report', 4, false),
    ('Manager Trained On Labor Profit Analysis', 4, false),
    ('Manager Trained On Tech Efficency And Productivity', 4, false);
