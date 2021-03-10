from dao.Model import session, User


def save(user):
    session.add(user)
    session.commit()

def load():
    return session.query(User)