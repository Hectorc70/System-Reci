async function mostrarRutas() {
    /* 
        let datos = document.getElementById("tbl-datos");
        datos.removeChild(tr) */

    /* let tabla = document.getElementById("tbl");
    let carga = document.createElement("div"); */
    let ruta = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;


    if (ruta != '' && anno != '' && periodo != '') {
        carga.setAttribute("class", "loading");
        tabla.appendChild(carga);
        debugger;
        let rutas = await eel.rutas_timbres_orig(ruta, periodo, anno)();
        const rutasNum = Object.getOwnPropertyNames(rutas);


        for (let i = 1; i < rutasNum.length; i++) {
            let lista = document.getElementById("tbl-datos");
            let tr = document.createElement("tr");
            let checkBox = document.createElement("input");
            checkBox.setAttribute("type", "checkbox");
            checkBox.setAttribute("class", "c-box");


            /* let ultimo = recibos[recibosNum[i - 1]]["length"]; */

            let columnaPeriodo = document.createElement("td");
            columnaPeriodo.setAttribute("class", "cl-per")
            columnaPeriodo.innerHTML = rutas[i][0];
            
            let columnaNomina = document.createElement("td");
            columnaNomina.innerHTML = rutas[i][1];
            
            let columnaArchivo = document.createElement("td");
            columnaArchivo.setAttribute("class", "ruta-archivo");
            columnaArchivo.innerHTML = rutas[i][2];


            lista.appendChild(tr);
            tr.appendChild(columnaPeriodo);
            columnaPeriodo.appendChild(checkBox);
            tr.appendChild(columnaNomina);
            tr.appendChild(columnaArchivo);

        }
      
    }
    else Precaucion('Seleccione Ruta, Año y Periodo');
}


async function iniciarCopiado() {
    let carp_orig = document.getElementsByName("ruta")[0].value;
    let carp_dest = document.getElementsByName("ruta_destino")[0].value;
    let archivos = [];
    let filaPeriodo = document.getElementsByClassName("cl-per");

    if (filaPeriodo.length > 0) {
        for (let i = 0; i < filaPeriodo.length; i++) {
            checkBox = filaPeriodo[i].getElementsByClassName("c-box");

            if (checkBox[0].checked == true) {
                let filaRuta = document.getElementsByClassName("ruta-archivo")[i].innerText;
                archivos.push(filaRuta);
            }

        }
        if (archivos.length > 0 && carp_dest != '') {

            if (carp_orig != carp_dest) {
                deshabilitar('principal');
                loader_tarea();
                let proceso = await eel.copiado_recibos(carp_orig, carp_dest, archivos)();
                if (proceso == true) {
                    habilitar('principal');                    
                }
                satisfactorio('Archivos Copiados');
            }
            else{
                Precaucion('La ruta de Destino y la Original No pueden ser la misma');
            }
        }

        else {
            Precaucion('Seleccione almenos una fila y la ruta de Destino');
        }

    }
    else {
        Precaucion('Debe buscar primero los Archivos');
    }




}