def pg1():
    from sqlalchemy.engine import create_engine
    connection = create_engine('postgresql://team18:team_18@51.250.99.11:5432/postgres')
    return connection

def pg2():
    import psycopg2
    connection = psycopg2.connect(
        dbname="postgres",
        user="team18",
        password="team_18",
        host="51.250.99.11",
        port="5432",
    )
    return connection

def api_key():
    return "862aa2d2-eb35-4c38-9f3d-ebb4d3d9f410"