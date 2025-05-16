from bs4 import BeautifulSoup


def test_collect_animal_counts_from_html():
    html_pages = [
        """
        <div class="mw-category mw-category-columns">
            <ul>
                <li>Аист</li>
                <li>Белка</li>
                <li>Гусь</li>
            </ul>
        </div>
        """,
        """
        <div class="mw-category mw-category-columns">
            <ul>
                <li>Бобр</li>
                <li>Дельфин</li>
                <li>Енот</li>
            </ul>
        </div>
        """
    ]

    def collect_animal_counts_from_html(html_pages):
        animal_dict = {chr(i): 0 for i in range(ord("А"), ord("Я") + 1)}
        for html in html_pages:
            soup = BeautifulSoup(html, "html.parser")
            category_div = soup.find("div", class_="mw-category mw-category-columns")
            if not category_div:
                continue

            animal_items = category_div.find_all("li")
            for animal in animal_items:
                first_letter = animal.text[0].upper()
                if first_letter in animal_dict:
                    animal_dict[first_letter] += 1
        return animal_dict

    expected_result = {
        'А': 1,
        'Б': 2,
        'В': 0,
        'Г': 1,
        'Д': 1,
        'Е': 1,
        **{chr(i): 0 for i in range(ord("Ж"), ord("Я") + 1)},
    }

    result = collect_animal_counts_from_html(html_pages)

    assert result == expected_result, 'Ожидаемый результат не получен'
