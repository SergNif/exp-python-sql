import pymysql  # MySQLdb
import string
import csv
import random
from difflib import SequenceMatcher

# соединяемся с базой данных
db = pymysql.connect(
    host="54.38.176.15",
    user="oc_serg",
    passwd="svgSD201",
    db="serg2",
    charset='utf8')
# формируем курсор
cursor = db.cursor()

# запрос к БД
#sql = """SELECT mail, name FROM eadres WHERE mail LIKE '%yandex.ru' LIMIT 10"""
#sql = "SELECT * FROM `oc_product_description` WHERE `description`  LIKE '%бойфренд%' OR `description` LIKE '%шорты%' OR `description` LIKE  '%жилет%' OR `description` LIKE '%бриджы%' OR `description` LIKE '%сарафан%"
sql = "SELECT * FROM `oc_product_description` #WHERE `description` NOT LIKE '%привлекательные%'"
# выполняем запрос
cursor.execute(sql)
h1 = ['модные джинсы',
      'утепленные джинсы женские',
      'джинсы варенки',
      'пиджак с джинсами',
      'джинсы с высокой посадкой',
      'пара джинс',
      'обтянутые джинсы',
      'джинсы пирамиды',
      'джинсы рваные',
      'джинсы порезаны',
      'джинсы с молнией',
      'прямые джинсы',
      'модные джинсы 2019',
      'светлые джинсы',
      'лук с джинсами',
      'джинсы на резинке',
      'женские джинсы 2019',
      'модели джинс',
      'рваные джинсы ',
      'голубые джинсы',
      'утепленные джинсы',
      'брюки джинсы',
      'синие джинсы',
      'джинсы 2019',
      'ты любишь рваные джинсы',
      'джинсы на флисе']
