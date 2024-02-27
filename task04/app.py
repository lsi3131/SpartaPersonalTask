import os
import sys
import flask
import random

from flask import Flask, render_template, request
from datetime import datetime

from task04.core.definitions import *
from task04.core.service import GameService
from task04.core.sqlalchemy_repo import create_sqlalchemy_sqlite, SQLAlchemyGameResultRepository

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_wrapper = create_sqlalchemy_sqlite(app, basedir, 'database.db')

rcp_image_url_table = {
    RCP_TYPE_ROCK: "../static/image/rcp_rock.png",
    RCP_TYPE_SCISSOR: "../static/image/rcp_scissor.png",
    RCP_TYPE_PAPER: "../static/image/rcp_paper.png",
}

repo = SQLAlchemyGameResultRepository(db_wrapper)
service = GameService(repo)
g_language = LANGUAGE_TYPE_KOR


@app.route('/')
def home():
    context = {}
    return render_template('index.html', data=context)


@app.route('/fight/<rcp_type>')
def fight(rcp_type):
    user_choice = int(rcp_type)
    computer_choice = random.choice(
        [RCP_TYPE_ROCK, RCP_TYPE_SCISSOR, RCP_TYPE_PAPER])

    result = service.fight(user_choice, computer_choice, datetime.now())

    context = {
        "computer_rcp_image_url": rcp_image_url_table[result.computer],
        "computer_text": to_string_rcp(result.computer, language=g_language),
        "user_rcp_image_url": rcp_image_url_table[result.user],
        "user_text": to_string_rcp(result.user, language=g_language),
        "game_result": to_string_game_result(result.result, language=g_language)
    }

    print(result)

    return render_template('index.html', data=context)


@app.route('/fight_rock')
def fight_rock():
    return flask.redirect(flask.url_for('fight', rcp_type=RCP_TYPE_ROCK))


@app.route('/fight_scissor')
def fight_scissor():
    return flask.redirect(flask.url_for('fight', rcp_type=RCP_TYPE_SCISSOR))


@app.route('/fight_paper')
def fight_paper():
    return flask.redirect(flask.url_for('fight', rcp_type=RCP_TYPE_PAPER))


@app.route('/record', methods=['GET'])
def record():

    max_count = 100

    check_filter_win = request.args.get('filter_win')
    check_filter_lose = request.args.get('filter_lose')
    check_filter_draw = request.args.get('filter_draw')

    is_win = check_filter_win == '1'
    is_lose = check_filter_lose == '1'
    is_draw = check_filter_draw == '1'

    print(f'check_filter_win={check_filter_win} check_filter_lose={check_filter_lose}, check_filter_draw={check_filter_draw}')
    print(f'win={is_win} lose={is_lose}, draw={is_draw}')

    filter_results = [GAME_RESULT_WIN, GAME_RESULT_LOSE, GAME_RESULT_DRAW]
    if not is_win:
        filter_results.remove(GAME_RESULT_WIN)
    if not is_lose:
        filter_results.remove(GAME_RESULT_LOSE)
    if not is_draw:
        filter_results.remove(GAME_RESULT_DRAW)

    context = []
    for i, game_record in enumerate(service.find_game_records(reverse=True, sort_option='game_datetime', max_count=max_count,
                                                              filtered_result=filter_results)):
        context.append({
            "num": game_record.id,
            "computer": to_string_rcp(game_record.computer, g_language),
            "user": to_string_rcp(game_record.user, g_language),
            "result": to_string_game_result(game_record.result, g_language),
            "datetime": game_record.game_datetime.strftime("%Y-%m-%d %H:%M:%S")
        })
    return render_template('record.html', records=context)


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        print(f'port = {sys.argv[1]}')
        app.run(debug=True, port=sys.argv[1])
    else:
        app.run(debug=True, port=5001)
