-- Lists all records for specified field (not NULL) in specified table within db
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score desc;
