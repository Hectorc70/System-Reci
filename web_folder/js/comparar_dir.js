async function mostrarDirectorioRutas() {
    let ruta1 = document.getElementsByName("ruta1")[0].value;
    let ruta2 = document.getElementsByName("ruta2")[0].value;

    let rutas = await eel.directorios(ruta1, ruta2)();
    const rutasNum = Object.getOwnPropertyNames(rutas);
    debugger;
    for (let i = 1; i < rutasNum.length; i++) {
        let lista = document.getElementById("t-datos1");
        let tr = document.createElement("tr");      
        let columnaRuta = document.createElement("td");
        columnaRuta.innerHTML = rutas[rutasNum[i]];

        lista.appendChild(tr);
        tr.appendChild(columnaRuta);      
    }
}
