-- Lists all the cities of California that can be found in the database.
SELECT cities.id, cities.name 
FROM cities, states 
WHERE state_id = (cities.state_id = states.id AND states.name = 'California') 
ORDER BY cities.id ASC;
