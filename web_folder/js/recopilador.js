'use stric'


async function mostrarDirectorio(){
    var periodoIn = document.getElementsByName("periodo")[0].value;
    var annoIn = document.getElementsByName("anno")[0].value;

    
    if(periodoIn!=='' && annoIn !== ''){

        let directorio = await eel.ruta_metadatos()();     
    
        document.getElementsByName("ruta-reci")[0].value = directorio;
    
        console.log(directorio);
    mostrarEnTabla()
    }
    else{
        alert("Escribe un Año y Periodo para continuar")
    }
    
}

async function mostrarEnTabla(){

    let directorio = document.getElementsByName("ruta-reci")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;
    let rutas = await eel.mostrar_rutas_recibos(directorio, periodo)();
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
    var rutas = [];
    let filaPer = document.getElementsByClassName("cl-per");
    let anno = document.getElementsByName("anno")[0].value;
    for(let i=0; i<filaPer.length; i++){

        checkBox = filaPer[i].getElementsByClassName("c-box");
        if(checkBox[0].checked == true){
            let filaRuta = document.getElementsByClassName("cl-ruta")[i].innerText;
            rutas.push(filaRuta);
        }
        else{
            console.log("fila no seleccionada");
        }
    }

    eel.guardar_mdatos(rutas, anno)();

    
} 