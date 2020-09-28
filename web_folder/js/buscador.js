'use strict'

function enviarDatosBusqueda() {
    let control = document.getElementsByName("control")[0].value;
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;

    if (periodoIni != '' && annoIni != '' &&
        periodoFin != '' && annoFin != '' && control != '') {

        if (annoIni < annoFin || annoIni == annoFin) {
            mostrarRecibos()          
        }
        else {
            Precaucion('Los Años Seleccionados no son validos');
        }
    }

    else {
        Precaucion('Seleccione Fechas Validas y/o Inserte un numero de control.');
    }

}



async function mostrarRecibos() { 
    deshabilitar('principal');
    loader_tarea();
    let control = document.getElementsByName("control")[0].value;
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;
    let recibos = await eel.obtener_reci_buscados(control, periodoIni, annoIni, periodoFin, annoFin)();
    const recibosNum = Object.getOwnPropertyNames(recibos);
    habilitar('principal');
    if (recibos != false) {        
        for (let i = 0; i < recibosNum.length; i++) {
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
       
    }
    else{
        error('No se encontro ningun registro en la Base de Datos.\
            Nota: Revise las fechas, periodos o numero de control seleccionados.')
    }
}




async function EnviarDatosExtraccion() {

    let ruta = document.getElementsByName("ruta-guardado")[0].value;
    let control = document.getElementsByName("control")[0].value;
    let recibos = [];
    let filaId = document.getElementsByClassName("cl-id");

    for (let i = 0; i < filaId.length; i++) {
        let checkBox = filaId[i].getElementsByClassName("c-box");
        if (checkBox[0].checked == true) {
            recibos.push(filaId[i].innerText);
        }
    }

    if (ruta != '' & recibos.length > 0) {
        deshabilitar('principal');
        loader_tarea();
        let reci = await eel.buscador_recibo(recibos, ruta)();
        if (reci == true) {
            habilitar('principal');
            satisfactorio("Se Guardaron todos los Recibos en: " + ruta + "/" + control)
        }
    }

    else {
        Precaucion("Seleccione ruta de guardado, Y Recibo(s) para extraer");
    }

}   
