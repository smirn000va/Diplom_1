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

  
    users = tools.get_all('users.search', 1000, values={'q': 'Женечка Владимирова', 'birth_day': '01', 'birth_month': '04','birth_year': '1987'}, key={'count', 'items', 'first_name','last_name', 'city', 'contacts'} )
    
    #users_search={'id': '', 'first_name': '', 'last_name': ''}
        #users_list = users[0]['id']
    
    #x=users.keys()
    for x in users.items(): 
        print (x)
 
if __name__ == '__main__':
    main()