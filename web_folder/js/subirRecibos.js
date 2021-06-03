function comprobarParametrosRespReci() {
    let ruta = document.getElementsByName("ruta")[0].value;
    let anno = document.getElementsByName("anno")[0].value;
    let periodo = document.getElementsByName("periodo")[0].value;


    if (ruta != '' && anno != '' && periodo != '') {
        mostrarRecibos(ruta, anno, periodo);

    }

    else Precaucion('Seleccione Ruta, Año y Periodo');
}


async function mostrarRecibos(ruta, anno, periodo) {
    animacionVistaArchivos()
    loader("tabla-resultados");
    deshabilitar("tabla-resultados");
    let recibosNomina = await eel.mostrar_rutas_recibos(ruta, anno, periodo)();

    let tablavistaArchivos = document.getElementById("recibos-a-subir");

    debugger;
    for (let i = 0; i < recibosNomina.length; i++) {
        let rutasRecibosLargo = recibosNomina[i].length

        let fila = document.createElement("a");
        let idFila = "fila" + i;
        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");

        let funcion = `SeleccionarFilaTabla('${idFila}')`;
        fila.setAttribute("onclick", funcion);

        let celdaNombre = document.createElement("div");
        celdaNombre.setAttribute("class", "cell");
        celdaNombre.innerHTML = recibosNomina[i][0];

        let celdaNom = document.createElement("div");
        celdaNom.setAttribute("class", "cell");
        celdaNom.innerHTML = recibosNomina[i][2];

        let celdaPer = document.createElement("div");
        celdaPer.setAttribute("class", "cell");
        celdaPer.innerHTML = recibosNomina[i][1];

        let celdaRutaRecibo = document.createElement("div");
        celdaRutaRecibo.setAttribute("class", "cell");
        celdaRutaRecibo.innerHTML = recibosNomina[i][rutasRecibosLargo - 1];
        tablavistaArchivos.appendChild(fila);
        fila.appendChild(celdaNombre);
        fila.appendChild(celdaPer);
        fila.appendChild(celdaNom);
        fila.appendChild(celdaRutaRecibo);
    }


    noLoader("tabla-resultados");
    habilitar("tabla-resultados");

}

async function SeleccionarTodoTablaSubirReci() {
    let elementoPadre = document.getElementById("recibos-a-subir");
    let elementos = elementoPadre.childNodes;

    for (let i = 0; i < elementos.length; i++) {
        SeleccionarFilaTabla("fila" + i);
    }


}


