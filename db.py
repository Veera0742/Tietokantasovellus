from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv
#import os
#import re

#uri = os.getenv("DATABASE_URL")  # or other relevant config var
#if uri.startswith("postgres://"):
#    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)