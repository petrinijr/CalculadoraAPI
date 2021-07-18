from flask import (
    blueprints,
    request,
    redirect,
    session,
    render_template,
    jsonify
)
import os
from markupsafe import Markup
from GeraTicketAPI.GeraTicketClasses import TicketGenerator

# urls
home_url = os.path.join(os.environ['APP_1_HOST'], os.environ['APP_1_PORT'])
calculate_url = '/calculate'

GeraTicket_blueprint = blueprints.Blueprint('GeraTicket_blueprint', __name__)


@GeraTicket_blueprint.route("/")
def show_welcome_page():
    return render_template(
        'welcome_page.html',
        url=calculate_url
    )


@GeraTicket_blueprint.route('/calculate', methods=['POST'])
def process_calculation_request_and_redirect():
    tickgen = TicketGenerator(jsonify(request.form).json)
    result = tickgen.process()
    session['result'] = result
    return redirect('/getticket')


@GeraTicket_blueprint.route('/getticket')
def give_ticket():
    result = session.get('result', None)
    if bool(result['is_valid']):
        result_str = Markup(f"""
            Requisição bem-sucedida ({result['timestamp']})! <br />
            Seu código é: {result["code"]}. Use-o para obter o resultado.
        """)

    else:
        result_str = Markup(f"""
            Requisição mal-sucedida ({result['timestamp']})! <br />
            Erro: {result["comment"]}<br />
            Tente gerar outro número.
        """)

    return render_template(
        'get_ticket.html',
        result_str=result_str
    )
