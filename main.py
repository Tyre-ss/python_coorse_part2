import psycopg2

PGHOST = 'ep-dry-night-a21o0x5h-pooler.eu-central-1.aws.neon.tech'
PGDATABASE = 'neon_db'
PGUSER = 'neon_db_owner'
PGPASSWORD = 'npg_kJpN7yVUWrw8'
PORT = 5432


with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS topic (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
            )
        """
        cursor.execute(query)

        query = """
            CREATE TABLE IF NOT EXISTS "users" (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                post_name VARCHAR(50) UNIQUE NOT NULL,
                post VARCHAR(1000) UNIQUE NOT NULL,
                user_id INTEGER REFERENCES users(id),
                topic_id INTEGER REFERENCES topic(id)
            );
            """
        cursor.execute(query)

