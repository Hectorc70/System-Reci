'use strict'




/* ICONOS */
let iconDownload = '<svg class="icon-opcion-buscador" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\
viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve">\
<g>\
<g>\
   <path d="M412.907,214.08C398.4,140.693,333.653,85.333,256,85.333c-61.653,0-115.093,34.987-141.867,86.08\
       C50.027,178.347,0,232.64,0,298.667c0,70.72,57.28,128,128,128h277.333C464.213,426.667,512,378.88,512,320\
       C512,263.68,468.16,218.027,412.907,214.08z M256,384L149.333,277.333h64V192h85.333v85.333h64L256,384z"/>\
</g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
</svg>'

let iconVer = '<svg class="icon-opcion-buscador" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"\
viewBox="0 0 469.333 469.333" style="enable-background:new 0 0 469.333 469.333;" xml:space="preserve">\
<g>\
<g>\
   <g>\
       <path d="M234.667,170.667c-35.307,0-64,28.693-64,64s28.693,64,64,64s64-28.693,64-64S269.973,170.667,234.667,170.667z"/>\
       <path d="M234.667,74.667C128,74.667,36.907,141.013,0,234.667c36.907,93.653,128,160,234.667,160\
           c106.773,0,197.76-66.347,234.667-160C432.427,141.013,341.44,74.667,234.667,74.667z M234.667,341.333\
           c-58.88,0-106.667-47.787-106.667-106.667S175.787,128,234.667,128s106.667,47.787,106.667,106.667\
           S293.547,341.333,234.667,341.333z"/>\
   </g>\
</g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
<g>\
</g>\
</svg>'

/* FUNCIONES */

function AnimacionBuscador() {

    let cardParams = document.getElementById("parametros-busqueda");
    let vista = document.getElementById("vista-resultado");

    cardParams.setAttribute('class', 'animate-move card-contenedor');
    cardParams.style.transform = 'translate(-30px,-570px);'
    vista.setAttribute('class', 'card-contenedor animate-move-r ');

}

async function validarInputsBuscador() {
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;


    if (periodoIni != '' && annoIni != '' &&
        periodoFin != '' && annoFin != '') {
        return true;

    }
}
async function enviarControl(periodoIni, annoIni, periodoFin, annoFin) {
    let control = document.getElementsByName("control")[0].value;
    let paramsValidados = validarInputsBuscador()


    if (control != '' && paramsValidados) {
        loader("recibos-datos-buscador");
        deshabilitar("parametros-busqueda");
        AnimacionBuscador();

        let resp = await eel.recuperar_por_control(control,
            periodoIni, annoIni,
            periodoFin, annoFin)();

        if (resp.length > 0) {
            mostrarDatosRecibos(resp);
            noLoader("recibos-datos-buscador");
            habilitar("parametros-busqueda")
        }
        else {
            noLoader('conte-buscador');
            habilitar('conte-buscador');
            error('Posibles Causas. \n \
                    -Datos no encontrados\n \
                    -Servidor no disponible \n \
                    -contacte a Soporte')

        }
    }
    else {
        Precaucion('Escriba un numero de control y seleccione periodo de\
        Inicio Y de Fin');

    }
}

async function enviarNombre() {
    let nombre = document.getElementsByName("control")[0].value;
    let apeP = document.getElementsByName("ape-p")[0].value;
    let apeM = document.getElementsByName("ape-m")[0].value;
    let paramsValidados = validarInputsBuscador()

    if (nombre != '' && apeP != '' &&
        apeM != '' && paramsValidados) {
        deshabilitar("conte-buscador");
        loader();
        AnimacionBuscador();
    }
    else {
        Precaucion('Llene todos los campos y seleccione periodo de\
        Inicio Y de Fin');

    }
}

async function enviarParametrosBusqueda() {
    let tipoBusqueda = document.getElementById("buscador-por-control");
    let estilo = window.getComputedStyle(tipoBusqueda);
    let opacidad = estilo.getPropertyValue("opacity");
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;

    if (opacidad == "1") {
        enviarControl(periodoIni, annoIni, periodoFin, annoFin);
    }
    else {
        enviarNombre();
    }
}

