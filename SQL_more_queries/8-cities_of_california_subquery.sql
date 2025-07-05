-- This script lists all the cities of California found in the hbtn_0d_usa database.
-- It uses a subquery to find the state id for 'California'.
-- The results are ordered by the city id in ascending order.

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
