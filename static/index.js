let drawarea=document.getElementById("myCanvas");

// let img=new Image();
// let context = drawarea.getContext('2d');
// context.drawImage(img,0,0);
// context.fillStyle = '#05EFFF';
// context.fillRect(0, 0, 150, 100);

$(document).ready(function(){
    let rows=30;
    let cols=30;
    for(i=0; i<rows; i++){
        drawarea.innerHTML+="<tr class='table_row'></tr>";
    
    }
    for(j=0; j<cols; j++){
        $('tr').append("<td class='cell'></td>");

    }
    
    const cells = document.querySelectorAll('.cell');
    for (i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', function (event) {    
        const color = "black";
        event.target.style.backgroundColor = color;
        });
    }
});


// draw on canvas
// function drawing(event){
//     let pageW=parseInt(document.body.clientWidth);
//     let posx=event.pageX-((pageW-500)/2);
//     let posy=event.pageY-97;
//     // console.log(`${posx},${posy}`);
//     // console.log(pageW);
    
//     context.fillStyle = '#05EFFF';
//     context.fillRect(posx*0.6, posy*0.37, 5, 5);

//     //img url - need to send to python and decode there
//     let dataUrl = drawarea.toDataURL();
//     console.log(dataUrl);

    

// }
// drawarea.addEventListener("click",drawing);











