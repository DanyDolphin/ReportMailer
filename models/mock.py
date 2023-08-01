# Models
from models import User, Transaction


def get_test_data():
    user = User(
        email="danielcastillo59814@gmail.com",
        name="Fernando Daniel Castillo Barrón",)

    t1 = Transaction(email=user.email, date="7/15", transaction=60.5)
    t2 = Transaction(email=user.email, date="7/28", transaction=-10.3)
    t3 = Transaction(email=user.email, date="8/12", transaction=-20.46)
    t4 = Transaction(email=user.email, date="8/13", transaction=10)

    return [user, t1, t2, t3, t4]
