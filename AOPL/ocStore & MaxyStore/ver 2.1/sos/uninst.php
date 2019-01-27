<?php
	echo '<meta http-equiv="content-type" content="text/html; charset=utf-8" />';
	
	$file = "admin/model/catalog/product.php";
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	
	$file = "admin/controller/catalog/product.php";
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, "''");
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	
	$file = "admin/view/template/catalog/product_form.tpl";
	$pb = 0;
	$pe = 0;
	FindHTML($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindHTML($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindHTML($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, '<td colspan="6"></td>');
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	
	$file = "admin/controller/common/menu.php";
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	
	$file = "admin/language/english/common/menu.php";
	if (file_exists($file)) {
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	}
	
	$file = "admin/language/english/catalog/product.php";
	if (file_exists($file)) {
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, "'Model';");
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, "'Model';");
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	}
	
	$file = "catalog/language/russian/product/product.php";
	if (file_exists($file)) {
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, "'Модель:';");
	}
	
	$file = "admin/language/russian/catalog/product.php";
	if (file_exists($file)) {
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, "'Модель';");
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, "'Модель:';");
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	}
	
	$file = "admin/language/ukrainian/catalog/product.php";
	if (file_exists($file)) {	
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	}
	
	$file = "admin/language/russian/common/menu.php";
	if (file_exists($file)) {
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	}
	
	$file = "admin/language/ukrainian/common/menu.php";
	if (file_exists($file)) {
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	}
	
	$file = "admin/language/russian/report/product_purchased.php";
	if (file_exists($file)) {
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) ins($file, $pb, $pe, $body, "'Модель';");
	$pb = 0;
	$pe = 0;
	FindPHP($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	}
	
	$file = "admin/view/template/common/menu.tpl";
	$pb = 0;
	$pe = 0;
	FindHTML($file, $pb, $pe, $body);
	if ($pb and $pe and !empty($body)) cat($file, $pb, $pe, $body);
	
	echo 'Clear';	
	/***********************************************************/
	
	function FindPHP($file, &$pb, &$pe, &$body) {	
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';			
		}
		$pb = stripos($body, '/*suppler');
		if (!$pb) return;			
		$pe = stripos($body, '/**suppler', $pb+1);			
		if (!$pe) return;
		$pe = $pe + 11;		
	}
	
	function FindHTML($file, &$pb, &$pe, &$body) {	
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';			
		}
		$pb = stripos($body, '<!-- *suppler');
		if (!$pb) return;			
		$pe = stripos($body, '**suppler', $pb+1);			
		if (!$pe) return;
		$pe = $pe + 13;		
	}
	
	function cat($file, $pb, $pe, &$body) {
		$a = substr($body, 0, $pb);
		$b = substr($body, $pe+1);
		$body = $a . $b;
		
		$e = @file_put_contents($file, $body);
		if (!$e) {
			echo 'Not writable file: ' . $file . ' <br />';
			$error++;
		}
	}
	
	function ins($file, $pb, $pe, $body, $c) {
		$a = substr($body, 0, $pb);
		$b = substr($body, $pe+1);
		$body = $a . $c . $b;
		
		$e = @file_put_contents($file, $body);
		if (!$e) {
			echo 'Not writable file: ' . $file . ' <br />';
			$error++;
		}
	}	

?>	
	