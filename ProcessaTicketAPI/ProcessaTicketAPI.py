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
from ProcessaTicketAPI.ProcessaTicketClasses import TicketProcessor

# urls
home_url = os.path.join(os.environ['APP_2_HOST'], os.environ['APP_2_PORT'])
process_url = '/process'

ProcessaTicket_blueprint = blueprints.Blueprint('ProcessaTicket_blueprint', __name__)


@ProcessaTicket_blueprint.route("/")
def show_welcome_page():
    return render_template(
        'welcome_page.html',
        url=home_url
    )


@ProcessaTicket_blueprint.route('/process', methods=['POST'])
def process_calculation_request_and_redirect():
    tickprocs = TicketProcessor(jsonify(request.form).json)
    result = tickprocs.process()
    session['result'] = result
    return redirect('/reqcomplete')


@ProcessaTicket_blueprint.route('/getticket')
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
        'force_ticket_process.html',
        result_str=result_str
    )
