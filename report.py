#!/usr/bin/env python3
'''The program connects to a database of a news website, 
and returns reports of the top 3 viewed articles, authors, 
and days when more than 1% of requests lead to errors.
'''

import psycopg2

DBNAME = "news"

def top_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select articles.title, count(*) as num from articles join log on log.path = concat('/article/', articles.slug) group by articles.title order by num desc limit 3;")
    rows = c.fetchall()
    db.close()
    print("The most popular three articles of all time:\n")
    for title, num in rows:
        print("\"{}\" -- {} views\n".format(title, num))

def top_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name, count(*) as num from articles, authors, log where log.path = concat('/article/', articles.slug) and authors.id = articles.author group by authors.name order by num desc;")
    rows = c.fetchall()
    db.close()
    print("The most popular article authors of all time:\n")
    for name, num in rows:
    	print("{} -- {} views\n".format(name, num))
#def busy_days():

if __name__ == '__main__':
    top_articles()
    top_authors()