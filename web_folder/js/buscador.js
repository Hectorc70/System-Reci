'use strict'




function AnimacionBuscador(){

    let cardParams = document.getElementById("parametros-busqueda");
    let vista = document.getElementById("vista-resultado");
    window.hei
    cardParams.setAttribute('class', 'animate-move card-contenedor');
    cardParams.style.transform = 'translate(-30px,-570px);'
    vista.setAttribute('class', 'card-contenedor animate-move-r ');

}

function validarInputs() {
    
    let control = document.getElementsByName("control")[0].value;
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;


    if (periodoIni != '' && annoIni != '' && 
        periodoFin != '' && annoFin != '' && 
        control != '') {
            deshabilitar("conte-buscador");
            loader();
        AnimacionBuscador();
        

    }

    else {
        Precaucion('Debe proporcinar Numero de control \
        e inicio y final');
    }
}


/* mostrar datos RECIBOS */
async function mostrarDatosRecibos() {
    let nombre = '0'


    if (periodoIni != '' && annoIni != '' &&
        periodoFin != '' && annoFin != '') {

        if (annoIni < annoFin || annoIni == annoFin) {
            deshabilitar('principal');
            loader_tarea();
            let control = document.getElementsByName("control")[0].value;


            let recibos = await eel.mostrar_datos_encontrados(control, nombre,
                periodoIni, annoIni,
                periodoFin, annoFin)();
            const recibosNum = Object.getOwnPropertyNames(recibos);
            habilitar('principal');

            if (recibos != false) {
                let num = 0
                for (let i = 1; i < recibosNum.length; i++) {
                    let lista = document.getElementById("tbl-datos");
                    let tr = document.createElement("tr");
                    let checkBox = document.createElement("input");
                    checkBox.setAttribute("type", "checkbox");
                    checkBox.setAttribute("class", "c-box");

                    let columnaId = document.createElement("td");
                    columnaId.setAttribute("class", "cl-id  ocultar-colum");
                    columnaId.innerHTML = recibos[recibosNum[i - 1]][3];

                    let columnaCtrl = document.createElement("td");
                    columnaCtrl.innerHTML = recibos[recibosNum[i - 1]][0];
                    columnaCtrl.setAttribute("class", "cl-ctrl");
                    columnaCtrl.appendChild(checkBox)

                    let columnaNom = document.createElement("td");
                    columnaNom.setAttribute("class", "cl-nom");
                    columnaNom.innerHTML = recibos[recibosNum[i - 1]][2];

                    let columnaPeriodo = document.createElement("td");
                    columnaPeriodo.setAttribute("class", "cl-per");
                    columnaPeriodo.innerHTML = recibos[recibosNum[i - 1]][1];

                    let columnaRutaArchivo = document.createElement("td");
                    num = num + 1

                    let num_str = "ruta-a" + num.toString()
                    columnaRutaArchivo.setAttribute("id", num_str);
                    columnaRutaArchivo.setAttribute("class", "ocultar-colum ruta-recibo");

                    columnaRutaArchivo.innerHTML = recibos[recibosNum[i - 1]][4];

                    let columnaV = document.createElement("td");
                    let opcionVer = document.createElement("button");
                    opcionVer.setAttribute("class", "btn btn-ver");
                    let parametro = `abrirReciboExt('${num_str}')`
                    opcionVer.setAttribute("onclick", parametro);



                    tr.appendChild(columnaId);
                    lista.appendChild(tr);
                    tr.appendChild(columnaCtrl);
                    columnaCtrl.appendChild(checkBox);
                    tr.appendChild(columnaNom);
                    tr.appendChild(columnaPeriodo);
                    tr.appendChild(columnaRutaArchivo);
                    tr.appendChild(columnaV);
                    opcionVer.innerHTML = "Ver";
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




async function abrirReciboExt(clase) {

    let filaRuta = document.getElementById(clase);
    let ruta = filaRuta.innerText

    let verReci = await eel.abrir_recibo(ruta)();

}


/* FUNCIONES QUE EJECUTAN EL PROCESO DE EXTRACCION */
async function EnviarDatosExtraccion() {

    let rutaGuardado = document.getElementsByName("ruta-guardado")[0].value;
    let control = document.getElementsByName("control")[0].value;
    let recibos = [];
    let filaControl = document.getElementsByClassName("cl-ctrl");

    for (let i = 0; i < filaControl.length; i++) {
        let checkBox = filaControl[i].getElementsByClassName("c-box");
        if (checkBox[0].checked == true) {

            let filaRuta = document.getElementsByClassName("ruta-recibo")[i].innerText;

            let datos = [];
            datos = [filaControl[i].innerText, filaRuta]
            recibos.push(datos);
        }
    }


    if (rutaGuardado != '' & recibos.length > 0) {
        deshabilitar('principal');
        loader_tarea();
        let reci = await eel.recuperar_recibos(recibos, rutaGuardado)();
        if (reci == true) {
            habilitar('principal');
            satisfactorio("Se Guardaron todos los Recibos en: " + rutaGuardado + "/" + control)
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

    for (let i = 1; i < controlNum.length; i++) {
        document.getElementsByName("control")[0].value = controles[i - 1];
        mostrarDatosRecibos();
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

let num = 1;
async function addCampo() {
    
    num = num +1;
    let numStr = num.toString();

    let card = document.getElementById("conte-control-buscador");
    let divCampo = document.createElement("div");
    divCampo.setAttribute("class", "conte-input-dinamico");
    divCampo.setAttribute("id", numStr);

    let inputControl = document.createElement("input");
    inputControl.setAttribute("type", "text");
    inputControl.setAttribute("class", "in-data in-control");
    inputControl.setAttribute("name", "control");
    inputControl.setAttribute("maxlength", "8");

    

    let conteIcon = document.createElement("a");

    let parametro = `removeCampo('${numStr}')`;
    conteIcon.setAttribute("onclick", parametro);

    let removeIcon = document.createElement("div");
    removeIcon.setAttribute("class", "icono-remove");
    
    

    card.appendChild(divCampo);
    divCampo.appendChild(inputControl);
    divCampo.appendChild(conteIcon);
    removeIcon.innerHTML = "-"
    conteIcon.appendChild(removeIcon);



}

async function removeCampo(num){
    let card = document.getElementById("conte-control-buscador");
    let campo = document.getElementById(num);

    card.removeChild(campo);
}
