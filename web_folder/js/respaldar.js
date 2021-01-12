'use strict'

function comprobarOpcionMostrar() {
    let rBtnRecibos = document.getElementById('op-recibos');
    let rBtnTimbres = document.getElementById('op-timbres');   

    if (rBtnRecibos.checked == true) {
        mostrarRutasRecibos();
    }
    else if (rBtnTimbres.checked == true) {
        mostrarRutasTimbres();
    }
    

}

function comprobarOpcionCopiar(){
    let rBtnRecibos = document.getElementById('op-recibos');
    let rBtnTimbres = document.getElementById('op-timbres');


    if (rBtnRecibos.checked == true) {
        iniciarCopiadoRecibos();
    }
    else if (rBtnTimbres.checked == true) {
        iniciarCopiadoTimbres();
    }
}
async function mostrarRutasRecibos() {


    
    let ruta = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;


    if (ruta != '' && anno != '' && periodo != '') {



        let rutas = await eel.rutas_recibos_orig(ruta, anno, periodo)();
        const rutasNum = Object.getOwnPropertyNames(rutas);

        deshabilitar('principal');
        loader_tarea();
        for (let i = 1; i < rutasNum.length; i++) {
            let lista = document.getElementById("tbl-datos");
            let tr = document.createElement("tr");
            let checkBox = document.createElement("input");
            checkBox.setAttribute("type", "checkbox");
            checkBox.setAttribute("class", "c-box");


            /* let ultimo = recibos[recibosNum[i - 1]]["length"]; */

            let columnaPeriodo = document.createElement("td");
            columnaPeriodo.setAttribute("class", "cl-per")
            columnaPeriodo.innerHTML = rutas[i-1][0];

            let columnaNomina = document.createElement("td");
            columnaNomina.innerHTML = rutas[i-1][1];

            let columnaArchivo = document.createElement("td");
            columnaArchivo.setAttribute("class", "ruta-archivo");
            columnaArchivo.innerHTML = rutas[i-1][2];


            lista.appendChild(tr);
            tr.appendChild(columnaPeriodo);
            columnaPeriodo.appendChild(checkBox);
            tr.appendChild(columnaNomina);
            tr.appendChild(columnaArchivo);

        }
        habilitar('principal');

    }
    else Precaucion('Seleccione Ruta, Año y Periodo');
}

async function mostrarRutasTimbres() {
    /* 
        let datos = document.getElementById("tbl-datos");
        datos.removeChild(tr) */

    
    let ruta = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;


    if (ruta != '' && anno != '' && periodo != '') {


        deshabilitar('principal');
        loader_tarea();
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
            columnaPeriodo.innerHTML = rutas[i-1][0];

            let columnaNomina = document.createElement("td");
            columnaNomina.innerHTML = rutas[i-1][1];

            let columnaArchivo = document.createElement("td");
            columnaArchivo.setAttribute("class", "ruta-archivo");
            columnaArchivo.innerHTML = rutas[i-1][2];


            lista.appendChild(tr);
            tr.appendChild(columnaPeriodo);
            columnaPeriodo.appendChild(checkBox);
            tr.appendChild(columnaNomina);
            tr.appendChild(columnaArchivo);

        }
        habilitar('principal');
    }
    else Precaucion('Seleccione Ruta, Año y Periodo');
}


async function iniciarCopiadoRecibos() {
    let carp_orig = document.getElementsByName("ruta")[0].value;
    let carp_dest = document.getElementsByName("ruta_destino")[0].value;
    let archivos = [];
    let filaPeriodo = document.getElementsByClassName("cl-per");

    if (filaPeriodo.length > 0) {
        for (let i = 0; i < filaPeriodo.length; i++) {
            let checkBox = filaPeriodo[i].getElementsByClassName("c-box");

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
                debugger;
                if (proceso[1] == true && proceso[0] != 'ERRORES') {
                    habilitar('principal');
                    satisfactorio('Archivos Copiados Sin errores');
                }
                else if(proceso[0] == 'ERRORES'){
                    habilitar('principal');
                    Precaucion('Archivos Copiado, Pero Hubo errores de Copiado');
                }
                else{
                    error('ERROR INESPERADO INTENTE CORRER NUEVAMENTE EL PROCESO');
                }
            }
            else {
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

async function iniciarCopiadoTimbres() {
    let carp_orig = document.getElementsByName("ruta")[0].value;
    let carp_dest = document.getElementsByName("ruta_destino")[0].value;
    let archivos = [];
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;

    let filaPeriodo = document.getElementsByClassName("cl-per");

    if (filaPeriodo.length > 0) {
        for (let i = 0; i < filaPeriodo.length; i++) {
            let checkBox = filaPeriodo[i].getElementsByClassName("c-box");

            if (checkBox[0].checked == true) {
                let filaRuta = document.getElementsByClassName("ruta-archivo")[i].innerText;
                archivos.push(filaRuta);
            }

        }
        debugger;
        if (archivos.length > 0 && carp_dest != '') {
            
            if (carp_orig != carp_dest) {
                deshabilitar('principal');
                loader_tarea();
                let proceso = await eel.copiar_timbres(carp_orig, carp_dest, archivos, anno, periodo)();
                if (proceso == true) {
                    habilitar('principal');
                }
                satisfactorio('Archivos Copiados');
            }
            else {
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