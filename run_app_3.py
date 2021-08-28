from flask import Flask
from VisualizaResultadoAPI.VisualizaResultadoAPI import VisualizaResultado_blueprint
import os

# app instantiation
app_3 = Flask(__name__, template_folder='VisualizaResultadoAPI/templates')

# blueprint registration
app_3.register_blueprint(VisualizaResultado_blueprint)

# secret key
app_3.secret_key = 'skey'

# debug
if __name__ == "__main__":
    app_3.run(
        host=os.environ['APP_3_HOST'],
        port=os.environ['APP_3_PORT'],
        debug=True
    )
