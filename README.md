Description:
The program reports top 3 viewed articles, most popular authors, 
and days when HTTP errors are more than 1% of all requests, from 
a sql database of a news website.


Steps to run the program:

1. Download the database:
     https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

2. Install Python 3 and PostgreSQL 9.5 if you haven't:
     https://www.python.org/downloads/
     https://www.postgresql.org/docs/9.5/static/tutorial-install.html

3. Unzip the sql file.

4. Import the sql file into PostgreSQL database:
     psql -d news -f newsdata.sql

4. Change working directory to where report.py is located.

5. Run python3 report.py

