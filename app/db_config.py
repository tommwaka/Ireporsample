import psycopg2

import os




url = "dbname='ireporter' host='localhost' port='5432' user='postgres' password='tomkin254'"


db_url = os.getenv('DATABASE_URL')


def connection(url):
    con = psycopg2.connect(url)
    return con


def init_db():
    con = connection(db_url)
    return con


def create_tables():

    conn = connection(db_url)
    curr = conn.cursor()
    queries = ireportertables()


    for query in queries:
        curr.execute(query)
    conn.commit()


def destroy_tables():

    conn = connection(db_url)
    curr = conn.cursor()
    incidents = "DROP TABLE IF EXISTS incidents CASCADE"
    users = "DROP TABLE IF EXISTS users CASCADE"
    queries = [incidents, users]
    for query in queries:
        curr.execute(query)
    conn.commit()


def ireportertables():

    redflags = """CREATE TABLE IF NOT EXISTS incidents (

	    incident_id serial PRIMARY KEY NOT NULL,
	    createdBy character varying(50) NOT NULL,
	    type character varying(50) NOT NULL,
	    location character varying(50) NOT NULL,
	    status  character varying(50) NOT NULL,
	    images  character varying(50) NOT NULL,
        videos  character varying(50) NOT NULL,
	    createdOn timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
	    )"""



    users = """CREATE TABLE IF NOT EXISTS users (

	    user_id serial PRIMARY KEY NOT NULL,
	    firstname character varying(50) NOT NULL,
        lastname character varying(50) NOT NULL,
        email character varying(50),
	    username character varying(50) NOT NULL,
	    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL,
	    password character varying(500) NOT NULL
	    )"""



    query = [redflags, users]

    return query