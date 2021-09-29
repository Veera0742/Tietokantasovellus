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
            return redirect("/mainpage")
        else:
            return render_template("error.html", message="Hups! Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    del session["username"]
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
    #users.check_csrf()

    if request.method == "GET":
        return render_template("add.html")

    if request.method == "POST":
        #users.check_csrf()

        name = request.form["name"]
        if len(name) < 1 or len(name) > 20:
            return render_template("error.html", message="Nimessä tulee olla 1-20 merkkiä")

        description = request.form["description"]
        if len(description) > 10000:
            return render_template("error.html", message="Sanalista on liian pitkä")

        place_id = places.add_place(name, description)
        return redirect("/places/"+str(place_id))           