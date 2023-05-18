-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-05-18 20:12:51.568

-- tables
-- Table: Word
CREATE TABLE Word (
    id integer NOT NULL CONSTRAINT Word_pk PRIMARY KEY,
    entry varchar(30) NOT NULL,
    clue varchar(150) NOT NULL,
    key_index integer NOT NULL,
    id_WordSet integer NOT NULL,
    CONSTRAINT Word_WordSet FOREIGN KEY (id_WordSet)
    REFERENCES WordSet (id)
);

-- Table: WordSet
CREATE TABLE WordSet (
    id integer NOT NULL CONSTRAINT WordSet_pk PRIMARY KEY,
    main_answer varchar(30) NOT NULL,
    theme varchar(30) NOT NULL
);

-- End of file.

