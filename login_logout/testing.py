import psycopg2

connection = psycopg2.connect(
    database='postgres', 
    host='localhost', 
    port='5432', 
    user='postgres', 
    password='rlfdz3012')

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

with connection.cursor() as c:
    c.execute("""   SELECT  password
                    FROM    kapus.kapus_auth_user 
                    WHERE   username = '{}'""".format('ralfidzaky'))
    
    data = dictfetchall(c)
    print(data[0]['password'])