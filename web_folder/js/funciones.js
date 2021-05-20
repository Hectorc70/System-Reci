'use strict'


/* function carga(){
    $('#preloader').fadeOut();
    $('#menu-principal').removeClass('hide');
} */
/* Funciones que son para mostrar una animación de loader*/
function loader(elemento) {
    let elementoPadre = document.getElementById(elemento);
    let loader = document.createElement("div");
    loader.setAttribute("id", "loader");
    elementoPadre.appendChild(loader);

    for(let i=0; i < 8; i++){
        let divLoader = document.createElement("div");
        loader.appendChild(divLoader);
    }
    loader.setAttribute("class", "lds-roller");
}
function noLoader(elemento) {
    let elementoPadre = document.getElementById(elemento);
    let loader = document.getElementById("loader");
    elementoPadre.removeChild(loader);
    
}

function deshabilitar(elemento) {
    let elementoPadre = document.getElementById(elemento);
    //elementoPadre.setAttribute("class", );
    elementoPadre.classList.add("deshabilitado");
    let backBlock = document.createElement("div");
    backBlock.setAttribute("id", "backloader");
    backBlock.style.position = "fixed";
    backBlock.style.display = "inline-block";
    backBlock.style.width = "100%";
    backBlock.style.height = "100%";
    backBlock.style.top = "0";
    backBlock.style.bottom = "0";
    backBlock.style.left = "0";
    backBlock.style.right = "0";
    backBlock.style.opacity = "10%";
    backBlock.style.background = "white";
    elementoPadre.appendChild(backBlock);
}


function habilitar(elemento) {
    let elementoPadre = document.getElementById(elemento);
    let backloader = document.getElementById("backloader");
    elementoPadre.classList.remove("deshabilitado");
    elementoPadre.removeChild(backloader);
    



}

/* Muestra una ruta en el imput pasado como parametro */
async function mostrarRuta(nombre) {
    let ruta = await eel.enviar_ruta()();
    document.getElementsByName(nombre)[0].value = ruta;
}

async function mostrarRutaArchivo(nombre) {
    let ruta = await eel.enviar_ruta_archivo()();

    document.getElementsByName(nombre)[0].value = ruta;

}




async function mostrar_en_tabla() {

    let directorio = document.getElementsByName("ruta-reci")[0].value;
    let rutas = await eel.mostrar_rutas_recibos(directorio)();
    const rutas_num = Object.getOwnPropertyNames(rutas)

    for (let i = 1; i < rutas_num.length; i++) {

        let tr = document.createElement('tr');
        let rutas_datos_num = Object.getOwnPropertyDescriptor
        for (j = 1; j < rutas[i].length; j++) {
            let td = document.createElement('td');

            td.appendChild(document.createTextNode(rutas[i][j]));
            tr.appendChild(td)
        }






    }
}

/* Limpia Tabla */

function limpiarTabla(nombreTabla, tabla2) {

    let tbl = document.getElementById(nombreTabla);
    tbl.innerHTML = '';

    if (tabla2 != '') {
        let tbl2 = document.getElementById(tabla2);
        tbl2.innerHTML = '';
    }
}

/* Nuevas */
async function SeleccionarFilaTabla(idElemento) {

    let fila = document.getElementById(idElemento);
    let elementoEstilo = window.getComputedStyle(fila);
    let colorSelect = elementoEstilo.getPropertyValue("background-color");

    if (colorSelect == "rgb(255, 136, 130)") {
        fila.style.backgroundColor = 'var(--color-contenedor)';
    }
    else {
        fila.style.backgroundColor = 'var(--color-resalte)';
    }
}

