from flask import Flask, request
from flask_httpauth import HTTPDigestAuth
import os
import dotenv

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = '111111111111'
auth = HTTPDigestAuth()

users = {
    "john": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/asdf')
def index():
    system_state = True
    devices = [
        {
            'type': 'device1',
            'channels': ['channel1', 'channel2', 'channel3']
        },
        {
            'type': 'device2',
            'channels': ['channel1', 'channel2']
        }
    ]
    configuration = [
        {
            'type': 'config1',
            'value': 'value1'
        },
        {
            'type': 'config2',
            'value': 'value2'
        }
    ]
    return render_template('dashboard.html', system_state=system_state, devices=devices, configuration=configuration)

@app.route('/flip-system-state', methods=['POST'])
def flip_system_state():
    file_path = os.getenv('SYSTEM_STATE_FILE')
    system_state = os.path.exists(file_path)

    if system_state:
        os.remove(file_path)
    else:
        open(file_path, 'a').close()

    return {
        "success": True,
        "data": {
            "msg": "Erfolgreich aktualisiert!",
            "system_state": not system_state
        }
    }



if __name__ == '__main__':
    app.run()
