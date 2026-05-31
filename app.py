from flask import Flask, render_template, request
from API.University_api import (search_universities, search_universities_by_name)
from API.country_api import get_country_details
from maps.map import create_university_map
from Database.database import (add_to_favorites, get_favorites, remove_favorites, clear_all_favorites, 
                               record_search, get_search_history, remove_search, clear_search_history, init_db)


app = Flask(__name__) # Creates the Flask application ----> Starting the Website.
init_db() # Creates the database tables if they do not already exist.

@app.route("/", methods=["GET", "POST"]) # This is the homepage for when users open the link. 
def home():

    if request.method == "POST": # Checks if the form is submitted via POST method, which happens when the user submits a search query.

        search_type = request.form.get("search_type") # Retrieves the type of search (by country or by university name) from the form data submitted by the user
        print(request.form)

        if search_type == "country":

            country = request.form["country"]

            universities = search_universities(country) # Calls the HipoLabs Universities API.
            country_info = get_country_details(country) # Calls the REST Countries API.

            record_search(                              # Stores the search inside the Search History database.
                f"Country: {country}",      
                len(universities)
            )

            return render_template(                     # Sends the retrieved universities and country information to the index.html template for rendering the search results on the webpage.
                "index.html",
                universities=universities,
                searched_country=country,
                country_info=country_info
            )

        elif search_type == "name":     # Checks if the search type is "name", which means the user is searching for universities by their name rather than by country.

            name = request.form["name"]                 # Retrieves the university name from the form data submitted by the user.

            universities = search_universities_by_name(name) # Calls the HipoLabs Universities API to search for universities based on the provided name.

            record_search(                       # Stores the search inside the Search History database.
                f"University: {name}",          
                len(universities)
            )

            return render_template(             # Displays the matching universities.
                "index.html",
                universities=universities,
                searched_name=name
            )

    return render_template("index.html")



@app.route("/favorite", methods=["POST"]) # New button to handle saving a university to favorites
def favorite():         

    name = request.form["name"]         # Retrieves the university name from the form data submitted by the user.
    country = request.form["country"]   # Retrieves the country name from the form data submitted by the user.
    website = request.form["website"]   # Retrieves the university website from the form data submitted by the user.

    add_to_favorites(name, country, website) # Calls the function to add the university to the favorites database.

    return f"{name} added to favorites!"    # Returns a simple message confirming that the university has been added to favorites. This response can be used for debugging or to provide feedback to the user on the frontend.



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
def history():          # New button to display the search history

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


@app.route("/map")
def map_page():

    country = request.args.get("country")

    universities = search_universities(country)

    create_university_map(
        universities,
        country
    )

    return render_template(
        "map.html",
        country=country
    )


if __name__ == "__main__": # Run the Flask application in debug mode
    app.run(debug=True)