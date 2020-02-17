<?php
  // The global $_POST variable allows you to access the data sent with the POST method by name
  // To access the data sent with the GET method, you can use $_GET
  $type = htmlspecialchars($_POST['type']);
  $assignment = htmlspecialchars($_POST['assignment']);
  $des = htmlspecialchars($_POST['des']);

  echo  $say, 'task assigned to', $assignment;
?>
