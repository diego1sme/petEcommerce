<?php

    function loop_array($array = array(),id=0){
        if(!empty($array[$id])){

        echo '<ul class = "dropbtn">';
        foreach($array[$id] as $items){
        echo '<li>';
        echo $items['type'];
        loop_array($array,$items['id']);
        echo '</li>';
        }
        echo '</ul>';
        }
    }

    function display_menus(){
        $con = mysqli_connect("localhost","root","","petsecommerce");
        if (mysqli_connect_errno()){
        echo "Failed to connect to MySQL: " . mysqli_connect_error();
         }
        //$query = $con->query("SELECT * FROM animaltype");
        mysqli_query($con,"SELECT * FROM animaltype");
        $array = array();

        if(mysqli_num_rows($query)){
            while($rows = mysqli_fetch_array($query)){
                $array[$rows['id']][]=$rows;
            }
            loop_array($array);
        }
    }

?>