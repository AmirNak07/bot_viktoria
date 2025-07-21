from scheduler.parsers.vk_parser.config import LINKS, VACANCY_URL_TEMPLATE
from scheduler.parsers.vk_parser.scraper.downloader import fetch_multiple_pages
from scheduler.parsers.vk_parser.scraper.parser import (
    extract_json_data,
    extract_vacancy_ids,
    transform_vacancy_data,
)


async def collect() -> list[dict[str, str]]:
    # Getting a page with job listings
    list_pages = await fetch_multiple_pages(LINKS)

    # Extracting the job IDs
    vacancy_ids = []
    for html in list_pages:
        page_data = extract_json_data(html, "vacancies")
        vacancy_ids.extend(extract_vacancy_ids(page_data))  # type: ignore

    # Creating URLs for detailed pages
    detail_urls = [VACANCY_URL_TEMPLATE.format(vacancy_id=id) for id in vacancy_ids]

    # Loading the detailed pages
    detail_pages = await fetch_multiple_pages(detail_urls)

    # Processing the data
    vacancies_data = [extract_json_data(page, "vacancy") for page in detail_pages]
    vacancies = transform_vacancy_data(vacancies_data)

    return vacancies
