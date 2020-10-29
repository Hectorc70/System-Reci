'use stric'


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
        columnaPer.innerHTML = rutas[i][0]
        columnaPer.appendChild(checkBox)

        let columnaAnno = document.createElement("td");
        columnaAnno.innerHTML = rutas[i][1];
        let columnaNom = document.createElement("td");
        columnaNom.innerHTML = rutas[i][2];

        let columnaRuta = document.createElement("td");
        columnaRuta.innerHTML = rutas[i][3];
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
    var rutas = [];
    let filaPer = document.getElementsByClassName("cl-per");
    let anno = document.getElementsByName("anno")[0].value;
    if (filaPer.length > 0) {
        for (let i = 0; i < filaPer.length; i++) {
            checkBox = filaPer[i].getElementsByClassName("c-box");
            if (checkBox[0].checked == true) {
                let filaRuta = document.getElementsByClassName("cl-ruta")[i].innerText;
                rutas.push(filaRuta);
            }
        }

        if (rutas.length > 0) {
            deshabilitar('principal');
            loader_tarea();
            let proceso = await eel.guardar_mdatos(rutas, anno)();
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
