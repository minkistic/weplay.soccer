# 메모장을 위한 서버를 만드는 과정입니다.
# 서버시작: mongod --dbpath ~/data/db

# HTML을 주는 API: 기본 실행
# HTML을 주는 API: HTML 파일 불러오기 -> render_template

import os
from flask import Flask, render_template, jsonify, request, send_from_directory

from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbgamestat  # 'dbsparta'라는 이름의 db를 만듭니다.

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/gamestats')
def gamestat():
    return render_template('shoot_record2.html')


@app.route('/gamestat', methods=['POST'])
def event_post():
    #  db에 저장한다.
    # print(11111)
    try:  # 이걸 시도해봐 우선
        eventType = request.form['eventType']
        team = request.form['team']
        score = request.form['score']
        shoot = request.form['shoot']
        playType = request.form['playType']
        shootMethod = request.form['shootMethod']
        errorOpponent = request.form['errorOpponent']
        setpiece = request.form['setpiece']
        scorePlayer = request.form['scorePlayer']
        scoreArea = request.form['scoreArea']
        assistPlayer = request.form['assistPlayer']
        assistArea = request.form['assistArea']



        # 4. 그래서 그걸로 doc 을 만들자
        doc = {
            'eventType': eventType,
            'team': team,
            'score': score,
            'shoot': shoot,
            'playType': playType,
            'shootMethod': shootMethod,
            'errorOpponent': errorOpponent,
            'setpiece': setpiece,
            'scorePlayer': scorePlayer,
            'scoreArea': scoreArea,
            'assistPlayer': assistPlayer,
            'assistArea': assistArea,

        }
        db.gamestat.insert_one(doc)
    except:  # 시도한게 안되면 이걸해
        return jsonify({'result': 'fail', 'msg': '이 요청은 POST!'})

    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/gamestat', methods=['GET'])
def event_get():
    # db에서 읽어온다.
    gamestats = list(db.gamestat.find({},{'_id':0}))  # db.bookmarks에서 가져와서 리스트로 만들어라,자동으로 들어가는 _id는 가져오지마라 제이슨으로 못만드니깐
    return jsonify(gamestats)  # 제이슨 형식으로 만들어라



# 매치 오버뷰치
@app.route('/matchoverviews')
def match_overview():
    return render_template('Game-MatchOverview.html')

@app.route('/matchoverview', methods=['GET'])
def eventData_get():
    # db에서 읽어온다.
    gamestats = list(db.gamestat.find({},{'_id':False}))  # db.bookmarks에서 가져와서 리스트로 만들어라,자동으로 들어가는 _id는 가져오지마라 제이슨으로 못만드니깐
    return jsonify(gamestats)  # 제이슨 형식으로 만들어라



# 팀관리
@app.route('/teammanagements')
def team_management():
    return render_template('team_manage.html')


@app.route('/teammanagement', methods=['POST'])
def teamlist_post():
    #  db에 저장한다.
    # print(11111)
    try:  # 이걸 시도해봐 우선
        PlayerNumber: request.form['PlayerNumber']
        PlayerName: request.form['PlayerName']

        # 4. 그래서 그걸로 doc 을 만들자
        doc = {
            'PlayerNumber': PlayerNumber,
            'PlayerName': PlayerName,

        }
        db.teammanagement.insert_one(doc)
    except:  # 시도한게 안되면 이걸해
        return jsonify({'result': 'fail', 'msg': '이 요청은 POST!'})

    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/teammanagement', methods=['GET'])
def teamlist_get():
    # db에서 읽어온다.
    teamlist = list(db.teammanagement.find({},{'_id':0}))  # db.bookmarks에서 가져와서 리스트로 만들어라,자동으로 들어가는 _id는 가져오지마라 제이슨으로 못만드니깐
    return jsonify(teamlist)  # 제이슨 형식으로 만들어라


# 선수선택화
# @app.route('/playerList')
# def player_list():
#     return render_template('player_list.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
