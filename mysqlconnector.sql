use db11mayo;

CREATE TABLE bicing(
	id int primary key,
    nombre varchar(20)
);

 drop table bicing;
﻿create table bicing
(
id serial primary key,
id_station int,
lat double,
lon double,
slots int,
bikes int,
hora timestamp,
hmin char(10),
bikesdifference int
);


select * from bicing;