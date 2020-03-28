import vk
    session = vk.Session(access_token='{b80bf0dc5908f8de536212ef3268cb07782de1f738acbaaed95ca18bfc4495557df1cfa7b3be17f64c9bd&expires_in=86400&user_id=1733129¬96&expires_in=86400&user_id=173312996}')
    vk_api = vk.API(session)
    vk_api.users.get(user_id='173312996')