<?php
include ('init.php');

session_start();
$upload_dir = "uploads/";
$upload_check = 1;
$imageFileType = strtolower(pathinfo($_FILES["legpic"]["name"], PATHINFO_EXTENSION));
$file_ = $upload_dir . md5(random_bytes(32)) . '.' . $imageFileType;

if (isset($_POST["submit"]) && isset($_POST['token'])) {
	$check = getimagesize($_FILES["legpic"]["tmp_name"]);
	if ($check !== false) {
		$upload_check = 1;
	}
	else {
		$upload_check = 0;
	}

	$t = $_POST['token'];
	if ($t != $_SESSION['csrf_token']) {
		die("Token tidak valid!");
	}

	$_SESSION['csrf_token'] = base64_encode(openssl_random_pseudo_bytes(32));
    
    if ($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg" && $imageFileType != "gif") {
		$upload_check = 0;
	}

	if ($upload_check == 0 || !move_uploaded_file($_FILES["legpic"]["tmp_name"], $file_)) {
		die("gagal upload :(");
	}

	$exif = exif_read_data($file_);
	parse_str($exif['ImageDescription'], $exif);
	if(!$exif) die("Gambar tidak valid!");
	$leg = SQLite3::escapeString($exif['leg']);
    
    $db->exec("DELETE FROM Legs Where Session='{$_SESSION['session_token']}';");
	query("INSERT INTO Legs (Session, Leg) VALUES ('{$_SESSION['session_token']}', {$leg})");
	unlink($file_);
    
    $dir = "results/";
	$fname = $dir . sha1(openssl_random_pseudo_bytes(32)) . '.php';
	$f = fopen($fname, "w");
    
    $result = $db->query("SELECT Leg FROM Legs Where Session='{$_SESSION['session_token']}' Limit 1");
	if (count($result) == 1) {
		foreach($result as $res) {
			if ($res['Leg'] == '1') {
				fwrite($f, 'Satu kaki');
			}
			else
			if ($res['Leg'] == '2') {
				fwrite($f, 'Dua kaki');
			}
			else {
				fwrite($f, 'Tidak diketahui');
			}
		}
	}

	fwrite($f, "<?php unlink(__FILE__); ?>");
	fclose($f);
	header("Location: /{$fname}");
	$db = NULL;
}

die();
?>