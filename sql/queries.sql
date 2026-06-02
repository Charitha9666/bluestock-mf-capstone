SELECT * FROM fact_nav LIMIT 10;

SELECT AVG(nav) AS average_nav
FROM fact_nav;

SELECT MAX(nav) AS highest_nav
FROM fact_nav;

SELECT MIN(nav) AS lowest_nav
FROM fact_nav;

SELECT COUNT(*) AS total_records
FROM fact_nav;