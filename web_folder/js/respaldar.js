'use strict'
/* Entrada */
function comprobarParametros() {
    let ruta = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;


    if (ruta != '' && anno != '' && periodo != '') {
        mostrarArchivosOriginales(ruta, anno, periodo);

    }

    else Precaucion('Seleccione Ruta, Año y Periodo');
}
function animacionCancelarVistaArchivos() {
    let cardParams = document.getElementById("recuperar-parametros");
    let dataTable = document.getElementsByClassName("cuerpo-tabla");

    dataTable[0].innerHTML = '';
    dataTable[1].innerHTML = '';
    let vista = document.getElementById("vista-resultados-archivos");
    let menu = document.getElementById('menu');
    vista.style.transform = 'translate(0px,1000px)';
    vista.style.transition = 'all 0.5s ease-in-out';
    menu.style.transform = 'translate(0px,0px)';
    menu.style.transition = 'all 0.5s ease-in-out';

    cardParams.style.transform = 'translate(0px,0px)';
    cardParams.style.transition = 'all 0.5s ease-in-out';
}

/* Vista Data */
function cambiardeTipoVista(idpest, idpestNoSelect, idTablaMostrar, idTablaNoMostrar) {
    let CuerpoTabla = document.getElementById(idTablaMostrar);
    let CuerpoTablaNoMostrar = document.getElementById(idTablaNoMostrar);

    let pestSelect = document.getElementById(idpest);
    let pestNoSelect = document.getElementById(idpestNoSelect);
    CuerpoTabla.style.transform = 'translate(0px,0px)';
    CuerpoTabla.style.opacity = '100%';
    CuerpoTabla.style.transition = 'all 0.5s ease-in-out';


    CuerpoTablaNoMostrar.style.transform = 'translate(2000px, 0px)';
    CuerpoTablaNoMostrar.style.opacity = '0%';
    CuerpoTablaNoMostrar.style.transition = 'all 0.5s ease-in-out';



    pestSelect.style.backgroundColor = 'var(--color-secundario)';
    pestSelect.style.borderTop = '3px solid var(--color-resalte)'
    pestNoSelect.style.backgroundColor = 'var(--color-contenedor)';
    pestNoSelect.style.borderTop = '3px solid var(--color-contenedor)';

}


function animacionVistaArchivos() {

    let cardParams = document.getElementById("recuperar-parametros");
    let vista = document.getElementById("vista-resultados-archivos");
    let menu = document.getElementById('menu');

    menu.style.transform = 'translate(550px,-600px)';
    menu.style.transition = 'all 0.5s ease-in-out';
    cardParams.setAttribute('class', 'animate-move card-contenedor');
    cardParams.style.transform = 'translate(-550px,-700px)';
    cardParams.style.transition = 'all 0.5s ease-in-out';

    vista.style.display = 'block';
    vista.style.visibility = 'visible';
    vista.style.transform = 'translate(0%, -80%)';
    vista.style.transition = 'all 0.5s ease-in-out';

}


async function mostrarArchivosOriginales(ruta, anno, periodo) {
    animacionVistaArchivos()

    loader("tabla-resultados");
    deshabilitar("tabla-resultados");
    let rutas = await eel.enviar_rutas(ruta, periodo, anno)();

    cambiardeTipoVista('pest-timbres', 'pest-recibos', 'timbres-datos', 'recibos-datos');
    let tablavistaTimbres = document.getElementById("timbres-datos");

    for (let i = 0; i < rutas[0].length; i++) {
        let fila = document.createElement("a");
        let idFila = "fila" + i;
        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");
        let funcion = `SeleccionarFilaTabla('${idFila}')`;
        fila.setAttribute("onclick", funcion);


        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = rutas[0][i][1];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = rutas[0][i][0];
        let celdaRuta = document.createElement("div");
        celdaRuta.setAttribute("class", "cell");
        celdaRuta.innerHTML = rutas[0][i][2];

        tablavistaTimbres.appendChild(fila);
        fila.appendChild(celdaNom);
        fila.appendChild(celdaPer);
        fila.appendChild(celdaRuta);
    }
    let tablavistaRecibos = document.getElementById("recibos-datos")
    for (let i = 0; i < rutas[1].length; i++) {
        let fila = document.createElement("a");
        let idFila = "fila-reci" + i;
        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");
        let funcion = `SeleccionarFilaTabla('${idFila}')`;
        fila.setAttribute("onclick", funcion);

        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = rutas[1][i][1];
        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = rutas[1][i][0];
        let celdaRuta = document.createElement("div");
        celdaRuta.setAttribute("class", "cell");
        celdaRuta.innerHTML = rutas[1][i][2];

        tablavistaRecibos.appendChild(fila);
        fila.appendChild(celdaNom);
        fila.appendChild(celdaPer);
        fila.appendChild(celdaRuta);
    }


    habilitar("tabla-resultados");
    noLoader("tabla-resultados");

}


