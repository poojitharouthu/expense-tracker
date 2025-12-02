from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# simple in-memory list – clears every time you restart Python
expenses = []


@app.route("/")
def index():
    return render_template("index.html", expenses=expenses)


@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form.get("title", "").strip()
    amount_raw = request.form.get("amount", "").strip()

    if title and amount_raw:
        try:
            amount = float(amount_raw)
        except ValueError:
            amount = 0.0

        expenses.append({"title": title, "amount": amount})

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

