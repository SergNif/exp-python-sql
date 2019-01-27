<meta http-equiv='refresh' content='2; url=http://site.com/'>
<meta charset="UTF-8" />
<title>Сообщение отправлено</title>
<?php
/* Проверяем существуют ли переменные, которые передала форма обратной связи. 
   Если не существуют, то мы их создаем.
   Если форма передала пустые значения мы их удаляем */
if (isset($_POST['fio'])) {$fio = $_POST['fio']; if ($fio == '') {unset($fio);}}
if (isset($_POST['ask'])) {$ask = $_POST['ask']; if ($ask == '') {unset($ask);}}
if (isset($_POST['email'])) {$email = $_POST['email']; if ($email == '') {unset($email);}}
if (isset($_POST['pr'])){$pr = $_POST['pr']; if ($pr == '') {unset($pr);}}
if (isset($_POST['captcha'])){$captcha = $_POST['captcha'];}

 

/* Проверяем заполнены ли все поля */
if (isset($fio) &&  isset($email) &&  isset($ask) && isset($pr))

{

/* Убираем все лишние пробелы, а также преобразуем все теги HTML в символы*/
$fio = htmlspecialchars(trim($fio));
$email = htmlspecialchars(trim($email));
$ask = htmlspecialchars(trim($ask));




/* Проверяем правильность ввода капчи */
  if ($captcha == $pr)
  {
/* Формируем сообщение */
$address = "test@site.com";
$sub = "Сообщение с магазина";
$mes = "Автор назвался: $fio \nОставил такой телефон: $email \nТема вопроса: $ask \n ";

/* Отправка сообщения */
$verify = mail ($address,$sub,$mes,"Content-type:text/plain; charset = UTF-8\r\nFrom:$fio");
      if ($verify == 'true')
    
     {
       echo "<body>
<div style='margin-top: 30px'><table border='1' width='450' align='center' cellpadding='20' cellspacing='6'>
<tr>
<td>
<div style='margin'><div align='center' style='color:#0E4194; font-size:24px;'>Наш менеджер свяжется с Вами в ближайшее время и ответит на все интересующие Вас вопросы!</div>
<p><div align='center' style='color:#fff' >Спасибо за покупку!</div>
<p style='color:#fff'><div align='right'><i><b style='color:#0E4194'>C уважением, администрация интернет магазина - sitename.com</b></i></div>
</tr>
</td>
</table></div>";
      }
      else 
	  {
	  echo "<span style='color:#fff'>Сообщение не отправлено!</span>";
	  }
  }
  else
  {
  echo "<span style='color:#fff'> Вы не правильно ввели сумму чисел с картинки </span>";
  }
 

}
else
{
echo "Вы заполнили не все поля!";
}
?>