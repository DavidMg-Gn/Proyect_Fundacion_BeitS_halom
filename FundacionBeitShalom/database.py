import pyodbc

def obtener_conexion():

    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=BeitShalomDB;"
        "UID=sa;"
        "PWD=TuContraseña;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    return conexion
