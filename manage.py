# Utils
import sys

# Models
from models import Base, engine
from models.mock import get_test_data

# SQLAlchemy
from sqlalchemy.orm import Session

if __name__ == '__main__':
    arg = sys.argv[1]
    if arg == 'create_db':
        Base.metadata.create_all(engine)
        print('Database created')
    elif arg == 'load_test_data':
        with Session(engine) as session:
            session.add_all(get_test_data())
            session.commit()
        print('Test data loaded')
