create database snake_game;

use snake_game;

create table usuario (
	id_usua int(250) auto_increment,
    nome_usua varchar(50),
    pont_usua int(250),
    data_jogd date,
    primary key (id_usua)
);