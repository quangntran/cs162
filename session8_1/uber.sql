.mode column
PRAGMA foreign_keys = ON; -- activates foreign key features in sqlite. It is disabled by default

CREATE TABLE Drivers (
    DRIVERNUMBER INTEGER PRIMARY KEY,
    NAME VARCHAR(20),
    PHONE VARCHAR(20)
);



CREATE TABLE Lifters ( -- Info on the one riders
    LIFTERNUMBER INTEGER PRIMARY KEY,
    NAME VARCHAR(20),
    PHONE VARCHAR(20)
);

CREATE TABLE Rides (
    RIDENUMBER INTEGER, -- A unique integer to identify this ride
    DRIVERNUMBER INTEGER,
    LIFTERNUMBER INTEGER,
    BILL NUMERIC(11, 2), -- Bill for lifter for this ride
    FOREIGN KEY (DRIVERNUMBER) REFERENCES Drivers(DRIVERNUMBER),
    FOREIGN KEY (LIFTERNUMBER) REFERENCES Lifters(LIFTERNUMBER)
);

INSERT INTO Drivers VALUES (1, 'Robert', '123');
INSERT INTO Drivers VALUES (2, 'Mary', '12');
INSERT INTO Drivers VALUES (3, 'John', '23');


INSERT INTO Lifters VALUES (1, 'A', '123');
INSERT INTO Lifters VALUES (2, 'B', '123');
INSERT INTO Lifters VALUES (3, 'C', '123');
INSERT INTO Lifters VALUES (4, 'D', '132');

INSERT INTO Rides VALUES (1, 1, 2, 20);
INSERT INTO Rides VALUES (2, 1, 3, 10);
INSERT INTO Rides VALUES (3, 1, 3, 25);
INSERT INTO Rides VALUES (4, 2, 4, 13);
INSERT INTO Rides VALUES (5, 2, 3, 24);
INSERT INTO Rides VALUES (6, 2, 2, 7);
INSERT INTO Rides VALUES (7, 3, 2, 18);
INSERT INTO Rides VALUES (8, 3, 2, 32);
INSERT INTO Rides VALUES (9, 3, 2, 15);
INSERT INTO Rides VALUES (10, 3, 3, 2.5);

-- Is the data there?
SELECT 'Drivers';
SELECT '----------------------------------------------------';
SELECT * FROM Drivers;
SELECT '';
SELECT 'Lifters';
SELECT '----------------------------------------------------';
SELECT * FROM Lifters;
SELECT 'Rides';
SELECT '----------------------------------------------------';
SELECT * FROM Rides; 

SELECT '1. how many trips have been made by each driver this month, and how much they will be paid.:';
SELECT '----------------------------------------------------';
/* They will be paid by 0.9 of the rides' worth*/
SELECT Drivers.NAME, COUNT(*) AS NUMBER_RIDES, 0.9*SUM(Rides.BILL) AS PAYMENT 
    FROM Rides
    JOIN Drivers ON Drivers.DRIVERNUMBER = Rides.DRIVERNUMBER
    GROUP BY Drivers.DRIVERNUMBER;

SELECT '';
SELECT '2. find all the riders who havmt taken any trips this month and their phone number';
SELECT '----------------------------------------------------';

SELECT * FROM Lifters 
    LEFT OUTER JOIN Rides
    ON Lifters.LIFTERNUMBER = Rides.LIFTERNUMBER
    GROUP BY Rides.LIFTERNUMBER HAVING SUM(Rides.LIFTERNUMBER) IS NULL;