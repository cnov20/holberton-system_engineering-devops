-- Lists the number of records with same value in specified table within db
SELECT score, count(*) as number FROM second_table GROUP BY score desc;
