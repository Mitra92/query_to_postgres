try:
    import logging
    from datetime import date
    import msvcrt as m
    import os
    import json
    import psycopg2 as psg
    import codecs
    import pandas as pd
    from pandas.io.excel import ExcelWriter

    logging.basicConfig(format='%(asctime)s - %(message)s',
                        filename='script_log.log', encoding='utf-8', level=logging.DEBUG)
    today = date.today()

    connection_path = "connections.json"


    def wait():
        """Задержка экрана"""
        m.getch()


    def connect(db):
        logging.info('User: %s', dict_db[query_name]["USER"])
        connect_to = psg.connect(database=dict_db[query_name]["BASE"],
                                 user=dict_db[query_name]["USER"],
                                 password=dict_db[query_name]["PASSWORD"],
                                 host=dict_db[query_name]["HOST"],
                                 port=dict_db[query_name]["PORT"])
        logging.info('Connection to %s is success', dict_db[query_name]["BASE"])
        return connect_to



    def read_query_from_file(file_name):
        sql_path = "sql_requests" + dict_db[query_name]["sql_file_path"]
        with codecs.open(sql_path, 'r', "utf_8_sig") as q:
            que = q.read()
        logging.info('Query %s read successfully', file_name)
        return que


    def send_query(que_sql, conn):
        curr = conn.cursor()
        logging.info('Send query to DB')
        curr.execute(que_sql)
        response = curr.fetchall()
        return response


    if __name__ == '__main__':
        with open(connection_path, 'r', encoding="utf-8") as f:
            dict_db = json.load(f)
            for query_name in dict_db:
                try:
                    excel_path = f'sql_response\\Отчёт_{query_name}_{today}.xlsx'
                    with ExcelWriter(excel_path, engine="openpyxl",
                                     mode="+w") as writer:
                        connection = connect(dict_db[query_name])
                        query = read_query_from_file(dict_db[query_name]["sql_file_path"])
                        response_rem_bso = send_query(query, connection)
                        df = pd.DataFrame(response_rem_bso)
                        df.to_excel(writer, sheet_name=dict_db[query_name]["sheet"],
                                    header=dict_db[query_name]["header"], index=False)
                        logging.info('result has been written')
                        print('result has been written')
                        connection.close()
                        writer.save()
                except Exception as error:
                    logging.warning('Unexpected ERROR: %s', error)
                    print(f'Unexpected ERROR: {error}', )


except Exception as error:
    logging.warning('Unexpected ERROR: %s', error)
    print(f'Unexpected ERROR: {error}', )

logging.info('Work is done')

wait()