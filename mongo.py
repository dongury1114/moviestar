from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbaws                     # 'dbsparta'라는 이름의 db를 만듭니다.


db.users.update_one({'name': 'bobby'}, {'$set': {'_id': False})

user = db.users.find_one({'name': 'bobby'}, {'_id': False})
