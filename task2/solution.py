from bs4 import BeautifulSoup
import requests
import csv


def collect_animal_counts(url):

    animal_dict = {chr(i): 0 for i in range(ord("А"), ord("Я") + 1)}

    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Ошибка загрузки страницы {url}: {e}")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        category_div = soup.find("div", class_="mw-category mw-category-columns")
        if not category_div:
            print("Не удалось найти блок с животными.")
            break

        animal_items = category_div.find_all("li")
        for animal in animal_items:
            first_letter = animal.text[0].upper()
            if first_letter in animal_dict:
                animal_dict[first_letter] += 1

        url = None

        # next_page_link = soup.find("a", text="Следующая страница")
        next_page_link = soup.find("a", string="Следующая страница")
        if next_page_link:
            url = next_page_link.get("href")
        if url:
            url = f"https://ru.wikipedia.org{url}"

    return animal_dict


def save_csv(data, filename):

    try:
        with open(filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            for letter, count in sorted(data.items()):
                if count >= 0:
                    writer.writerow([letter, count])
        print(f"Данные успешно сохранены в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


if __name__ == "__main__":
    url = "https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from=А"
    animal_counts = collect_animal_counts(url)

    output_file = "animal_counts.csv"
    save_csv(animal_counts, output_file)
