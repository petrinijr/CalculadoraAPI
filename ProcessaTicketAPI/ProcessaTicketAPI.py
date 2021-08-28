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
from ProcessaTicketAPI.ProcessaTicketClasses import TicketProcessor
from settings import APP_1_HOME_URL, APP_3_HOME_URL


ProcessaTicket_blueprint = blueprints.Blueprint('ProcessaTicket_blueprint', __name__)


@ProcessaTicket_blueprint.route("/")
def show_welcome_page():
    return render_template(
        'welcome_page.html',
        url='/process',
        home_url='//' + APP_1_HOME_URL,
        get_result_url='//' + APP_3_HOME_URL
    )


@ProcessaTicket_blueprint.route('/process', methods=['POST'])
def process_calculation_request_and_redirect():

    tickprocs = TicketProcessor(jsonify(request.form).json)

    result = tickprocs.process()

    session['result'] = result

    return redirect('/process_result')


@ProcessaTicket_blueprint.route('/process_result')
def report_on_request():

    result = session.get('result')

    if result['successful'] == 'true':
        result_str = Markup(f"""
            Requisição bem-sucedida ({result['timestamp']})! <br />
            O cálculo de código {escape(result["code"])} foi processado. <br /> 
            Use-o no seguinte <a href="//{APP_3_HOME_URL}"> link</a> para obter o resultado. <br />
            Ou volte para a página inicial e <a href="//{APP_1_HOME_URL}">gere outro código<a/>.
        """)

    else:
        result_str = Markup(f"""
            Requisição mal-sucedida ({result['timestamp']})! <br />
            Código: {escape(result['code'])}<br />
            Erro: {escape(result['error'])}<br />
            Tente gerar <a href="//{APP_1_HOME_URL}">outro código<a>.
        """)

    return render_template(
        'request_complete.html',
        result_str=result_str
    )
