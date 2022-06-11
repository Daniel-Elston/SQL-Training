# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:57:40 2022

@author: delst

SQL Theory
"""

import sqlite3
import pandas as pd

# select all, certain columns and distinct columns from tables in the database
select * from campaign;
select campaign_id, volume, opens from campaign;

select * from recipient;
select first_name from recipient;

select * from delivery_logs;
select distinct campaign_id from delivery_logs


# the where clause
select * from delivery_logs;

select * from delivery_logs where open_flag - 1;

select distinct campaign_id from delivery_logs where open_flag = 1;


# between clause
select
  *
from delivery_logs
where date_received between "2020-01-02" and "2020-02-02";
 
select
  *
from delivery_logs
where date_received >= "2020-01-02" and date_received <="2020-02-02";


# wildcards
select * from recipient where first_name like "Dave";

select * from recipient where last_name like "W%";


# the in operator
select * from recipient where first_name like "Dave";

select recipient_id from recipient where first_name like "Dave";

select
  *
from delivery_logs
where recipient_id in
  (select
      recipient_id
   from recipient
   where first_name like "Dave"
   );


# sum aggregate functions
select * from campaign;
select sum(volume) as total_volume from campaign;
select sum(opens)/sum(volume) * 100 as open_rate from campaign;

# more aggregate functions
select avg(volume) from campaign;
select min(volume) from campaign;
select max(volume) from campaign;
####################################################################

select * from delivery_logs;

# count opens where open flag is 1 for each campaign id
select
  campaign_id,
  count(open_flag) as count_opens
from delivery_logs
where open_flag = 1
group by campaign_id;

# count opens where open flag is 1 for each campaign id, having open count greater or equal to 3
select
  campaign_id,
  count(open_flag) as
  count_opens
from delivery_logs
where open_flag = 1
group by campaign_id
having count_opens >= 3;

# ordered open count where open flag is 1 for each campaign id, having open count > or = to 3
select
  campaign_id,
  count(open_flag) as
  count_opens
from delivery_logs
where open_flag = 1
group by campaign_id
having count_opens >= 3
order by count_opens;


# joins
select * from recipient;
select * from delivery_logs;

select
  dl.campaign_id,
  dl.recipient_id,
  dl.date_received,
  dl.click_flag,
  r.first_name,
  r.last_name
from delivery_logs as dl
left join recipient as r
on dl.recipient_id = r.recipient_id;



