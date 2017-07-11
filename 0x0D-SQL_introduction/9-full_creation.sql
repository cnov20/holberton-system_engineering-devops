-- Creates a specified table and add multiple rows to database on MYSQL server
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);

INSERT into `second_table` (`id`, `name`, `score`)
VALUES ('1', 'John', '10'),
       ('2', 'Alex', '3'),
       ('3', 'Bob', '14'),
       ('4', 'George', '8');
