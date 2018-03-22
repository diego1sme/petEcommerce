<?php

    function loop_array($array = array(), $parent_id=0){
        if(!empty($array[$parent_id])){

        echo '<ul class = "dropbtn">';
        foreach($array[$parent_id] as $items){
        echo '<li>';
        echo $items['type'];
        loop_array($array,$items['id']);
        echo '</li>';
        }
        echo '</ul>';
        }
    }

    function displayMenus(){
        $con = mysqli_connect("localhost","root","","petsecommerce");
        $query = $con->query("SELECT * FROM animaltype");
        $array = array();

        if(mysqli_num_rows($query)){
            while($rows = mysqli_fetch_array($query)){
                $array[$rows['parent_id']][]=$rows;
            }
            loop_array($array);
        }
    }

?>