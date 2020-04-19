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
    
    
    with open('data_3.csv', 'r', encoding='utf-8') as f:
        fields = ['first_name', 'last_name', 'birthday', 'place birthday', 'phone number', 'email']
        reader = csv.DictReader(f, fields, delimiter=',')
        for row in reader:

            search_string=f"{row['first_name']} {row['last_name']}"

            search_birthday=f"{row['birthday']}".split('.')

            #print(search_string)
            
            #print(search_birthday)

            users = tools.get_all('users.search', 1000, values={'q': search_string, 'birth_day': search_birthday[1], 'birth_month': search_birthday[2], 'birth_year': search_birthday[3], 'fields': ['bdate', 'contacts', 'city', 'connections', 'followers_count']})
        
            for x in users.items(): 
                print(x)

        pass

if __name__ == '__main__':
    main()


    #поиск из базы через юзерсеач