from django.http import JsonResponse
from .simulacion import Simulacion

simulacion = Simulacion()
def reiniciar_simulacion(request):
    simulacion.reiniciar()
    return JsonResponse({
        "automata": simulacion.grid.tolist(),
        "humedad" : simulacion.humedad_grid.tolist(),
        "quemado" : simulacion.quemado
    })

def siguiente_paso(request):
    simulacion.siguiente_paso()
    return JsonResponse({
        "automata": simulacion.grid.tolist(),
        "humedad" : simulacion.humedad_grid.tolist(),
        "quemado" : simulacion.quemado
    })

def pender_fuego(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    try:
        x = float(x)
        y = float(y)
        simulacion.poner_fuego([x, y])
    except (TypeError, ValueError):
        return JsonResponse({"error": "Los parámetros deben ser números flotantes"}, status=400)

    return JsonResponse({
        "automata": simulacion.grid.tolist(),
        "humedad": simulacion.humedad_grid.tolist(),
        "quemado": simulacion.quemado
    })

def poner_agua(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    try:
        x = float(x)
        y = float(y)
        simulacion.poner_agua([x, y])
    except (TypeError, ValueError):
        return JsonResponse({"error": "Los parámetros deben ser números flotantes"}, status=400)

    return JsonResponse({
        "automata": simulacion.grid.tolist(),
        "humedad": simulacion.humedad_grid.tolist(),
        "quemado": simulacion.quemado
    })

def cambiar_viento(request):
    direccion = request.GET.get('dir')
    simulacion.cambiar_velocidad(direccion)
    return JsonResponse({
        "automata": simulacion.grid.tolist(),
        "humedad": simulacion.humedad_grid.tolist(),
        "quemado": simulacion.quemado
    })