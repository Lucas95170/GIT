<?php

try{

  $bd=new PDO('pgsql:host=aquabdd;dbname=etudiants', '11802551', '081854331JK');
  $bd->query("SET NAMES 'utf8'");
  $bd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

  if(isset($_GET["identifiant"]) and preg_match("#^\d+$#", $_GET["identifiant"])){
    $req=$bd->prepare("Select * from nobels where id= :identifiant");
    $req->bindValue(":identifiant", $_GET["identifiant"]);
    $req->execute();
    $ligne=$req->fetch();
    var_dump($ligne);
  }

  else{
    echo "Ah...";
  }

} catch(PDOException $e) {

  echo "ERROR";

}

 ?>
