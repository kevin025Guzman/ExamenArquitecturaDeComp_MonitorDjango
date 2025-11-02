import psutil
import platform
from django.shortcuts import render

def obtener_datos_sistema():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disco = psutil.disk_usage('/')
    
    datos = {
        'cpu': cpu,
        'cpu_libre': 100 - cpu,
        'ram_total': round(ram.total / (1024**3), 2),
        'ram_usada': round(ram.used / (1024**3), 2),
        'ram_percent': ram.percent,
        'ram_libre': round(ram.total / (1024**3) - ram.used / (1024**3), 2),
        'disco_total': round(disco.total / (1024**3), 2),
        'disco_usado': round(disco.used / (1024**3), 2),
        'disco_libre': round(disco.free / (1024**3), 2),
        'os_info': platform.platform(),
        'cores': psutil.cpu_count(),
    }
    return datos

def index(request):
    datos = obtener_datos_sistema()
    return render(request, 'sistema/index.html', {'datos': datos})
