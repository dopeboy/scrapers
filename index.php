<?php


    $dbname = "COMPETITORS";
    $dbuser = "root";
    $dbpass = '';
$dbhost="localhost";

        try 
        {
            $dbh = new PDO('mysql:host=' . $dbhost . ';dbname=' . $dbname, $dbuser, $dbpass);
            $dbh->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        }

        catch (PDOException $e) 
        {
            $dbh = null;
            print "Error!: " . $e->getMessage() . "<br/>";
            die();
        }

	$preparedStatement = $dbh->prepare('DESCRIBE MENU');
        $preparedStatement->execute();        
       $export_path = "/root/public_html/scrapers/exports/";
        
        $file = "menu_export_" . date("Ymd_His") . '.csv';
        $file2 = "menu_export_" . date("Ymd_His") . '.xls';
        $data = fopen($export_path . $file, 'w');
        $columns = array();
        
        while ($row = $preparedStatement->fetch(PDO::FETCH_COLUMN))
        {
            array_push($columns, $row);
        }    
        
        fputcsv($data, $columns);
        
        $preparedStatement = $dbh->prepare('SELECT * FROM MENU');
        $preparedStatement->execute();        

        while ($row = $preparedStatement->fetch(PDO::FETCH_ASSOC))
        {
            fputcsv($data, $row);
        }
	exec("unoconv --format  xls  " . $export_path . $file);
        
?>

<a href="<?php echo "exports/" . $file2?>"/>download excel</a>        




