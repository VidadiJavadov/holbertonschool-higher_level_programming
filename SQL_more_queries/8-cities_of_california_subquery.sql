--without join
SELECT name, state_id, name 
FROM states s, cities c
WHERE s.name = c.name;
