function enviarDatosBusqueda(){
    let control = document.getElementsByName("control")[0].value;
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;
  

    if (annoIni < annoFin || annoIni == annoFin){       
        eel.obtener_reci_buscados(control, periodoIni, annoIni, periodoFin, annoFin);
    }
    else{
        alert('los Años no son validos')
    }

}



async function mostrarDirGuardado(){
    let directorio = await eel.ruta_metadatos()();     
    
    document.getElementsByName("ruta")[0].value = directorio;    
    
}


async function mostrarRecibos(){
    /* 
        let datos = document.getElementById("tbl-datos");
        datos.removeChild(tr) */
        
        let tabla =document.getElementById("tbl");  
        let carga = document.createElement("div");
        carga.setAttribute("class", "loading");    
        tabla.appendChild(carga);
    
        let control = document.getElementsByName("control")[0].value;
        let periodoIni = document.getElementsByName("periodo-ini")[0].value;
        let annoIni = document.getElementsByName("anno-ini")[0].value;
        let periodoFin = document.getElementsByName("periodo-fin")[0].value;
        let annoFin = document.getElementsByName("anno-fin")[0].value;
        
        let recibos = await eel.obtener_reci_buscados(control, periodoIni, annoIni, periodoFin, annoFin)();
        const recibosNum = Object.getOwnPropertyNames(recibos);
            
        /* debugger; */
        for(let i=0; i<recibosNum.length; i++){
            let lista = document.getElementById("tbl-datos");
            let tr = document.createElement("tr");      
            let checkBox = document.createElement("input");
            checkBox.setAttribute("type", "checkbox");
            checkBox.setAttribute("class", "c-box");
            
    
            let columnaId = document.createElement("td"); 
            columnaId.setAttribute("class", "cl-id");    
            columnaId.innerHTML = recibos[recibosNum[i]][0];
            columnaId.appendChild(checkBox)    
            let columnaPeriodo = document.createElement("td");
            columnaPeriodo.innerHTML = recibos[recibosNum[i]][1];
            let columnaAnno = document.createElement("td");
            columnaAnno.innerHTML = recibos[recibosNum[i]][2];    
            let columnaArchivo = document.createElement("td");     
            columnaArchivo.innerHTML = recibos[recibosNum[i]][4];   
                
            
            lista.appendChild(tr);  
            tr.appendChild(columnaId);
            columnaId.appendChild(checkBox);      
            tr.appendChild(columnaPeriodo);
            tr.appendChild(columnaAnno);
            tr.appendChild(columnaArchivo);
        
        }
        tabla.removeChild(carga);
    }
    



async function EnviarDatosExtraccion(){
    
    let ruta = document.getElementsByName("ruta")[0].value;
    let control = document.getElementsByName("control")[0].value;
    let tabla =document.getElementById("tbl");
    let carga = document.createElement("div");
    carga.setAttribute("class", "loading");    
    tabla.appendChild(carga);

    if(ruta != ''){
                
        let recibos = [];
        let filaId = document.getElementsByClassName("cl-id");     

    
        for(let i=0; i<filaId.length; i++){
            
            
            checkBox = filaId[i].getElementsByClassName("c-box");
            
            if(checkBox[0].checked == true){
                recibos.push(filaId[i].innerText);
            }
        }
        
        if(recibos.length >0){
            let reci = await eel.buscador_recibo(recibos, ruta)();
            debugger;
            if(reci==true){
                tabla.removeChild(carga);
                alert("Se Guardaron todos los Recibos en: "+ ruta + "/" + control)
            }
        }
        else{
            alert("seleccione Todo o algun Registro")
        }

        
        
        
    } 
    else{
        alert("Seleccione ruta de guardado")
    }
   
}   
