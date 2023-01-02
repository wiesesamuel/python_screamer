from flask import Flask
from flask_httpauth import HTTPDigestAuth
import os
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
auth = HTTPDigestAuth()

@auth.get_password
def get_pw(username):
    if username == os.getenv('ADMIN_NAME'):
        return os.getenv('ADMIN_PW')
    return None

@app.before_request
@auth.login_required
def login_required_for_all_request():
    pass
