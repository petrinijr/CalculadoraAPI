from flask import Flask
from GeraTicketAPI.GeraTicketAPI import GeraTicket_blueprint

# app instantiation
app_1 = Flask(__name__)

# blueprint registration
app_1.register_blueprint(GeraTicket_blueprint)

if __name__ == '__main__':
    app_1.run(port=5000)
