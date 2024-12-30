create table baby(
Id INT,
Name Varchar(255),
Year INT,
Sex VARCHAR(5),
Count INT,
PRIMARY KEY(Id)
)

Load data local infile '/home/ruksad/Documents/learn/AIandContent/ProgrammingForDataScience/sources/babynames.csv'
into table baby fields terminated by ','
lines terminated by '\n'
ignore 1 rows

select Year, sum(count) from BABY_NAMES bn group by year;
select year,sex, sum(count) from BABY_NAMES group by year,sex;
select year,sex,name, sum(count) total from BABY_NAMES bn group by year,sex,name order by total desc;
select year,sex,name, max(count) max_names from BABY_NAMES  where sex='M' group by year,sex,name;
-- find maximum length of a name in a particular year
select year,sex,max(length(name)) max_name_size from BABY_NAMES  group by year,sex;

select *, substr(name,1,1) initials from BABY_NAMES;

-- find total names with letter L in a year

with letters as ( select *,substr(name,1,1) initials from BABY_NAMES)
select initials, year, sum(count) total_names from letters where initials='L' group by year;