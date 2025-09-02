# database/update_lote.py
from sqlalchemy import text
from conexion import engine

def actualizar_estado_lote(lote_id: int, nuevo_estado_id: int):
    query = text("""
        UPDATE lote
        SET estado_id = :estado_id
        WHERE id = :lote_id
    """)
    try:
        with engine.begin() as conn:
            conn.execute(query, {
                "estado_id": nuevo_estado_id,
                "lote_id": lote_id
            })
        print(f"✅ Lote {lote_id} actualizado al estado {nuevo_estado_id}")
    except Exception as e:
        print("❌ Error al actualizar el lote:", e)
