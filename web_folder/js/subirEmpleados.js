function comprobarParametrosEmp() {
    let ruta = document.getElementsByName("ruta")[0].value;
    if (ruta != '') {
        mostrarDatosEmpleados(ruta);

    }

    else Precaucion('Seleccione Archivo en Excel');
}


async function mostrarDatosEmpleados(ruta) {
    animacionVistaArchivos()
    loader("tabla-resultados");
    deshabilitar("tabla-resultados");
    let datosEmpleados = await eel.mostrar_datos_empleados(ruta)();

    let tablavistaDatos = document.getElementById("empleados-a-subir");

    debugger;
    for (let i = 0; i < datosEmpleados.length; i++) {

        let fila = document.createElement("a");
        let idFila = "fila" + i;
        fila.setAttribute("id", idFila);
        fila.setAttribute("class", "fila");

        let funcion = `SeleccionarFilaTabla('${idFila}')`;
        fila.setAttribute("onclick", funcion);

        let celdaControl = document.createElement("div");
        celdaControl.setAttribute("class", "cell");
        celdaControl.innerHTML = datosEmpleados[i][0];

        let celdaNombre = document.createElement("div");
        celdaNombre.setAttribute("class", "cell");
        celdaNombre.innerHTML = datosEmpleados[i][1];

        let celdaApePaterno = document.createElement("div");
        celdaApePaterno.setAttribute("class", "cell");
        celdaApePaterno.innerHTML = datosEmpleados[i][2];

        let celdaApeMaterno = document.createElement("div");
        celdaApeMaterno.setAttribute("class", "cell");
        celdaApeMaterno.innerHTML = datosEmpleados[i][3];

        tablavistaDatos.appendChild(fila);
        fila.appendChild(celdaControl);
        fila.appendChild(celdaNombre);
        fila.appendChild(celdaApePaterno);
        fila.appendChild(celdaApeMaterno);
    }


    noLoader("tabla-resultados");
    habilitar("tabla-resultados");

}


async function SeleccionarTodoTablaSubirEmp() {
    let elementoPadre = document.getElementById("empleados-a-subir");
    let elementos = elementoPadre.childNodes;

    for (let i = 0; i < elementos.length; i++) {
        SeleccionarFilaTabla("fila" + i);
    }
}