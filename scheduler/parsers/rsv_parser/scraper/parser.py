from typing import Any


def parse_internships(
    internships: list[dict[str, Any]], regions: dict[int, str]
) -> list[dict[str, Any]]:
    result = []
    for i in internships:
        tmp = {}
        tmp["title"] = i["name"]
        tmp["institute_name"] = i["instituteName"]
        tmp["regions"] = (
            regions[i["region_ids"][0]]
            if len(i["region_ids"]) == 1
            else [regions[x] for x in i["region_ids"]]
        )
        tmp["industry_name"] = i["industryName"]
        tmp["skills"] = i["skills"][0] if len(i["skills"]) == 1 else i["skills"]
        tmp["duration"] = i["duration"]
        tmp["work_format"] = i["participationFormatName"]
        tmp["payment"] = i.get("paymentAmount", "-")
        tmp["link"] = f"https://rsv.ru/internships/0/{i['id']}"
        result.append(tmp)
    return result
