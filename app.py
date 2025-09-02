# app.py
from fastapi import FastAPI
from sqlalchemy import text
from database.conexion import engine

app = FastAPI()

@app.get("/estado_lote/{lote_id}")
def get_estado_lote(lote_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("""
                SELECT el.nombre AS estado
                FROM public.lote l
                LEFT JOIN public.estado_lote el ON el.id = l.estado_id
                WHERE l.id = :lote_id
            """),
            {"lote_id": lote_id}
        ).fetchone()

    if result:
        return {"estado": result.estado}
    return {"error": "Lote no encontrado"}
