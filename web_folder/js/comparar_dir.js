async function mostrarDirectorioRutas() {
    let ruta1 = document.getElementsByName("ruta1")[0].value;
    let ruta2 = document.getElementsByName("ruta2")[0].value;

    let rutas = await eel.recuperar_directorios(ruta1, ruta2)();
    const rutasNum = Object.getOwnPropertyNames(rutas);
    debugger;
    for (let i = 1; i < rutasNum.length; i++) {
        let lista = document.getElementById("tbl-datos");
        let tr = document.createElement("tr");
        let checkBox = document.createElement("input");
        checkBox.setAttribute("type", "checkbox");
        checkBox.setAttribute("class", "c-box");


        let ultimo = rutas[rutasNum[i - 1]]["length"];

        let columnaNum = document.createElement("td");
        columnaNum.setAttribute("class", "cl-num")
        columnaNum.innerHTML = i;
        let columnaRuta1 = document.createElement("td");
        columnaRuta1.innerHTML = rutas[rutasNum[i - 1]][4];
        let columnaRuta2 = document.createElement("td");
        //columnaArchivo.setAttribute("class", "ruta-archivo");
        columnaRuta2.innerHTML = rutas[rutasNum[i - 1]][ultimo - 1];

        lista.appendChild(tr);
        tr.appendChild(columnaNum);
        columnaNum.appendChild(checkBox);
        tr.appendChild(columnaRuta1);
        tr.appendChild(columnaRuta2);
    }
}
