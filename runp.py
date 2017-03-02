#!flask/bin/python
#Run server in production mode (not development)
from app import app

app.run(debug=False)
