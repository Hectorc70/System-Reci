'use strict'

function enviarDatosBusqueda() {

    let control = document.getElementsByName("control")[0].value; 
    let ruta = document.getElementsByName("ruta-masivo")[0].value;
    if (ruta != '') {
        buscarVariosEmpleados()
    }
    if (control != '') {
        mostrarRecibos()
    }
}



async function mostrarRecibos() {
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;

    if (periodoIni != '' && annoIni != '' &&
        periodoFin != '' && annoFin != '') {

        if (annoIni < annoFin || annoIni == annoFin) {
            deshabilitar('principal');
            loader_tarea();
            let control = document.getElementsByName("control")[0].value;          
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
                    let columnaV = document.createElement("td");
                    let opcionVer = document.createElement("button");                   
                    opcionVer.setAttribute("class","btn btn-ver");
                    opcionVer.setAttribute("onclick", "verRecibo()");
                    opcionVer.innerHTML = "Ver";


                    lista.appendChild(tr);
                    tr.appendChild(columnaId);
                    columnaId.appendChild(checkBox);
                    tr.appendChild(columnaPeriodo);
                    tr.appendChild(columnaAnno);
                    tr.appendChild(columnaArchivo);
                    tr.appendChild(columnaV);
                    columnaV.appendChild(opcionVer)

                }

            }
            else {
                error('No se encontro ningun registro en la Base de Datos.\
                        Nota: Revise las fechas, periodos o numero de control seleccionados.')
            }
        }
        else {
            Precaucion('Los Años Seleccionados no son validos');
        }
    }
    else {
        Precaucion('Seleccione Fechas Validas y/o Inserte un numero de control.');
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

async function buscarVariosEmpleados() {
    let ruta = document.getElementsByName("ruta-masivo")[0].value;
    let controles = await eel.leer_txt(ruta)();
    const controlNum = Object.getOwnPropertyNames(controles);
    debugger;
    for (let i = 1; i < controlNum.length; i++) {
        document.getElementsByName("control")[0].value = controles[i - 1];
        mostrarRecibos();
    }
    document.getElementsByName("control")[0].value = '';

}


async function verRecibo(){
    let visualizador = document.getElementById("overlay");
    visualizador.removeAttribute("class");
    deshabilitar("menu")
}

async function salirVerRecibo(){
    let visualizador = document.getElementById("overlay");
    visualizador.setAttribute("class", "no-mostrar")
    habilitarElemento("menu")
}


/* VISOR DE PDF'S */


async function VerPdf(){
    pdfjsLib.getDocument('../img/Control_ORDINARIA_202019.pdf').then((pdf) => {
        
    });
}