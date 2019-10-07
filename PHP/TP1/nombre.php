<?php

if( isset ($_GET['nombre'])){
  if(preg_match("#^-?\d+$#",$_GET['nombre']))
    echo "Il s'agit d'un nombre";
  else {
    echo "Il ne s'agit pas d'un nombre";
  }
}
 ?>
