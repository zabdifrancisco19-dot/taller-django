# LIBRERIAS
import json
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Proyecto


# VISTA
@method_decorator(csrf_exempt, name='dispatch')
class ProyectoView(View):

    # GET: leer. Si no llega pk lista todos, si llega pk trae solo uno
    def get(self, request, pk=None):
        if pk is None:
            proyectos = list(Proyecto.objects.values())
            return JsonResponse(proyectos, safe=False)

        try:
            proyecto = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return JsonResponse({'error': 'Proyecto no encontrado'}, status=404)

        return JsonResponse({
            'id': proyecto.id,
            'nombre': proyecto.nombre,
            'descripcion': proyecto.descripcion,
        })

    # POST: crear un proyecto nuevo con los datos que llegan en el cuerpo
    def post(self, request):
        try:
            datos = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)

        proyecto = Proyecto.objects.create(
            nombre=datos['nombre'],
            descripcion=datos.get('descripcion', ''),
        )
        return JsonResponse({'id': proyecto.id, 'mensaje': 'Proyecto creado'}, status=201)

    # PUT: actualizar un proyecto que ya existe
    def put(self, request, pk):
        try:
            proyecto = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return JsonResponse({'error': 'Proyecto no encontrado'}, status=404)

        datos = json.loads(request.body)
        proyecto.nombre = datos['nombre']
        proyecto.descripcion = datos.get('descripcion', '')
        proyecto.save()
        return JsonResponse({'mensaje': 'Proyecto actualizado'})

    # DELETE: eliminar un proyecto
    def delete(self, request, pk):
        try:
            proyecto = Proyecto.objects.get(pk=pk)
        except Proyecto.DoesNotExist:
            return JsonResponse({'error': 'Proyecto no encontrado'}, status=404)

        proyecto.delete()
        return JsonResponse({'mensaje': 'Proyecto eliminado'})