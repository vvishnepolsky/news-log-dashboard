import psycopg2

DBNAME = 'news'



class DBConnection:

# 1. Establish Connection to Database

    def __init__(self):
        self.db = psycopg2.connect(dbname = DBNAME)

# 2. List Most Popular Articles

    def popular_articles(self):

        q = """
            SELECT title, count(*) FROM
                articles, log as a
                WHERE ('/article/' || slug) = a.path
                AND a.status = '200 OK'
                AND a.method = 'GET'
                GROUP BY title
                ORDER BY count(*) DESC
        """

        c = self.db.cursor()
        c.execute(q)

        results = c.fetchall()

        print ("The Most Viewed Articles: " + '\n')
        for article in results:
            print(article[0] + ' - ' + str(article[1]) + ' Views')
        print('\n\n')

# 3. List Most Popular Authors

    def popular_authors(self):

        q = """
            SELECT authors.name, count(*) from
                authors, articles, log
                WHERE ('/article/' || slug) = path
                AND authors.id = articles.author
                AND status = '200 OK'
                AND method = 'GET'
                GROUP BY authors.name
                ORDER BY count(*) DESC
        """

        c = self.db.cursor()
        c.execute(q)

        results = c.fetchall()

        print ("The Most Viewed Auhtors: " + '\n')
        for author in results:
            print(author[0] + ' - ' + str(author[1]) + ' Views')
        print('\n\n')


# 3. Error Statistics

    def request_stats(self):

        q= """
            SELECT A.date, CAST (B.count * 100/A.count as FLOAT) from total_requests as A
            JOIN bad_requests as B
            on A.date = B.date
            WHERE (B.count * 100/A.count) > 1
        """
        c = self.db.cursor()
        c.execute(q)
        results = c.fetchall()


        print ("Request Error Statistics: " + '\n')
        for error in results:
            print(str(error[0]) + ' - ' + str(error[1]) + '%')
        print('\n\n')

# 3. Close Connection
    def close(self):
        self.db.close()


con = DBConnection()
con.popular_articles()
con.popular_authors()
con.request_stats()
con.close()
