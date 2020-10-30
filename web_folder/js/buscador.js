'use strict'

function enviarDatosBusqueda() {

    let control = document.getElementsByName("control")[0].value;
    let ruta = document.getElementsByName("ruta-masivo")[0].value;
    if (ruta != '') {
        buscarVariosEmpleados()
    }
    else if (control != '') {
        mostrarRecibos()
    }

    else {
        Precaucion('Escriba un numero de control para poder Buscar\
        O seleccione archivo de carga masiva');
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


                    let columnaCtrl = document.createElement("td");
                    columnaCtrl.innerHTML = recibos[recibosNum[i]][1];
                    columnaCtrl.setAttribute("class", "cl-ctrl");
                    columnaCtrl.appendChild(checkBox)

                    let columnaId = document.createElement("td");
                    columnaId.setAttribute("class", "cl-id  ocultar-colum");
                    columnaId.innerHTML = recibos[recibosNum[i]][0];

                    let columnaPeriodo = document.createElement("td");
                    columnaPeriodo.setAttribute("class", "cl-per");
                    columnaPeriodo.innerHTML = recibos[recibosNum[i]][2];

                    let columnaAnno = document.createElement("td");
                    columnaAnno.setAttribute("class", "cl-anno");
                    columnaAnno.innerHTML = recibos[recibosNum[i]][3];

                    let columnaNom = document.createElement("td");
                    columnaNom.setAttribute("class", "cl-nom");
                    columnaNom.innerHTML = recibos[recibosNum[i]][4];

                    let columnaArchivo = document.createElement("td");
                    columnaArchivo.setAttribute("class", "cl-ruta ocultar-colum");
                    columnaArchivo.innerHTML = recibos[recibosNum[i]][5];

                    let columnaV = document.createElement("td");
                    let opcionVer = document.createElement("button");
                    opcionVer.setAttribute("class", "btn btn-ver");
                    opcionVer.setAttribute("onclick", "verRecibo()");
                    opcionVer.innerHTML = "Ver";


                    lista.appendChild(tr);
                    tr.appendChild(columnaCtrl);
                    columnaCtrl.appendChild(checkBox);

                    tr.appendChild(columnaId);
                    tr.appendChild(columnaPeriodo);
                    tr.appendChild(columnaAnno);
                    tr.appendChild(columnaNom);
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
    let filaControl = document.getElementsByClassName("cl-ctrl");
    debugger;
    for (let i = 0; i < filaControl.length; i++) {
        let checkBox = filaControl[i].getElementsByClassName("c-box");
        if (checkBox[0].checked == true) {
            let filaId = document.getElementsByClassName("cl-id")[i].innerText;
            let filaPer = document.getElementsByClassName("cl-per")[i].innerText;
            let filaAnno = document.getElementsByClassName("cl-anno")[i].innerText;
            let filaNomina = document.getElementsByClassName("cl-nom")[i].innerText;
            let filaRuta = document.getElementsByClassName("cl-ruta")[i].innerText;
            
            let datos = [];
            datos = [filaControl[i].innerText, filaId, filaPer, filaAnno, filaNomina, filaRuta]
            recibos.push(datos);
        }
    }

    debugger;
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


async function verRecibo() {
    let visualizador = document.getElementById("overlay");
    visualizador.removeAttribute("class");
    deshabilitar("menu")
}

async function salirVerRecibo() {
    let visualizador = document.getElementById("overlay");
    visualizador.setAttribute("class", "no-mostrar")
    habilitarElemento("menu")
}


/* VISOR DE PDF'S */


async function VerPdf() {
    pdfjsLib.getDocument('../img/Control_ORDINARIA_202019.pdf').then((pdf) => {

    });
}