async function mostrarRutas() {
    /* 
        let datos = document.getElementById("tbl-datos");
        datos.removeChild(tr) */

    let tabla = document.getElementById("tbl");
    let carga = document.createElement("div");
    let ruta = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;
    carga.setAttribute("class", "loading");
    tabla.appendChild(carga);

    let recibos = await eel.rutas_recibos_orig(ruta, anno, periodo)();
    const recibosNum = Object.getOwnPropertyNames(recibos);

    for (let i = 0; i < recibosNum.length; i++) {
        let lista = document.getElementById("tbl-datos");
        let tr = document.createElement("tr");
        let checkBox = document.createElement("input");
        checkBox.setAttribute("type", "checkbox");
        checkBox.setAttribute("class", "c-box");


        let ultimo = recibos[recibosNum[i]]["length"];

        let columnaPeriodo = document.createElement("td");
        columnaPeriodo.setAttribute("class", "cl-per")
        columnaPeriodo.innerHTML = recibos[recibosNum[i]][3];
        let columnaNomina = document.createElement("td");
        columnaNomina.innerHTML = recibos[recibosNum[i]][4];
        let columnaArchivo = document.createElement("td");
        columnaArchivo.setAttribute("class", "ruta-archivo");
        columnaArchivo.innerHTML = recibos[recibosNum[i]][ultimo - 1];


        lista.appendChild(tr);
        tr.appendChild(columnaPeriodo);
        columnaPeriodo.appendChild(checkBox);
        tr.appendChild(columnaNomina);
        tr.appendChild(columnaArchivo);

    }
    tabla.removeChild(carga);
}


function iniciarCopiado() {
    let carp_orig = document.getElementsByName("ruta")[0].value;
    let carp_dest = document.getElementsByName("ruta_destino")[0].value;
    let archivos = [];
    let filaPeriodo = document.getElementsByClassName("cl-per");

    if (carp_dest != '' & carp_orig != '' &
        filaPeriodo.length > 0){
        for (let i = 0; i < filaPeriodo.length; i++) {
            checkBox = filaPeriodo[i].getElementsByClassName("c-box");

            if (checkBox[0].checked == true) {
                let filaRuta = document.getElementsByClassName("ruta-archivo")[i].innerText;
                archivos.push(filaRuta);
            }
            
        }

    }
    else {
        alert('Se debe seleccionar Directorios de Destino Y/O Origen y buscar Archivos Primero');
    }

    if(archivos.length > 0){
        deshabilitar('principal');
        loader_tarea();
        eel.copiado_recibos(carp_orig, carp_dest, archivos);
    }
    
    else{
        alert('Seleccione almenos una fila');
    }

    habilitar('principal');
    
}