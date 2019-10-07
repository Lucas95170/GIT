<!DOCTYPE html>
<html>
<head>
<title>header</title>
	<meta charset="utf-8">
	<link rel="stylesheet" type="text/css">
</head>
<body>
    <form action = "Formulaire.php" method="post">
    Votre id : <input type = "text" name = "identify"><br />
    Votre mdp : <input type = "text" name = "password"><br />
    <input type = "submit" value = "Envoyer"><br />

    <?php
        if (isset($_POST["identify"]) && isset($_POST["password"])) {
            echo 'Votre nom est '.$_POST["identify"].' et votre mot de passe est '.$_POST["password"];
        }
    ?>
</body>
</html>