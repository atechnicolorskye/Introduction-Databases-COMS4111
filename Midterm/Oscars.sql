-- 1
select distinct m.title
from movies m, nominees n
where m.mid = n.mid

-- 2
select p.name, m.title, n.won
from category c, nominees n, people p, movies m
where c.name = 'Actress in a Leading Role' and
      n.cid = c.cid and
      n.year = 2016 and
      n.pid = p.pid and
      n.mid = m.mid

-- 3
select n.year, c.name, m.title, n.won
from nominees n, category c, movies m, people p
where p.name = 'Jennifer Lawrence' and
      n.pid = p.pid and
      m.mid = n.mid and
      c.cid = n.cid
order by n.year asc

-- 4
select m.title, count(n.mid)
from movies m
    left outer join nominees n on n.mid = m.mid
group by m.title

-- 5
select m.title, sum(n.won::int)
from movies m
    left outer join nominees n on n.mid = m.mid
group by m.title, n.won

-- 6
select max(count(n.mid))
from nominees n
group by n.mid