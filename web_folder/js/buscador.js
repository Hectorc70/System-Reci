function enviarDatosBusqueda(){
  
    let control = document.getElementsByName("control")[0].value;
    let periodoIni = document.getElementsByName("periodo-ini")[0].value;
    let annoIni = document.getElementsByName("anno-ini")[0].value;
    let periodoFin = document.getElementsByName("periodo-fin")[0].value;
    let annoFin = document.getElementsByName("anno-fin")[0].value;

    eel.buscador_recibo(control, periodoIni, annoIni, periodoFin, annoFin)

}