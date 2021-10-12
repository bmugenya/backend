import psycopg2

url = "dbname='Rafiki' user='postgres' host='localhost' port=5432 password='Qw12Er34'"

# url = "dbname='d3j0idnmrkm7ud' user='kzlggknuovccko' host='ec2-54-221-215-228.compute-1.amazonaws.com' port=5432 password='ddeec1900b9caaebda4e7bf4191e70775e9478076833523b4c5d79e161ff0d86'"



class database_setup(object):

    def __init__(self):
        self.conn = psycopg2.connect(url)
        self.cursor = self.conn.cursor()

    def destroy_tables(self):
        self.cursor.execute("""DROP TABLE IF EXISTS user CASCADE;""")

        self.conn.commit()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Users (
            user_id SERIAL NOT NULL,
            name VARCHAR(50) NOT NULL,
            registration_date TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
            email VARCHAR(50)  UNIQUE NOT NULL,
            password VARCHAR(256) NOT NULL,
            photo VARCHAR(255) NOT NULL,
            PRIMARY KEY (email)
            );""")




        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Share (
            share_id SERIAL NOT NULL,
            story TEXT NOT NULL,
            post_date TIMESTAMP  NOT NULL DEFAULT CURRENT_DATE,
            email VARCHAR(50) REFERENCES Users(email) NOT NULL,
            approved BOOLEAN NOT NULL,
            PRIMARY KEY (share_id)
            );""")
