import urllib3, json, sys
token = 'b80bf0dc5908f8de536212ef3268cb07782de1f738acbaaed95ca18bfc4495557df1cfa7b3be17f64c9bd&expires_in=86400&user_id=173312996' #Ваш токен
 
def vk(meth, param):
    url  = u'https://api.vk.com/method/%s' %meth
    method = {
        'friends.get'    : 'user_id=%s',
        'users.get'      : 'user_ids=%s' ,
        'groups.get'     : 'user_id=%s&access_token=' + token,
        'groups.getById' : 'group_ids=%s&fields=contacts,description,members_count',
    }[meth] %param
 
    res  = urllib3.urlopen(url, method).read()
    data = json.loads( res )
   
    if 'error' in data:
        print (data)
        return list()
    return data[u'response']