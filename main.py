from flask import Flask
from GeraTicketAPI.GeraTicketAPI import GeraTicket_blueprint
import os

# app instantiation
app_1 = Flask(__name__, template_folder='GeraTicketAPI/templates')

# blueprint registration
app_1.register_blueprint(GeraTicket_blueprint)

if __name__ == '__main__':
    app_1.secret_key = 'skey'

    app_1.run(
        host=os.environ['APP_1_HOST'],
        port=os.environ['APP_1_PORT']
    )
