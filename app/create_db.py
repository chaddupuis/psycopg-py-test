import psycopg2

db_url = 'mskdb'
db_name = 'db'
db_pass = '238947239487239874239847fklajd'
db_user = 'root'
db_port = '5436'

print('starting connection...\n')
print(f'{psycopg2.__version__} version')

conn = psycopg2.connect(
    dbname=db_name, 
    user=db_user,
    password=db_pass,
    host=db_url,
    port=db_port
)
cur = conn.cursor()
cur.execute("SELECT version();")
db_version = cur.fetchone()
print(db_version)

cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS classes (
        class_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        grade_id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES students(student_id),
        class_id INTEGER REFERENCES classes(class_id),
        grade NUMERIC NOT NULL
    );
""")
try:
    conn.commit()
except:
    print(f'conn could not commit')

# test
cur.execute("SELECT * FROM information_schema.tables;")
schema=cur.fetchone()
print(f'TABLES \n\n {schema}')
cur.close()
conn.close()
