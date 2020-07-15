'use stric'



async function mostrar_ruta_metadatos(){
    let ruta = await eel.ruta_metadatos()();   
    document.getElementsByName("ruta-reci")[0].value = ruta;
    console.log(ruta);
}

async function mostrar_en_tabla(datos, nombre_tabla){
    let ruta = await eel.mostrar_periodos()();   
    document.getElementsByName("ruta-reci")[0].value = ruta;
    console.log(ruta);
}
/* eel.expose(prueba);
function prueba(){
    console.log("22")
    
} */
