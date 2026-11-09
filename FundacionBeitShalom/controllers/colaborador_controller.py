from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for
)

from models.colaborador import Colaborador

colaborador_bp = Blueprint(
    "colaborador",
    __name__
)


@colaborador_bp.route(
    "/registro",
    methods=["GET", "POST"]
)
def registrar():

    if request.method == "POST":

        colaborador = Colaborador(
            nombre=request.form.get("nombre", ""),
            pais=request.form.get("pais", ""),
            correo=request.form.get("correo", ""),
            telefono=request.form.get("telefono", ""),
            modalidad=request.form.get("modalidad", ""),
            disponibilidad=request.form.get(
                "disponibilidad", ""
            ),
            motivacion=request.form.get("motivacion", "")
        )

        errores = colaborador.validar()

        areas = request.form.getlist("areas")

        if not areas:
            errores.append(
                "Selecciona al menos un área."
            )

        privacidad = request.form.get("privacidad")

        if privacidad != "1":
            errores.append(
                "Debes aceptar la política de privacidad."
            )

        if errores:

            for error in errores:
                flash(error, "error")

            return render_template("registro.html")

        # Aquí se invocará el repository
        # para guardar el colaborador.

        return redirect(
            url_for("colaborador.confirmacion")
        )

    return render_template("registro.html")


@colaborador_bp.route("/confirmacion")
def confirmacion():

    return render_template("confirmacion.html")
