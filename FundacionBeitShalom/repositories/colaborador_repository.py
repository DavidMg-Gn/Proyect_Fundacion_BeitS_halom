from database import obtener_conexion

class ColaboradorRepository:
    def guardar(self, colaborador, areas):
        conexion = obtener_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Colaboradores (
                    nombre_completo,
                    pais,
                    correo,
                    telefono,
                    modalidad,
                    disponibilidad,
                    motivacion,
                    acepta_privacidad
                )
                OUTPUT INSERTED.id
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                colaborador.nombre,
                colaborador.pais,
                colaborador.correo,
                colaborador.telefono,
                colaborador.modalidad,
                colaborador.disponibilidad,
                colaborador.motivacion,
                True
            ))

            colaborador_id = cursor.fetchone()[0]

            for area_id in areas:
                cursor.execute("""
                    INSERT INTO ColaboradorAreas (
                        colaborador_id,
                        area_id
                    )
                    VALUES (?, ?)
                """, (
                    colaborador_id,
                    int(area_id)
                ))

            conexion.commit()

            return colaborador_id

        except Exception:
            conexion.rollback()
            raise

        finally:
            conexion.close()
