from flask import Flask, render_template, request
from API.University_api import search_universities

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        country = request.form["country"]

        universities = search_universities(country)

        return render_template(
            "index.html",
            universities=universities,
            searched_country=country
        )
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)