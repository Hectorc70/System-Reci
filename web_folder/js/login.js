'use strict'

async function  loginUser() {

    let control = document.getElementsByName("control")[0].value;
    let password = document.getElementsByName("password")[0].value;
    if (control != '' && password != '') {
        deshabilitar("form-login");
        loader("form-login");
        let resp = await eel.login_user(control, password)();
        habilitar("form-login");
        noLoader("form-login");
        if (resp[0] == 0){

            error(resp[1])
        }
        else if (resp[0] == 200){
            if(resp[1]['is_staff'] == true){
                
                window.location.replace("/menu.html");
            }   
            else{
                window.location.replace("/buscador.html");
            }
            
        }
        
        else{
            error(resp[1]['non_field_errors'][0])
        }
        
        
    }

    else {
        Precaucion('Llene todos los campos');
    }
}
