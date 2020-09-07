function enviarDatosBusqueda(){
    let control = document.getElementsByName("control")[0].value;
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;
    let ruta = document.getElementsByName("ruta")[0].value;

    if (annoIni < annoFin || annoIni == annoFin){
        
        if(ruta != ""){
            eel.buscador_recibo(control, periodoIni, annoIni, periodoFin, annoFin, ruta);
        }
        
    }
    else{
        alert('los Años no son validos')
    }

}



async function mostrarDirGuardado(){
    let directorio = await eel.ruta_metadatos()();     
    
    document.getElementsByName("ruta")[0].value = directorio;
    
    console.log(directorio);
}