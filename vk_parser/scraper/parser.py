import json
from typing import Any

from config import VACANCY_URL_TEMPLATE


def extract_json_data(html: str, key: str) -> dict[str, Any]:
    """Extracts JSON data from a script on a page"""
    full_json = json.loads(
        html[html.find('<script id="__NEXT_DATA__"') :]
        .replace('<script id="__NEXT_DATA__" type="application/json">', "")
        .replace("</script></body></html>", "")
    )
    result: dict[str, Any] = full_json["props"]["pageProps"]["page"][key]

    return result


def extract_vacancy_ids(vacancy_json: list[dict[str, Any]]) -> list[str]:
    """Retrieves the ID of open vacancies"""
    return [vacancy["id"] for vacancy in vacancy_json if vacancy["is_opened"]]


def transform_vacancy_data(data: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Converts raw job data into a structured format"""
    result_json = []
    for id in data:
        tmp = {}
        tmp["title"] = id["title"]
        tmp["team"] = id["business_unit"]["name"]
        tmp["city"] = id["city"]
        tmp["format_of_work"] = id["format"]
        tmp["employment"] = id["employment"]
        tmp["tasks"] = "\n".join(id["landing"]["aboutTasksText"]["items"])
        tmp["need_to_have"] = "\n".join(id["landing"]["aboutSkillsText"]["items"])
        tmp["link"] = VACANCY_URL_TEMPLATE.format(vacancy_id=id["id"])
        tmp["type_of_work"] = (
            "Стажировка" if id["internship_type"] == "internship" else "Вакансия"
        )
        tmp["direction"] = id["direction"]
        result_json.append(tmp)
    return result_json
