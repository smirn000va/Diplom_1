import csv
import vk_api

def main():
   
    login, password = 'smirn000va@gmail.com', 'rjcz11011101'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    tools = vk_api.VkTools(vk_session)
    
    
    with open('data.csv', 'r', encoding='utf-8') as f:
        fields = ['first_name', 'last_name', 'birthday', 'place birthday', 'phone number', 'email']
        reader = csv.DictReader(f, fields, delimiter=',')
        for row in reader:
            #print(row['first_name'], row['last_name'])
            users = tools.get_all('users.search', 1000, values={'q': row['last_name']})

        pass

if __name__ == '__main__':
    main()


    #поиск из базы через юзерсеач