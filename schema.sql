CREATE TABLE users (
	id SERIAL PRIMARY KEY, 
	username TEXT UNIQUE, 
	password TEXT,
	role INTEGER
);
CREATE TABLE places (
	id SERIAL PRIMARY KEY,
	name TEXT,
	description TEXT
);
CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
	place_id INTEGER REFERENCES places,
    stars INTEGER,
    comment TEXT
);