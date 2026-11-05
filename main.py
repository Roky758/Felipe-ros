import csv
import os
import random
from datetime import datetime, timezone
from pathlib import Path

import requests

THINGSPEAK_URL = "https://api.thingspeak.com/update"
CSV_PATH = Path("temperatura_humedad.csv")


def main() -> None:
    api_key = os.environ.get("THINGSPEAK_API_KEY")
    if not api_key:
        raise RuntimeError("Configura el secreto THINGSPEAK_API_KEY.")

    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)

    with CSV_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["fecha_hora_utc", "temperatura_c", "humedad_pct"])
        writer.writerow([timestamp, temperature, humidity])

    response = requests.post(
        THINGSPEAK_URL,
        data={
            "api_key": api_key,
            "field1": temperature,
            "field2": humidity,
        },
        timeout=20,
    )
    response.raise_for_status()

    try:
        entry_id = int(response.text.strip())
    except ValueError as exc:
        raise RuntimeError(
            f"ThingSpeak devolvio una respuesta inesperada: {response.text[:200]!r}"
        ) from exc

    if entry_id == 0:
        raise RuntimeError(
            "ThingSpeak no acepto la medicion. Comprueba el canal y el intervalo."
        )

    print(
        f"Medicion enviada (entrada {entry_id}): "
        f"temperatura={temperature} C, humedad={humidity}%"
    )
    print(f"Medicion guardada en {CSV_PATH}")


if __name__ == "__main__":
    main()
