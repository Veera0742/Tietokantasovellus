from db import db

def get_all_places():
    sql = "SELECT id, name FROM places ORDER BY name"
    return db.session.execute(sql).fetchall()

