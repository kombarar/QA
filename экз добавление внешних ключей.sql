use [ нижный магазин];
alter table Authors add foreign key (CountryID) references Countries([Id]);
alter table Books add foreign key (AuthorID) references Authors([Id]);
alter table Books add foreign key (ThemeID) references Themes([Id]);
alter table Sales add foreign key (BookID)  references Books([Id]);
alter table Sales add foreign key (ShopID)  references Shops([Id]);
alter table Shops add foreign key (CountryID) references Countries([Id]);
