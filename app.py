import json

from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/toasts')
def get_toasts():
    with open('toasts.json', 'r') as f:
        res = json.load(f)
    print(res[0])
    return {'toasts': res}


def get_app():
    return app


if __name__ == '__main__':
    app.run()
