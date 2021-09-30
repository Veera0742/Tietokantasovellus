from db import db

def get_all_places():
    sql = "SELECT id, name FROM places ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_place_info(place_id):
    sql = "SELECT name, description FROM places WHERE places.id=:place_id"
    return db.session.execute(sql, {"place_id": place_id}).fetchone()

def get_reviews(place_id):
    sql = """SELECT u.username, r.stars, r.comment FROM reviews r, users u
             WHERE r.user_id=u.id AND r.place_id=:place_id ORDER BY r.id"""
    return db.session.execute(sql, {"place_id": place_id}).fetchall()

def add_review(user_id, place_id, stars, comment):
    sql = "INSERT INTO reviews (user_id, place_id, stars, comment) VALUES (:user_id, :place_id, :stars, :comment)"
    db.session.execute(sql, {"user_id":user_id, "place_id":place_id, "stars":stars, "comment":comment})
    db.session.commit()

def add_place(name, description):
    sql = "INSERT INTO places (name, description) VALUES (:name, :description) RETURNING id"
    place_id = db.session.execute(sql, {"name":name, "description":description}).fetchone()[0]
    db.session.commit()
    return place_id