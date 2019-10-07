<?php

$tabMagazines = [
  'le monde'              => ['frequence' => 'quotidien', 'type' => 'actualité', 'prix' => 220],
  'le point'              => ['frequence' => 'hebdo'    , 'type' => 'actualité', 'prix' => 80 ],
  'causette'              => ['frequence' => 'mensuel'  , 'type' => 'féministe', 'prix' => 180],
  'politis'               => ['frequence' => 'hebdo'    , 'type' => 'opinion'  , 'prix' => 100],
  'le monde diplomatique' => ['frequence' => 'mensuel'  , 'type' => 'analyse'  , 'prix' => 60 ]
];

$tabMagazinesAbonne = ['le monde', 'le monde diplomatique'];

#Question 1
$tab = array_keys($tabMagazines);
sort($tab);
$pastest = implode(" , ", $tab);
echo "$pastest";


#Question 2
echo "<ul>";
$y=0;
foreach($tabMagazines as $key => $val){
  echo "<li> $key (";
  $c = array_keys($tabMagazines)[$y];
  $v = $tabMagazines[$c];
  foreach($v as $k => $fin){
    if ($k=="prix")
      echo "$fin";
    else echo "$fin, ";
  }
  echo ") </li>";
  $y+=1;
}
echo "</ul>"


#Question3
$calcule=0;
  foreach($tabMagazinesAbonne as $val){
  $so = $tabMagazines[$val]['prix'];
  $calcule += $so;
  }
  echo "Le prix totals est : $calcule";
 ?>
