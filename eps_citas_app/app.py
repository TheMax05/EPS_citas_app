from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models.pacientes import registrar_paciente, paciente_existe, obtener_paciente
from models.citas import reservar_cita, consultar_cita, obtener_cita_por_id, actualizar_cita

app = Flask(__name__)
app.secret_key = Config.SECRET_KEY

# ─── INICIO ────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

# ─── PACIENTES ─────────────────────────────────────────────────────────────────
@app.route('/registro_paciente', methods=['GET', 'POST'])
def registro_paciente():
    if request.method == 'POST':
        documento  = request.form['documento'].strip()
        nombre     = request.form['nombre'].strip()
        apellido   = request.form['apellido'].strip()
        telefono   = request.form['telefono'].strip()
        correo     = request.form['correo'].strip()
        eps        = request.form['eps'].strip()

        if not all([documento, nombre, apellido, telefono, correo, eps]):
            flash('Todos los campos son obligatorios.', 'error')
            return render_template('registro_paciente.html')

        if paciente_existe(documento):
            flash('Ya existe un paciente con ese número de identificación.', 'error')
            return render_template('registro_paciente.html')

        try:
            registrar_paciente(documento, nombre, apellido, telefono, correo, eps)
            flash('Paciente registrado exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al registrar: {str(e)}', 'error')

    return render_template('registro_paciente.html')

# ─── CITAS ─────────────────────────────────────────────────────────────────────
@app.route('/reservar_cita', methods=['GET', 'POST'])
def reservar_cita_view():
    if request.method == 'POST':
        documento     = request.form['documento'].strip()
        medico        = request.form['medico'].strip()
        tipo_cita     = request.form['tipo_cita']
        fecha         = request.form['fecha']
        hora          = request.form['hora']
        direccion_eps = request.form['direccion_eps'].strip()

        if not all([documento, medico, tipo_cita, fecha, hora, direccion_eps]):
            flash('Todos los campos son obligatorios.', 'error')
            return render_template('reservar_cita.html')

        if not paciente_existe(documento):
            flash('No existe un paciente con ese documento. Regístrelo primero.', 'error')
            return render_template('reservar_cita.html')

        try:
            reservar_cita(documento, medico, tipo_cita, fecha, hora, direccion_eps)
            flash('Cita reservada exitosamente.', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error al reservar la cita: {str(e)}', 'error')

    return render_template('reservar_cita.html')

@app.route('/consulta_cita', methods=['GET', 'POST'])
def consulta_cita():
    resultados = None
    documento = ''
    if request.method == 'POST':
        documento = request.form['documento'].strip()
        if not documento:
            flash('Ingrese un número de identificación.', 'error')
        else:
            resultados = consultar_cita(documento)
            if not resultados:
                flash('No se encontraron citas para ese documento.', 'error')
    return render_template('consulta_cita.html', resultados=resultados, documento=documento)

@app.route('/actualizar_cita/<int:cita_id>', methods=['GET', 'POST'])
def actualizar_cita_view(cita_id):
    cita = obtener_cita_por_id(cita_id)
    if not cita:
        flash('Cita no encontrada.', 'error')
        return redirect(url_for('consulta_cita'))

    if request.method == 'POST':
        medico    = request.form['medico'].strip()
        tipo_cita = request.form['tipo_cita']
        fecha     = request.form['fecha']
        hora      = request.form['hora']

        if not all([medico, tipo_cita, fecha, hora]):
            flash('Todos los campos son obligatorios.', 'error')
        else:
            try:
                actualizar_cita(cita_id, medico, tipo_cita, fecha, hora)
                flash('Cita actualizada exitosamente.', 'success')
                return redirect(url_for('consulta_cita'))
            except Exception as e:
                flash(f'Error al actualizar: {str(e)}', 'error')

    return render_template('actualizar_cita.html', cita=cita)

if __name__ == '__main__':
    app.run(debug=True)
