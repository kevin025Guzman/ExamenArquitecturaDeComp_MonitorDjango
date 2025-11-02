import psutil
import platform

def obtener_datos_sistema():
    try:
        cpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()
        disco = psutil.disk_usage('/')

        return {
            "cpu": cpu,
            "ram_total": round(memoria.total / (1024**3), 2),
            "ram_usada": round(memoria.used / (1024**3), 2),
            "ram_porcentaje": memoria.percent,
            "disco_total": round(disco.total / (1024**3), 2),
            "disco_usado": round(disco.used / (1024**3), 2),
            "disco_libre": round(disco.free / (1024**3), 2),
            "disco_porcentaje": disco.percent,
            "so": platform.system(),
            "version": platform.release(),
            "nucleos": psutil.cpu_count(logical=True),
        }
    except Exception as e:
        return {"error": str(e)}
