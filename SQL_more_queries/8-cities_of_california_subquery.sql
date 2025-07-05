--without join
SELECT id, name 
FROM states s, cities c
WHERE s.states_id = c.id;
