from typing import Any

FIELD_LABELS = {
    "creator": "платформа",
    "title": "название",
    "place": "место",
    "date": "дата",
    "category_of_participants": "категории участников",
    "link": "ссылка",
    "institute_name": "компания",
    "regions": "город",
    "industry_name": "направление",
    "skills": "необходимые навыки",
    "duration": "продолжительность",
    "work_format": "формат работы",
    "payment": "заработная плата",
    "team": "команда",
    "city": "город",
    "format_of_work": "формат работы",
    "employment": "занятость",
    "tasks": "предстоящие задачи",
    "need_to_have": "необходимо иметь",
    "type_of_work": "раздел",
    "direction": "направление",
}


def format_event(doc: dict[str, Any]) -> dict[str, Any]:
    correct_doc = {}
    for key, label in FIELD_LABELS.items():
        if key in doc:
            correct_doc[label.capitalize()] = doc[key]
    return correct_doc
