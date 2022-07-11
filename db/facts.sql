CREATE DATABASE pet_facts;

-- switch connection to a new database
\c pet_facts;


CREATE TABLE users(
    id bigserial NOT NULL,
    name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    username varchar(100) NOT NULL UNIQUE,
    email varchar(150) NOT NULL UNIQUE,
    password varchar(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE pets(
    id bigserial NOT NULL,
    name varchar(100) NOT NULL UNIQUE,
    PRIMARY KEY(id)
);


CREATE TABLE facts (
    id bigserial NOT NULL,
    user_id bigint NOT NULL,
    pet_id bigint NOT NULL,
    title VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(400) NOT NULL,
    source VARCHAR(200),
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(pet_id) REFERENCES pets(id)
);


INSERT INTO users (id, name, last_name, username, email, password) VALUES (1, 'Javier', 'Amaya','javieramayapat', 'javier@gmail.com', 'easypassword');

INSERT INTO pets (id, name) VALUES(1, 'cats'); 
INSERT INTO pets (id, name) VALUES(2, 'dogs'); 
INSERT INTO pets (id, name) VALUES(3, 'chickens'); 


INSERT INTO facts (id, user_id, pet_id, title, description, source) VALUES (1, 1, 3, 'Chickens can recognize up to 100 faces.', 'Chickens do not just recognize other chickens - these faces include those of humans! Chickens even remember positive or negative experiences with the faces they recognize and pass that information on to their flock members.', 'https://www.worldanimalprotection.cr/blogs/11-datos-sobre-los-pollos-que-te-sorprenderan');
INSERT INTO facts (id, user_id, pet_id, title, description, source) VALUES (2, 1, 3, 'Chickens dream.', 'Like dogs and cats, which can act as if they are chasing something in their sleep, chickens also have very vivid dreams! Chickens experience rapid eye movement (REM) sleep, but researchers do not yet know what they dream about - we can only imagine!', 'https://www.worldanimalprotection.cr/blogs/11-datos-sobre-los-pollos-que-te-sorprenderan');
INSERT INTO facts (id, user_id, pet_id, title, description, source) VALUES (3, 1, 3, 'Chickens transmit information.', 'It is not just your grandparents or parents who can show you the tricks of the trade, like the best way to cook spinach or the best cleaning methods. Chickens do it with their young too, passing the knowledge from generation to generation if given the opportunity to do so.', 'https://www.worldanimalprotection.cr/blogs/11-datos-sobre-los-pollos-que-te-sorprenderan');
INSERT INTO facts (id, user_id, pet_id, title, description, source) VALUES (4, 1, 3, 'Chickens chirp at their eggs.', 'One of the sweetest things you will hear is that the hens chirp at their babies while they are in the eggs and the chickens chirp back. They also produce about 30 different sounds to communicate with each other, expressing everything from "thanks for the food!" to "there is a predator in the coop!"', 'https://www.worldanimalprotection.cr/blogs/11-datos-sobre-los-pollos-que-te-sorprenderan');
INSERT INTO facts (id, user_id, pet_id, title, description, source) VALUES (5, 1, 3, 'Chickens are hierarchical.', 'If you have ever heard the term "pecking order" in your life, that comes from the flock structure of chickens. These pecking orders are extremely complex social structures and flock members know exactly where they fit in.', 'https://www.worldanimalprotection.cr/blogs/11-datos-sobre-los-pollos-que-te-sorprenderan');
INSERT INTO facts (id, user_id, pet_id, title, description, source) VALUES (6, 1, 3, 'Chickens have excellent memories.', 'They can solve puzzles by pecking at pieces with their beaks so that their human helpers know which ones go where. Chickens have also been filmed finding treats hidden under cups.', 'https://www.worldanimalprotection.cr/blogs/11-datos-sobre-los-pollos-que-te-sorprenderan');

