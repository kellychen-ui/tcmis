from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>歡迎進入陳宜琳的網站首頁</h1>"
    link += "<a href=/mis>課程</a><hr>"
    link += "<a href=/today>今天日期</a><hr>"
    link += "<a href=/about>關於宜琳</a><hr>"
    link += "<a href=/welcome?u=宜琳&dep=靜宜資管>GET傳值</a><hr>"
    link += "<a href=/account>POST傳值(帳號密碼)</a><hr>"
    link += "<a href=/math>數學運算</a><hr>"
    return link

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year) #取得年份
    month = str(now.month) #取得月份
    day = str(now.day) #取得日期
    now = year + "/" + month + "/" + day
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
    return render_template("abou8-2.html")

@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route('/math', methods=['GET', 'POST'])
def math():
    Result = None
    error_msg = None
    x, y, opt = None, None, None

    if request.method == 'POST':
        try:
            # 從表單取得資料
            x = int(request.form.get('x'))
            y = int(request.form.get('y'))
            opt = request.form.get('opt')

            # 你的核心邏輯：判斷除數與運算
            if opt == "/" and y == 0:
                error_msg = "錯誤：除數不能為 0"
            else:
                match opt:
                    case "+": Result = x + y
                    case "-": Result = x - y
                    case "*": Result = x * y
                    case "/": Result = x / y
                    case "%": Result = x % y
                    case _: error_msg = f"錯誤：不支援的符號 '{opt}'"
        except (ValueError, TypeError):
            error_msg = "請輸入有效的數字"

    return render_template('math.html', Result=Result, error_msg=error_msg, x=x, y=y, opt=opt)
        
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


