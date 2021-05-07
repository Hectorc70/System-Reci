'use strict'
/* MAIN */
window.onload = function () {
    setTimeout(carga, 1000);}
/* 

function carga(){
    $('#preloader').fadeOut();
    $('#menu-principal').removeClass('hide');
} */
/* Funciones que son para mostrar una animación de loader*/
function loader(){      
    let carga = document.getElementById("loader");    
    carga.setAttribute("class", "lds-roller");
}

function deshabilitar(elemento){
    let elementoPadre = document.getElementById(elemento);
    elementoPadre.setAttribute("class", "deshabilitado");
    let backBlock = document.createElement("div");
    backBlock.style.position = "absolute";
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

function habilitarElemento(elemento){
    let etiqueta = document.getElementById(elemento);
    etiqueta.removeAttribute("class");
}

function habilitar(elemento){ 
    let carga = document.getElementById("loader");  
    let etiqueta = document.getElementById(elemento);  
    carga.removeAttribute("class");
    etiqueta.removeAttribute("class");
    
        

}

/* Muestra una ruta en el imput pasado como parametro */
async function mostrarRuta(nombre) {
    let ruta = await eel.enviar_ruta()();
    document.getElementsByName(nombre)[0].value = ruta;
    console.log(ruta);
}

async function mostrarRutaArchivo(nombre){
    let ruta = await eel.enviar_ruta_archivo()();

    document.getElementsByName(nombre)[0].value = ruta;

}




async function mostrar_en_tabla() {

    let directorio = document.getElementsByName("ruta-reci")[0].value;
    let rutas = await eel.mostrar_rutas_recibos(directorio)();
    const rutas_num = Object.getOwnPropertyNames(rutas)

    debugger;
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

function limpiarTabla(nombreTabla, tabla2){
    
    let tbl = document.getElementById(nombreTabla);   
    tbl.innerHTML = '';    

    if(tabla2 !=''){
        let tbl2 = document.getElementById(tabla2);
        tbl2.innerHTML = '';
    }
}
