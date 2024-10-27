from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])  # авторизация
def login():
    if request.method == 'GET':
        return 'GET'
    elif request.method == 'POST':
        return 'POST'


@app.route('/register', methods=['GET', 'POST'])  # регистрация
def register():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/logout', methods=['GET', 'POST'])  # выйти с учетной записи
def logout():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'DELETE':
        return 'DELETE'


@app.route('/profile', methods=['GET', 'PUT', 'PATCH', 'DELETE'])  # страница моего акаунта
def profil():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'PUT':
        return 'PUT'
    if request.method == 'PATCH':
        return 'PATCH'
    if request.method == 'DELETE':
        return 'DELETE'


@app.route('/profile/favourites', methods=['GET', 'POST', 'PATCH', 'DELETE'])  # страница избраных предложений
def favourites():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'
    if request.method == 'PATCH':
        return 'PATCH'
    if request.method == 'DELETE':
        return 'DELETE'


@app.route('/profile/favourites/<favourite_id>',
           methods=['GET', 'DELETE'])  # страница избраного конкретного предложения
def favourites(favourite_id):
    if request.method == 'GET':
        return f'GET {favourite_id}'
    if request.method == 'DELETE':
        return f'DELETE {favourite_id}'


@app.route('/profile/me_contracts', methods=['GET', 'POST'])  # список моих контрактов
def me_contracts():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/profile/me_contracts/<me_contract_id>', methods=['GET', 'PATCH'])  # страница конкретного моего контракта
def me_contracts(me_contract_id):
    if request.method == 'GET':
        return f'GET {me_contract_id}'
    if request.method == 'PATCH':
        return f'DELETE {me_contract_id}'


@app.route('/profile/search_history', methods=['GET', 'DELETE'])  # история поиска
def search_history():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'DELETE':
        return 'DELETE'


@app.route('/items', methods=['GET', 'POST'])  # список предложений вещей
def items():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/items/<item_id>', methods=['GET', 'POST'])  # конкретная вещь
def items(item_id):
    if request.method == 'GET':
        return f'GET {item_id}'
    if request.method == 'DELETE':
        return f'DELETE {item_id}'


@app.route('/leasers', methods=['GET'])  # страница всех других пользователей
def leasers():
    if request.method == 'GET':
        return f'GET'


@app.route('/leasers/<leaser_id>', methods=['GET'])  # страница пользователя
def leasers(leaser_id):
    if request.method == 'GET':
        return f'GET {leaser_id}'


@app.route('/leasers/<leasers_id>/leaser_contracts',
           methods=['GET', 'POST'])  # список контрактов выбраного пользователя
def leaser_contracts():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('leasers/<leasers_id>/leaser_contracts/<leaser_contract_id>',
           methods=['GET', 'PATCH'])  # страница конкретного контракта арендодателя
def leaser_contracts(leaser_contract_id):
    if request.method == 'GET':
        return f'GET {leaser_contract_id}'
    if request.method == 'PATCH':
        return f'DELETE {leaser_contract_id}'


@app.route('/search', methods=['GET', 'POST'])  # поиск
def search():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'POST':
        return 'POST'


@app.route('/complain', methods=['GET', 'POST'])  # пожаловаться
def complain():
    if request.method == 'POST':
        return 'POST'


@app.route('/compare', methods=['GET', 'PATCH'])  # сравнение
def compare():
    if request.method == 'GET':
        return 'GET'
    if request.method == 'PATCH':
        return 'PATCH'
