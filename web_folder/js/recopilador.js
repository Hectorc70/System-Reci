'use stric'



async function mostrarDirectorio(){
    let directorio = await eel.ruta_metadatos()();     

    document.getElementsByName("ruta-reci")[0].value = directorio;
    
    console.log(directorio);

    mostrarEnTabla()
}

async function mostrarEnTabla(){

    let directorio = document.getElementsByName("ruta-reci")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;
    let rutas = await eel.mostrar_rutas_recibos(directorio)();
    const rutasNum = Object.getOwnPropertyNames(rutas);

    /* debugger; */
    for(let i=1; i<=rutasNum.length; i++){
        let lista = document.getElementById("tbl-datos");
        let tr = document.createElement("tr");      
        let checkBox = document.createElement("input");
        checkBox.setAttribute("type", "checkbox");
        checkBox.setAttribute("class", "c-box");
        

        let columnaPer = document.createElement("td"); 
        columnaPer.setAttribute("class", "cl-per");    
        columnaPer.innerHTML = rutas[i].per;
        columnaPer.appendChild(checkBox)

        let columnaAnno = document.createElement("td");
        columnaAnno.innerHTML = rutas[i].anno;
        let columnaNom = document.createElement("td");
        columnaNom.innerHTML = rutas[i].nom;

        let columnaRuta = document.createElement("td");     
        columnaRuta.innerHTML = rutas[i].ruta;   
        columnaRuta.setAttribute("class", "cl-ruta");    
        
        lista.appendChild(tr);                 
        columnaPer.appendChild(checkBox);
        tr.appendChild(columnaPer);      
        tr.appendChild(columnaAnno);
        tr.appendChild(columnaNom);
        tr.appendChild(columnaRuta);

        

    
    
}
}




function elementosTabla(){
    let filaPer = document.getElementsByClassName("cl-per");
    debugger;
    for(let i=1; i<=filaPer.length; i++){

        checkBox = filaPer[i].getElementsByClassName("c-box");
        if(checkBox[0].checked == true){
            let filaRuta = document.getElementsByClassName("cl-ruta")[0].value;
            console.log('fila seleccionada ' + filaRuta);
        }
        else{
            console.log("fila no seleccionada");
        }
    }

    
} 