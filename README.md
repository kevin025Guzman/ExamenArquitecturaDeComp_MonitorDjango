# Monitor del Sistema con Django y Psutil

Este proyecto es una aplicación web desarrollada con **Django** que permite monitorear en tiempo real el estado del sistema utilizando la librería externa **psutil**.

La aplicación muestra información como:

- Porcentaje de uso del CPU
- Uso de memoria RAM (GB y %)
- Información del disco duro (espacio libre, usado y total)
- Información del sistema operativo
- Número de núcleos del procesador

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|----------|-----|
| Python 3 | Lenguaje principal |
| Django | Framework web |
| Psutil | Obtención de datos del sistema |
| HTML / CSS | Interfaz básica |
| Bootstrap (opcional) | Estilos para la interfaz |
| Git + GitHub | Control de versiones |

---

## 📦 Instalación y Dependencias

### ✅ 1. Clonar el repositorio

```bash
git clone https://github.com/kevin025Guzman/ExamenArquitecturaDeComp_MonitorDjango.git
cd ExamenArquitecturaDeComp_MonitorDjango
```bash
git clone <proyecto>
cd monitor
python -m venv venv
venv\Scripts\activate
pip install django psutil
python manage.py runserver