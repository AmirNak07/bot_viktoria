from typing import Any

from bs4 import BeautifulSoup
from bs4.element import AttributeValueList

from scheduler.parsers.rosmol_parser.scraper.utils.bs4_utils import (
    safe_find,
    safe_find_all,
)


def get_forum_links(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    forums_div = safe_find(
        soup,
        "div",
        {
            "class": [
                "catalog-section-items",
                "intec-grid",
                "intec-grid-wrap",
                "intec-grid-a-v-stretch",
                "intec-grid-a-h-start",
            ],
            "data-role": "items",
            "data-entity": "i-10-bitrix-catalog-section-catalog-tile-3rm-OQ3k9PHlVICg-1",
        },
    )
    forums = safe_find_all(forums_div, "div", {"class": "catalog-section-item-wrapper"})
    forums_links: list[str | AttributeValueList] = [
        safe_find(forum, "a", {"class": "btn-link"})["href"] for forum in forums
    ]
    return forums_links  # type: ignore[return-value]


def get_participants(soup: BeautifulSoup) -> str:
    try:
        titles: list[str] = [
            x.text.strip()
            for x in soup.find_all("div", {"class": "properties-preview-item-name"})
        ]
        index = titles.index("Категории участников:")
        results: str = (
            soup.find_all("div", {"class": "properties-preview-item-value"})[index]
            .text.strip()
            .replace("\xa0", "")
        )
    except ValueError:
        results = "-"
    return results


def parse_html(forums_html: list[str]) -> list[dict[str, Any]]:
    result = []
    for html in forums_html:
        soup = BeautifulSoup(html, "html.parser")
        tmp = {}
        tmp["creator"] = "rosmol"
        tmp["title"] = (
            safe_find(soup, "h1", {"class": "forum-name"})
            .text.replace("\n", " ")
            .strip()
        )
        tmp["place"] = (
            safe_find(soup, "div", {"class": "forum-region"})
            .text.replace("\n", " ")
            .strip()
        )
        tmp["date"] = (
            safe_find(soup, "div", {"class": "period-event"})
            .text.replace("\n", " ")
            .strip()
        )
        tmp["category_of_participants"] = (
            get_participants(soup).replace("\n", " ").replace("\r", " ")
        )
        tmp["link"] = safe_find(soup, "meta", {"name": "og:url"}).attrs["content"]  # type: ignore[assignment]
        result.append(tmp)
    return result
