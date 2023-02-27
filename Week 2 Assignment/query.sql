--SQL.  Julia conducted a days of learning SQL contest. The start date of the contest was March 01, 2016 and the end date was March 15, 2016.
--Write a query to print total number of unique hackers who made at least submission each day (starting on the first day of the contest), and find the hacker_id and name of the hacker who made maximum number of submissions each day. If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. The query should print this information for each day of the contest, sorted by the date.


SET @rownum=0;
select x.submission_date, (select count(distinct ls.hacker_id) from
                           Submissions ls where x.rownum =
                           (select count(distinct q.submission_date) from Submissions q
                            where q.hacker_id = ls.hacker_id and q.submission_date <= x.submission_date)
                           ) as zz, h.hacker_id, h.name from
(
select w.*, @rownum:=@rownum+1 as rownum from
(
select * from
(
select * from
(
select * from
(select s.submission_date, count(*) as co, s.hacker_id from Submissions s group by s.submission_date, s.hacker_id) t
order by t.co desc, t.hacker_id asc
    ) u group by u.submission_date
) v
order by v.submission_date asc
    ) w
) x
 inner join Hackers h on h.hacker_id = x.hacker_id
order by x.submission_date asc;