#!/usr/bin/python3
"""Lists all City objects grouped by State."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    results = session.query(State, City)\
        .join(City, State.id == City.state_id)\
        .order_by(City.id)\
        .all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
