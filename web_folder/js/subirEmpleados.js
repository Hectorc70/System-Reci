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

async function enviarDatosEmpleados() {
    let elementoPadre = document.getElementById("empleados-a-subir");
    let elementos = elementoPadre.getElementsByClassName("fila");

    let datosEmpleados = [];
    for (let i = 0; i < elementos.length; i++) {
        let fila = document.getElementById("fila" + i);
        let estiloFila = window.getComputedStyle(fila);
        let colorFila = estiloFila.getPropertyValue("background-color");

        if (colorFila == "rgb(255, 136, 130)") {
            let control = fila.childNodes[0].innerHTML;
            let nombre = fila.childNodes[1].innerHTML;
            let apePaterno = fila.childNodes[2].innerHTML;
            let apeMaterno = fila.childNodes[3].innerHTML;
            let datos = [control, nombre, apePaterno, apeMaterno];

            datosEmpleados.push(datos);
        }
    }

    loader("empleados-a-subir");
    deshabilitar("empleados-a-subir");

    let resp= await eel.subir_datos_empleados(datosEmpleados)();
    debugger;
    if (resp != 'ERROR') {
        let respuesta = await eel.leer_log_empleados_subidos()();

        if (respuesta[0] == 'ERRORES') {
            noLoader("empleados-a-subir");
            habilitar("empleados-a-subir");
            Precaucion('Tarea Terminada pero hubo Errores');



        }
        else {
            noLoader("empleados-a-subir");
            habilitar("empleados-a-subir");
            satisfactorio('Tarea Terminada');


        }
    }
    else{
        noLoader("empleados-a-subir");
        habilitar("empleados-a-subir");
        error('No se pudo realizar la Tarea \
                reinicie la aplicacion \
                e Inicie Sesion nuevamente')
        
    }

}

async function SeleccionarTodoTablaSubirEmp() {
    let elementoPadre = document.getElementById("empleados-a-subir");
    let elementos = elementoPadre.childNodes;

    for (let i = 0; i < elementos.length; i++) {
        SeleccionarFilaTabla("fila" + i);
    }
}