from bs4 import BeautifulSoup

class Hotel: 
    def __init__(self, HTML) -> None:
        self.soup = BeautifulSoup(HTML, 'html.parser')

    def get_data(self):
        return {
            "name": self.get_name(),
            "address": self.get_address(),
            "description": self.get_description(),
            "stars": self.get_stars(),
            "review_points": self.get_review_points(),
            "room_categories": self.get_room_categories(),
            "alternative_hotels": self.get_alternative_hotels(),
        }

    def get_name(self):
        return self.soup.find("span", { "id": "hp_hotel_name" }).get_text("", True)
    
    def get_description(self):
        summary_paragraphs = self.soup.find("div", {"id": "summary"}).find_all("p")
        summary = "\n".join([p.text for p in summary_paragraphs])
        hotel_meta_infos = self.soup.find("p", {"class": "summary"}).get_text("\\")

        # remove all line breaks 
        hotel_meta_infos = "".join(hotel_meta_infos.split('\n'))
        # replace the separator '\\' with one line break
        hotel_meta_infos = "\n".join(hotel_meta_infos.split("\\"))

        return summary + "\n" + hotel_meta_infos  

    def get_address(self):
        return self.soup.find("span", { "id": "hp_address_subtitle" }).get_text("", True)

    def get_stars(self):
        stars_element = self.soup.find("i", { "class": "stars" })
        classes = stars_element.attrs['class']
        for i in range(1, 6):
            if 'ratings_stars_' + str(i) in classes:
                return i
        return 0

    def get_review_points(self , element=None):
        if element == None:
            element = self.soup
        review = {}
        rating_elements = element.find("span", { "class": "rating"})
        review["average"] = rating_elements.find("span", { "class": "average"}).text
        review['out_of'] = rating_elements.find("span", { "class": "out_of"}).text[1:]
        review["number_of_reviews"] = element.find("span", {"class": "score_from_number_of_reviews"}).find("strong").text
        return review
    
    def get_room_categories(self):
        room_element = self.soup.find("table", { "id": "maxotel_rooms" }).find("tbody")
        categories_elements = room_element.find_all("tr")
        return [  el.find_all("td")[1].get_text("", True) for el in categories_elements ]
    
    def get_alternative_hotels(self):
        hotels_table = self.soup.find("table", {"id": "althotelsTable"}).find("tbody")
        hotels_elements = hotels_table.find("tr", {"id": "althotelsRow"}).find_all("td")

        alternative_hotels= []
        for hotel_el in hotels_elements :
            hotel = {}
            hotel["name"] = hotel_el.find("p", {"class": "althotels-name" }).get_text("", True)
            hotel["description"]  = hotel_el.find("span", {"class": "hp_compset_description" }).get_text("", True)
            hotel["url"]  = hotel_el.find("a", {"class": "althotel_link" }).attrs["href"]
            
            hotel["review_points"]  = self.get_review_points(hotel_el)

            alternative_hotels.append(hotel)
        return alternative_hotels
