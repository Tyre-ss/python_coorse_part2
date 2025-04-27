import psycopg2

PGHOST = 'ep-round-moon-a2toiy10-pooler.eu-central-1.aws.neon.tech'
PGDATABASE = 'book_store'
PGUSER = 'book_store_owner'
PGPASSWORD = 'npg_Q9zgrIW0nwvs'
PORT = 5432


with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS authors (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL,
                year_of_author VARCHAR(4) UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL,
                author_id INTEGER REFERENCES authors(id),
                price VARCHAR(50) NOT NULL,
                description VARCHAR(1000) UNIQUE NOT NULL
            );
        """
        cursor.execute(query)
