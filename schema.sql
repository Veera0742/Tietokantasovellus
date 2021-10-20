CREATE TABLE users (
	id SERIAL PRIMARY KEY, 
	username TEXT UNIQUE, 
	password TEXT,
	role INTEGER
);
CREATE TABLE places (
	id SERIAL PRIMARY KEY,
	name TEXT,
	description TEXT,
	visible INTEGER,
	location_id INTEGER REFERENCES locations,
	service_id INTEGER REFERENCES services,
	group_id INTEGER REFERENCES groups
);
CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
	place_id INTEGER REFERENCES places,
    stars INTEGER,
    comment TEXT
);
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    service TEXT,
    place_id INTEGER REFERENCES places
);
CREATE TABLE locations (
	id SERIAL PRIMARY KEY,
	name TEXT, 
	description TEXT, 
	place_id INTEGER REFERENCES places
);
CREATE TABLE groups (
	id SERIAL PRIMARY KEY,
	name TEXT, 
	description TEXT, 
	place_id INTEGER REFERENCES places
);
CREATE TABLE service_relations (
	place_id INTEGER REFERENCES places, 
	service_id INTEGER REFERENCES services
);
CREATE TABLE group_relations (
	place_id INTEGER REFERENCES places, 
	group_id INTEGER REFERENCES groups
);