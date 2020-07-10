from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def gra():
    if request.method == "GET":
        return render_template("index.html")
    else:
        min_num = int(request.form.get("min"))
        max_num = int(request.form.get("max"))
        user_answer = request.form.get("user_answer")
        guess = int(request.form.get("guess", 500))
        if user_answer == "Za duzo":
            max_num = guess
        elif user_answer == "Za malo":
            min_num = guess
        elif user_answer == "Wygrales":
            return render_template("win.html", guess=guess)
        guess = (max_num - min_num) // 2 + min_num
        return render_template("game.html", guess=guess, min=min_num, max=max_num)


if __name__ == "__main__":
    app.run(debug=True)
