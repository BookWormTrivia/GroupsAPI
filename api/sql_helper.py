import psycopg2
import config
import sys
import json

def _fetch_all_rows_for_query(query):
    '''
    Returns a list of rows obtained from the games database by the specified SQL
    query. If the query fails for any reason, an empty list is returned.

    Note that this is not necessarily the right error-handling choice. Would users
    of the API like to know the nature of the error? Do we as API implementors
    want to share that information? There are many considerations to balance.
    '''
    try:
        connection = psycopg2.connect(host=config.db_host, database=config.database, user=config.user, password=config.password, port=config.db_port)
    except Exception as e:
        print('Connection error:', e, file=sys.stderr)
        return []

    rows = []
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall() # This can be trouble if your query results are really big.
    except Exception as e:
        print('Error querying database:', e, file=sys.stderr)

    connection.close()
    print(rows)
    return rows

def execute_query(query):
    try:
        connection = psycopg2.connect(host=config.db_host, database=config.database, user=config.user, password=config.password, port=config.db_port)
    except Exception as e:
        print('Connection error:', e, file=sys.stderr)
        return
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print('Error querying database:', e, file=sys.stderr)

    connection.close()
