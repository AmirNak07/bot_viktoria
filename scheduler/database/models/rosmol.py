from beanie import Document


class RosmolEventModel(Document):
    creator: str
    title: str
    place: str
    date: str
    category_of_participants: str
    link: str

    class Settings:
        name = "events"
