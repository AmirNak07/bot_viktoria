from bs4 import Tag


def safe_find(tag: Tag | None, *args, **kwargs) -> Tag:  # type: ignore
    if tag is None:
        raise ValueError("Tag is None")
    return tag.find(*args, **kwargs)  # type: ignore


def safe_find_all(tag: Tag | None, *args, **kwargs) -> list[Tag]:  # type: ignore
    if tag is None:
        return []
    return tag.find_all(*args, **kwargs)  # type: ignore