async function SeleccionarTodoTablaRespaldar() {
    let elementoPadre = document.getElementById("recibos-datos");
    let estilo = window.getComputedStyle(elementoPadre);
    let opacidad = estilo.getPropertyValue("opacity");
    if (opacidad == '1') {

        let elementos = elementoPadre.childNodes;

        for (let i = 0; i < elementos.length; i++) {
            SeleccionarFilaTabla("fila-reci" + i);
        }
    }
    else {
        let elementoPadre = document.getElementById("timbres-datos");

        let elementos = elementoPadre.childNodes;
        for (let i = 0; i < elementos.length; i++) {
            SeleccionarFilaTabla("fila" + i);
        }
    }


}



/* SALIDA*/
function animacionVistaParametrosRespaldar() {

    let cardParams = document.getElementById("respaldar-parametros");
    deshabilitar("vista-resultados-archivos");

    cardParams.style.display = 'block';
    cardParams.style.visibility = 'visible';
    cardParams.style.transform = 'translate(200px,0px)';
    cardParams.style.transition = 'all 0.5s ease-in-out';


}

function cancelarVistaParametrosRespaldar() {
    let cardParams = document.getElementById("respaldar-parametros");
    cardParams.style.display = 'inline';
    cardParams.style.visibility = 'hidden';
    cardParams.style.transform = 'translate(-1000px,0px)';
    cardParams.style.transition = 'all 0.5s ease-in-out';
    habilitar("vista-resultados-archivos");
    document.getElementsByName('ruta-destino')[0].value = '';
}
async function iniciarCopiadoArchivos() {
    let rutaDestino = document.getElementsByName("ruta-destino")[0].value;
    let rutaOrigen  = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;
    if (rutaDestino != '') {

    
        let elementoPadre = document.getElementById("recibos-datos");
        let estilo = window.getComputedStyle(elementoPadre);
        let opacidad = estilo.getPropertyValue("opacity");


        if (opacidad == '1') {
            let elementos = elementoPadre.getElementsByClassName("fila");;
            
            let recibosRutas = [];
            for (let i = 0; i < elementos.length; i++) {
                let fila = document.getElementById("fila-reci" + i);
                let estiloFila = window.getComputedStyle(fila);
                let colorFila = estiloFila.getPropertyValue("background-color");
                let ruta = fila.lastElementChild.innerHTML;

                if (colorFila == "rgb(255, 136, 130)") {
                    recibosRutas.push(ruta);
                    
                }
            }


            /* Envia las rutas de los recibos y copia */
            loader("respaldar-parametros");
            deshabilitar("respaldar-parametros");
            debugger;
            for(let i = 0; i < recibosRutas.length; i++){
                
                    let respuesta = await eel.respaldar('recibos', rutaOrigen,recibosRutas[i], rutaDestino, periodo, anno)();
                    
                    if (respuesta[0] == 'ERROR'){
                        noLoader("respaldar-parametros");
                        habilitar("respaldar-parametros");
                        error('EL destino no contiene timbres. Primero copie los timbres');
                        cancelarVistaParametrosRespaldar();
                        
                    }
                    
            }

            noLoader("respaldar-parametros");
            habilitar("respaldar-parametros");


            let respuesta = await eel.leer_log_recibos()();
            
            if (respuesta[0] == 'ERRORES'){
                cancelarVistaParametrosRespaldar();
                Precaucion('Tarea Terminada pero hubo Errores de lectura mas info en el LOG');
                
                
            }
            else{
                cancelarVistaParametrosRespaldar();
                satisfactorio('Tarea Terminada');
                
                
            }


        }
        else {

            let elementoPadre = document.getElementById("timbres-datos");
            let elementos = elementoPadre.getElementsByClassName("fila");
            
            
            let timbresRutas = [];
            for (let i = 0; i < elementos.length; i++) {
                let fila = document.getElementById("fila" + i);
                let estiloFila = window.getComputedStyle(fila);
                let colorFila = estiloFila.getPropertyValue("background-color");
                let ruta = fila.lastElementChild.innerHTML;
                
                if (colorFila == "rgb(255, 136, 130)") {
                    timbresRutas.push(ruta);
                    
                }
            }

            /* Envia las rutas de los timbres y copia */
            loader("respaldar-parametros");
            deshabilitar("respaldar-parametros");
            for (let i = 0; i < timbresRutas.length; i++) {
                debugger;
                await eel.respaldar('timbres', rutaOrigen, timbresRutas[i], rutaDestino, periodo, anno)();
            }
            noLoader("respaldar-parametros");
            habilitar("respaldar-parametros");
            satisfactorio('Timbres Respaldados');
        }
    }
    else {
        Precaucion('Seleccione ruta de Destino');
    }

    }


function almacenarFilasSelecionadas(){
    
}