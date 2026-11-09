document.addEventListener("DOMContentLoaded", () => {

    const formulario =
        document.getElementById("formRegistro");

    formulario.addEventListener("submit", (evento) => {

        let valido = true;

        const nombre =
            document.getElementById("nombre");

        const telefono =
            document.getElementById("telefono");

        const correo =
            document.getElementById("correo");

        const areas =
            document.querySelectorAll(
                'input[name="areas"]:checked'
            );

        const errorAreas =
            document.getElementById("errorAreas");

        // Validar nombre

        if (nombre.value.trim().length < 5) {

            nombre.setCustomValidity(
                "Ingresa tu nombre completo."
            );

            valido = false;

        } else {

            nombre.setCustomValidity("");

        }

        // Validar correo

        if (!correo.validity.valid) {

            correo.setCustomValidity(
                "Ingresa un correo electrónico válido."
            );

            valido = false;

        } else {

            correo.setCustomValidity("");

        }

        // Validar teléfono si se proporciona

        if (telefono.value.trim() !== "") {

            const patron =
                /^\+?[0-9\s()-]{7,30}$/;

            if (!patron.test(telefono.value.trim())) {

                telefono.setCustomValidity(
                    "Revisa el número de teléfono."
                );

                valido = false;

            } else {

                telefono.setCustomValidity("");

            }

        } else {

            telefono.setCustomValidity("");

        }

        // Validar selección de áreas

        if (areas.length === 0) {

            errorAreas.textContent =
                "Selecciona al menos un área.";

            valido = false;

        } else {

            errorAreas.textContent = "";

        }

        // Validar campos obligatorios restantes

        if (!formulario.checkValidity()) {

            valido = false;

        }

        // Evitar envío si hay errores

        if (!valido) {

            evento.preventDefault();

            formulario.reportValidity();

        }

    });

});