text = ['Модные джинсы. Джинсы — всегда в моде. Пиджак, жакет, юбка, туфли сегодня, завтра и вчера. Неподвластно времени. Всегда на пике. Одежда является частью тебя. Ты - совершенство.',
        'Ваш внешний вид, его уместность и сообразность ситуации могут помочь Вам достичь своих высоких целей. Джинсы с высокой и низкой посадкой — уверенный шаг к мечте.',
        'В чем вы чувствуете себя привлекательным? Соблазнительным? А убедительным? Обтянутые джинсы? Джинсы пирамиды? Светлые, черные? Разные модели джинс. Одна цель — прийти к мечте.',
        'Модные джинсы. Джинсы — всегда в моде. Пиджак, жакет, юбка, туфли сегодня, завтра и вчера. Неподвластно времени. Всегда на пике. Одежда является частью тебя. Ты - совершенство.',
        'Ваш внешний вид, его уместность и сообразность ситуации могут помочь Вам достичь своих высоких целей. Джинсы с высокой и низкой посадкой — уверенный шаг к мечте.',
        'В чем вы чувствуете себя привлекательным? Соблазнительным? А убедительным? Обтянутые джинсы? Джинсы пирамиды? Светлые, черные? Разные модели джинс. Одна цель — прийти к мечте.Чем более ты раскован и уверен в себе с другими людьми, тем больше раскрываешь себя, тем больше всего удается сделать, тем больше людей тобой восхищаются.',
        'Выбранная вами одежда – это послание не только окружающим, но и самому себе. Разные модели джинс. Потому что все стремительно меняется. Ты любишь рваные джинсы. Или джинсы пирамиды. Лук с джинсами — это без проигрыша.',
        'Джинсы подходят людям всех возрастов и типов телосложения. Классика стала классикой именно потому, что этот стиль уже проверен временем и работает всегда – вне зависимости от того, кто вы.',
        'В такой одежде ты начинаешь себя ощущать более уверенно, чувствуешь себя важным, значимым и при общении с друг людьми ведешь себя более раскованно.Чем более ты раскован и уверен в себе с другими людьми, тем больше раскрываешь себя, тем больше всего удается сделать, тем больше людей тобой восхищаются.',
        'В джинсах, купленных в нашем магазине не надо учиться создавать привлекательный образ, который сам будет рассказывать о вас как об интересном человеке, отличном специалисте, творческой личности. Джинсы с молнией, джинсы на резинке, прямые джинсы уже обучены этому и сделают всё за Вас.',
        'Даже природная красота может проиграть яркой привлекательности, обаятельности и харизме, если на Вас обтянутые джинсы или джинсы порезаны по замыслу опытных модельеров.',
        'В этих джинсах результаты профессиональной деятельности достигнут заоблачных высот без особых усилий и временных затрат. Вы будете лучшим среди лучших. Джинсы.',
        'Вам не нужно будет обдумывать Ваш образ до мельчайших подробностей: работодатели и клиенты будут смотреть волнующим взглядом. Джинсы.',
        'В этих джинсах Вы будете внешне привлекательны, чем подчеркнете свои внутренние качества. Эта гармония не останется незамеченной.',
        'Увидев девушку в этих джинсах, мужчины вспомнят об элементарной истине и будут восхищаться не одеждой, а восклицать «Какая Вы красивая».',
        'Рваные джинсы — целая философия: чем меньше целых кусков, тем больше захватывает дух.',
        'Женские джинсы и юбки одержали больше побед, чем у френчи и эполеты.',
        'В модных джинсах просто выразить себя. Это еще одна форма искусства. Пиджак с джинсами. Рубашка с джинсами. Я буду делать то, что хочу.',
        'Неважно, с чем носить джинсы, — намного важнее, что ты при этом чувствуешь.',
        'Джинсы варенки или другие модели джинс —  не просто прикрывают тело. Это отражение внутреннего мира человека. Поэтому пара джинс говорит о человеке гораздо больше.',
        'В одежде старайся быть изящным, но не щеголем; признак изящества — приличие, а признак щегольства — излишество.',
        'Красота становится живой и интересной, когда она скрыта голубыми светлыми джинсами.',
        'Носите джинсы с высокой посадкой, но не позволяйте джинсам носить вас. Не становитесь рабом моды. В наших джинсах Вы будете законодателем моды.',
        'Порезанные джинсы - не только удобство или способ соблазнить. Одежда может быть состоянием Духа, характером, властью.',
        'Девушки в джинсах - это даже не элегантность или статус, а некие нюансы внутри статуса.',
        'Чистые, сильные эмоции. Это не о моде. Это о голубых джинсах . ',
        'Модная джинса 2019 – это простой способ говорить о сложных вещах.',
        'Дайте девушке правильные утепленные женские джинсы, и она сможет покорить мир. ',
        'дизайнеры представляют моду четыре раза в год. Где купить джинсы – Вы выбираете сами.',
        'Носите утепленные женские джинсы всегда так, будто за вами идут трое мужчин.',
        'Выглядеть моделью легко. Найти наш магазин, чтобы купить джинсы с молнией - труднее. ',
        'Быть не похожей на других - просто, быть уникальной в обтянутых джинсах – очень просто. Купите джинсы у нас, станьте неотразимой.',
        'Модные джинсы 2019 – это способ сказать всем, кто вы есть, без слов.',
        'Ваш лук с джинсами — это чья-то мечта. Создайте мечту, превратите её в реальность.',
        'Рубашка с джинсами - союз комфорта и роскоши, практичного и желаемого.',
        'Мужские рваные джинсы должны быть модными и роскошными. Иначе это не мода и не роскошь.',
        'Если хочешь быть лучше своего конкурента, то купи в нашем магазине лучшее. Одевайся в прямые джинсы или джинсы пирамиды.',
        'Чего хотят женщины? Женщины хотят купить пару джинс в нашем магазине и быть красивыми.',
        'Рубашка с джинсами — альфа, пиджак с джинсами — омега модного алфавита.',
        'Мода — это Ваши луки с джинсами, купленными в нашем магазине с доставкой на дом.',
        'Мода — это вдохновение и уют, приобретённые с утепленными джинсами в нашем интернет магазине.',
        'Носи богатые одежды - они откроют перед тобой все двери. Это же можно сказать и про синие джинсы, купленные в нашем магазине с доставкой на дом.',
        'Не покоряйтесь стандартам моды , носите светлые джинсы, они Вам точно идут.',
        'Театр — это жизнь. Если Вы носите купленные у нас утепленные джинсы, то Вы становитесь участником этого зрелища.',]
