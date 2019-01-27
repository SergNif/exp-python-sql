Это необязательное действие ускоряет работу модуля.
Делается только 1 раз.

В тексте, который вы видите ниже, исправьте везде, префикс БД (у меня это "oc_", у вас может быть другой префикс), если вы, вообще, используете префикс. Скопируйте исправленный текст: 


ALTER TABLE `oc_suppler_data` ADD INDEX( `category_id` ) ;
ALTER TABLE `oc_suppler_data` ADD INDEX( `form_id` ) ;
ALTER TABLE `oc_product` ADD INDEX( `sku` ) ;
ALTER TABLE `oc_suppler_sku_description` ADD INDEX( `sku` ) ;
ALTER TABLE `oc_suppler_sku` ADD INDEX( `sku_id` ) ;
ALTER TABLE `oc_product_option_value` ADD INDEX( `optsku` ) ;
ALTER TABLE `oc_attribute_description` ADD INDEX( `name` ) ;
ALTER TABLE `oc_manufacturer` ADD INDEX( `name` ) ;

зайдите через phpMyAdmin в БД магазина, вставьте этот текст в закладку SQL и нажмите OK. 