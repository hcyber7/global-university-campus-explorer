from flask import Flask, render_template, request
from API.University_api import search_universities
from Database.database import add_to_favorites, get_favorites, remove_favorites, clear_all_favorites

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # Main route to handle the home page and search functionality
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

@app.route("/favorite", methods=["POST"]) # New button to handle saving a university to favorites
def favorite():

    name = request.form["name"]
    country = request.form["country"]
    website = request.form["website"]

    add_to_favorites(name, country, website)

    return f"{name} added to favorites!"

@app.route("/favorites")  # New button to display the list of favorite universities
def favorites():

    favorites_list = get_favorites()

    return render_template(
        "favorites.html",
        favorites=favorites_list
    )

@app.route("/delete_favorite", methods=["POST"]) # New button to handle deletion of a favorite university individually
def delete_favorite():

    name = request.form["name"]

    remove_favorite(name)

    favorites_list = get_favorites()

    return render_template(
        "favorites.html",
        favorites=favorites_list
    )

@app.route("/clear_favorites", methods=["POST"]) # New button to clear all favorites
def clear_favorites():

    clear_all_favorites()

    return render_template(
        "favorites.html",
        favorites=[]
    )

if __name__ == "__main__": # Run the Flask application in debug mode
    app.run(debug=True)