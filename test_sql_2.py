import MySQLdb
import string
import csv

# соединяемся с базой данных
db = MySQLdb.connect(
    host="54.38.176.15",
    user="oc_serg",
    passwd="svgSD201",
    db="serg2",
    charset='utf8')
# формируем курсор
cursor = db.cursor()

# запрос к БД
#sql = """SELECT mail, name FROM eadres WHERE mail LIKE '%yandex.ru' LIMIT 10"""
sql = "SELECT * FROM `oc_product` WHERE `quantity` > 100 "
# выполняем запрос
cursor.execute(sql)

# получаем результат выполнения запроса
data = cursor.fetchall()
# перебираем записи
for rec in data:
    # извлекаем данные из записей - в том же порядке, как и в SQL-запросе
    name = rec
    # выводим информацию
    print(name)

cursor2 = db.cursor()  # get the cursor

# len(cursor.description)

cursor2.execute("USE serg2")  # select the database
cursor3 = db.cursor()
# execute 'SHOW TABLES' (but data is not returned)
cursor2.execute("SHOW TABLES")
for (table_name) in cursor2:

    sql2 = "SELECT * FROM " + ''.join(map(str, table_name))
    # ''.join("SELECT * FROM ", table_name)#[2:-3]
    #print( ''.join("SELECT * FROM "), str(table_name)[2:-3])
    # print(sql2)
    cursor3.execute(sql2)
    field_names = [i[0] for i in cursor3.description]
    # print(table_name)
    # for x in field_names:
    #	print(x)
    # print(type(field_names))
    c=''.join(map(str, table_name))
    
    for x in field_names:
        #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        #print(type(x))
        f=''.join( x)
        #print(type(c),'  ',type(x))
        with open('eggs.csv', 'a') as csvfile:
            spamwriter = csv.writer(
                csvfile,
                delimiter=';',
                #quotechar='|',
                #quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([c, f])
        #print(''.join(map(str,table_name)), '   ' ,x)

db.close()

# SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS  выводит все поля таблицы SQL
#Что касается вашего вопроса, то при добавлении товаров обовляются еще таблицы oc_product_description, oc_product_to_store, oc_product_to_category, oc_url_alias И это если нет опций и атрибутов.
#https://wmasteru.org/threads/sql-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81-%D0%BD%D0%B0-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0.9207/