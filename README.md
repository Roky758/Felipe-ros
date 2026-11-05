# Registro simulado de temperatura y humedad

El proyecto genera valores simulados, los envia a ThingSpeak y guarda cada
medicion en un CSV. GitHub Actions lo ejecuta cada 15 minutos. Cada ejecucion
genera un artefacto CSV descargable que se conserva durante 30 dias.

## Configuracion

1. En el repositorio, abre **Settings > Secrets and variables > Actions**.
2. Crea un repository secret llamado `THINGSPEAK_API_KEY` e introduce ahi la
   API key de ThingSpeak. No la incluyas en el codigo ni la publiques.
3. Abre **Actions**, selecciona **Enviar temperatura y humedad** y pulsa
   **Run workflow** para probarlo.

El workflow tambien se ejecuta automaticamente cada 15 minutos. GitHub puede
retrasar las ejecuciones programadas y no garantiza que ocurran exactamente
al minuto previsto.

## Descargar el CSV

En **Actions**, abre una ejecucion y descarga el artefacto
`temperatura-humedad-...`. GitHub Actions usa una maquina temporal: cada
ejecucion produce un CSV independiente, guardado como artefacto por 30 dias.

## Ejecucion local

Instala dependencias con `python -m pip install -r requirements.txt`, configura
la variable de entorno `THINGSPEAK_API_KEY` y ejecuta `python main.py`.
El script genera una medicion por ejecucion.

Los valores son aleatorios y no proceden de un sensor fisico.
