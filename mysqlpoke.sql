use db11mayo;

drop table pokemon35;
create table pokemon35(
	id int primary key,
    nombre varchar(20),
    base_experience int,
    height int,
    is_default bool,
    orden int,
    weight int
);
select * from pokemon35;


/*abilities text,
    forms text,
    game_indices text,
    held_items text,
    location_area_encounters text,
    moves text,
    past_types text,
    sprites text,
    species text,
    stats text,
    typos text*/