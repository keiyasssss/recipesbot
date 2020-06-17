# Bot Telegram

Este es un proyecto python con el código para interactuar con un bot de telegram

## Comandos disponibles

Los comandos disponibles de momento son:

- add: Suma números separados por espacio
- start: Da un mensaje de bienvenida
- hello: Saluda al usuario por su nombre
- weather: Se conecta a AEMET y descarga la previsión meteorológica

## Tareas periódicas

Las tareas que se ejecutan periódicamente son las siguientes:

- weather

## Configuración

Es necesaria la creación de un fichero **config.py** con los siguientes datos:

TELEGRAM_TOKEN = "AAAA"
TELEGRAM_GROUP_ID = 12345
WAIT_TIME_SECONDS_WEATHER = 3600
AEMET_TOKEN = "BBBBB"
CITY_ID = "03333"