PRAGMA automatic_index=off;
.mode column
.headers on

-- CREATE SOME TABLES
CREATE TABLE TEST1 (
    id INT,
    x INT DEFAULT(ABS(RANDOM() / 17592186044416)),
    y INT DEFAULT(ABS(RANDOM() / 17592186044416)),
    z INT DEFAULT(ABS(RANDOM() / 17592186044416))
);
CREATE TABLE TEST2 (
    id INT,
    x INT DEFAULT(ABS(RANDOM() / 17592186044416)),
    y INT DEFAULT(ABS(RANDOM() / 17592186044416)),
    z INT DEFAULT(ABS(RANDOM() / 17592186044416))
);
CREATE TABLE TEST3 (
    id INT,
    x INT DEFAULT(ABS(RANDOM() / 17592186044416)),
    y INT DEFAULT(ABS(RANDOM() / 17592186044416)),
    z INT DEFAULT(ABS(RANDOM() / 17592186044416))
);

-- PUT RANDOM DATA IN THEM
INSERT INTO TEST1 (id) WITH TempIDs(id) AS
  (VALUES(1) UNION ALL SELECT id+1 FROM TempIDs WHERE id < 10000 )
  SELECT id FROM TempIDs;

INSERT INTO TEST2 (id) WITH TempIDs(id) AS
  (VALUES(1) UNION ALL SELECT id+1 FROM TempIDs WHERE id < 10000 )
  SELECT id FROM TempIDs;

INSERT INTO TEST3 (id) WITH TempIDs(id) AS
  (VALUES(1) UNION ALL SELECT id+1 FROM TempIDs WHERE id < 10000 )
  SELECT id FROM TempIDs;


-- Now we have 3 large tables with random numbers in them
SELECT COUNT(*) AS TEST1SIZE FROM TEST1;
SELECT COUNT(*) AS TEST2SIZE FROM TEST2;
SELECT COUNT(*) AS TEST3SIZE FROM TEST3;

SELECT * FROM TEST1 LIMIT 10;

SELECT "SLOW QUERY";

EXPLAIN QUERY PLAN SELECT COUNT(*) FROM TEST1 t1
    JOIN TEST2 t2 ON (t1.x) = (t2.x)
    JOIN TEST3 t3 ON (t1.y) = (t3.y)
    WHERE t3.z > t1.z;

.timer ON
SELECT COUNT(*) FROM TEST1 t1
    JOIN TEST2 t2 ON (t1.x) = (t2.x)
    JOIN TEST3 t3 ON (t1.y) = (t3.y)
    WHERE t3.z > t1.z;

CREATE INDEX indx1 ON TEST1(x);
CREATE INDEX indx2 ON TEST2(x);
CREATE INDEX indy1 ON TEST1(y);
CREATE INDEX indy3 ON TEST3(y);
CREATE INDEX indz1 ON TEST1(z);
CREATE INDEX indz3 ON TEST3(z);

SELECT "FAST QUERY";
EXPLAIN QUERY PLAN SELECT COUNT(*) FROM TEST1 t1
    JOIN TEST2 t2 ON (t1.x) = (t2.x)
    JOIN TEST3 t3 ON (t1.y) = (t3.y)
    WHERE t3.z > t1.z;

SELECT COUNT(*) FROM TEST1 t1
    JOIN TEST2 t2 ON (t1.x) = (t2.x)
    JOIN TEST3 t3 ON (t1.y) = (t3.y)
    WHERE t3.z > t1.z;

/*
Time taken: 0.003 vs 5.599 in slow query

Write pseudo code explaining how the fast query is now being implemented:
For each row in t1:
    Binary search for t1.x in t2
    Binary search t1.y in t3 
    Binary search for t1.z in t3

Time complexity: O(3NlogN)=O(NlogN)


Query optimization and indices:

SELECT Name, Phone FROM Customer WHERE Gender = 'f' AND ZipCode = '90210';

1. Give pseudo-code for the case that there are no indexes.
For each row, check if gender is 'f'. If yes check if Zipcode is '90210'. 


2. Give pseudo-code for the case that there is an index on Gender. Roughly how much more efficient is this than without any indices? (Assuming that your customers are evenly split between men and women.)
Binary search for 'f' and get the rowid. Binary search for this rowid in the table. Check the zip code. O(NlogN). Even less efficient. 


3. Give pseudo-code for the case that there is an index on ZipCode. Assuming that there are roughly 10,000 different zip codes for your customers, how much more efficient is this than without any indices?
Binary search for the zipcode to get the rowid. Binary search for the rowid in the table. check the gender. 
N/(log(N)^2)=10,000/log^2(10,000)=56 times faster.



4. Find out about composite indices. What would a good composite index look like in this case? Write pseudo-code for this case.
CREATE INDEX Idx3 ON Customer(Gender, Zipcode); 
Binary search for ('f', '90210') to get the row id. Binary search for the rowid. 
N/(log(N))=10,000/log(10,000)=256 times faster.
 
5. Find out what a covering index is. What would it look like in this case? Is a covering index more or less efficient than a composite index, and why?
CREATE INDEX Idx3 ON Customer(Gender, Zipcode, Name, Phone); 
Binary search for ('f', '90210') and get the name and phone.
N/(log(N))/log(N)=56 times faster than the composite index. 


*/
