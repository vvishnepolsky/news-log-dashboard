# News Paper Data Analysis Dashboard
The news paper data analysis dashboard is a text based analysis tool written in `python` that analyzes a set of system log data to determine:
1. Most Popular Articles by total views
2. Most Popular Authors by total views
3. Request error statistics by day

## Software Dependancies

## Installation

## Required Views
In order to execute the program the following views will need to be created in the database:

```sql
  CREATE VIEW total_requests AS
    SELECT date(time), count(*) from log
    GROUP BY date(time)

  CREATE VIEW bad_requests AS
    SELECT date(time), count(*) from log
    WHERE status = '404 NOT FOUND'
    GROUP BY date(time)
```
