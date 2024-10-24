# Quiz_DJANGO_Hospital
Hola amigos de YouTUbe bienvenidos a este videotutorial el dia de hoy vengo a explicarles este trabajo hecho por alejandro y dariel asi que empezemos:

Paso 1: instala las dependencias: pip install mysqlclient, pip install djangorestframework, py -m pip install Django==5.1.2

Paso 2:dando por hecho que cuentas con unos modelos ya establecidos (cosa que el trabajo otorga al tester) deberias revisar el achivo urls.py en e cual deberias encontrar codigos similares a :

path('pacientes/', views.PacientesListCreate.as_view(), name='producto-list'),      ##(el valor "paciente" deberia ser remplazado por el endpoint a revisar)##
path('pacientes/<int:pk>/', views.PacientesDetail.as_view(), name='producto-detail'),

los cuales tienen el objetivo de establecer la ruta de el endpoint para acceder al framework de django con el endpoint y el segundo nos srive para acceder a un valor especifico del endpoint por medio de un id, 

Paso 3: luego deberias darle un vistazo al archivo views.py en el cual deberia haber dos vistas para cada endpoint una que ejecute el get y post (generics.ListCreateAPIView) y la otra para realizar el delete, put y patch. 

Paso 3:tras esto la ultima parte de las verificaciones manuales seria revisar si tu endpoint esta serializado (convertido a json) en serializers.py 

Paso 4:tras revisar y verificar todos los archivos ya deberias ser capaz de levantar tu servidor con el comando: python manage.py runserver

Paso5: crea en tu mysql workbench una base de datos llamada "hospital" 

paso 6: ejecuta el comando:python manage.py makemigrations para establecer la migracion

paso 7: ejecuta el comando: python manage.py migrate para realizar la migracion previamente establecida

Tras realizar estos pasos deberias ser capaz de visualizar los endpoints que migraste en tu base de datos como tablas

paso 8: tras haber levantado el servidor  en el paso 4 en tu terminal deberia haberse generado un enlace, realiza un click + control para que el enlace te lleve al framework, ahi deberias poner en la url el endpoint que quieras revisar

Get y Post: puedes realizar el metodo post con el boton "get" y para el metodo post deberias ingresar los valores que quieres ingresar a el endpoint

Delete y Put: para poder acceder a estos metodos debes añadir la id del endpoint que quieras revisar, para realizar el put deberias cambiar los valores que desees editar y clickear el boton correspondiente, y para realizar el delete simplemente debes clickear el boton correspondiente  