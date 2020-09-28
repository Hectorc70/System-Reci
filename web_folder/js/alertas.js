
function Precaucion(mensaje) {
    deshabilitar('principal');
    Swal.fire({
        title: 'AVISO',
        text: mensaje,
        icon: 'warning',
        confirmButtonText: 'Entendido',
        confirmButtonColor: '#008992',
        background: '#363535',
        backdrop: false,
        width: '18rem',
        heightAuto: false,
    })
    habilitarElemento('principal');
}

function satisfactorio(mensaje) {
    Swal.fire({
        title: 'AVISO',
        text: mensaje,
        icon: 'success',
        confirmButtonText: 'Entendido',
        confirmButtonColor: '#008992',
        background: '#363535',
        backdrop: false,
        width: '18rem',
        heightAuto: false,
    })
    habilitarElemento('principal');

}

