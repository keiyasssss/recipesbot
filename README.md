# Bot Telegram

Este es un proyecto python con el código para interactuar con un bot de telegram

## Comandos disponibles

Los comandos disponibles de momento son:

* recipe - Gestión de recetas y menús semanales
* add - Suma números separados por espacio
* start - Da un mensaje de bienvenida
* hello - Saluda al usuario por su nombre
* weather - Se conecta a AEMET y descarga la previsión meteorológica

## Tareas periódicas

Las tareas que se ejecutan periódicamente son las siguientes:

- weather

## Configuración

Es necesario la creación de un fichero **docker-compose.override.yml** con los siguientes datos:

```
version: '3'
services:
  recipesbot:
    environment: 
        - TELEGRAM_TOKEN=AAAA
        - TELEGRAM_GROUP_ID=1111
        - AEMET_TOKEN=
        - CITY_ID=
```

### Aclaración

Descripción de parámetros de configuración que se sobreescribirá en el fichero **docker-compose.override.yml**:

- TELEGRAM_TOKEN --> Token del bot telegram
- TELEGRAM_GROUP_ID --> Token del chat/grupo al que quieres mandar mensajes.
- AEMET_TOKEN --> Token de la AEMET para consultar el tiempo
- CITY_ID --> Id de la ciudad según el INE para consultar el tiempo

Descripción de parámetros de configuración del fichero  **docker-compose.yml**:

- POSTGRES_HOST --> Servidor de base de datos (host)
- POSTGRES_USER --> Usuario de la base de datos
- POSTGRES_PASSWORD --> Password de la base de datos
- POSTGRES_DATABASE --> Nombre de la base de datos
- WEATHER_SCHEDULE --> Horas separadas por ',' a las que queremos que se nos mande la previsión

## Servidor PosrgreSQL con Docker

El servidor Postgre también está dockerizado

### Scripts creación de tablas

Tabla **menu_recipe**:

```
create table if not exists menu_recipe
(
    id        serial                not null
        constraint menu_recipe_pk
            primary key,
    is_lunch  boolean default false not null,
    is_dinner boolean default false not null,
    for_adult boolean default false not null,
    for_kids  boolean default false not null,
    name      text
);
```

# ¿Cómo montar el entorno?

Ir a la raíz del proyecto, una vez creado el **docker-compose.override.yml** y ejecutar el comando:

```
$ docker-compose build
```

Una vez termine dejamos el entorno en ejecución:

```
$ docker-compose up
```

Para resetear el entorno:

```
$ docker-compose down -v
```

A la base de datos podremos conectarnos usando los datos configurados, el host será **0.0.0.0**

# Funcionamiento

Describimos alguna de las funcionalidades del bot.

## Recetas

La idea de la parte de recetas es que sea capaz de:

- Listar todas las recetas
- Dar una receta aleatoria
- Proponer un menú semanal para adultos y niños sin que se repitan las recetas

Así es como está ahora mismo:

![Alt Text](img/bot_telegram.gif)