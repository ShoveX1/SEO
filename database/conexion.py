# database/conexion.py
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Cargar variables de entorno (.env)
load_dotenv()

# Leer la variable de entorno con tu URL de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL no está configurado en el archivo .env")

# Crear un engine reutilizable
engine = create_engine(DATABASE_URL, echo=False, future=True)
