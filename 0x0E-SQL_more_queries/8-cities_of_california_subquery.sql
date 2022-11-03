-- lists all the cities of california found in a databases
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California')
ORDER BY cities.id ASC;
