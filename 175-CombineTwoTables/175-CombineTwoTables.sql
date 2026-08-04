-- Last updated: 04/08/2026 11:37:25
# Write your MySQL query statement below
SELECT firstName , lastName, city, state FROM Person LEFT JOIN Address on Person.personId = Address.personId;