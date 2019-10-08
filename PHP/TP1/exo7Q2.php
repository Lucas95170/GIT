<?php

echo "<form action = 'exo7Q2.php' method='post'>
    <input type = 'text' name = 'pseudo' placeholder=".$_POST["pseudo"].">
    <input type = 'submit' value = 'Rechercher'>
</form>";

$personnes = [
    'mdupond' => ['Prénom' => 'Martin', 'Nom' => 'Dupond', 'Age' => 25, 'Ville' => 'Paris'       ],
    'jm'      => ['Prénom' => 'Jean'  , 'Nom' => 'Martin', 'Age' => 20, 'Ville' => 'Villetaneuse'],
    'toto'    => ['Prénom' => 'Tom'   , 'Nom' => 'Tonge' , 'Age' => 18, 'Ville' => 'Epinay'      ],
    'arn'     => ['Prénom' => 'Arnaud', 'Nom' => 'Dupond', 'Age' => 33, 'Ville' => 'Paris'       ],
    'email'   => ['Prénom' => 'Emilie', 'Nom' => 'Ailta' , 'Age' => 46, 'Ville' => 'Villetaneuse'],
    'dask'    => ['Prénom' => 'Damien', 'Nom' => 'Askier', 'Age' => 7 , 'Ville' => 'Villetaneuse']
  ];
  

if (isset($_POST["pseudo"]) == True && preg_match("#^\w+$#",$_POST["pseudo"])){ 
    //On vérifie si le pseudo est entré dans la zone de text et si il est composé d'au moins 1 caractère
    foreach ($personnes as $key => $value) 
    //On parcours les clés et valeurs du tableau 
        if ($_POST["pseudo"] == $key){ 
            //On vérifie si le pseudo correspond à la clé
            foreach ($value as $k => $v) 
            //On parcours le tableau de la clé 
                echo "$k : $v "; 
                //On affiche la clé et la valeur de cette dernière
            }
}

else echo "Désolé, votre pseudonyme n'apparait pas dans le tableau";
?>