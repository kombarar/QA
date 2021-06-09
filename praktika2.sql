use praktika2

create table Departments
(
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Building int NOT NULL,
check (0 < Building and Building < 6),
Financing money NOT NULL default(0),
check (Financing >=0),
"Name" nvarchar(100) NOT NULL UNIQUE,
)

create table Diseases
(
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(100) NOT NULL UNIQUE,
Severity int NOT NULL default(1),
check (Severity >=1),
)

create table Doctors
(
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(max) NOT NULL,
Phone char(10),
Salary money NOT NULL,
check (Salary > 0),
Surname nvarchar(max) NOT NULL,
)

