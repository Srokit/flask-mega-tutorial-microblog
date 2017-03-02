WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    {
        'url': "https://www.myopenid.com",
        'name': "MyOpenID"
    },
    {
        'url': "http://www.openid.aol.com/<username>",
        'name': "AOL"
    }
]