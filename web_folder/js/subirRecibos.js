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
    loader("recibos-a-subir");
    deshabilitar("recibos-a-subir");
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


    noLoader("recibos-a-subir");
    habilitar("recibos-a-subir");

}


async function SubirDatosRecibos() {
    let elementoPadre = document.getElementById("recibos-a-subir");
    let elementos = elementoPadre.getElementsByClassName("fila");

    let datosRecibos = [];

    for (let i = 0; i < elementos.length; i++) {
        let fila = document.getElementById("fila" + i);
        let estiloFila = window.getComputedStyle(fila);
        let colorFila = estiloFila.getPropertyValue("background-color");

        if (colorFila == "rgb(255, 136, 130)") {
            let archivo = fila.childNodes[0].innerHTML;
            let periodo = fila.childNodes[1].innerHTML;
            let nomina = fila.childNodes[2].innerHTML;
            let ruta = fila.childNodes[3].innerHTML;

            let datos = [archivo, periodo,nomina, ruta];
            
            datosRecibos.push(datos);
        }
    }


    /* Envia datos  */
    loader("recibos-a-subir");
    deshabilitar("recibos-a-subir");

    
    let resp= await eel.guardar_mdatos_recibos(datosRecibos)();

    if (resp != 'ERROR') {
        let respuesta = await eel.leer_log_recibos_subidos()();

        if (respuesta[0] == 'ERRORES') {
            noLoader("recibos-a-subir");
            habilitar("recibos-a-subir");
            Precaucion('Tarea Terminada pero hubo Errores');



        }
        else {
            noLoader("recibos-a-subir");
            habilitar("recibos-a-subir");
            satisfactorio('Tarea Terminada');


        }
    }
    else{
        noLoader("recibos-a-subir");
        habilitar("recibos-a-subir");
        error('No se pudo realizar la Tarea \
                reinicie la aplicacion \
                e Inicie Sesion nuevamente')
        
    }




}


async function SeleccionarTodoTablaSubirReci() {
    let elementoPadre = document.getElementById("recibos-a-subir");
    let elementos = elementoPadre.childNodes;

    for (let i = 0; i < elementos.length; i++) {
        SeleccionarFilaTabla("fila" + i);
    }


}


