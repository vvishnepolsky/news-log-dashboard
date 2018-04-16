# News Paper Data Analysis Dashboard
The news paper data analysis dashboard is a text based analysis tool written in `python` that analyzes a set of system log data to determine:
1. Most Popular Articles by total views
2. Most Popular Authors by total views
3. Request error statistics by day

## Software Dependancies
To run the news paper data analysis dashboard the following must be installed on your system:
1. `vagrant` -  Configuration Program
2. `VirtualBox` - Virtual Environment

## Installation
To install and run the application ensure you have installed the necessary dependancies and have created the proper database structure, refer to the code below for necessary tables/data structure:

1. From the terminal/command prompt `cd` into the `vagrant` folder
2. Execute the `vagrant up` command
3. Initiate vagrant by running the `vagrant ssh` command
4. Download and unzip the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Place the data into the `vagrant directory`
5. With vagrant running (Step 2) run the following command `psql -d news -f newsdata.sql`
6. With vagrant running execute `cd news-log-dashboard python dashboard.py`

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
