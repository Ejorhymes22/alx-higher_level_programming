-- lists all the cities of california found in a databases
SELECT *
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California')
ORDER BY id ASC;
