# Taller: Peticiones en Django

Docente: Jose Javier Torres Vanstrahlen
Curso: Desarrollo de aplicaciones Web I 4E
Estudiante: Zabdi Francisco

## Qué se hizo

Se creó un endpoint en Django nativo, sin librerías externas, con una vista basada en clase llamada `ProyectoView`. La clase tiene los métodos `get()`, `post()`, `put()` y `delete()`, uno por cada verbo HTTP. Los archivos modificados fueron `views.py` y `urls.py` de la app `peticiones`, además de `models.py` para la tabla y `settings.py` para registrar la app.

## Verbos HTTP y CRUD

- GET es Read. Sirve para consultar un proyecto o la lista completa, y no modifica datos.
- POST es Create. Envía datos en el cuerpo de la petición para crear un registro nuevo.
- PUT es Update. Reemplaza los datos de un registro que ya existe, por eso necesita el pk en la URL.
- DELETE es Delete. Elimina el registro que indica el pk.

## Módulos, funciones y decoradores usados

- django.views.View: clase base de las vistas basadas en clase. Trae as_view, dispatch y http_method_names.
- as_view(): se usa en urls.py y convierte la clase en una vista que Django puede ejecutar.
- dispatch(): revisa el verbo de la petición y la envía al método que se llama igual, como get o post. Si no existe, responde 405.
- http_method_names: lista de verbos que acepta la vista.
- django.http.JsonResponse: devuelve la respuesta en formato JSON. Con safe=False permite devolver listas y con status define el código.
- request.body: contiene el cuerpo de la petición. En POST y PUT se lee con json.loads.
- json: módulo de Python que convierte el texto JSON a diccionario.
- django.urls.path: define las rutas, y con int:pk captura el identificador de la URL.
- django.urls.include: conecta el urls.py de la app con el del proyecto.
- django.views.decorators.csrf.csrf_exempt: desactiva la verificación del token CSRF. Se usó para poder probar POST, PUT y DELETE desde la consola.
- django.utils.decorators.method_decorator: permite usar un decorador de funciones sobre una clase. Se aplicó sobre dispatch.
- Métodos del ORM: objects.values, get, create, save y delete, para consultar, crear, guardar y borrar en la base de datos.

## Rutas

- GET y POST: `/api/proyectos/`
- GET, PUT y DELETE: `/api/proyectos/<id>/`

## Cómo ejecutarlo

Instalar Django con `pip install django`, correr `python manage.py migrate` y luego `python manage.py runserver`. Después abrir `http://127.0.0.1:8000/api/proyectos/`.

## Fuentes consultadas

- https://docs.djangoproject.com/en/stable/ref/class-based-views/base/
- https://docs.djangoproject.com/en/stable/topics/class-based-views/intro/
- https://docs.djangoproject.com/en/stable/ref/request-response/
- https://docs.djangoproject.com/en/stable/topics/http/urls/
- https://docs.djangoproject.com/en/stable/ref/csrf/
- https://docs.python.org/3/library/json.html