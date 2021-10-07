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
	location_id INTEGER REFERENCES locations
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
    place_id INTEGER REFERENCES places,
    key TEXT,
    value TEXT
);
CREATE TABLE locations (
	id SERIAL PRIMARY KEY,
	name TEXT, 
	description TEXT, 
	place_id INTEGER REFERENCES places
);