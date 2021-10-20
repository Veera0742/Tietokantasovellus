from db import db

def get_all_places():
    sql = "SELECT id, name FROM places WHERE visible=1 ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_all_locations():
    sql = "SELECT id, name FROM locations ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_all_groups():
    sql = "SELECT id, name FROM groups ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_place_info(place_id):
    sql = "SELECT name, description FROM places WHERE places.id=:place_id"
    return db.session.execute(sql, {"place_id": place_id}).fetchone()

def get_location_info(place_id):
    sql = "SELECT name, description FROM locations WHERE place_id=:place_id"
    return db.session.execute(sql, {"place_id": place_id}).fetchone()

def get_reviews(place_id):
    sql = """SELECT u.username, r.stars, r.comment FROM reviews r, users u
             WHERE r.user_id=u.id AND r.place_id=:place_id ORDER BY r.id"""
    return db.session.execute(sql, {"place_id": place_id}).fetchall()

def places_in_locations(location_id):
    sql = "SELECT id, name FROM places WHERE location_id=:location_id"
    return db.session.execute(sql, {"location_id": location_id}).fetchall()

def places_by_groups(group_id):
    sql = "SELECT id, name FROM places WHERE group_id=:group_id"
    return db.session.execute(sql, {"group_id": group_id}).fetchall()

def add_review(user_id, place_id, stars, comment):
    sql = """INSERT INTO reviews (user_id, place_id, stars, comment) 
        VALUES (:user_id, :place_id, :stars, :comment)"""
    db.session.execute(sql, {"user_id":user_id, "place_id":place_id, "stars":stars, "comment":comment})
    db.session.commit()

def add_place(name, description, location_id, service_id, group_id):
    sql = """INSERT INTO places (name, description, visible, location_id) 
        VALUES (:name, :description, 1, :location_id) RETURNING id"""
    place_id = db.session.execute(sql, {"name":name, "description":description, "location_id":location_id}).fetchone()[0]
    
    for service_id in service_id:
        sql = "INSERT INTO service_relations (place_id, service_id) VALUES (:place_id, :service_id)"
        db.session.execute(sql, {"place_id":place_id, "service_id":service_id})

    for group_id in group_id:
        sql = "INSERT INTO group_relations (place_id, group_id) VALUES (:place_id, :group_id)"
        db.session.execute(sql, {"place_id":place_id, "group_id":group_id})

    db.session.commit()
    return place_id

def get_remove_places(user_id):
    sql = "SELECT id, name FROM places ORDER BY name"
    return db.session.execute(sql, {"user_id":user_id}).fetchall()

def remove_place(place_id):
    sql = "UPDATE places SET visible=0 WHERE id=:id"
    db.session.execute(sql, {"id":place_id})
    db.session.commit()

def get_services(place_id):
    sql = "SELECT s.service FROM services s, service_relations sr WHERE sr.service_id=s.id AND sr.place_id=:place_id"
    return db.session.execute(sql, {"place_id":place_id}).fetchall()

def get_all_reviews():
    sql = """SELECT p.id, p.name FROM reviews r, places p
            WHERE r.place_id=p.id ORDER BY r.stars DESC LIMIT 5"""
    return db.session.execute(sql).fetchall()

def search_word(query):
    sql = "SELECT id, name, description FROM places WHERE visible=1 AND description LIKE :query"
    return db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()

def search_word_services(value):
    sql = """SELECT p.id, p.name, s.service FROM places p, services s 
            WHERE p.visible=1 AND s.place_id=p.id AND s.service.id=value"""
    return db.session.execute(sql, {"query":"%"+value+"%"}).fetchall()