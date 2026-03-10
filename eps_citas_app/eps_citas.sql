-- ============================================================
--  Script SQL – EPS CitaMédica
--  Base de datos: eps_citas
--  Tablas: pacientes, citas
-- ============================================================

CREATE DATABASE IF NOT EXISTS eps_citas
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE eps_citas;

-- ── TABLA: pacientes ──────────────────────────────────────────
CREATE TABLE IF NOT EXISTS pacientes (
  id        INT AUTO_INCREMENT PRIMARY KEY,
  documento VARCHAR(15)  NOT NULL UNIQUE,
  nombre    VARCHAR(80)  NOT NULL,
  apellido  VARCHAR(80)  NOT NULL,
  telefono  VARCHAR(20),
  correo    VARCHAR(100),
  eps       VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ── TABLA: citas ──────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS citas (
  id            INT AUTO_INCREMENT PRIMARY KEY,
  documento     VARCHAR(15)  NOT NULL,
  medico        VARCHAR(100) NOT NULL,
  tipo_cita     VARCHAR(50)  NOT NULL,
  fecha         DATE         NOT NULL,
  hora          TIME         NOT NULL,
  direccion_eps VARCHAR(150),
  FOREIGN KEY (documento) REFERENCES pacientes(documento)
    ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ── DATOS DE PRUEBA ───────────────────────────────────────────
INSERT INTO pacientes (documento, nombre, apellido, telefono, correo, eps)
VALUES
  ('1020304050', 'María',  'Rodríguez', '3001234567', 'maria@correo.com', 'Sura'),
  ('9876543210', 'Carlos', 'Pérez',     '3117654321', 'carlos@correo.com', 'Sanitas');

INSERT INTO citas (documento, medico, tipo_cita, fecha, hora, direccion_eps)
VALUES
  ('1020304050', 'Dr. Andrés Gómez',  'General',     '2024-08-15', '09:00:00', 'Calle 45 # 12-30, Bogotá'),
  ('1020304050', 'Dra. Laura Torres', 'Especialista', '2024-09-02', '14:30:00', 'Carrera 7 # 32-16, Bogotá'),
  ('9876543210', 'Dr. Felipe Ruiz',   'Odontología',  '2024-08-20', '11:00:00', 'Av. El Dorado # 68B-85, Bogotá');

-- ── CONSULTA JOIN (referencia del proyecto) ───────────────────
-- SELECT
--   pacientes.nombre, pacientes.apellido,
--   citas.medico, citas.tipo_cita,
--   citas.fecha, citas.hora, citas.direccion_eps
-- FROM pacientes
-- INNER JOIN citas ON pacientes.documento = citas.documento
-- WHERE pacientes.documento = %s;
