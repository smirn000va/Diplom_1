import csv
import vk_api
from datetime import datetime

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

            search_birthday=f"{row['birthday']}"

            if len(search_birthday) > 0:

                data_search_birthday = datetime.strptime (search_birthday, '%m/%d/%y')

                print(data_search_birthday)

            users = tools.get_all('users.search', 1000, values={'q': search_string, 'birth_day': data_search_birthday.day, 'birth_month': data_search_birthday.month, 'birth_year': data_search_birthday.year, 'fields': ['bdate', 'contacts', 'city', 'connections', 'followers_count']})
        
            for x in users.items(): 
                print(x)

        pass

if __name__ == '__main__':
    main()
