
import random

SUBJECTS = 9
OBJECTS = 4

PERMISSIONS = ['NONCONFIDENTIAL','CONFIDENTIAL','SECRET','TOP SECRET']

class Mixin:

    def __init__(self, permission):
        self.base_permission = permission
        self.permission = self.base_permission

    def __repr__(self):
        return str(self.name) + ' : ' + str(PERMISSIONS[self.permission])


class User(Mixin):
    _glob_dict = {}

    def __init__(self, permission):
        super().__init__(permission)
        self.name = len(self._glob_dict) + 1
        self._glob_dict[self.name] = self

    @classmethod
    def find(cls, string):
        user = cls._glob_dict.get(int(string))
        if user:
            return user
        raise Exception(f'{user} not found!')

    def change(self):
        new_permisison = input("Enter Classificaiton 'NONCONFIDENTIAL','CONFIDENTIAL','SECRET','TOP SECRET'\n")
        level_permission = PERMISSIONS.index(new_permisison)

        if level_permission <= self.base_permission:
            print(
                f'Done, now your permission {self.permission} change to {new_permisison}')
            self.permission = level_permission
        else:
            raise PermissionError(
                f"You can't change to permisison {new_permisison}!")


class File(Mixin):
    _glob_dict = {}

    def __init__(self, permission):
        super().__init__(permission)
        self.name = len(self._glob_dict) + 1
        self._glob_dict[self.name] = self

    @classmethod
    def find(cls, string):
        file = cls._glob_dict.get(int(string))
        if file:
            return file
        raise KeyError(f'{file} not found!')

    @classmethod
    def command(cls, string, user):
        name = input('Enter name file\n')
        object = File.find(name)

        if string == 'write':
            object.write(user)
        elif string == 'read':
            object.read(user)
        else:
            raise KeyError('Wrong command!')

    def write(self, user):
        if user.permission <= self.permission:
            print('\nDone :)\n')
            return
        raise PermissionError('\nNot enough permisisons!!!\n')

    def read(self, user):
        if user.permission >= self.permission:
            print('Done')
            return
        raise PermissionError('\nNot enough permisisons!!!\n')


if __name__ == '__main__':

    users = [User(random.randint(0, 3)) for x in range(SUBJECTS)]
    files = [File(random.randint(0, 3)) for x in range(OBJECTS)]

    while True:
        try:
            print('Users:')
            print(users)
            print('Files')
            print(files)
            print('')

            name = input('Login: ')
            user = User.find(name)
            command = input(
                f"Welcome, {user.name}! What's command do you want to do User{name}?\
                Choose: 'read', 'write', 'change', 'exit'\n")

            if command == 'change':
                user.change()
                continue

            if command == 'exit':
                break

            File.command(command, user)

        except BaseException as e:
            print(e)
