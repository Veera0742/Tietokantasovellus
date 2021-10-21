from app import app
from flask import redirect, render_template, request, session
import users
import places

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Hups! Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Hups! Salasanat eroavat")

        role = request.form["role"]
        if role not in ("1", "2"):
            return render_template("error.html", message="Tuntematon käyttäjärooli")

        if users.register(username, password1, role):
            return redirect("/")
        else:
            return render_template("error.html", message="Hups! Rekisteröinti epäonnistui")

@app.route("/mainpage", methods=["GET", "POST"])
def mainpage():
    return render_template("mainpage.html", places=places.get_all_places())

@app.route("/locations", methods=["GET", "POST"])
def locations():
    return render_template("locations.html", locations=places.get_all_locations())

@app.route("/groups", methods=["GET", "POST"])
def groups():
    return render_template("groups.html", groups=places.get_all_groups())

@app.route("/reviews", methods=["GET", "POST"])
def reviews():
    return render_template("reviews.html", places=places.get_all_reviews())    
    
@app.route("/locations/<int:location_id>")
def show_place_in_location(location_id):
    places_in_locations=places.places_in_locations(location_id)

    return render_template("places_in_locations.html", places_in_locations=places_in_locations)

@app.route("/groups/<int:group_id>")
def show_place_in_groups(group_id):
    places_by_groups=places.places_by_groups(group_id)

    return render_template("places_by_groups.html", places_by_groups=places_by_groups)

@app.route("/places/<int:place_id>")
def show_place(place_id):
    info = places.get_place_info(place_id)
    print(info)

    reviews = places.get_reviews(place_id)

    return render_template("place.html", id=place_id, name=info[0], description=info[1], reviews=reviews)
      

@app.route("/review", methods=["post"])
def review():

    users.require_role(1)

    place_id = request.form["place_id"]

    stars = int(request.form["stars"])
    if stars < 1 or stars > 5:
        return render_template("error.html", message="Virheellinen tähtimäärä")

    comment = request.form["comment"]
    if len(comment) > 1000:
        return render_template("error.html", message="Kommentti on liian pitkä")
    if comment == "":
        comment = "-"

    places.add_review(users.user_id(), place_id, stars, comment)

    return redirect("/places/"+str(place_id))    

@app.route("/add", methods=["get", "post"])
def add_place():
    users.require_role(2)

    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":

        name = request.form["name"]
        if len(name) < 1 or len(name) > 50:
            return render_template("error.html", message="Hups! Nimi on väärän pituinen")

        description = request.form["description"]
        if len(description) > 100000:
            return render_template("error.html", message="Hups! Kuvaus ei mahdu")

        location_id = request.form["location_id"]

        group_id = request.form["group_id"]
        
        service_id = request.form["service_id"]

        place_id=places.add_place(name, description, location_id, service_id, group_id)

        return redirect("/places/"+str(place_id))  

@app.route("/remove", methods=["get", "post"])
def remove_place():
    users.require_role(2)

    if request.method == "GET":
        all_places = places.get_remove_places(users.user_id())
        return render_template("remove.html", list=all_places)

    if request.method == "POST":
        users.check_csrf()

        if "place" in request.form:
            place = request.form["place"]
            places.remove_place(place)

        return redirect("/")

@app.route("/services/<int:place_id>")
def show_services(place_id):
    return render_template("services.html", services=places.get_services(place_id))

@app.route("/result", methods=["GET"])
def result():
    query = request.args["query"]
    results = places.search_word(query)
    return render_template("result.html", places=results)

@app.route("/result_services", methods=["GET"])
def result_services():
    value = request.args["value"]
    results = places.search_word_services(value)
    return render_template("result.html", places=results)
