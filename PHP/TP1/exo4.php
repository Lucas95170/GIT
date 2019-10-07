<?php

$personnes = [
  'mdupond' => ['Prénom' => 'Martin', 'Nom' => 'Dupond', 'Age' => 25, 'Ville' => 'Paris'       ],
  'jm'      => ['Prénom' => 'Jean'  , 'Nom' => 'Martin', 'Age' => 20, 'Ville' => 'Villetaneuse'],
  'toto'    => ['Prénom' => 'Tom'   , 'Nom' => 'Tonge' , 'Age' => 18, 'Ville' => 'Epinay'      ],
  'arn'     => ['Prénom' => 'Arnaud', 'Nom' => 'Dupond', 'Age' => 33, 'Ville' => 'Paris'       ],
  'email'   => ['Prénom' => 'Emilie', 'Nom' => 'Ailta' , 'Age' => 46, 'Ville' => 'Villetaneuse'],
  'dask'    => ['Prénom' => 'Damien', 'Nom' => 'Askier', 'Age' => 7 , 'Ville' => 'Villetaneuse']
];

$scores = [
  ['Joueur' => 'Camille'  , 'score' => 156 ],
  ['Joueur' => 'Guillaume', 'score' => 254 ],
  ['Joueur' => 'Julien'   , 'score' => 192 ],
  ['Joueur' => 'Nabila'   , 'score' => 317 ],
  ['Joueur' => 'Lorianne' , 'score' => 235 ],
  ['Joueur' => 'Tom'      , 'score' => 83  ],
  ['Joueur' => 'Michael'  , 'score' => 325 ],
  ['Joueur' => 'Eddy'     , 'score' => 299 ]
];

function tableEnHtml($tab){
  $c1 = array_keys($tab)[0];      #correspond à la clef "mdupond"
  $v1 = $tab[$c1];                #correspond à la clef "Prénom" de la clef "mdupond"
  foreach($v1 as $c2 => $fin){    #permet de récupérer toutes les clefs de la clef "mdupond"
    echo "<td> $c2 </td>";        #écrit toues les clefs
  }

  echo "<table>";

  foreach($tab as $c => $v){
    echo "<tr>";

    foreach($v as $k => $vv){
      echo "<td> $vv </td>";
    }
    echo "</tr>";
  }
  echo "</table>";
}

tableEnHtml($scores);
//tableEnHtml($personnes);
?>
