def solution(id_pw, db):
    for id, pw in db:
        if id == id_pw[0]:
            if pw == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

'''
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
'''