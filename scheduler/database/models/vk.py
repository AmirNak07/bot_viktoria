from beanie import Document


class VKEventModel(Document):
    creator: str
    title: str
    team: str
    city: str
    format_of_work: str
    employment: str
    tasks: list[str]
    need_to_have: list[str]
    link: str
    type_of_work: str
    direction: str

    class Settings:
        name = "events"
