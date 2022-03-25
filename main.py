
HTML = None
with open(".//Task//task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html", "r", encoding="utf8") as f :
    HTML = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(HTML, 'html.parser')

# Hotel Name 
hotel_name = soup.find("span", { "id": "hp_hotel_name" }).text

# Hotel address
hotel_address = soup.find("span", { "id": "hp_address_subtitle" }).text

# Hotel stars 
stars_element = soup.find("i", { "class": "stars" })
classes = stars_element.attrs['class']
stars = 0
for i in range(1, 6):
    if 'ratings_stars_' + str(i) in classes:
        stars = i
        break

# Hotel review point and number of reviews
rating_elements = soup.find("span", { "class": "rating"})
average = rating_elements.find("span", { "class": "average"}).text
out_of = rating_elements.find("span", { "class": "out_of"}).text[1:]

number_of_reviews = soup.find("span", {"class": "score_from_number_of_reviews"}).find("strong").text

# DESCRIPTION
summary_paragraphs = soup.find("div", {"id": "summary"}).find_all("p")
summary = "\n".join([p.text for p in summary_paragraphs])
hotel_meta_infos = soup.find("p", {"class": "summary"}).get_text("\\")

# remove all line breaks 
hotel_meta_infos = "".join(hotel_meta_infos.split('\n'))
# replace the separator '\\' with one line break
hotel_meta_infos = "\n".join(hotel_meta_infos.split("\\"))

description = summary + "\n" + hotel_meta_infos


# Room Categories 
room_element = soup.find("table", { "id": "maxotel_rooms" }).find("tbody")
categories_elements = room_element.find_all("tr")

categories = [  el.find_all("td")[1].get_text("", True) for el in categories_elements ]

print(categories)