<?php $mois = [
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre"
];



echo "<ol>";
foreach($mois as $c => $v){
    echo "<li> $v </li>";
  }
echo "</ol>";

$mois2 = [
   "janvier"   => 31,
   "février"   => 28,
   "mars"      => 31,
   "avril"     => 30,
   "mai"       => 31,
   "juin"      => 30,
   "juillet"   => 31,
   "août"      => 31,
   "septembre" => 30,
   "octobre"   => 31,
   "novembre"  => 30,
   "décembre"  => 31
];

echo "<ol>";
  foreach($mois2 as $c => $v){
    echo "<li> $c : $v </li>";
  }
echo "</ol>"; ?>
