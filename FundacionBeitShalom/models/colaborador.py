class Colaborador:

    def __init__(
        self,
        nombre,
        pais,
        correo,
        telefono,
        modalidad,
        disponibilidad,
        motivacion
    ):

        self.nombre = nombre
        self.pais = pais
        self.correo = correo
        self.telefono = telefono
        self.modalidad = modalidad
        self.disponibilidad = disponibilidad
        self.motivacion = motivacion

    def validar(self):

        errores = []

        if not self.nombre.strip():
            errores.append(
                "El nombre es obligatorio."
            )

        if not self.pais.strip():
            errores.append(
                "Debes seleccionar un país."
            )

        if "@" not in self.correo:
            errores.append(
                "El correo no es válido."
            )

        if self.modalidad not in [
            "Presencial",
            "Virtual",
            "Ambas"
        ]:
            errores.append(
                "La modalidad no es válida."
            )
return errores
