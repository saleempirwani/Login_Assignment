import pymongo


def conn(database, collection):

    conn = pymongo.MongoClient("mongodb://localhost:27017/")

    db = conn[database]
    coll = db[collection]

    return coll


def get_user():

    col = conn('login', 'users')
    users = [{'username': x['username'], 'pwd': x['pwd']} for x in col.find()]

    return users


def user_login():
    print('User Login\n**********')
    username = input('Enter your username: ')
    pwd = input('Enter your password: ')

    users = get_user()
    for user in users:
        if (user['username'] == username) and (user['pwd'] == pwd):
            print('User is valid...')
            break
    else:
        print('Not valid user')


user_login()
