import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


import psycopg2

conn = psycopg2.connect(
    dbname="api_dev",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Generate 1000 users

for _ in range(1000):
    username = fake.user_name()
    email = fake.email()

    cur.execute("""
        INSERT INTO users (username, email, inserted_at, updated_at)
        VALUES (%s, %s, NOW(), NOW()) RETURNING id;
    """, (username, email))
    user_id = cur.fetchone()[0]

    for _ in range(5):
        time = fake.date_time_this_year()
        status = fake.boolean()
        # affiliate clocks to all users
        cur.execute("""
            INSERT INTO clocks (time, status, user_id, inserted_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW());
        """, (time, status, user_id))

    for _ in range(5):
        start_time = fake.date_time_this_year()
        end_time = start_time + timedelta(hours=random.randint(1, 8))
        # affiliate working_times to all users
        cur.execute("""
            INSERT INTO working_times (start, "end", user_id, inserted_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW());
        """, (start_time, end_time, user_id))

conn.commit()
cur.close()
conn.close()