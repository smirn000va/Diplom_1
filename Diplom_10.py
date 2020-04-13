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

  
    users = tools.get_all('users.search', 1000, values={'q': 'Женечка Владимирова', 'birth_day': '01', 'birth_month': '04','birth_year': '1987', 'fields': ['bdate', 'contacts', 'city', 'connections', 'followers_count']})
    
    friends = tools.get_all('friends.get', 1000, values={'q': 'Женечка Владимирова', 'birth_day': '01', 'birth_month': '04','birth_year': '1987', 'fields': ['bdate', 'contacts', 'city', 'connections', 'followers_count']})
    friends_count = friends['count']

    wall = tools.get_all('wall.get', 1000, values={'q': 'Женечка Владимирова', 'birth_day': '01', 'birth_month': '04','birth_year': '1987', 'fields': ['bdate', 'contacts', 'city', 'connections', 'followers_count']})
    wall_count = wall['count']

    print (friends_count)  
    print (wall_count)   
    #x=users.keys()
    for x in users.items(): 
        print (x)
 
if __name__ == '__main__':
    main()


    #вывод количества друзей и 