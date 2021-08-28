from flask import (
    blueprints,
    request,
    redirect,
    session,
    render_template,
    jsonify
)
from markupsafe import Markup, escape
from GeraTicketAPI.GeraTicketClasses import TicketGenerator
from settings import APP_1_HOME_URL, APP_2_HOME_URL, APP_3_HOME_URL

GeraTicket_blueprint = blueprints.Blueprint('GeraTicket_blueprint', __name__)


@GeraTicket_blueprint.route("/")
def show_welcome_page():
    return render_template(
        'welcome_page.html',
        url='/calculate',
        force_url='//' + APP_2_HOME_URL,
        result_url='//' + APP_3_HOME_URL
    )


@GeraTicket_blueprint.route('/calculate', methods=['POST'])
def process_calculation_request_and_redirect():

    tickgen = TicketGenerator(jsonify(request.form).json)

    result = tickgen.process()

    session['result'] = result

    return redirect('/get_ticket')


@GeraTicket_blueprint.route('/get_ticket')
def give_ticket():

    result = session.get('result', None)

    if bool(result['is_valid']):
        result_str = Markup(f"""
            Requisição bem-sucedida ({result['timestamp']})! <br />
            Seu código é: {result["code"]}. Use-o para obter o resultado.<br />
            Caso deseje acelerar o cálculo, <a href="//{APP_2_HOME_URL}">clique aqui.</a><br />
            Ou pode esperar o término em alguns minutos e 
            consultar diretamente o resultado <a href="//{APP_3_HOME_URL}">neste link</a>.
        """)

    else:
        result_str = Markup(f"""
            Requisição mal-sucedida ({result['timestamp']})! <br />
            Erro: {escape(result["comment"])}<br />
            <a href="//{APP_1_HOME_URL}">Tente gerar outro código</a>.
        """)

    return render_template(
        'get_ticket_page.html',
        result_str=result_str
    )
