-- Lists all the cities of California that can be found in the database.
SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
