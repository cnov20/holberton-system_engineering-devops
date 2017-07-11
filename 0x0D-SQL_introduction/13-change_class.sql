-- Remove all records of table <= certain value, from database on MYSQL server
DELETE `score` FROM second_table WHERE `score` <= 5 ORDER BY score desc;
