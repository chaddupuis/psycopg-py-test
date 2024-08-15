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
cur.execute("INSERT INTO students (name) VALUES ('Bill'), ('Frank'), ('Charlie');")
cur.execute("INSERT INTO classes (name) VALUES ('Math'), ('Science'), ('History');")
cur.execute("""
    INSERT INTO grades (student_id, class_id, grade) VALUES
    (1, 1, 85), (1, 2, 90), (1, 3, 88),
    (2, 1, 78), (2, 2, 82), (2, 3, 80),
    (3, 1, 92), (3, 2, 87), (3, 3, 85);
""")


conn.commit()
#test
cur.execute("SELECT * FROM grades;")
test_grades=cur.fetchone()
print(f'GRADES TEST \n\n {test_grades}')
cur.close()
conn.close()

