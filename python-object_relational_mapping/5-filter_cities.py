#!/usr/bin/python3
"""Lists all cities of a given state safely (no SQL injection)."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """,
        (sys.argv[4],)
    )

    rows = cursor.fetchall()

    print(", ".join(city[0] for city in rows))

    cursor.close()
    db.close()
