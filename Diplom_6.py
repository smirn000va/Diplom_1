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

    user = tools.method('users.get', {'user_ids': 173312996})
    fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']

if __name__ == '__main__':
    main()