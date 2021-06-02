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

async function borrarTabla(idTablaCuerpo){
    let dataTable = document.getElementById(idTablaCuerpo);

    if (dataTable.innerHTML != ''){
        dataTable.innerHTML = '';
    }
}

/* Animaciones de card de parametros de entrada */

function animacionCancelarVistaArchivos(idTablaCuerpo) {
    let cardParams = document.getElementById("recuperar-parametros");
    borrarTabla(idTablaCuerpo)
    let vista = document.getElementById("vista-resultados-archivos");
    vista.style.transform = 'translate(0px,1000px)';
    vista.style.transition = 'all 0.5s ease-in-out';

    cardParams.style.transform = 'translate(0px,0px)';
    cardParams.style.transition = 'all 0.5s ease-in-out';
}


function animacionVistaArchivos() {

    let cardParams = document.getElementById("recuperar-parametros");
    let vista = document.getElementById("vista-resultados-archivos");
    cardParams.setAttribute('class', 'animate-move card-contenedor');
    cardParams.style.transform = 'translate(-550px,-700px)';
    cardParams.style.transition = 'all 0.5s ease-in-out';

    vista.style.display = 'block';
    vista.style.visibility = 'visible';
    vista.style.transform = 'translate(0%, -80%)';
    vista.style.transition = 'all 0.5s ease-in-out';

}


/* Utilidades  tablas */

function cambiardeTipoVista(idpest, idpestNoSelect, idTablaMostrar, idTablaNoMostrar) {
    let CuerpoTabla = document.getElementById(idTablaMostrar);
    let CuerpoTablaNoMostrar = document.getElementById(idTablaNoMostrar);

    let pestSelect = document.getElementById(idpest);
    let pestNoSelect = document.getElementById(idpestNoSelect);
    CuerpoTabla.style.transform = 'translate(0px,0px)';
    CuerpoTabla.style.opacity = '100%';
    CuerpoTabla.style.transition = 'all 0.5s ease-in-out';


    CuerpoTablaNoMostrar.style.transform = 'translate(2000px, 0px)';
    CuerpoTablaNoMostrar.style.opacity = '0%';
    CuerpoTablaNoMostrar.style.transition = 'all 0.5s ease-in-out';



    pestSelect.style.backgroundColor = 'var(--color-secundario)';
    pestSelect.style.borderTop = '3px solid var(--color-resalte)'
    pestNoSelect.style.backgroundColor = 'var(--color-contenedor)';
    pestNoSelect.style.borderTop = '3px solid var(--color-contenedor)';

}