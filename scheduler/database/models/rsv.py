from beanie import Document


class RSVEventModel(Document):
    creator: str
    title: str
    institute_name: str
    regions: str | list[str]
    industry_name: str
    skills: str | list[str]
    duration: str
    work_format: str
    payment: str
    link: str

    class Settings:
        name = "events"
