from flask import Flask
from ProcessaTicketAPI.ProcessaTicketAPI import ProcessaTicket_blueprint
import os

# app instantiation
app_2 = Flask(__name__, template_folder='ProcessaTicketAPI/templates')

# blueprint registration
app_2.register_blueprint(ProcessaTicket_blueprint)

# secret key
app_2.secret_key = 'skey'

# debug
if __name__ == "__main__":
    app_2.run(
        host=os.environ['APP_2_HOST'],
        port=os.environ['APP_2_PORT'],
        debug=True
    )
