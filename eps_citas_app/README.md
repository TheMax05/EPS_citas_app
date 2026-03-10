# 🏥 EPS CitaMédica – Guía de Instalación y Uso

Aplicación web desarrollada con **Python + Flask + MySQL** para la gestión de citas médicas.  
Proyecto SENA – Análisis y Desarrollo de Software (ADSO).

---

## 📁 Estructura del Proyecto

```
eps_citas_app/
├── app.py                  ← Rutas principales (Flask)
├── config.py               ← Configuración de la BD
├── database.py             ← Conexión MySQL
├── eps_citas.sql           ← Script SQL (crear BD y tablas)
├── requirements.txt        ← Dependencias Python
├── models/
│   ├── pacientes.py        ← CRUD pacientes
│   └── citas.py            ← CRUD citas
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── registro_paciente.html
│   ├── reservar_cita.html
│   ├── consulta_cita.html
│   └── actualizar_cita.html
└── static/
    └── css/
        └── style.css
```

---

## ⚙️ Instalación Paso a Paso

### 1. Requisitos previos
- Python 3.10+
- MySQL Server o XAMPP (con MySQL activo)
- Visual Studio Code (recomendado)

### 2. Crear entorno virtual
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos
1. Abre MySQL Workbench o phpMyAdmin.
2. Ejecuta el archivo `eps_citas.sql` completo.
3. Esto creará la base de datos `eps_citas` con las tablas y datos de prueba.

### 5. Ajustar credenciales (si es necesario)
Edita `config.py`:
```python
MYSQL_HOST     = "localhost"
MYSQL_USER     = "root"
MYSQL_PASSWORD = ""          # Tu contraseña de MySQL
MYSQL_DB       = "eps_citas"
```

### 6. Ejecutar la aplicación
```bash
python app.py
```

Abre el navegador en: **http://127.0.0.1:5000**

---

## 🚀 Funcionalidades

| Módulo | Ruta | Descripción |
|---|---|---|
| Inicio | `/` | Menú principal |
| Registrar Paciente | `/registro_paciente` | Crear nuevo paciente |
| Reservar Cita | `/reservar_cita` | Agendar cita médica |
| Consultar Cita | `/consulta_cita` | Buscar citas por documento |
| Actualizar Cita | `/actualizar_cita/<id>` | Modificar datos de cita |

---

## 🛠️ Tecnologías
- Python 3 · Flask · MySQL · Jinja2 · HTML5 · CSS3
