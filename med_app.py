from flask import Flask
from auth import auth_bp
from meds import meds_bp
from index import index_bp


app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)
app.register_blueprint(meds_bp)
app.register_blueprint(index_bp)




if __name__ == '__main__':
    app.run(debug=True)
