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

    document.getElementById("myCanvas").addEventListener('mousedown', e => {

        if (!e.target.matches('td')) {
            return false;
        }
        setCellColor(e.target, "black");

    });

    //erase with double click
    $('td').dblclick(function(){
        setCellColor(this, "white");
    });

});

function setCellColor(cell, color) {
    cell.style.backgroundColor = color;
}