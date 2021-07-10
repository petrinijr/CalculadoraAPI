from flask import blueprints, request, jsonify
from GeraTicketAPI.GeraTicketClasses import TicketGenerator

GeraTicket_blueprint = blueprints.Blueprint('GeraTicket_blueprint', __name__)


@GeraTicket_blueprint.route("/")
def show_welcome_page():
    welcome_text = """
    <H2>CalculadoraAPI</H2>
    <H4>O que é?</H4>
    <p>Uma API simples que funcionará como prova de conceito 
    da utilização de Flask na prototipagem rápida de web APIs.
    </p>
    <H4>Vamos usar!</H4>
    """
    return welcome_text


@GeraTicket_blueprint.route('/calculate', methods=['POST'])
def process_calculation_request():
    tickgen = TicketGenerator(request.json)
    result = tickgen.process()
    return jsonify(result)
