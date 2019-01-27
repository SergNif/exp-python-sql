import MySQLdb
import string

# соединяемся с базой данных
db = MySQLdb.connect(host="54.38.176.15",user="oc_serg",passwd="svgSD201",db="serg2",charset='utf8')
# формируем курсор
cursor = db.cursor()

# запрос к БД
#sql = """SELECT mail, name FROM eadres WHERE mail LIKE '%yandex.ru' LIMIT 10"""   UPDATE `oc_product_description` SET `description`= REPLACE(`description`, 'Симпатичные', 'Привлекательные')    SELECT * FROM `oc_product_description` WHERE LIKE `description`= 'Симпатичные'
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

# закрываем соединение с БД
db.close()
