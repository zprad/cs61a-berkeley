.read lab12.sql

-- Q5
CREATE TABLE fa18favpets AS
  SELECT pet, COUNT(*) As count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE fa18dog AS
  SELECT pet, count FROM fa18favpets WHERE pet = "dog";


CREATE TABLE fa18alldogs AS
  SELECT pet, COUNT(*) from students where pet like '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) from students where seven = "7" group by denero;

-- Q6
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) from students group by smallest;
