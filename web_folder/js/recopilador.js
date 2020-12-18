'use stric'
async function CargarEmpleados(){
    let archivo = document.getElementsByName("ruta-carga-empleados")[0].value;
    debugger;
    if (archivo != ''){
        deshabilitar('principal');
        loader_tarea();
        let respuesta = await eel.guardar_empleados(archivo)();

        if (respuesta == true) {
            habilitar('principal');
            satisfactorio('Carga Terminada');
        }
    }
    else{
        Precaucion("Selecciona Archivo de Carga");
    }
    

}

async function validarInputs() {
    let periodoIn = document.getElementsByName("periodo")[0].value;
    let annoIn = document.getElementsByName("anno")[0].value;
    let directorio = document.getElementsByName("ruta-reci")[0].value;

    if (annoIn !== '' && periodoIn != '' && directorio != '') {
        mostrarEnTabla(directorio, periodoIn, annoIn)
    }
    else {
        Precaucion("Selecciona Ruta, Año y Periodo para continuar");
    }

}

async function mostrarEnTabla(directorio, periodo, anno) {
    /* 
        let datos = document.getElementById("tbl-datos");
        datos.removeChild(tr) */


    let rutas = await eel.mostrar_rutas_recibos(directorio, anno, periodo)();
    const rutasNum = Object.getOwnPropertyNames(rutas);


    for (let i = 1; i <= rutasNum.length; i++) {
        let lista = document.getElementById("tbl-datos");
        let tr = document.createElement("tr");
        let checkBox = document.createElement("input");
        checkBox.setAttribute("type", "checkbox");
        checkBox.setAttribute("class", "c-box");


        let columnaPer = document.createElement("td");
        columnaPer.setAttribute("class", "cl-per");
        columnaPer.innerHTML = rutas[i-1][0]
        columnaPer.appendChild(checkBox)

        let columnaAnno = document.createElement("td");
        columnaAnno.setAttribute("class", "cl-anno");
        columnaAnno.innerHTML = rutas[i-1][1];

        let columnaNom = document.createElement("td");
        columnaNom.setAttribute("class", "cl-nom");        
        columnaNom.innerHTML = rutas[i-1][2];

        let columnaRuta = document.createElement("td");
        columnaRuta.innerHTML = rutas[i-1][3];
        columnaRuta.setAttribute("class", "cl-ruta");

        lista.appendChild(tr);
        columnaPer.appendChild(checkBox);
        tr.appendChild(columnaPer);
        tr.appendChild(columnaAnno);
        tr.appendChild(columnaNom);
        tr.appendChild(columnaRuta);

    }

}




async function elementosTabla() {
    var datos = [];
    let filaPer = document.getElementsByClassName("cl-per");
    let anno = document.getElementsByName("anno")[0].value;
    
    
    debugger;
    if (filaPer.length > 0) {
        for (let i = 0; i < filaPer.length; i++) {
            checkBox = filaPer[i].getElementsByClassName("c-box");
            if (checkBox[0].checked == true) {
                let filaPer = document.getElementsByClassName("cl-per")[i].innerText;
                let filaAnno = document.getElementsByClassName("cl-anno")[i].innerText;
                let filaNom = document.getElementsByClassName("cl-nom")[i].innerText;
                let filaRuta = document.getElementsByClassName("cl-ruta")[i].innerText;
                datos_fila = [filaPer, filaAnno, filaNom, filaRuta]
                datos.push(datos_fila);
            }
        }
        debugger;
        if (datos.length > 0) {
            deshabilitar('principal');
            loader_tarea();
            let proceso = await eel.guardar_mdatos(datos)();
            if (proceso == true) {
                habilitar('principal');
                satisfactorio('Proceso Terminado');
            }
        }

        else {
            Precaucion('Seleccione almenos una fila');
        }
    }
    else {
        Precaucion('Se debe buscar primero');
    }




}
