-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-06-16 23:25:37.091

-- tables
-- Table: Color
CREATE TABLE Color (
    id_Color integer NOT NULL CONSTRAINT Color_pk PRIMARY KEY,
    name varchar(20) NOT NULL
);

-- Table: CompletedWordSets
CREATE TABLE CompletedWordSets (
    id_User integer NOT NULL,
    id_WordSet integer NOT NULL,
    CONSTRAINT CompletedWordSets_pk PRIMARY KEY (id_User,id_WordSet),
    CONSTRAINT CompletedWordSets_User FOREIGN KEY (id_User)
    REFERENCES User (id_User),
    CONSTRAINT CompletedWordSets_WordSet FOREIGN KEY (id_WordSet)
    REFERENCES WordSet (id_WordSet)
);

-- Table: GameType
CREATE TABLE GameType (
    id_GameType integer NOT NULL CONSTRAINT GameType_pk PRIMARY KEY,
    name varchar(30) NOT NULL,
    description varchar(100) NOT NULL
);

-- Table: Level
CREATE TABLE Level (
    id_Level integer NOT NULL CONSTRAINT Level_pk PRIMARY KEY,
    title varchar(30) NOT NULL,
    min_points integer NOT NULL,
    max_points integer NOT NULL
);

-- Table: Prize
CREATE TABLE Prize (
    id_Prize integer NOT NULL CONSTRAINT Prize_pk PRIMARY KEY,
    min_points integer,
    description varchar(100) NOT NULL
);

-- Table: Scores
CREATE TABLE Scores (
    id_Scores integer NOT NULL CONSTRAINT Scores_pk PRIMARY KEY,
    id_User integer NOT NULL,
    id_GameType integer NOT NULL,
    points integer NOT NULL,
    date date NOT NULL,
    CONSTRAINT Scores_User FOREIGN KEY (id_User)
    REFERENCES User (id_User),
    CONSTRAINT Scores_GameType FOREIGN KEY (id_GameType)
    REFERENCES GameType (id_GameType)
);

-- Table: User
CREATE TABLE User (
    id_User integer NOT NULL CONSTRAINT User_pk PRIMARY KEY,
    login varchar(50) NOT NULL,
    password varchar(100) NOT NULL,
    points integer NOT NULL,
    id_Level integer NOT NULL,
    CONSTRAINT User_Level FOREIGN KEY (id_Level)
    REFERENCES Level (id_Level)
);

-- Table: UserSettings
CREATE TABLE UserSettings (
    id_User integer NOT NULL CONSTRAINT UserSettings_pk PRIMARY KEY,
    id_Color_background integer NOT NULL,
    id_Color_outline integer NOT NULL,
    id_Color_font integer NOT NULL,
    CONSTRAINT UserSettings_ColorBackground FOREIGN KEY (id_Color_background)
    REFERENCES Color (id_Color),
    CONSTRAINT UserSettings_ColorOutline FOREIGN KEY (id_Color_outline)
    REFERENCES Color (id_Color),
    CONSTRAINT UserSettings_ColorFont FOREIGN KEY (id_Color_font)
    REFERENCES Color (id_Color),
    CONSTRAINT UserSettings_User FOREIGN KEY (id_User)
    REFERENCES User (id_User)
);

-- Table: User_Prize
CREATE TABLE User_Prize (
    id_Prize integer NOT NULL,
    id_User integer NOT NULL,
    CONSTRAINT User_Prize_pk PRIMARY KEY (id_Prize,id_User),
    CONSTRAINT UserPrize_Prize FOREIGN KEY (id_Prize)
    REFERENCES Prize (id_Prize),
    CONSTRAINT UserPrize_User FOREIGN KEY (id_User)
    REFERENCES User (id_User)
);

-- Table: Word
CREATE TABLE Word (
    id_Word integer NOT NULL CONSTRAINT Word_pk PRIMARY KEY,
    entry varchar(30) NOT NULL,
    clue varchar(150) NOT NULL,
    key_index integer NOT NULL,
    id_WordSet integer NOT NULL,
    CONSTRAINT Word_WordSet FOREIGN KEY (id_WordSet)
    REFERENCES WordSet (id_WordSet)
);

-- Table: WordSet
CREATE TABLE WordSet (
    id_WordSet integer NOT NULL CONSTRAINT WordSet_pk PRIMARY KEY,
    main_answer varchar(30) NOT NULL,
    theme varchar(30) NOT NULL,
    id_User integer,
    CONSTRAINT WordSet_User FOREIGN KEY (id_User)
    REFERENCES User (id_User)
);

-- End of file.