/* mostrar datos RECIBOS */
async function mostrarDatosRecibos(datos) {

    let tablavista = document.getElementById("recibos-datos-buscador");

    for (let i = 0; i < datos.length; i++) {
        let fila = document.createElement("a");
        let idFila = "fila" + i;
        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");

        /* let checkBox = document.createElement("input");
        checkBox.setAttribute("type", "checkbox");
        checkBox.setAttribute("class", "c-box"); */
        /* let funcion = `SeleccionarFilaTabla('${idFila}')`;
        fila.setAttribute("onclick", funcion); */

        let celdaId = document.createElement("div");
        celdaId.setAttribute("class", "cell colum-oculta");
        celdaId.innerHTML = datos[i][0];

        let celdaControl = document.createElement("div");
        celdaControl.setAttribute("class", "cell");
        celdaControl.innerHTML = datos[i][1];


        let celdaPeriodo = document.createElement("div");
        celdaPeriodo.setAttribute("class", "cell");
        celdaPeriodo.innerHTML = datos[i][2];


        let celdaNomina = document.createElement("div");
        celdaNomina.setAttribute("class", "cell");
        celdaNomina.innerHTML = datos[i][3];

        let celdaVer = document.createElement("a");
        let funcionVer = `verRecibo('${datos[i][0]}')`;
        celdaVer.setAttribute("class", "cell-con-icono");
        celdaVer.setAttribute("onclick", funcionVer);
        celdaVer.innerHTML = iconVer;

        let celdaDescargar = document.createElement("a");
        let data = [datos[i][0], datos[i][1], datos[i][3], datos[i][2]]
        let funcionDescargar = `descargarRecibo('${data}')`;
        celdaDescargar.setAttribute("class", "cell-con-icono");
        celdaDescargar.setAttribute("onclick", funcionDescargar);
        celdaDescargar.innerHTML = iconDownload;

        tablavista.appendChild(fila);
        fila.appendChild(celdaId);
        fila.appendChild(celdaControl);
        
        fila.appendChild(celdaPeriodo);
        fila.appendChild(celdaNomina);
        fila.appendChild(celdaDescargar);
        fila.appendChild(celdaVer);

    }

}







/*  UTULIDADES DE RECIBOS*/
async function descargarRecibo(data) {
    let resp = await eel.descargar_recibo(data)();

    debugger;
    if (resp[0] != 0){
        satisfactorio(resp[1]);
    }
    else{
        Precaucion(resp[1]);
    }
    
    
}


async function addCampo() {

    num = num + 1;
    let numStr = num.toString();

    let card = document.getElementById("conte-in-control");
    let divCampo = document.createElement("div");
    divCampo.setAttribute("class", "conte-input-dinamico in-buscar-control");
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

async function removeCampo(num) {
    let card = document.getElementById("conte-in-control");
    let campo = document.getElementById(num);

    card.removeChild(campo);
}


function cambiardeTipoBusqueda(idpest, idpestNoSelect, idMostrar, idNoMostrar) {

    let contenedorParams = document.getElementById(idMostrar);
    let contenedorParamsNoMostrar = document.getElementById(idNoMostrar);

    let pestSelect = document.getElementById(idpest);
    let pestNoSelect = document.getElementById(idpestNoSelect);
    contenedorParams.style.transform = 'translate(0px,0px)';
    contenedorParams.style.display = 'block';
    contenedorParams.style.opacity = '100%';
    contenedorParams.style.width = '100%';
    contenedorParams.style.height = '95%';
    contenedorParams.style.transition = 'all 0.5s ease-in-out';



    contenedorParamsNoMostrar.display = 'none';
    contenedorParamsNoMostrar.style.transform = 'translate(200px, 0px)';
    contenedorParamsNoMostrar.style.width = '0px';
    contenedorParamsNoMostrar.style.height = '0px';
    contenedorParamsNoMostrar.style.opacity = '0%';
    contenedorParamsNoMostrar.style.transition = 'all 0.5s ease-in-out';



    pestSelect.style.backgroundColor = 'var(--color-secundario)';
    pestSelect.style.borderTop = '3px solid var(--color-resalte)'
    pestNoSelect.style.backgroundColor = 'var(--color-contenedor)';
    pestNoSelect.style.borderTop = '3px solid var(--color-contenedor)';

}



async function SeleccionarTodoTablaBuscar() {
    let elementoPadre = document.getElementById("recibos-datos-buscador");
    let elementos = elementoPadre.childNodes;

    for (let i = 0; i < elementos.length; i++) {
        SeleccionarFilaTabla("fila" + i);
    }
}

/* VISOR DE RECIBO */

async function verRecibo(idRecibo) {
    let resp = await eel.recuperar_recibo(idRecibo)();

    if (resp[0] == 200) {
        animacionVisor(resp[1]);


    }

    else {
        error('No se puede ver el recibo');
    }

}


function animacionVisor(archivo) {
    
    let visor = document.getElementById('conte-view-recibo')
    let btn = document.getElementById('btn-cerrar')
    let visorRecibo = document.getElementById('visor')

    visor.style.display = "block";
    visor.style.visibility = "visible";
    visor.style.width = '50%';
    visor.style.height = '80%';
    btn.style.display = 'flex';
    visor.style.transition = 'all 0.5s ease-in-out';

    let obj = document.createElement('object');
    obj.setAttribute("id", "archivo-pdf")
    obj.setAttribute("src", "zoom=100")
    obj.style.width = '100%';
    obj.style.height = '842pt';
    obj.type = 'application/pdf';
    obj.data = "data:application/pdf;base64, " + [archivo.slice(1,archivo.length-1)];
    visorRecibo.appendChild(obj);


}

async function cerrarVisor(){
    let conteVisor = document.getElementById('conte-view-recibo');
    let visor = document.getElementById('visor');
    let reciboconte = document.getElementById('archivo-pdf');

    let btn = document.getElementById('btn-cerrar');
    visor.removeChild(reciboconte);
    
    conteVisor.style.width = '0px';
    conteVisor.style.height = '0px';
    conteVisor.style.top = '0';
    conteVisor.style.left = '0';
    conteVisor.style.transition = 'all 0.5s ease-in-out';
    conteVisor.style.display = "block";
    conteVisor.style.visibility = "visible";
}