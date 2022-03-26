from booking_scrappers.Hotel import Hotel
from booking_scrappers.helpers import save_to_json

HTML = None
with open(".//Task//task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html", "r", encoding="utf8") as f :
    HTML = f.read()


hotel = Hotel(HTML)

save_to_json(hotel.get_data(), "./output/hotel.json")