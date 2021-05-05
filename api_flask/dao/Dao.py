from dao.Model import session, User


def save(user):
    session.add(user)
    session.commit()
    return user

def load():
    return session.query(User)