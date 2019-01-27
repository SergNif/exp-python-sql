<?php
	echo '<meta http-equiv="content-type" content="text/html; charset=utf-8" />';
	$error = 0;
	$file = "admin/model/catalog/product.php";
	$text = "this->addProduct(";
	$pos = Find($file, $text, 1, $body);
	if ($pos == 'no') {
		echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
		$error++;
	} else {
		$a = substr($body, $pos-60, 120);	
		if (!substr_count($body, 'suppler')) {
			$text = '			
			/*suppler*/
			$row1 = $this->getMaxModel();
			$max_mod = $row1["max(product_id)"];
			$next_code = $max_mod + 1;
			$p = strpos($data["model"], "-");
			if (!$p) strpos($data["model"], "~");
			if ($p) {
				$p = substr($data["model"], $p);
				$data["model"] = $next_code.$p;
			} /**suppler*/';
			Insert($file, $pos, $text, $error);
		}	
	}	
	
	$text = "public function getProducts(";	
	$pos = FindText($file, $text, 1);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') {
			echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = '
	/*suppler*/	
	public function getMaxModel() {		
		$query = $this->db->query("SELECT max(product_id) FROM " . DB_PREFIX . "product");			
		return $query->row;
	} /**suppler*/ ';
	
			Insert($file, $pos, $text, $error);
		}		
	}
	$text = "optsku=";	
	$pos = FindText($file, $text, 1);	
	if ($pos == 'no') {
		$text = ", weight_prefix";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') {
				echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
			$text = "/*suppler*/ optsku= '".'" . $this->db->escape($product_option_value["optsku"]) . "'."',/**suppler*/ ";
	
				Insert($file, $pos, $text, $error);
			}	
		}		
	}
	$text = "optsku=";	
	$pos = FindText($file, $text, 2);	
	if ($pos == 'no') {
		$text = ", weight_prefix";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') {
				echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 4 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
			$text = "/*suppler*/ optsku= '".'" . $this->db->escape($product_option_value["optsku"]) . "'."',/**suppler*/ ";

				Insert($file, $pos, $text, $error);
			}	
		}		
	}
	$text = "'weight_prefix'";	
	$pos = FindText($file, $text, 3);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 5 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = '
		/*suppler*/	"optsku"          		  => $product_option_value["optsku"], /**suppler*/';	
			Insert($file, $pos, $text, $error);	
		}	
	}
	
	$file = "admin/controller/catalog/product.php";	
	$text = "uct(" ."$"."this->request->get['product_id']);";
	$pos = FindAfter($file, $text, 1);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = ' /*suppler*/else {
			$row = $this->model_catalog_product->getMaxModel();
			$max_model = $row["max(product_id)"];
			$next_code = $max_model + 1;
			$next_code = $next_code."-";
		} /**suppler*/';
	
			Insert($file, $pos, $text, $error);	
		}	
	}	
	$text = "data['model'] = ''";
	$pos = FindText($file, $text, 1);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') ;
		 else {	
			$rep = "data['model'] = /*suppler*/ "."$"."next_code /**suppler*/ ";
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
		}
	}
	$text = "data['entry_tag']";	
	$pos = FindText($file, $text, 1);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = '
/*suppler*/$data["entry_optsku"] = $this->language->get("entry_optsku"); /**suppler*/';	
			Insert($file, $pos, $text, $error);	
		}	
	}
	$text = "'weight_prefix'";	
	$pos = FindText($file, $text, 1);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 4 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = '
			/*suppler*/	"optsku"          		  => $product_option_value["optsku"], /**suppler*/';	
			Insert($file, $pos, $text, $error);	
		}	
	}
	
	$file = "admin/view/template/catalog/product_form.tpl";
	$text = "entry_weight; ?></";
	$pos = FindAfter2($file, $text, 2);		
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = ' 
<!-- *suppler* --><td class="text-right"><?php echo $entry_optsku; ?></td> <!-- **suppler* -->
';
	
			Insert($file, $pos, $text, $error);	
		}	
	}
	$text = '<td class="text-left"><button type';
	$pos = FindText($file, $text, 3);		
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = ' 
<!-- *suppler* --> <td><input type="text" name="product_option[<?php echo $option_row; ?>][product_option_value][<?php echo $option_value_row; ?>][optsku]" value="<?php echo $product_option_value["optsku"]; ?>" size="12" /></td> <!-- **suppler* -->
';
					
			Insert($file, $pos, $text, $error);	
		}	
	}	
	$text = 'colspan="7"';
	$pos = FindText($file, $text, 1);	
	if ($pos == 'no') {
		$text = '<td colspan="6"></td>';
		$pos = FindText($file, $text, 1);		
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
$rep = '<!-- *suppler* --><td colspan="7"></td> <!-- **suppler* -->
';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
			}
		}	
	}	
	$text = "html += '        <td></td>';";
	$pos = FindText($file, $text, 1);	
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 4 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = " 
/*suppler*/html += '        <td class=" . '"right"' . '><?php echo $entry_optsku; ?></td>'."'" . "; /**suppler*/
";
					
			Insert($file, $pos, $text, $error);	
		}	
	}	
	$text = "html += '  <td class=".'"text-left"><button';
	$pos = FindText($file, $text, 2);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 5 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = " 
