from flask import jsonify
from DBService import *
from config import *

app = Flask(__name__)
#setup session
SESSION_TYPE = 'redis'
app.secret_key = 'super secret key'
app.config.from_object(__name__)
# Session(app)

@app.route("/login",methods = ['GET','POST'])
def login():
    if request.method == "GET":
        return "ping success"
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username,password)
        password = hashlib.md5(password.encode()).hexdigest()
        account = UserService(db_file)
        check = account.LoginTask(username,password)
        if check == 0:
            return jsonify({"status": "0"})
        else:
            account_data = account.getInfor()
            session["user_info"] = account_data
            res = {"userid":account_data[0][0],
                    "name":account_data[0][1],
                    "dob":account_data[0][2],
                    "score":account_data[0][3]
            }
            return jsonify(res)
        # return jsonify({"uname":username,"password":password})
@app.route("/updateScore",methods =["POST"])
def update():
    if request.method == "POST":
        uid = request.form["uid"]
        score = request.form["score"]
        account = UserService(db_file)
        account.update(score,uid)
        return jsonify({"status":"update success"})
app.run(host = "0.0.0.0",port = 80)
        

