import psycopg2
import json

with open("db/db.json") as read_json:
    properties = json.load(read_json)["db"]

CONN = conn = psycopg2.connect(properties)


def check_user(username: str, password: str) -> dict:
    """
    :param data: dict that contains username and password
    :return: dict {id: int, correct: True/False}
    """
    cursor = CONN.cursor()

    cursor.execute("""
    SELECT password, id FROM auth
    WHERE username = %s
    """, (username,))
    fetched = cursor.fetchall()[0]
    if fetched[0].strip() == password:
        return {"id": fetched[1],
                "correct": True}


def register(username, password):
    cursor = CONN.cursor()

    cursor.execute("""
       SELECT id FROM auth
       WHERE username = %s
       """, (username,))

    fetched = cursor.fetchall()

    if fetched:
        cursor.close()
        return False

    cursor.execute("""
       INSERT INTO auth (username, password)
       values (%s, %s)
       """, (username, password,))

    cursor.execute("""
           SELECT id FROM auth
           WHERE username = %s
           """, (username,))

    user_id = cursor.fetchall()[0][0]

    cursor.execute("""
           INSERT INTO food (id, food)
           values (%s, %s)
           """, (user_id, json.dumps({"food": []})))

    cursor.execute("""
               INSERT INTO trains (id, trains)
               values (%s, %s)
                """, (user_id, json.dumps({"trains": []})))

    CONN.commit()
    cursor.close()
    return {"id": user_id}


def change_password(username, password):
    cursor = CONN.cursor()

    cursor.execute("""
          SELECT id FROM auth
          WHERE username = %s
          """, (username,))

    fetched = cursor.fetchall()

    if not fetched:
        cursor.close()
        return False

    cursor.execute("""
          UPDATE auth 
          SET password = %s
          WHERE username = %s
          """, (password, username))

    CONN.commit()
    cursor.close()
    return True


def add_food(user_id, food):
    cursor = CONN.cursor()

    cursor.execute("""
              SELECT food FROM food
              WHERE id = %s
              """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_food = fetched[0][0]
        old_food["food"].append(food)
        cursor.execute("""
                  UPDATE food 
                  SET food = %s
                  WHERE id = %s
                  """, (json.dumps(old_food), user_id))
        CONN.commit()
        cursor.close()
        return True
    cursor.close()
    return False

def remove_food(user_id, food):
    cursor = CONN.cursor()

    cursor.execute("""
              SELECT food FROM food
              WHERE id = %s
              """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_food = fetched[0][0]
        old_food["food"].remove(food)
        cursor.execute("""
                  UPDATE food 
                  SET food = %s
                  WHERE id = %s
                  """, (json.dumps(old_food), user_id))
        CONN.commit()
        cursor.close()
        return True
    cursor.close()
    return False


def add_train(user_id, train):
    cursor = CONN.cursor()

    cursor.execute("""
                  SELECT trains FROM trains
                  WHERE id = %s
                  """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_trains = fetched[0][0]
        old_trains["trains"].append(train)
        cursor.execute("""
                      UPDATE trains 
                      SET trains = %s
                      WHERE id = %s
                      """, (json.dumps(old_trains), user_id))
        CONN.commit()
        cursor.close()
        return True
    cursor.close()
    return False

def remove_train(user_id, train):
    cursor = CONN.cursor()

    cursor.execute("""
                  SELECT trains FROM trains
                  WHERE id = %s
                  """, (user_id,))

    fetched = cursor.fetchall()
    if fetched:
        old_trains = fetched[0][0]
        old_trains["trains"].remove(train)
        cursor.execute("""
                      UPDATE trains 
                      SET trains = %s
                      WHERE id = %s
                      """, (json.dumps(old_trains), user_id))
        CONN.commit()
        cursor.close()
        return True
    cursor.close()
    return False

def get_trains(user_id):
    cursor = CONN.cursor()

    cursor.execute("""
                      SELECT trains FROM trains
                      WHERE id = %s
                      """, (user_id,))

    fetched = cursor.fetchall()

    if fetched:
        return fetched[0][0]["trains"]

def get_food(user_id):
    cursor = CONN.cursor()

    cursor.execute("""
                      SELECT food FROM food
                      WHERE id = %s
                      """, (user_id,))

    fetched = cursor.fetchall()

    if fetched:
        return fetched[0][0]["food"]
