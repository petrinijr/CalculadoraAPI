from flask import (
    blueprints,
    request,
    redirect,
    session,
    render_template,
    jsonify
)
import os
from markupsafe import Markup, escape
from VisualizaResultadoAPI.VisualizaResultadoClasses import TicketRetriever
from settings import APP_1_HOME_URL, APP_2_HOME_URL, APP_3_HOME_URL


VisualizaResultado_blueprint = blueprints.Blueprint('VisualizaResultado_blueprint', __name__)


@VisualizaResultado_blueprint.route("/")
def show_welcome_page():
    return render_template(
        'welcome_page.html',
        url='/get_result',
        home_url='//' + APP_1_HOME_URL,
        process_url='//' + APP_2_HOME_URL
    )


@VisualizaResultado_blueprint.route('/get_result', methods=['GET'])
def process_calculation_request_and_redirect():
    tickret = TicketRetriever(request.args)

    result = tickret.process()

    session['result'] = result

    return redirect('/retrieve_result')


@VisualizaResultado_blueprint.route('/retrieve_result')
def report_on_request():
    pass
    result = session.get('result')

    if result['successful'] == 'true':
        result_str = Markup(f"""
            Requisição bem-sucedida ({result['timestamp']})! <br />
            O valor calculado para o código {result["code"]} foi: {result['val']}<br />
        """)

    else:
        result_str = Markup(f"""
            Requisição mal-sucedida ({result['timestamp']})! <br />
        """)

    return render_template(
        'retrieve_result.html',
        result_str=result_str,
        home_url='//' + APP_1_HOME_URL,
        force_url='//' + APP_2_HOME_URL,
        retrieve_url='//' + APP_3_HOME_URL
    )
