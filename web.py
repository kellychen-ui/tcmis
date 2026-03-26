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
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
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
        # 使用 f-string 讓字串拼接更乾淨
        result = f"您輸入的帳號是：{user}；密碼為：{pwd}" 
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


