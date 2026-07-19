#!/usr/bin/python3
"""Prints the State object with the given name."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State)\
        .filter(State.name == state_name)\
        .first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
