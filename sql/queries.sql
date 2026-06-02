
SELECT * FROM fact_nav
ORDER BY nav DESC
LIMIT 5;


SELECT AVG(nav) AS average_nav
FROM fact_nav;


SELECT MAX(nav) AS highest_nav
FROM fact_nav;


SELECT MIN(nav) AS lowest_nav
FROM fact_nav;


SELECT COUNT(*) AS total_records
FROM fact_nav;


SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


SELECT MAX(date) AS latest_date
FROM fact_nav;


SELECT MIN(date) AS earliest_date
FROM fact_nav;


SELECT *
FROM fact_nav
WHERE nav > (
    SELECT AVG(nav)
    FROM fact_nav
);

SELECT amfi_code,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY avg_nav DESC
LIMIT 10;