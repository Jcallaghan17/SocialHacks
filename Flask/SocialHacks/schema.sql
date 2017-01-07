drop table if exists event;
create table event (
	id integer primary key autoincrement,
	title text not null,
	description text not null,
	'date' text not null,
	'time' text not null,
	'geolocation' text not null,
	street_address text,
	building_name text,
	university text not null,
	special_diet text, 



);