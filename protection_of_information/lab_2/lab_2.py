# user 9 and 4 files
import random 

POLITICS_SENTENCE = {
    0:set(''),
    1:set('s'),
    2:set('w'),
    3:set('sw'),
    4:set('r'),
    5:set('sr'),
    6:set('rw'),
    7:set('srw'),
}

def check_permisison(table_users, user, permission,num_file):
    return True if permission in table_users[user][num_file] else False
        
def send_permisison(table_users, user, permission,num_file):
    table_users[user][num_file].add(permission)

def security_policy(table_users):
    
    while 1: 
        for x in range(amount_users):
            print(f'Номер пользователя {x}, права: {table_users[x]}')
        user = int(input('Введите имя пользователя\n'))
        print(f'Ваши права на файлы')
        print(table_users[user])

        num_file = int(input("Введите номер файла\n"))
        act = input('Введите номер файла и что с ним хотите сделать : передать права - "s", прочитать - "r", записать - "w"\n')
    

        if check_permisison(table_users,user,act,num_file) is True:
            if act == 's':
                recipient = int(input('Кому передать права\n'))
                permisison = input('Что хотите передать: передача прав - "s", чтение - "r", запись - "w"\n')
                if check_permisison(table_users,user,permisison,num_file):
                    send_permisison(table_users,recipient,permisison,num_file)
                    print('Операция успешно выполнена!\n')
                else:
                    print('У вас нет прав')
            else:
                print('Операция успешно выполнена!\n')
        else:
            print('Вы не имеете достаточно прав!\n')


if __name__=='__main__' :
    amount_users = 9
    amount_objects = 4 
    table_users = [[POLITICS_SENTENCE[random.randint(0,4)] for x in range(4)] for x in range(9)]
    security_policy(table_users)