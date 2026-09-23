# Write your MySQL query statement below
delete person1 
from Person as person1
join Person as person2
on person1.email = person2.email
and person1.id > person2.id