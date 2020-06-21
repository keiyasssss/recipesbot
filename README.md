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

```
TELEGRAM_TOKEN = "AAAA"
TELEGRAM_GROUP_ID = 12345
AEMET_TOKEN = "BBBBB"
CITY_ID = "03333"
WEATHER_SCHEDULE = (
    '08:00',
    '12:00',
    '15:00',
    '18:00',
    '22:00',
    '00:00'
)
```

### Aclaración

Descripción de cada parámetro de la configuración:

- TELEGRAM_TOKEN --> Token del bot telegram
- TELEGRAM_GROUP_ID --> Token del chat/grupo al que quieres mandar mensajes.
- AEMET_TOKEN --> Token de la AEMET para consultar el tiempo
- CITY_ID --> Id de la ciudad según el INE para consultar el tiempo
- WEATHER_SCHEDULE --> Lista de horas en las que quieres que se te envíe el tiempo