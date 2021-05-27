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
        let idFila = "fila" + i;

        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");
        let funcion = `SeleccionarFilaTabla('${idFila}')`;
        fila.setAttribute("onclick", funcion);

        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = rutas[0][i][rutasRecibosLargo-2];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = rutas[0][i][rutasRecibosLargo-3];

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
        let funcion = `SeleccionarFilaTabla('${idFila}')`;
        fila.setAttribute("onclick", funcion);

        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = rutas[1][i][rutasTimbresLargo-2];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = rutas[1][i][rutasTimbresLargo-3];

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