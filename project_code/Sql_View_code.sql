
---------SQLITE WAY-------------------------
select 
a.member_id,
a.ACTIVITY_YEAR_MONTH,
case when a.current_active_count > 0 and a.prev_active_count is null then 'New'
     when a.current_active_count > 0 and a.prev_active_count is not null and a.prev_active_count > 0 then 'Retained'
     when a.current_active_count = 0 and a.prev_active_count is not null and a.prev_active_count > 0 then 'Unretained'
     when a.current_active_count > 0 and a.prev_active_count is not null and a.prev_active_count = 0 then 'Reactivated'
     when a.current_active_count = 0 and a.prev_active_count is not null and a.prev_active_count = 0 then 'Lapsed'
  end as member_lifecycle_status
from
(
with monthly_data as 
(
select MEMBER_ID,activity_year_month,sum(case when bank_type_id = 0 then 1 else 0 end) as monthly_active_count from  revenue_analysis group by MEMBER_ID,activity_year_month
)
select 
curr.MEMBER_ID,
curr.ACTIVITY_YEAR_MONTH,
curr.monthly_active_count as current_active_count,
(select monthly_active_count from monthly_data prev 
        where prev.member_id = curr.member_id and 
              prev.ACTIVITY_YEAR_MONTH < curr.ACTIVITY_YEAR_MONTH 
        order by ACTIVITY_YEAR_MONTH desc limit 1) as prev_active_count
from monthly_data curr
)a
where not (a.current_active_count = 0 and a.prev_active_count is null)--starting from the month when he placed a real wager money;
--------------------------------------------------------------------------------------------------------------------------------------------------------------------


-----------------------Query Which Support windowing-----------------------------------------------------------------------
select 
a.member_id,
a.ACTIVITY_YEAR_MONTH,
case when a.current_active_count > 0 and a.prev_active_count is null then 'New'
     when a.current_active_count > 0 and a.prev_active_count is not null and a.prev_active_count > 0 then 'Retained'
     when a.current_active_count = 0 and a.prev_active_count is not null and a.prev_active_count > 0 then 'Unretained'
     when a.current_active_count > 0 and a.prev_active_count is not null and a.prev_active_count = 0 then 'Reactivated'
     when a.current_active_count = 0 and a.prev_active_count is not null and a.prev_active_count = 0 then 'Lapsed'
  end as member_lifecycle_status,
case when (a.current_active_count = 0 and a.prev_active_count is not null and a.prev_active_count = 0)
     then count(a.MEMBER_ID) over (partition by a.MEMBER_ID,case when a.current_active_count = 0 and a.prev_active_count is not null and a.prev_active_count = 0
                                                          then 1 else 0 end order by a.MEMBER_ID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
                        )
     else 0
     end as lapsed_month
from
(
select 
curr.MEMBER_ID,
curr.ACTIVITY_YEAR_MONTH,
curr.monthly_active_count as current_active_count,
lag(monthly_active_count) over (partition by curr.MEMBER_ID) as prev_active_count
from (
select MEMBER_ID,activity_year_month,sum(case when bank_type_id = 0 then 1 else 0 end) as monthly_active_count from  test123 group by MEMBER_ID,activity_year_month
) curr
)a
where not (a.current_active_count = 0 and a.prev_active_count is null)--starting from the month when he placed a real wager money
order by a.MEMBER_ID asc,a.ACTIVITY_YEAR_MONTH asc
