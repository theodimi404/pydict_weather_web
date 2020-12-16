from flask import Flask
from controllers import controller_home, controller_predict

app = Flask(__name__)

app.register_blueprint(controller_home.api)
app.register_blueprint(controller_predict.api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
