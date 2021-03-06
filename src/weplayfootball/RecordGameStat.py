
# 서버시작: mongod --dbpath ~/data/db

# HTML을 주는 API: 기본 실행
# HTML을 주는 API: HTML 파일 불러오기 -> render_template

import os
from flask import Flask, render_template, jsonify, request, send_from_directory

from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbgamestat  # 'dbsparta'라는 이름의 db를 만듭니다.
#
teaminfo = client.dbteaminfo


app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/recordevent')
def gamestat():
    return render_template('record_event.html')

@app.route('/gamestat', methods=['POST'])
def event_post():
    #  db에 저장한다.
    print(11111)
    try:  # 이걸 시도해봐 우선
        eventTime = request.form['eventTime']
        eventType = request.form['eventType']
        team = request.form['team']

        score = request.form['score']
        playType = request.form['playType']
        scorePlayer = request.form['scorePlayer']
        scoreArea = request.form['scoreArea']
        shootMethod = request.form['shootMethod']
        assistPlayer = request.form['assistPlayer']
        assistArea = request.form['assistArea']
        errorOpponent = request.form['errorOpponent']
        setpiece = request.form['setpiece']
        bulidupPlayer = request.form['bulidupPlayer']
        buildupArea = request.form['buildupArea']

        shoot = request.form['shoot']
        shootPlayType = request.form['shootPlayType']
        shootPlayer = request.form['shootPlayer']
        shootArea = request.form['shootArea']
        shootshootMethod = request.form['shootshootMethod']
        keypassPlayer = request.form['keypassPlayer']
        keypassArea = request.form['keypassArea']
        shooterrorOpponent = request.form['shooterrorOpponent']
        shootsetpiece = request.form['shootsetpiece']
        shootBuildupPlayer = request.form['shootBuildupPlayer']
        shootBuildupArea = request.form['shootBuildupArea']

        cornerkick = request.form['cornerkick']
        kicker = request.form['kicker']

        offsidePlayer = request.form['offsidePlayer']
        offsideArea = request.form['offsideArea']
        badCallOffside = request.form['badCallOffside']

        foulPlayer = request.form['foulPlayer']
        foulArea = request.form['foulArea']
        foulCard = request.form['foulCard']
        badCall = request.form['badCall']


        # 4. 그래서 그걸로 doc 을 만들자
        doc = {
            'eventTime': eventTime,
            'eventType': eventType,
            'team': team,
            'score': score,
            'shoot': shoot,

            'playType': playType,
            'scorePlayer': scorePlayer,
            'scoreArea': scoreArea,
            'shootMethod': shootMethod,
            'assistPlayer': assistPlayer,
            'assistArea': assistArea,
            'errorOpponent': errorOpponent,
            'setpiece': setpiece,
            'bulidupPlayer': bulidupPlayer,
            'buildupArea': buildupArea,

            'shootPlayType': shootPlayType,
            'shootPlayer': shootPlayer,
            'shootArea': shootArea,
            'shootshootMethod': shootshootMethod,
            'keypassPlayer': keypassPlayer,
            'keypassArea': keypassArea,
            'shooterrorOpponent': shooterrorOpponent,
            'shootsetpiece': shootsetpiece,
            'shootBuildupPlayer': shootBuildupPlayer,
            'shootBuildupArea': shootBuildupArea,

            'cornerkick': cornerkick,
            'kicker': kicker,

            'offsidePlayer': offsidePlayer,
            'offsideArea': offsideArea,
            'badCallOffside': badCallOffside,

            'foulPlayer': foulPlayer,
            'foulArea': foulArea,
            'foulCard': foulCard,
            'badCall': badCall,

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



# 게임 오버뷰
@app.route('/gameoverviews')
def game_overview():
    return render_template('game_overview.html')

@app.route('/gameoverview', methods=['GET'])
def eventData_get():
    # db에서 읽어온다.
    gamestats = list(db.gamestat.find({},{'_id':False}))  # db.bookmarks에서 가져와서 리스트로 만들어라,자동으로 들어가는 _id는 가져오지마라 제이슨으로 못만드니깐
    return jsonify(gamestats)  # 제이슨 형식으로 만들어라



# # 팀관리
@app.route('/teammanagements')
def team_management():
    return render_template('team_manage.html')


@app.route('/teammanagement', methods=['POST'])
def teaminfo_post():
    #  db에 저장한다.
    # print(11111)
    try:  # 이걸 시도해봐 우선
        # teamname = request.form['teamname']
        # backnumber = request.form['PlayerNumber']
        # playername = request.form['PlayerName']
        playerlist = request.form['playerlist']

#

# .drop 으로 여기서 페이지 갱신 후 돌면서 다시 넣기
#
#        # 4. 그래서 그걸로 doc 을 만들자
#         doc = {
#             'teamname': teamname,
#             'backnumber': backnumber,
#             'playername': playername,
#
#         }
        doc = {
            playerlist : playerlist
        }
        teaminfo.teaminfo.insert_one(doc)
    except:  # 시도한게 안되면 이걸해
        return jsonify({'result': 'fail', 'msg': '이 요청은 POST!'})

    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})
#
#
@app.route('/teammanagement', methods=['GET'])
def teamlist_get():
    # db에서 읽어온다.
    teaminfo = list(db.teaminfo.find({},{'_id':0}))  # db.bookmarks에서 가져와서 리스트로 만들어라,자동으로 들어가는 _id는 가져오지마라 제이슨으로 못만드니깐
    return jsonify(teaminfo)  # 제이슨 형식으로 만들어라


# 선수선택화면
@app.route('/playerList')
def player_list():
    return render_template('player_list.html')

@app.route('/players', methods=['GET'])
def playerlist_get():
    # db에서 읽어온다.
    playerlist = list(db.players.find({},{'_id':False}))  # db.bookmarks에서 가져와서 리스트로 만들어라,자동으로 들어가는 _id는 가져오지마라 제이슨으로 못만드니깐
    return jsonify(playerlist)  # 제이슨 형식으로 만들어라


# 필드영역 선택기
@app.route('/fieldAreaSelection')
def fieldAreaSelection_get():
    return render_template('field_area_selection.html')

# 매치 리스트
@app.route('/matchlist')
def matchList_get():
    return render_template('matchList.html')

# 매치 오버뷰
@app.route('/matchoverviews')
def matchOverview_get():
    return render_template('match_overview.html')

# 매치 만들
@app.route('/makematch')
def makeMatch_get():
    return render_template('make_match.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
