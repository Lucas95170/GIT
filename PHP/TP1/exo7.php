<?php
$personnes = [
  'mdupond' => ['Prénom' => 'Martin', 'Nom' => 'Dupond', 'Age' => 25, 'Ville' => 'Paris'       ],
  'jm'      => ['Prénom' => 'Jean'  , 'Nom' => 'Martin', 'Age' => 20, 'Ville' => 'Villetaneuse'],
  'toto'    => ['Prénom' => 'Tom'   , 'Nom' => 'Tonge' , 'Age' => 18, 'Ville' => 'Epinay'      ],
  'arn'     => ['Prénom' => 'Arnaud', 'Nom' => 'Dupond', 'Age' => 33, 'Ville' => 'Paris'       ],
  'email'   => ['Prénom' => 'Emilie', 'Nom' => 'Ailta' , 'Age' => 46, 'Ville' => 'Villetaneuse'],
  'dask'    => ['Prénom' => 'Damien', 'Nom' => 'Askier', 'Age' => 7 , 'Ville' => 'Villetaneuse']
];

// Question 1

if (isset($_GET["pseudo"]) && preg_match("#^\w+$#",$_GET["pseudo"])){ 
    //On vérifie si le pseudo est entré en url et si il est composé d'au moins 1 caractère
    foreach ($personnes as $key => $value) 
    //On parcours les clés et valeurs du tableau 
        if ($_GET["pseudo"] == $key){ 
            //On vérifie si le pseudo correspond à la clé
            foreach ($value as $k => $v) 
            //On parcours le tableau de la clé 
                echo "$k : $v "; 
                //On affiche la clé et la valeur de cette dernière
        }
    echo "Désolé, votre pseudonyme n'apparait pas dans le tableau";
}

?>