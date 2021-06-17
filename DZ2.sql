use Академия

create table Groups
(
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(100) NOT NULL UNIQUE,
Rating int NOT NULL,
check (0 <= Rating and Rating <= 5),
"Year" int NOT NULL,
check (0 < "Year" and "Year" < 6),
)

create table Departments
(
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Financing money NOT NULL default(0),
check (Financing >=0),
"Name" nvarchar(100) NOT NULL UNIQUE,
)

create table Faculties
(
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
"Name" nvarchar(100) NOT NULL UNIQUE,
)

create table Teachers
(
ID int NOT NULL IDENTITY(1,1) PRIMARY KEY,
EmploymentDate date NOT NULL,
Check (EmploymentDate <= '01.01.1990'),
"Name" nvarchar(max) NOT NULL,
Premium money NOT NULL default(0), 
check (Premium >= 0),
Salary money NOT NULL,
check (Salary > 0),
Surname nvarchar(max) NOT NULL,
)


