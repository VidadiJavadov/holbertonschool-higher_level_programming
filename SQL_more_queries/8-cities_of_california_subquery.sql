--without join
SELECT id, name 
FROM states s, cities c
WHERE s.name = c.name;
