insert into Color
VALUES (1, 'white'),
       (2, 'black');

insert into GameType
VALUES (0, 'Normal SP', 'Single player, normal game mode.'),
       (1, 'Time SP', 'Single player, time based game mode.'),
       (2, 'One mistake SP', 'Single player, one mistake game mode.');


insert into Level
values
    (0, 'Beginner', 0, 9),
    (1, 'Novice', 10, 49),
    (2, 'Intermediate', 50, 99),
    (3, 'Advanced', 100, 199),
    (4, 'Expert', 200, 499),
    (5, 'Master', 500, 999),
    (6, 'Grandmaster', 1000, 9999);

insert into User
values
    (0, 'Guest', 'Password', 0, 0),
    (1, 'iMeReJ', 's24914tak', 100, 3),
    (2, 'SzefJulia', '420Top_Secret69', 750, 5);

insert into Prize
values (0, 0, 'Create an account.'),
       (1, 10, 'Advance to Novice rank.'),
       (2, 50, 'Advance to Intermediate rank.'),
       (3, 100, 'Advance to Advanced rank.'),
       (4, 200, 'Advance to Expert rank.'),
       (5, 500, 'Advance to Master rank.'),
       (6, 1000, 'Advance to Grandmaster rank.');

insert into Prize (id_Prize, description)
values (7, 'Complete your first crossword.'),
       (8, 'Make your first crossword.'),
       (9, 'Complete a crossword without any mistakes.'),
       (10, 'Complete 10 crosswords.');

insert into User_Prize
VALUES  (0, 0),
        (0, 1),
        (0, 2),
        (1, 1),
        (2, 1),
        (3, 1),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (5, 2),
        (7, 1),
        (7, 2);


insert into WordSet (id_WordSet, main_answer, theme)
values (0, 'germination', 'Plants');

insert into Word
VALUES (0,'growth','Process of increasing in physical size, mass, volume, or number of cells.',0, 0),
       (1,'tree', 'Plant with a single stem or trunk, supporting branches and leaves above the ground.', 2, 0),
       (2,'herbs', 'Plants that are used for medicinal, culinary, or aromatic purposes.', 2, 0),
       (3,'stamen', 'The male reproductive organ of a flower, consisting of a filament and an anther.', 3, 0),
       (4,'vines', 'Plants with long, slender stems that grow along the ground or climb up and wrap around other objects or plants for support.', 1, 0),
       (5,'beans', 'A type of legume that are commonly consumed as food.', 3, 0),
       (6,'leaves', 'Flattened, usually green structures that are attached to the stem of a plant.', 2, 0),
       (7,'trowel', 'Small handheld tool with a flat, pointed blade that is used for digging, spreading, and smoothing materials.', 0, 0),
       (8,'mildew', 'Type of fungus that can grow on surfaces, such as walls, fabrics, and plants.', 1, 0),
       (9,'tomatoes', 'Typically round or oblong in shape and come in a variety of colors, including red, yellow, and green.', 5, 0),
       (10,'orange', 'What color are marigold flowers?', 3, 0);

insert into CompletedWordSets
VALUES (1, 0),
       (2, 0);
