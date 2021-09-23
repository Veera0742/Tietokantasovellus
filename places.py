from db import db

def get_all_places():
    sql = "SELECT id, name FROM places ORDER BY name"
    return db.session.execute(sql).fetchall()

def get_place_info(place_id):
    sql = """SELECT name, description FROM places WHERE places.id=:place_id"""
    return db.session.execute(sql, {"place_id": place_id}).fetchone()