#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(State.name.like("%a%"))\
        .order_by(State.id)\
        .all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
