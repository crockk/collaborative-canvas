let drawarea=document.getElementById("myCanvas");

$(document).ready(function(){
    let rows=30;
    let cols=30;
    let id = 0;
    for(i=0; i<rows; i++){
        drawarea.innerHTML+="<tr class='table_row'></tr>";
    
    }
    for(j=0; j<cols; j++){
        $('tr').append("<td class='cell' id='p"+id+"'></td>");
        id++;
    }
    
    const cells = document.querySelectorAll('.cell');
    for (i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', function (event) {    
        const color = "black";
        event.target.style.backgroundColor = color;
        });
    }
});












