# query_to_postgres

### Вторая версия скрипта send_query_to_postrgresql

Включена возможность добавлять любое количество запросов и БД

/dist/query_to_postgresql.exe - то же самое, но собранное в екзешник

### JSON

```json
  "query_name": {
      "USER": "user",
      "PASSWORD": "password",
      "HOST": "host",
      "BASE": "db_name",
      "PORT": 15432,
      "header": [
        "column1",
        "column2",
        "колонка3",
        "колонка42"
      ],
      "sheet": "sheet_name",
      "sql_file_path": "\\query.sql"
```     
      query_name - имя, выгрузка будет называться "Отчёт_{query_name}_{today}".xlsx
      
      header - имена колонок
      
      sheet - имя страницы
      
      sql_file_path - название файла с запросом, лежащего в папке sql_requests
      
