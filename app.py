from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return 'Hello Flask!'

# @app.route('/game/3')
# def game3():
#     return 'The witcher 3: Wild Hunt'

@app.route('/game/<game_number>')
def games(game_number):
    return f'The witcher {game_number}'

# @app.route('/game/<game_number>/<pack_number>')
# def expansion_pack(game_number, pack_number):
#     return f'The witcher {game_number}: add-on {pack_number}'

@app.route('/game/<int:game_number>/<pack_number>')
def expansion_pack(game_number, pack_number):
    return f'The witcher {game_number}: add-on {pack_number}'

#Задание1
@app.route('/about')
def about():
    return f'Разработчик этого сайта Айтигеник'

#Задание2
#Пример, задание может быть выполнено по разному
@app.route('/task2/<name>/<int:age>')
def expansion_pack(name, age):
    return f'Привет {name} тебе и правда {age} лет?'