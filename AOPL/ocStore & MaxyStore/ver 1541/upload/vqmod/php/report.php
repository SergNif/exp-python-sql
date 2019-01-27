<?php header('Content-type: text/html; charset=utf-8 BOM')?> 
<p style="text-align: center"><input type='button' onclick='javascript:history.go(-1)' value="Back"></p><hr/>
<?php

function read_file_func($file)
    {
    if(file_exists($file))
        {
        $f=fopen($file, "r+t") or die("Can not read file");
        flock($f, LOCK_SH);
        $cont=explode("\n",fread($f,filesize($file))); 
        fclose($f); 
        }
    else $cont="File not exist";
    return $cont;
    }
?> 
<?php $q = 1; ?>

<?php
    $mass=read_file_func($_SERVER['DOCUMENT_ROOT'] . '/admin/uploads/report.tmp');
	if ($mass != 'File not exist') {
		foreach($mass as $value) {
			if($q & 1) $color="0000FF";
			else $color="CC3333";	
			echo "<font color=\"336633\">".$q."  |"."</font>"."<font color=\"".$color."\">"."   ".$value."</font>"."<br>"."<hr/>";
			$q=$q+1;
		}
	}	else echo "File not exist";
?>

<p style="text-align: center"><input type='button' onclick='javascript:history.go(-1)' value="Back"></p>
<br/><br/><br/><br/>