/*suppler*/html += '".'    <td><input type="text" name="product_option['."' + option_row + '][product_option_value][' + option_value_row + ']".'[optsku]" value="" size="12" /></td>'."'; /**suppler*/
";
					
			Insert($file, $pos, $text, $error);	
		}	
	}
	
    $file = "admin/controller/common/column_left.php";
	$text = "catalog/manufacturer";	
	$pos = FindAfter($file, $text, 1);
	if ($pos == 'yes') ;
	else {
		if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			$error++;
		} else {	
		$text = " 
/*suppler*/	if ("."$"."this->user->hasPermission('access', 'catalog/suppler')) {
				"."$"."catalog[] = array(
					'name'	   => "."$"."this->language->get('text_suppler'),
					'href'     => "."$"."this->url->link('catalog/suppler', 'token=' . "."$"."this->session->data['token'], true),
					'children' => array()		
				);
			}   /**suppler*/
";
	
			Insert($file, $pos, $text, $error);	
		}	
	}
		
	$file = "admin/language/english/common/column_left.php";
	if (file_exists($file)) {
		$text = "['text_manufacturer']";	
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . $text . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["text_suppler"]                	   = "Suppliers"; /**suppler*/
';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}
	
	$file = "admin/language/en-us/common/column_left.php";
	if (file_exists($file)) {
		$text = "['text_manufacturer']";	
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . $text . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["text_suppler"]                	   = "Suppliers"; /**suppler*/
';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}

	$file = "admin/language/en-gb/common/column_left.php";
	if (file_exists($file)) {
		$text = "['text_manufacturer']";	
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . $text . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["text_suppler"]                	   = "Suppliers"; /**suppler*/
';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}
	
	$file = "admin/language/english/catalog/product.php";
	if (file_exists($file)) {
		$text = "'Model';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Model';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Model:';";
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code:"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'entry_status'";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = ' 
/*suppler*/$_["entry_optsku"]      	 = "SKU:"; /**suppler*/ ';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}
	
	$file = "admin/language/en-us/catalog/product.php";
	if (file_exists($file)) {
		$text = "'Model';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Model';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Model:';";
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code:"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'entry_status'";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = ' 
/*suppler*/$_["entry_optsku"]      	 = "SKU:"; /**suppler*/ ';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}

	$file = "admin/language/en-gb/catalog/product.php";
	if (file_exists($file)) {
		$text = "'Model';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Model';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Model:';";
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Product code:"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'entry_status'";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = ' 
/*suppler*/$_["entry_optsku"]      	 = "SKU:"; /**suppler*/ ';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}
	
	$file = "catalog/language/russian/product/product.php";
	if (file_exists($file)) {
		$text = "'Модель:';";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара:"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
	}	

	$file = "catalog/language/ru-ru/product/product.php";
	if (file_exists($file)) {
		$text = "'Модель:';";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара:"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
	}

	$file = "admin/language/russian/catalog/product.php";
	if (file_exists($file)) {
		$text = "'Модель';";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Модель';";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Модель:';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара:"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Вес";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["entry_optsku"]      	 = "Артикул:"; /**suppler*/
  ';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}

	$file = "admin/language/ru-ru/catalog/product.php";
	if (file_exists($file)) {
		$text = "'Модель';";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Модель';";	
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Модель:';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара:"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 2 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
		$text = "'Вес";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 3 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["entry_optsku"]      	 = "Артикул:"; /**suppler*/
  ';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}
	
	$file = "admin/language/ukrainian/catalog/product.php";
	if (file_exists($file)) {
		$text = "'Вага";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["entry_optsku"]      	 = "Артикул:"; /**suppler*/
  ';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}
	
	$file = "admin/language/ua-ua/catalog/product.php";
	if (file_exists($file)) {
		$text = "'Вага";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["entry_optsku"]      	 = "Артикул:"; /**suppler*/
  ';
	
				Insert($file, $pos, $text, $error);
			}	
		}
	}
	
	$file = "admin/language/russian/common/column_left.php";
	if (file_exists($file)) {
		$text = "['text_manufacturer']";	
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["text_suppler"]                	   = "Поставщики"; /**suppler*/
 ';
	
				Insert($file, $pos, $text, $error);	
			}	
		}
	}

	$file = "admin/language/ru-ru/common/column_left.php";
	if (file_exists($file)) {
		$text = "['text_manufacturer']";	
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["text_suppler"]                	   = "Поставщики"; /**suppler*/
 ';
	
				Insert($file, $pos, $text, $error);	
			}	
		}
	}
	
	$file = "admin/language/ukrainian/common/column_left.php";
	if (file_exists($file)) {
		$text = "['text_manufacturer']";	
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["text_suppler"]                	   = "Постачальники"; /**suppler*/
 ';
	
				Insert($file, $pos, $text, $error);	
			}	
		}
	}
	
	$file = "admin/language/ua-ua/common/column_left.php";
	if (file_exists($file)) {
		$text = "['text_manufacturer']";	
		$pos = FindText($file, $text, 1);	
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') { echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
				$error++;
			} else {	
		$text = '
/*suppler*/$_["text_suppler"]                	   = "Постачальники"; /**suppler*/
 ';
	
				Insert($file, $pos, $text, $error);	
			}	
		}
	}

	$file = "admin/language/russian/report/product_purchased.php";
	if (file_exists($file)) {
		$text = "'Модель';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
	}

	$file = "admin/language/ru-ru/report/product_purchased.php";
	if (file_exists($file)) {
		$text = "'Модель';";
		$pos = FindText($file, $text, 1);
		if ($pos == 'yes') ;
		else {
			if ($pos == 'no') ;
			else {	
		$rep = '/*suppler*/"Код товара"; /**suppler*/';
			$err = Replace($file, $pos, $text, $rep, $error);
			if ($err) echo 'FAIL&nbsp;&nbsp;&nbsp;&nbsp;Text: <b>' . 1 . '</b> not found in file: ' . $file . ' <br />';
			}	
		}
	}	
	
	require_once 'config.php';
	
	$dbhost = DB_HOSTNAME;
	$dbuser = DB_USERNAME;
	$dbpass = DB_PASSWORD;
	$dbdatabase = DB_DATABASE;
	$dbprefix = DB_PREFIX;
	
	$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbdatabase);
	if(!$conn ) die('Could not connect: ' . mysql_error());

	$sql = 'CREATE TABLE IF NOT EXISTS `' . $dbprefix . 'key`( '.
       'id INT NOT NULL AUTO_INCREMENT, '.
       'value text, '.
       'main_key  VARCHAR(256), '.
       'license_key text, '.       
       'primary key ( id ))';
	
	$retval = $conn->query($sql);
	if(!$retval ) die('Could not create table: ' . mysql_error());
	echo "Table key created<br />";	
	$conn->close();

	$conn = new mysqli($dbhost, $dbuser, $dbpass, $dbdatabase);
	$query = "select * from `" . $dbprefix . "key` where `main_key`='local_key'";	
	$retval = $conn->query($query);
	if(!$retval) die('Could not read table: ' . mysql_error());	
	$rows = $retval->fetch_assoc();
	if (empty($rows)) {
		$query = "INSERT INTO `" . $dbprefix . "key` SET `value` = '', `main_key` = 'local_key', `license_key` = ''";
		$query_res = $conn->query($query);
		if($query_res) echo " Open new license";
		else echo " Can not write to table 'key'";
	}
	
	$conn->close();
	if (!$error) echo " MODULE SUCCESSFULLY INSTALLED";
	else echo 'Module not installed. Please, check ' . $error . ' error(s)';
	
  /*******************************************************/
		
	function Replace($file, $pos, $text, $rep, &$error) {
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return 1;
		}	
		$h1 = substr($body, 0, $pos);
		$h2 = substr($body, $pos+1, 400);
		$h3 = substr($body, $pos+401);
		$h2 = str_replace($text, $rep , $h2);
		$body = $h1.' '.$h2.$h3;
		$e = @file_put_contents($file, $body);
		if (!$e) {
			echo 'Not writable file: ' . $file . ' <br />';
			$error++;
			return 1;
		} else return 0;			
	}
	
	function Insert($file, $pos, $text, &$error) {		
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return;
		}
		$h1 = substr($body, 0, $pos);
		$h2 = substr($body, $pos+1);
		$body = $h1.$text.$h2;
		$e = @file_put_contents($file, $body);
		if (!$e) {
			echo 'Not writable file: ' . $file . ' <br />';
			$error++;
		}
	}
	
	function FindText($file, $text, $n) {
	//	$pos = 0;
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return "no";
		}
		$p = 0;
		for ($i=1; $i<=$n; $i++) {
			$pos = stripos($body, $text, $p);
			if (!$pos) return "no";			
			$p = $pos + 2;			
		}
		$h = substr($body, $pos-180, 400);
		if (substr_count($h, "*suppler*")) return "yes";
		
		for ($i=0; $i<60; $i++) {
			$s = substr($body, $pos-$i, 1);			
			if ($s == "}" or $s == ";" or $s == "," or $s == ">") break;
		}
		$pos = $pos - $i + 1;		
		
		return $pos;
	}
	
	function FindAfter($file, $text, $n) {
	//	$pos = 0;
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return "no";
		}
		$p = 0;
		for ($i=1; $i<=$n; $i++) {
			$pos = stripos($body, $text, $p);
			if (!$pos) return "no";			
			$p = $pos + 2;			
		}
		$h = substr($body, $pos-2, 400);
		if (substr_count($h, "*suppler*")) return "yes";		
		
		$pos = $pos + strlen($text);
		$pos = stripos($body, '}', $pos);
		if (!$pos) return "no";
		
		return $pos+1;
	}
	
	function FindAfter1($file, $text, $n) {
	//	$pos = 0;
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return "no";
		}
		$p = 0;
		for ($i=1; $i<=$n; $i++) {
			$pos = stripos($body, $text, $p);
			if (!$pos) return "no";			
			$p = $pos + 2;			
		}
		$h = substr($body, $pos-2, 400);
		if (substr_count($h, "*suppler*")) return "yes";		
		
		$pos = $pos + strlen($text);
		$pos = stripos($body, '(', $pos);
		if (!$pos) return "no";
		
		return $pos+1;
	}
	
	function FindAfter2($file, $text, $n) {
	//	$pos = 0;
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return "no";
		}
		$p = 0;
		for ($i=1; $i<=$n; $i++) {
			$pos = stripos($body, $text, $p);
			if (!$pos) return "no";			
			$p = $pos + 2;			
		}
		$h = substr($body, $pos-2, 100);
		if (substr_count($h, "*suppler*")) return "yes";		
		
		$pos = $pos + strlen($text);
		$pos = stripos($body, 'd>', $pos);
		if (!$pos) return "no";
		
		return $pos+2;		
	}
	
	function FindAfter3($file, $text, $n) {
	//	$pos = 0;
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return "no";
		}
		$p = 0;
		for ($i=1; $i<=$n; $i++) {
			$pos = stripos($body, $text, $p);
			if (!$pos) return "no";			
			$p = $pos + 2;			
		}
		$h = substr($body, $pos-2, 90);
		if (substr_count($h, "*suppler*")) return "yes";		
		
		$pos = $pos + strlen($text);
		$pos = stripos($body, '{', $pos);
		if (!$pos) return "no";
		
		return $pos+1;
	}	

	function Find($file, $text, $n, &$body) {
	//	$pos = 0;
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return "no";
		}
		$p = 0;
		for ($i=1; $i<=$n; $i++) {
			$pos = stripos($body, $text, $p);
			if (!$pos) return "no";			
			$p = $pos + 2;			
		}		
		for ($i=0; $i<60; $i++) {
			$s = substr($body, $pos-$i, 1);			
			if ($s == "}" or $s == ";" or $s == "," or $s == ">") break;
		}
		$pos = $pos - $i + 1;		
		
		return $pos;
	}
	
	function Find1($file, $text, $n) {
	//	$pos = 0;
		$body = file_get_contents($file);
		if (empty($body)) {
			echo 'Cannot read file: ' . $file . ' <br />';
			return "no";
		}
		$p = 0;
		for ($i=1; $i<=$n; $i++) {
			$pos = stripos($body, $text, $p);
			if (!$pos) return "no";			
			$p = $pos + 2;			
		}				
		
		$pos = $pos + strlen($text);
		$pos = stripos($body, 'd>', $pos);
		if (!$pos) return "no";
		
		return $pos+2;
	}

?>
