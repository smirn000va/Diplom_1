import vk_api

#vk = vk_api.VkApi(token='b80bf0dc5908f8de536212ef3268cb07782de1f738acbaaed95ca18bfc4495557df1cfa7b3be17f64c9bd&expires_in=86400&user_id=173312996') 
vk = vk_api.VkApi(login='smirn000va@gmail.com', password='rjcz11011101')
vk.auth()


user = vk.method('users.get', {'user_ids': 9930357})
fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']

print (fullname)

#Возвращает ФИ конкретного пользователя по ID