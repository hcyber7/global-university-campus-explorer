from flask import Flask, render_template, request
from API.University_api import search_universities, search_universities_by_name
from Database.database import add_to_favorites, get_favorites, remove_favorites, clear_all_favorites, record_search, get_search_history, remove_search, clear_search_history, init_db


app = Flask(__name__)
init_db() # Initialize the database when the application starts

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        search_type = request.form["search_type"]

        if search_type == "country":

            country = request.form["country"]

            universities = search_universities(country)

            record_search(
                f"Country: {country}",
                len(universities)
            )

            return render_template(
                "index.html",
                universities=universities,
                searched_country=country
            )

        elif search_type == "name":

            name = request.form["name"]

            universities = search_universities_by_name(name)

            record_search(
                f"University: {name}",
                len(universities)
            )

            return render_template(
                "index.html",
                universities=universities,
                searched_name=name
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

    remove_favorites(name)

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


@app.route("/history")
def history():

    history_list = get_search_history()

    return render_template(
        "history.html",
        history=history_list
    )


@app.route("/delete_history", methods=["POST"])
def delete_history():

    search_id = request.form["id"]

    remove_search(search_id)

    history_list = get_search_history()

    return render_template(
        "history.html",
        history=history_list
    )

@app.route("/clear_history", methods=["POST"])
def clear_history():

    clear_search_history()

    return render_template(
        "history.html",
        history=[]
    )

if __name__ == "__main__": # Run the Flask application in debug mode
    app.run(debug=True)