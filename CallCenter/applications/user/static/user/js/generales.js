function generals(event) {
    event.preventDefault();
    $("#btnEnviar").prop('disabled', true);
    var auth = $('input[name=csrfmiddlewaretoken]').val();
    let text_information = $("#text_information").val();
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", auth);
    formData.append("response", text_information);
    $.ajax({
        url: '/give_response/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            if (data.allOk == true){
                $("#btnEnviar").prop('disabled', false);
                $("#text_information").val('');
            } else {
                Swal.fire(
                    'Algo ha salido mal',
                    'Por favor vuelvelo a intentar.',
                    'error'
                )
            }
        },
        error: function (xhr, status, error) {
            // Función que se ejecuta si la solicitud falló
            Swal.fire(
                'Error',
                'Algo salio mal',
                'error'
            ).then(() => {
                location.reload();
            });
        }
    });
}

function get_conversacion(event) {
    event.preventDefault();
    $("#btnConversation").prop('disabled', true);
    var auth = $('input[name=csrfmiddlewaretoken]').val();
    $("#send_information").val('');
    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", auth);
    $.ajax({
        url: '/get_conversacion/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            if (data.allOk == true){
                $("#btnConversation").prop('disabled', false);
                $("#send_information").val(data.conversation);
            } else {
                Swal.fire(
                    'Algo ha salido mal',
                    'Por favor vuelvelo a intentar.',
                    'error'
                )
            }
        },
        error: function (xhr, status, error) {
            // Función que se ejecuta si la solicitud falló
            Swal.fire(
                'Error',
                'Algo salio mal',
                'error'
            ).then(() => {
                location.reload();
            });
        }
    });
}
