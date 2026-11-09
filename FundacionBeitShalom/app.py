from flask import Flask

from controllers.colaborador_controller import (
    colaborador_bp
)

from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config["SECRET_KEY"] = "CAMBIAR_POR_UNA_CLAVE_SEGURA"
csrf = CSRFProtect(app)
app.register_blueprint(colaborador_bp)
@app.route("/")
def inicio():

    from flask import redirect, url_for

    return redirect(
        url_for("colaborador.registrar")
    )

if __name__ == "__main__":
    app.run(debug=True)
