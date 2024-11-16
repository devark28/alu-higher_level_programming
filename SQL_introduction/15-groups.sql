--
SELECT DISTINCT
    s1.score,
    (SELECT
         count(*)
     FROM second_table as s2
     WHERE s2.score = s1.score) as number
FROM second_table as s1;