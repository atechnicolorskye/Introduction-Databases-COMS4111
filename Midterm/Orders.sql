-- 1
select sum(ol.quantity), sum(i.price * ol.quantity)
from orderlines ol, items i
where ol.iid = i.iid

-- 2
select distinct names
from customers
where cid in (select cid
              from order
              where oid in (select ol.oid
                            from orderline ol, items i
                            where ol.iid = i.iid and
                                  description = 'Nexus 5X'
                            ))

-- Alternatively,

select distinct name
from customers c, orders o, orderlines ol, items i
where ol.iid = i.iid and
      description = 'Nexus 5X' and
      o.oid = ol.oid and
      c.cid = o.cid

-- 3
select o1.iid, o2.iid
from orderlines o1, orderlines o2
where o1.oid = o2.oid and
      o1.iid < o2.iid
group by o1.iid, o2.iid
order by count(*) desc

-- 4
select i.iid, count(distinct o.cid)
from items i
    left outer join orderlines ol on i.iid = ol.iid
    left outer join orders o on ol.oid = o.oid
group by i.iid

-- 5
select i.iid, sum(ol.quantity), sum(ol.quantity) * i.price as total price
from items i
    left outer join orderlines ol on i.iid = ol.iid
group by i.iid

-- 6
select count(distinct o.oid)/ count(distinct c.cid)::real as average
from customers c, orders o

-- Optional:
select distinct c.cid, c.name, sum(ol.quantity), sum(i.price* ol.quantity)
from customers c
    left outer join orders o on c.cid = o.cid
    left outer join orderlines ol on o.oid = ol.oid
    left outer join items i on ol.iid = i.iid
group by c.cid
order by c.cid;

-- Key: Remember to use outer joins to check for Nulls and COALESCE(SUM(ol.quantity), 0) to remove Nulls