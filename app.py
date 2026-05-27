from flask import Flask, render_template, request
from API.University_api import search_universities
from Database.database import add_to_favorites, get_favorites

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

@app.route("/favorite", methods=["POST"])
def favorite():

    name = request.form["name"]
    country = request.form["country"]
    website = request.form["website"]

    add_to_favorites(name, country, website)

    return f"{name} added to favorites!"

@app.route("/favorites")
def favorites():

    favorites_list = get_favorites()

    return render_template(
        "favorites.html",
        favorites=favorites_list
    )

if __name__ == "__main__":
    app.run(debug=True)