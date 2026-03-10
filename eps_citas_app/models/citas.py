from database import get_connection

def reservar_cita(documento, medico, tipo_cita, fecha, hora, direccion_eps):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """INSERT INTO citas (documento, medico, tipo_cita, fecha, hora, direccion_eps)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (documento, medico, tipo_cita, fecha, hora, direccion_eps))
    conn.commit()
    cursor.close()
    conn.close()

def consultar_cita(documento):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    sql = """SELECT
                pacientes.nombre,
                pacientes.apellido,
                pacientes.documento,
                pacientes.eps,
                citas.id,
                citas.medico,
                citas.tipo_cita,
                citas.fecha,
                citas.hora,
                citas.direccion_eps
             FROM pacientes
             INNER JOIN citas ON pacientes.documento = citas.documento
             WHERE pacientes.documento = %s
             ORDER BY citas.fecha DESC, citas.hora DESC"""
    cursor.execute(sql, (documento,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

def obtener_cita_por_id(cita_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM citas WHERE id = %s", (cita_id,))
    cita = cursor.fetchone()
    cursor.close()
    conn.close()
    return cita

def actualizar_cita(cita_id, medico, tipo_cita, fecha, hora):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """UPDATE citas SET medico=%s, tipo_cita=%s, fecha=%s, hora=%s
             WHERE id=%s"""
    cursor.execute(sql, (medico, tipo_cita, fecha, hora, cita_id))
    conn.commit()
    cursor.close()
    conn.close()
