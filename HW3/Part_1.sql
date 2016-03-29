--1
select s.store
from iowasmall i, (select distinct store from iowasmall) s
where s.store = i.store
group by s.store
order by sum(i.bottle_qty) desc
limit 1;

--2
select description
from iowasmall
where store = 2633
group by description
order by sum(bottle_qty) desc
limit 1;

--3-1
select zipcode, category_name
from (select max(bq) from (select count(bottle_qty) as bq from iowasmall group by zipcode, category name) c) max



--3-2
select distinct zipcode, category_name
from iowasmall i
group by zipcode, category_name
order by sum(bottle_qty) desc
limit 5;

--4
select