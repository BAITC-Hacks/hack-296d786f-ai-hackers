import json
from pathlib import Path


def main():
    # Читаем события из файла рядом со скриптом.
    path = Path(__file__).with_name("events.json")
    events = json.loads(path.read_text(encoding="utf-8"))

    # «Тихий пульт»: пропускаем только критичные события.
    critical_events = [
        event for event in events
        if event["level"] == "critical"
    ]

    # Показываем события, которые требуют внимания.
    for event in critical_events:
        print(f'{event["message"]} (critical)')

    print(f"критичных {len(critical_events)}")


if __name__ == "__main__":
    main()