import json
import os


class User:
    def __init__(self, s_username, s_password, s_email):
        self.username = s_username
        self.password = s_password
        self.email = s_email


class UserRepository:
    def __init__(self):

        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load users from .json file
        self.loaduser()

    def loaduser(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r', encoding='utf-8') as file:
                users = json.load(file)
                for s_user in users:
                    n_user = json.loads(s_user)
                    newuser = User(s_username=n_user['username'], s_password=n_user['password'],
                                   s_email=n_user['email'])
                    self.users.append(newuser)
            print(self.users)

    def register(self, e_user: User):
        self.users.append(e_user)
        self.savetofile()
        print("user created")

    def login(self, l_username, l_password):
        for c_user in self.users:
            if c_user.username == l_username and c_user.password == l_password:
                self.isLoggedIn = True
                self.currentUser = c_user
                print('succesfull')
            else:
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('exit')

    def identity(self):
        if self.isLoggedIn:
            print(f'username:{self.currentUser}')
        else:
            print('başaramadın')

    def savetofile(self):
        users_list = []
        for n_user in self.users:
            users_list.append(json.dumps(n_user.__dict__))
        with open('users.json', 'w') as file:
            json.dump(users_list, file)


repository = UserRepository()

while True:
    print('Menu'.center(50, '*'))
    choise = input('1- Register\n2- Login\n3- Logout\n4- Identiy\n5- Exit\n which one\n')

    if choise == '5':
        break
    else:
        if choise == '1':
            # register
            enter_username = input('username: ')
            enter_password = input('password: ')
            enter_email = input('email: ')

            user = User(s_username=enter_username, s_password=enter_password, s_email=enter_email)
            repository.register(user)

        elif choise == '2':
            # login
            username = input('username: ')
            password = input('password: ')

            repository.login(username, password)
        elif choise == '3':
            # logout
            repository.logout()
        elif choise == '4':
            # display username
            repository.identity()
        else:
            print('wrong one')
