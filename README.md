## Proyecto con Django

### Pasos a seguir

##### Para generar la base de datos
- Cambiar los datos correspondientes a la base de datos en `settings.py`
- Ejecutar `python manage.py migrate`

#####  Crear un superusuario
- Ejecutar `python manage.py createsuperuser`
- Seguir pasos

##### Ejecutar los tests:
- Ejecutar `python manage.py test`
- Esperar el siguiente resultado

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.005s

OK
Destroying test database for alias 'default'...
```

Recordar ademas, cambiar los datos referentes al envio de correo via SMTP en `settings.py`
