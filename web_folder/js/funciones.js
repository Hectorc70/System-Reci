'use strict'
/* MAIN */
window.onload = function () {
    setTimeout(carga, 1000);
}

function carga(){
    $('#preloader').fadeOut();
    $('#menu-principal').removeClass('hide');
}
/* Funciones que son para mostrar una animación de loader*/
function loader_tarea(){      
    let carga = document.getElementById("loader");    
    carga.setAttribute("class", "preloader_2");
}

function deshabilitar(elemento){
    let etiqueta = document.getElementById(elemento);
    etiqueta.setAttribute("class", "deshabilitado");
    
    
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
