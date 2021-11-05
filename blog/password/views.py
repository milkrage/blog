from flask import Blueprint, request, jsonify, render_template
from flask.views import MethodView
from . import utils


class PasswordView(MethodView):
    def get(self):
        password_length = [length for length in range(8, 65, 4)]

        return render_template(
            'password/password.html',
            password_length=password_length
        )

    def post(self):
        query = request.get_json()

        if not isinstance(query, dict):
            return 'Bad Request', 400

        lowercase = utils.set_value(query, 'lowercase', True)
        uppercase = utils.set_value(query, 'uppercase', True)
        number = utils.set_value(query, 'number', True)
        symbol = utils.set_value(query, 'symbol', True)
        length = utils.set_value(query, 'length', 16, type=int, min=8, max=64)
        amount = utils.set_value(query, 'amount', 10, type=int)

        if not any([lowercase, uppercase, number, symbol]):
            return 'Needs at least 1 set parameter', 400

        return jsonify(
            utils.generator(
                lowercase=lowercase,
                uppercase=uppercase,
                number=number,
                symbol=symbol,
                length=length,
                amount=amount
            )
        )


password = Blueprint(
    name='password',
    import_name=__name__,
    url_prefix='/password',
    template_folder='templates',
    static_folder='static'
)

password.add_url_rule('/generate', view_func=PasswordView.as_view('generate'))
