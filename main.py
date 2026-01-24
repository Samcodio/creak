import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_a_x4ITfWKc-ctP31X8u@pg-ba435c9-cybrongaming247-64dc.d.aivencloud.com:14803/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()