.mode column
PRAGMA foreign_keys = ON; -- activates foreign key features in sqlite. It is disabled by default

CREATE TABLE Racers (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(20),
    EMAIL VARCHAR(20)
);

CREATE TABLE Races (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(40)
);

CREATE TABLE Challenges (
    ID INTEGER PRIMARY KEY,
    NAME VARCHAR(40)
);

CREATE TABLE Challenge_Info ( -- mapping races to challenges
    CHALLENGEID INTEGER,
    RACEID INTEGER,
    FOREIGN KEY (CHALLENGEID) REFERENCES Challenges(ID),
    FOREIGN KEY (RACEID) REFERENCES Races(ID),
    PRIMARY KEY (CHALLENGEID, RACEID)
);

CREATE TABLE Racer_Participation ( -- record racers' results in races
    RACERID INTEGER, -- ID of the racer
    RACEID INTEGER, -- the race the racer joins
    RUNTIME INTEGER, -- in seconds, the performance of the racer 
    FOREIGN KEY (RACEID) REFERENCES Races(ID),
    FOREIGN KEY (RACERID) REFERENCES Racers(ID),
    PRIMARY KEY (RACERID, RACEID)
);

/** Insert races **/

INSERT INTO Races VALUES (1, 'The ruby marathon');
INSERT INTO Races VALUES (2, 'The bridge challenge');
INSERT INTO Races VALUES (3, 'The sea to mountain sprint');
INSERT INTO Races VALUES (4, 'Flat and fast marathon');
INSERT INTO Races VALUES (5, 'The wine route stroll');

/** Insert challenges **/
INSERT INTO Challenges VALUES (1, 'The marathon challenge');
INSERT INTO Challenges VALUES (2, 'The terrain challenge');

/** Insert racers **/
INSERT INTO Racers VALUES (1, 'Smith', 'email1@gmail.com');
INSERT INTO Racers VALUES (2, 'Bob', 'email2@gmail.com');
INSERT INTO Racers VALUES (3, 'Marry', 'emai3@gmail.com');
INSERT INTO Racers VALUES (4, 'John', 'email4@gmail.com');
INSERT INTO Racers VALUES (5, 'David', 'email5@gmail.com');
INSERT INTO Racers VALUES (6, 'Corona', 'email6@gmail.com');
INSERT INTO Racers VALUES (7, 'David', 'email7@gmail.com');

/** Insert into Challenge_Info **/
INSERT INTO Challenge_Info VALUES (1, 1);
INSERT INTO Challenge_Info VALUES (1, 4);
INSERT INTO Challenge_Info VALUES (2, 2);
INSERT INTO Challenge_Info VALUES (2, 3);
INSERT INTO Challenge_Info VALUES (2, 1);

/** Racers' performance **/
INSERT INTO Racer_Participation VALUES (1, 1, 100);
INSERT INTO Racer_Participation VALUES (2, 2, 150);
INSERT INTO Racer_Participation VALUES (2, 3, 90);
INSERT INTO Racer_Participation VALUES (3, 4, 20);
INSERT INTO Racer_Participation VALUES (3, 5, 160);
INSERT INTO Racer_Participation VALUES (3, 1, 170);
INSERT INTO Racer_Participation VALUES (4, 2, 260);
INSERT INTO Racer_Participation VALUES (5, 3, 120);
INSERT INTO Racer_Participation VALUES (5, 4, 300);
INSERT INTO Racer_Participation VALUES (6, 5, 400);
INSERT INTO Racer_Participation VALUES (6, 1, 250);
INSERT INTO Racer_Participation VALUES (6, 2, 302);
INSERT INTO Racer_Participation VALUES (7, 3, 108);


-- Is the data there?
SELECT 'Racers';
SELECT '----------------------------------------------------';
SELECT * FROM Racers;
SELECT '';
SELECT 'Races';
SELECT '----------------------------------------------------';
SELECT * FROM Races;
SELECT 'Challenges';
SELECT '----------------------------------------------------';
SELECT * FROM Challenges; 
SELECT 'Racer_Participation';
SELECT '----------------------------------------------------';
SELECT * FROM Racer_Participation; 

SELECT '1. find the top 3 fastest women runners for "The ruby marathon" race';
SELECT '----------------------------------------------------';
SELECT * FROM
(SELECT * FROM Racer_Participation 
    WHERE RACEID = (SELECT ID FROM Races WHERE NAME="The ruby marathon")
    ORDER BY RUNTIME)
    LIMIT 3;
SELECT '';

SELECT '2. find all the runners email addresses that successfully finished the marathon challenge';
SELECT '----------------------------------------------------';
SELECT EMAIL FROM
(SELECT Racers.EMAIL, COUNT(*) as num_race_finished FROM Racers
    JOIN Racer_Participation ON Racers.ID=Racer_Participation.RACERID
    WHERE Racer_Participation.RACEID IN 
        (SELECT RACEID FROM Challenge_Info
            WHERE CHALLENGEID=(SELECT ID FROM Challenges WHERE NAME="The marathon challenge")) -- select all the ID of all races in The marathon challenge
    GROUP BY Racers.ID
    HAVING num_race_finished=(SELECT COUNT(*) FROM
                                (SELECT RACEID FROM Challenge_Info
                                    WHERE CHALLENGEID=(SELECT ID FROM Challenges WHERE NAME="The marathon challenge"))));

