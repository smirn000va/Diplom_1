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

  
    friends = tools.get_all('friends.get', 100, {'user_id': 156277124})

    print (friends)

if __name__ == '__main__':
    main()

#Возвращает список друзей, но только моей записи