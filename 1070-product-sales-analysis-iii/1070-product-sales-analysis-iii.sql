# Write your MySQL query statement below

with Results AS (
select product_id,year,quantity,price,
rank() over(partition by product_id  order by year) rk from sales
)
select product_id,year as first_year,quantity,price from Results
where rk=1;