# получаем результат выполнения запроса  UPDATE `oc_seo_url` SET `keyword`= CONCAT('ffffff ', `keyword` , ' yyyyyyyyyy') WHERE `query` = 'product_id=50'  джинсы-женские-утепленные-sessanta-3687
data = cursor.fetchall()
index_h1 = -1
s = ''
# перебираем записи
for rec in data:
    index_h1 += 1
    if index_h1 > (len(h1) - 1):
        index_h1 = len(h1) % index_h1
    # извлекаем данные из записей - в том же порядке, как и в SQL-запросе
    f = h1[index_h1]
    random.shuffle(text)
    s = ''
    index_text = 0

    for j, i in enumerate(text):
        rat = 0
        if f not in i:
            st = SequenceMatcher(lambda x: x == " ", f, i)
            if st.ratio() > rat:
                rat = st.ratio()
                index_text = j
        else:
            s = i
            break
    if s == '':
        s = text[index_text]

    name = rec
#     `product_id`=[0],`language_id`=[1],`name`=[2],`description`=[3],`tag`=[4],`meta_title`=[5],`meta_description`=[6],`meta_keyword`=[7]
    #s = text[random.randint(0, 43)] + ' ' + name[3]
    sql_up = "UPDATE `oc_product_description` SET `description`= " + '"' + s + ' ' + str(name[3]) + '"' + " WHERE `product_id` = " + str(name[0])  # description
    cursor.execute(sql_up)
    # выводим информацию
    #print(sql_up)
    sql_up = "UPDATE `oc_product_description` SET `meta_description`= " + '"' + ' '  + str(name[2]) + ' ' + f + '"' + " WHERE `product_id` = " + str(name[0])
    cursor.execute(sql_up)
    # выводим информацию
    #print(sql_up)

    # title
    sql_up = "UPDATE `oc_product_description` SET `meta_title`= " + '"' + str(name[5]) + ' ' +  f + ' jns4u.ru' + '"' + " WHERE `product_id` = " + str(name[0])
    cursor.execute(sql_up)
    # выводим информацию
    #print(sql_up)
    
    # tag
    sql_up = "UPDATE `oc_product_description` SET `tag`= " + '"' + str(name[2]) + ' ' +  f + ' jns4u.ru' + '"' + " WHERE `product_id` = " + str(name[0])
    cursor.execute(sql_up)
    # выводим информацию    
    #print(sql_up)
    
    # meta_keyword
    sql_up = "UPDATE `oc_product_description` SET `meta_keyword`= " + '"' + str(name[2]) + ' '  + s + ' ' + f + ' jns4u.ru' + '"' + " WHERE `product_id` = " + str(name[0])
    cursor.execute(sql_up)
    # выводим информацию
    #print(sql_up)
    
# cursor2 = db.cursor()  # get the cursor             /*  <p><Font Color=&quot;#333333&quot;>
# UPDATE `oc_product_description` SET `description`= REPLACE (`description`, ' <br /> Покупайте для удовольствия  <br /> Покупайте для удовольствия', ' <br /> Покупайте для удовольствия.')
# len(cursor.description)  UPDATE `oc_product_description` SET `description`= REPLACE (`description`, '</Font><Font Face=&quot;Arial Cyr&quot; x:CharSet=&quot;204&quot; Size=&quot;10&quot;>', '')
#
# cursor2.execute("USE serg2")  # select the database
#cursor3 = db.cursor()
# execute 'SHOW TABLES' (but data is not returned)
#cursor2.execute("SHOW TABLES")
# for (table_name) in cursor2:
#
#    sql2 = "SELECT * FROM " + ''.join(map(str, table_name))
#    # ''.join("SELECT * FROM ", table_name)#[2:-3]
#    #print( ''.join("SELECT * FROM "), str(table_name)[2:-3])
#    # print(sql2)
#    cursor3.execute(sql2)
#    field_names = [i[0] for i in cursor3.description]
#    # print(table_name)
#    # for x in field_names:
#    #  print(x)
#    # print(type(field_names))
#    c=''.join(map(str, table_name))
#
#    for x in field_names:
#        #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#        #print(type(x))
#        f=''.join( x)
#        #print(type(c),'  ',type(x))
#        with open('eggs.csv', 'a') as csvfile:
#            spamwriter = csv.writer(
#                csvfile,
#                delimiter=';',
#                #quotechar='|',
#                #quoting=csv.QUOTE_MINIMAL)
#            spamwriter.writerow([c, f])
#        #print(''.join(map(str,table_name)), '   ' ,x)

db.close()

# SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS  выводит все поля таблицы SQL
# Что касается вашего вопроса, то при добавлении товаров обовляются еще таблицы oc_product_description, oc_product_to_store, oc_product_to_category, oc_url_alias И это если нет опций и атрибутов.
# https://wmasteru.org/threads/sql-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81-%D0%BD%D0%B0-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0.9207/
