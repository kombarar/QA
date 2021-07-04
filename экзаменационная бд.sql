use [ нижный магазин];

create table [Authors]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(max) not null  check ([Name] <> N''),
	[Surname] nvarchar(max) not null  check ([Surname] <> N''),
	[CountryID] int not null,
);

create table [Books]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(max) not null  check ([Name] <> N''),
	[Pages] int not null check ([Pages] > 0),
	[Price] int not null check ([Price] >= 0),
	[PublishDate] date not null check ([PublishDate] >= '04.07.2021'),
	[AuthorID] int not null,
	[ThemeID] int not null,
);

create table [Countries]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(50) not null unique check ([Name] <> N''),
);

create table [Sales]
(
	[Id] int not null identity(1, 1) primary key,
	[Price] money not null check ([Price] > 0),
	[Quantity] int not null check ([Quantity] >= 0),
	[SaleDate] date not null check ([SaleDate] >= '04.07.2021') default '04.07.2021',
	[BookID] int not null,
	[ShopId] int not null,
);

create table [Shops]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(max) not null check ([Name] <> N''),
	[CountryID] int not null,
);

create table [Themes]
(
	[Id] int not null identity(1, 1) primary key,
	[Name] nvarchar(100) not null unique check ([Name] <> N''),
);