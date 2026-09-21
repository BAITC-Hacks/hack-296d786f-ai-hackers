from pathlib import Path


def classify(message):
    text = message.lower()

    if "очередь" in text or "холодная" in text:
        return (
            "жалоба",
            "Сожалеем о неудобствах в столовой. "
            "Уточните, пожалуйста, дату и время посещения."
        )

    if "wi-fi" in text or "wi‑fi" in text:
        return (
            "жалоба",
            "Уточните, пожалуйста, этаж и аудиторию в корпусе B, "
            "где не работает Wi-Fi."
        )

    if "справк" in text:
        return (
            "справка",
            "Для уточнения порядка получения справки о месте учёбы "
            "обратитесь в учебную часть."
        )

    if "парковк" in text:
        return (
            "справка",
            "Уточните, пожалуйста, адрес корпуса, чтобы можно было "
            "подсказать расположение гостевой парковки."
        )

    if "консультац" in text:
        return (
            "другое",
            "Уточните, пожалуйста, к какому специалисту вы хотите "
            "записаться и какое время завтра вам удобно."
        )

    return (
        "другое",
        "Уточните, пожалуйста, детали вашего обращения."
    )


def main():
    path = Path(__file__).with_name("messages.txt")
    lines = path.read_text(encoding="utf-8").splitlines()
    messages = [line.strip() for line in lines if line.strip()]

    for number, message in enumerate(messages, start=1):
        category, reply = classify(message)

        print(f"{number}. {message}")
        print(f"Категория: {category}")
        print(f"Черновик ответа: {reply}")
        print()


if __name__ == "__main__":
    main()
