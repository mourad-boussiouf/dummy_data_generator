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

# Generate 500 users
for _ in range(500):
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
        cur.execute("""
            INSERT INTO clocks (time, status, user_id, inserted_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW());
        """, (time, status, user_id))

    for _ in range(5):
        base_time = fake.date_time_this_year()

        # Ensure start time is between 6am and 10am
        start_time = base_time.replace(hour=random.randint(6, 10), minute=random.randint(0, 59),
                                       second=random.randint(0, 59))

        # Ensure end time is between 4pm and 8pm
        end_time = base_time.replace(hour=random.randint(16, 20), minute=random.randint(0, 59),
                                     second=random.randint(0, 59))

        # Ensure end time is after start time
        if end_time <= start_time:
            end_time += timedelta(hours=random.randint(1, 4))

        cur.execute("""
            INSERT INTO working_times (start, "end", user_id, inserted_at, updated_at)
            VALUES (%s, %s, %s, NOW(), NOW());
        """, (start_time, end_time, user_id))

conn.commit()
cur.close()
conn.close()
