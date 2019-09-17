CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name, b.size from dogs as a, sizes as b where a.height > b.min and a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.name from dogs as a, parents as b, dogs as c where b.child = a.name and b.parent = c.name order by - c.height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name as sibling_first, b.name as sibling_second from dogs as a, dogs as b, parents as c, parents as d where a.name != b.name and c.child = a.name and d.child = b.name and c.parent = d.parent and a.name < b.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.sibling_first || " and " || a.sibling_second || " are " || b.size || " siblings" from siblings as a, size_of_dogs as b, size_of_dogs as c where a.sibling_first = b.name and a.sibling_second = c.name and b.size = c.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name, height, height from dogs;

INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.dogs || ", " || b.dogs, a.stack_height+b.last_height, b.last_height from stacks_helper as a, stacks_helper as b where b.dogs != a.dogs and b.last_height > a.last_height;

INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.dogs || ", " || b.name, a.stack_height+b.height, b.height from stacks_helper as a, dogs as b where a.dogs not like '%${b.name}%' and b.height > a.last_height;

INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.dogs || ", " || b.name, a.stack_height+b.height, b.height from stacks_helper as a, dogs as b where a.dogs not like '%${b.name}%' and b.height > a.last_height;


CREATE TABLE stacks AS
  SELECT dogs, stack_height from stacks_helper where stack_height >= 170 order by stack_height;
