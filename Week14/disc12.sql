CREATE TABLE cats(name, weight DEFAULT 1, notes DEFAULT "meow");

INSERT INTO cats(name) VALUES ("Tom"), ("Whiskers");

INSERT INTO cats VALUES ("Mittens", 2, "Actually likes shoes"), ("Rascal", 4, "Prefers to associate with dogs"), ("Magic", 2, "Expert at card games");

UPDATE cats SET notes = "A cat" WHERE notes = "meow";

CREATE TABLE food AS
    SELECT 1 AS cat_weight, 0.5 AS amount UNION
    SELECT 2 , 2.5 UNION
    SELECT 3 , 4.0 UNION
    SELECT 4 , 4.5;

select sum(a.amount) from food as a, cats as b where a.cat_weight = b.weight;
