# Write your MySQL query statement below
Select employee.name as Employee
from Employee employee 
join Employee manager
on employee.managerID =manager.id
where employee.salary > manager.salary
