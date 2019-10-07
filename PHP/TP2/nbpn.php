<?php
try{
  $bd=new PDO('pgsql:host=aquabdd;dbname=etudiants', '11802551', '081854331JK');
  $bd->query("SET NAMES 'utf8'");
  $bd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  $req=$bd->prepare("Select count(*) from nobels");
  $req->execute();
  $ligne=$req->fetch();
  var_dump($ligne);
} catch(PDOException $e) {
  echo "ERROR";
}

 ?>
