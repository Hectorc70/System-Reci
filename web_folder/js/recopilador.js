'use stric'



async function mostrarDirectorio(){
    let ruta = await eel.ruta_metadatos()();   
    document.getElementsByName("ruta-reci")[0].value = ruta;
    console.log(ruta);
}

async function mostrarEnTabla(){

    let directorio = document.getElementsByName("ruta-reci")[0].value;
    let rutas = await eel.mostrar_rutas_recibos(directorio)();
    const rutasNum = Object.getOwnPropertyNames(rutas);

    /* debugger; */
    for(let i=1; i<=rutasNum.length; i++){
        let lista = document.getElementById("tbl-datos");
        let tr = document.createElement("tr");
        
        let checkBox = document.createElement("input");
        checkBox.setAttribute("type", "checkbox");

        let columnaPer = document.createElement("td");        
        columnaPer.innerHTML = rutas[i].per;
        let columnaAnno = document.createElement("td");
        columnaAnno.innerHTML = rutas[i].anno;
        let columnaNom = document.createElement("td");
        columnaNom.innerHTML = rutas[i].nom;
        let columnaRuta = document.createElement("td");     
        columnaRuta.innerHTML = rutas[i].ruta;        
        
        lista.appendChild(tr);  
        tr.appendChild(checkBox);      
        tr.appendChild(columnaPer);
        tr.appendChild(columnaAnno);
        tr.appendChild(columnaNom);
        tr.appendChild(columnaRuta);

        

    
    
}
}
