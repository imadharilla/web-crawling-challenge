
from booking_scrappers.Hotel import Hotel
from booking_scrappers.helpers import load_json
import sys, os

# Preparing Test Data 
HTML = None
with open(".//Task//task 1 - Kempinski Hotel Bristol Berlin, Germany - Booking.com.html", "r", encoding="utf8") as f :
    HTML = f.read()
# loading the expected results 
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data/hotel.json')
RESULTS = load_json(filename)


def test_hotel_name():
    hotel = Hotel(HTML)
    assert hotel.get_name() == RESULTS["name"]
    
def test_hotel_address():
    hotel = Hotel(HTML)
    assert hotel.get_address() == RESULTS["address"]
    
def test_hotel_description():
    hotel = Hotel(HTML)
    assert hotel.get_description() == RESULTS["description"]
    
def test_room_categories():
    hotel = Hotel(HTML)
    assert hotel.get_room_categories() == RESULTS["room_categories"]
    
def test_alternative_hotels():
    hotel = Hotel(HTML)
    assert hotel.get_alternative_hotels() == RESULTS["alternative_hotels"]
    
    
def test_hotel_stars():
    hotel = Hotel(HTML)
    assert hotel.get_stars() == RESULTS["stars"]
    
    
def test_hotel_review_points():
    hotel = Hotel(HTML)
    assert hotel.get_review_points() == RESULTS["review_points"]
    