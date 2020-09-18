const API = "http://localhost:3000/api/";

$("#login").submit(function (e) {
    e.preventDefault();
});

function contacto() {
    $("#alertas").append(
        generarTexto(
            "Si has olvidado tu contraseña comunicate con la institucion"
        )
    );
    $("#alertas").show(300);
    alerta(10000);
}

function alerta(tiempo) {
    if (tiempo == null) {
        tiempo = 2000;
    }
    window.setTimeout(function () {
        $(".alert")
            .fadeTo(500, 0)
            .slideUp(500, function () {
                $(this).remove();
            });
    }, tiempo);
}

function generarTexto(texto, tipo) {
    let general = `
  <div class="alert alert-${tipo}" role="alert">
        ${texto}
  </div>
  `;
    return general;
}

function validateData() {
    $("#alertas").css("display", "none");
    const data = $("form").serializeArray();

    if (data[0].value === "") {
        $("#alertas").append(generarTexto("Ingrese un Nickname", "danger"));
    }

    if (data[1].value === "") {
        $("#alertas").append(generarTexto("Ingrese una Contraseña", "danger"));
    }

    if (data[0].value !== "" && data[1].value !== "") {
        buscarDatosUsuariosNick(data[0].value).then((datosAPI) => {
            if (datosAPI.response.length === 0) {
                $("#alertas").append(
                    generarTexto("Nombre de usuario no encontrado", "danger")
                );
            } else {
                if (datosAPI.response[0].pass === data[1].value) {
                    $("#alertas").append(
                        generarTexto("Contraseña correcta, Ingresando", "success")
                    );
                    setTimeout(function () {
                        location.href = "../Dashboard/views/index.html";
                    }, 3000);
                } else {
                    $("#alertas").append(generarTexto("Contraseña Incorrecta", "danger"));
                    console.log("no puedes pasar");
                }
            }
        });
        $("#alertas").show(300);
    }

    $("#alertas").show(300);
    alerta();
}

async function buscarDatosUsuariosNick(nick) {
    let url = "" + API + `usuarios/${nick}`;
    let defaultOptions = {
        mode: "cors",
        headers: {
            "Access-Control-Allow-Origin": "*",
        },
    };
    let response = await fetch(url, defaultOptions);
    return await response.json();
}
