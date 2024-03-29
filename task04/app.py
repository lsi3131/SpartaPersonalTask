import os
import sys
import flask
import random

from flask import Flask, render_template, request
from datetime import datetime

from task04.core.config import AppConfig
from task04.core.definitions import *

config = AppConfig(app_name=__name__, basedir_path=os.path.abspath(os.path.dirname(__file__)), db_name='database.db')
app = config.app
service = config.get_game_result_service()

rcp_image_url_table = {
    RCP_TYPE_ROCK: "../static/image/rcp_rock.png",
    RCP_TYPE_SCISSOR: "../static/image/rcp_scissor.png",
    RCP_TYPE_PAPER: "../static/image/rcp_paper.png",
}

g_language = LANGUAGE_TYPE_KOR


@app.route('/')
def home():
    context = {}
    return render_template('index.html', data=context)


@app.route('/fight', methods=["POST"])
def fight():
    rock = request.form.get('rock')
    scissor = request.form.get('scissor')
    paper = request.form.get('paper')

    # rock = request.args.get('rock')
    # scissor = request.args.get('scissor')
    # paper = request.args.get('paper')

    print(f'rock={rock}, scissor={scissor}, paper={paper}')

    if rock:
        user_choice = RCP_TYPE_ROCK
    elif scissor:
        user_choice = RCP_TYPE_SCISSOR
    elif paper:
        user_choice = RCP_TYPE_PAPER
    else:
        print(f'invalid type has come. rock,scissor,paper are none')
        return render_template('index.html', data={})

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

    return render_template('index.html', data=context)


@app.route('/record', methods=['GET'])
def record():
    check_filter_win = request.args.get('filter_win')
    check_filter_lose = request.args.get('filter_lose')
    check_filter_draw = request.args.get('filter_draw')
    max_count = request.args.get('number_of_results',default=0)
    max_count = int(max_count)

    is_win = check_filter_win == '1'
    is_lose = check_filter_lose == '1'
    is_draw = check_filter_draw == '1'

    print(
        f'check_filter_win={check_filter_win} check_filter_lose={check_filter_lose}, check_filter_draw={check_filter_draw}')
    print(f'win={is_win} lose={is_lose}, draw={is_draw}')

    filter_results = [GAME_RESULT_WIN, GAME_RESULT_LOSE, GAME_RESULT_DRAW]
    if not is_win:
        filter_results.remove(GAME_RESULT_WIN)
    if not is_lose:
        filter_results.remove(GAME_RESULT_LOSE)
    if not is_draw:
        filter_results.remove(GAME_RESULT_DRAW)

    context = []
    for i, game_record in enumerate(
            service.find_game_records(reverse=True, sort_option='game_datetime', max_count=max_count,
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
