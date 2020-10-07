async function mostrarDirectorioRutas() {
    let ruta1 = document.getElementsByName("ruta1")[0].value;
    let ruta2 = document.getElementsByName("ruta2")[0].value;
    if (ruta1 != '' && ruta2 != '' && ruta1 != ruta2) {
        let rutas = await eel.directorios(ruta1, ruta2)();
        const rutasNum = Object.getOwnPropertyNames(rutas);

        for (let i = 1; i < rutasNum.length; i++) {
            let lista = document.getElementById("t-datos1");
            let tr = document.createElement("tr");
            let columnaRuta = document.createElement("td");
            columnaRuta.innerHTML = rutas[rutasNum[i - 1]];

            lista.appendChild(tr);
            tr.appendChild(columnaRuta);
        }
        for (let i = 1; i < rutasNum.length; i++) {
            let lista = document.getElementById("t-datos2");
            let tr = document.createElement("tr");
            let columnaRuta = document.createElement("td");
            columnaRuta.innerHTML = rutas[rutasNum[i - 1]];

            lista.appendChild(tr);
            tr.appendChild(columnaRuta);
        }
        debugger;
        for (let i = 1; i < rutasNum.length; i++) {
            let lista = document.getElementById("t-flechas");
            let tr = document.createElement("tr");
            let columnaF = document.createElement("td");
            let flecha = document.createElement("a")
            let check = document.createElement("input")
            check.setAttribute("type", "checkbox")
            check.setAttribute("class", "c-box")
            flecha.innerHTML = "I H";

            lista.appendChild(tr);
            tr.appendChild(columnaF);
            columnaF.appendChild(check);
            columnaF.appendChild(flecha);
        }
    }
    else{
        Precaucion("1.-Debe seleccionar rutas. \n \
                    2.-Las rutas no pueden ser iguales.");
    }
}
