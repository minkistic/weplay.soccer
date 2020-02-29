# 메모장을 위한 서버를 만드는 과정입니다.
# 서버시작: mongod --dbpath ~/data/db

# HTML을 주는 API: 기본 실행
# HTML을 주는 API: HTML 파일 불러오기 -> render_template

import os
from flask import Flask, render_template, jsonify, request, send_from_directory

from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbteaminfo

app = Flask(__name__)

players = client.dbteaminfo.players
players.insert_one({'playername':'bobby','number':100})