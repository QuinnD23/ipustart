from data.config import userc, passc, hostc

import psycopg2.extras


async def create_db():
    conn = psycopg2.connect(dbname="postgres", user=userc, password=passc, host=hostc)

    with conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # -----
            try:
                cur.execute("CREATE TABLE orders (index varchar primary key,"
                            "clothes varchar default 0,"
                            "colour varchar default 0,"
                            "level integer default 0,"
                            "price integer default 0,"
                            "date varchar default 0,"
                            "photo_id varchar default 0);")
            except:
                pass
            # -----
            try:
                cur.execute("CREATE TABLE info (user_id varchar primary key,"
                            "user_num serial,"
                            "user_name varchar default 0,"
                            "url_name varchar default 0,"
                            "place varchar default 0,"
                            "reg_date varchar default 0,"
                            "status integer default 0,"
                            "order_num integer default 1);")
            except:
                pass
            # -----
            try:
                cur.execute("CREATE TABLE ads (user_id varchar primary key,"
                            "ads_text text default 0);")
            except:
                pass
            # -----

    conn.close()
