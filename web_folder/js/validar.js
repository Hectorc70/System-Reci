'use strict'
/* Entrada */
function comprobarParametrosV() {
    let ruta = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;


    if (ruta != '' && anno != '' && periodo != '') {
        mostrarArchivos(ruta, anno, periodo);

    }

    else Precaucion('Seleccione Ruta, Año y Periodo');
}

async function mostrarArchivos(ruta, anno, periodo){
    animacionVistaArchivos()
    loader("tabla-resultados");
    deshabilitar("tabla-resultados");
    let rutas = await eel.mostrar_archivos(ruta, anno, periodo)();
    
    let tablavistaArchivos = document.getElementById("datos-recibos-validadados");
    cambiardeTipoVista('pest-recibos', 'pest-timbres', 'datos-recibos-validadados', 'datos-timbres-validadados')
    for (let i = 0; i < rutas[0].length; i++) {
        let rutasRecibosLargo = rutas[0][i].length
        
        let fila = document.createElement("a");
        let idFila = "fila-reci" + i;

        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");
        

        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = rutas[0][i][rutasRecibosLargo-4];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = rutas[0][i][rutasRecibosLargo-5];

        let celdaRutaRecibo = document.createElement("div");
        celdaRutaRecibo.setAttribute("class", "cell");
        celdaRutaRecibo.innerHTML = rutas[0][i][rutasRecibosLargo-1]; 
        tablavistaArchivos.appendChild(fila);
        fila.appendChild(celdaPer);
        fila.appendChild(celdaNom);
        fila.appendChild(celdaRutaRecibo);
    }


    let tablavistatimbres = document.getElementById("datos-timbres-validadados");
    
    for (let i = 0; i < rutas[1].length; i++) {
        let rutasTimbresLargo = rutas[1][i].length
        
        let fila = document.createElement("a");
        let idFila = "fila" + i;

        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");


        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = rutas[1][i][rutasTimbresLargo-4];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = rutas[1][i][rutasTimbresLargo-5];

        let celdaRutaTimbre = document.createElement("div");
        celdaRutaTimbre.setAttribute("class", "cell");
        celdaRutaTimbre.innerHTML = rutas[1][i][rutasTimbresLargo-1]; 
        
        tablavistatimbres.appendChild(fila);
        fila.appendChild(celdaPer);
        fila.appendChild(celdaNom);
        fila.appendChild(celdaRutaTimbre);
    }
    habilitar("tabla-resultados");
    noLoader("tabla-resultados");



}

async function validar(){
    deshabilitar("vista-resultados-archivos");
    loader("vista-resultados-archivos");
    let tablaRecibos = document.getElementById("datos-recibos-validadados");
    let tablaTimbres = document.getElementById("datos-timbres-validadados");
    //let recibos = recuperarValoresFilas(tablaRecibos);

    let filasRecibos = tablaRecibos.getElementsByClassName("fila");
    let filasTimbres = tablaTimbres.getElementsByClassName("fila");
    //let resp = await eel.mostrar_archivos(timbres, recibos)();
    
    let recibos = [];
    for (let i = 0; i < filasRecibos.length; i++) {
        
        let fila = document.getElementById("fila-reci" + i);
        let ruta = fila.lastElementChild.innerHTML;
        recibos.push(ruta);
    }

    let timbres = [];
    for (let i = 0; i < filasTimbres.length; i++) {
        
        let fila = document.getElementById("fila" + i);
        let ruta = fila.lastElementChild.innerHTML;
        timbres.push(ruta);
    }  

    verResultadosValidacion(timbres, recibos)
}

async function verResultadosValidacion(timbres, recibos){
    
    let respuesta = await eel.validar_archivos(timbres, recibos)();
    let tablavistaArchivos = document.getElementById("datos-recibos-validadados");
    borrarTabla("datos-recibos-validadados");
    borrarTabla("datos-timbres-validadados");
    let tituloTablavistaArchivos = document.getElementById("titulo-tabla-vista-archivos");
    
    cambiardeTipoVista('pest-recibos', 'pest-timbres', 'datos-recibos-validadados', 'datos-timbres-validadados')
    tituloTablavistaArchivos.innerHTML = "Recibos - Timbres con Error"
    
    
    for (let i = 0; i < respuesta[0].length; i++) {
        let rutasRecibosLargo = respuesta[0][i].length
        
        let fila = document.createElement("a");
        let idFila = "fila-reci" + i;

        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");
        

        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = respuesta[0][i][rutasRecibosLargo-2];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = respuesta[0][i][rutasRecibosLargo-3];

        let celdaRutaRecibo = document.createElement("div");
        celdaRutaRecibo.setAttribute("class", "cell");
        celdaRutaRecibo.innerHTML = respuesta[0][i][rutasRecibosLargo-1]; 
        tablavistaArchivos.appendChild(fila);
        fila.appendChild(celdaPer);
        fila.appendChild(celdaNom);
        fila.appendChild(celdaRutaRecibo);
    }


    let tablavistatimbres = document.getElementById("datos-timbres-validadados");
    
    for (let i = 0; i < respuesta[1].length; i++) {
        let rutasTimbresLargo = respuesta[1][i].length
        
        let fila = document.createElement("a");
        let idFila = "fila" + i;

        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");


        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = respuesta[1][i][rutasTimbresLargo-2];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = respuesta[1][i][rutasTimbresLargo-3];

        let celdaRutaTimbre = document.createElement("div");
        celdaRutaTimbre.setAttribute("class", "cell");
        celdaRutaTimbre.innerHTML = respuesta[1][i][rutasTimbresLargo-1]; 
        
        tablavistatimbres.appendChild(fila);
        fila.appendChild(celdaPer);
        fila.appendChild(celdaNom);
        fila.appendChild(celdaRutaTimbre);
    }
    
    


    habilitar("vista-resultados-archivos");
    noLoader("vista-resultados-archivos");
}   

function CancelarVistaArchivosValidar(){
    animacionCancelarVistaArchivos('datos-recibos-validadados');
    animacionCancelarVistaArchivos('datos-timbres-validadados');
}

