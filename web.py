from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>陳宜琳Python網頁</h1>"
    homepage += "<a href='/mis'>MIS</a><br>"
    homepage += "<a href='/today'>顯示日期時間</a><br>"
    homepage += "<a href='/welcome?nick=tcyang'>傳送使用者暱稱</a><br>"
    homepage += "<a href='/account'>網頁表單傳值</a><br>"
    homepage += "<a href='/about'>宜琳簡介網頁</a><br>"
    # 新增計算機功能超連結
    homepage += "<a href='/calc'>網頁版計算機</a><br>" 
    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    year = str(now.year) # 取得年份
    month = str(now.month) # 取得月份
    day = str(now.day) # 取得日期
    now_str = year + "/" + month + "/" + day
    return render_template("today.html", datetime=now_str)

@app.route("/welcome")
def welcome():
    # 使用 request.args.get 來取得 URL 上的 GET 參數
    nick = request.args.get("nick", "訪客")
    return f"<h1>歡迎來到本站，{nick}！</h1>"

@app.route("/about")
def about():
    return render_template("abou8-2.html")

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "；密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")

@app.route("/calc", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        try:
            # 從網頁表單取得 x, y 與 opt
            x = int(request.form["x"])
            y = int(request.form["y"])
            opt = request.form["opt"]
            
            Result = None
            if opt == "/" and y == 0:
                return "<h3>錯誤：除數不能為 0</h3><a href='/calc'>回上一頁</a>"
            else:
                match opt:
                    case "+": Result = x + y
                    case "-": Result = x - y
                    case "*": Result = x * y
                    case "/": Result = x / y
                    case _: return f"<h3>錯誤：不支援的符號 '{opt}'</h3><a href='/calc'>回上一頁</a>"
            
            return f"<h3>{x} {opt} {y} 的結果是 {Result}</h3><a href='/calc'>繼續計算</a>"
            
        except ValueError:
            return "<h3>錯誤：請輸入有效的數字</h3><a href='/calc'>回上一頁</a>"
            
    else:
        # GET 請求時顯示計算機表單
        return '''
            <h2>網頁版計算機</h2>
            <form method="post">
                x：<input type="text" name="x" required><br><br>
                運算：
                <select name="opt">
                    <option value="+">+</option>
                    <option value="-">-</option>
                    <option value="*">*</option>
                    <option value="/">/</option>
                </select><br><br>
                y：<input type="text" name="y" required><br><br>
                <input type="submit" value="計算">
            </form>
            <br><a href="/">回首頁</a>
        '''

if __name__ == "__main__":
    app.run(debug=True)


