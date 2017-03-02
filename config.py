import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

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