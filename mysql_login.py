import mysql.connector


def conn():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd=''
    )


def select():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='login'
    )

    select_query = 'SELECT * FROM users'

    cursor = conn.cursor()
    cursor.execute(select_query)
    user= [{'username': x[1], 'pwd': x[2]} for x in cursor.fetchall()]
    return user


def user_login():
    print('User Login\n**********')
    username = input('Enter your username: ')
    pwd = input('Enter your password: ')

    conn()
    users = select()
    for user in users:
        if (user['username'] == username) and (user['pwd'] == pwd):
            print('User is valid...')
            break
    else:
        print('Not valid user')


user_login()
