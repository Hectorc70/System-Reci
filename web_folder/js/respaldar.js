async function mostrarRutas(){
    /* 
        let datos = document.getElementById("tbl-datos");
        datos.removeChild(tr) */
        
        let tabla =document.getElementById("tbl");  
        let carga = document.createElement("div");
        carga.setAttribute("class", "loading");    
        tabla.appendChild(carga);    
        
        let recibos = await eel.rutas_recibos_orig()();
        const recibosNum = Object.getOwnPropertyNames(recibos);
            
        debugger;
        for(let i=0; i<recibosNum.length; i++){
            let lista = document.getElementById("tbl-datos");
            let tr = document.createElement("tr");      
            let checkBox = document.createElement("input");
            checkBox.setAttribute("type", "checkbox");
            checkBox.setAttribute("class", "c-box");
            
    
            let ultimo = recibos[recibosNum[i]]["length"];
            let columnaPeriodo = document.createElement("td");
            columnaPeriodo.innerHTML = recibos[recibosNum[i]][3];
            let columnaNomina = document.createElement("td");
            columnaNomina.innerHTML = recibos[recibosNum[i]][4];    
            let columnaArchivo = document.createElement("td");     
            columnaArchivo.innerHTML = recibos[recibosNum[i]][ultimo-1];   
                
            
            lista.appendChild(tr);               
            tr.appendChild(columnaPeriodo);
            columnaPeriodo.appendChild(checkBox); 
            tr.appendChild(columnaNomina);
            tr.appendChild(columnaArchivo);
        
        }
        tabla.removeChild(carga);
    }
    