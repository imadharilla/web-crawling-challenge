# Web Scraper Assignment

## Project setup 
Please install the required dependencies. (Using a virtual environment is recommended)

<sub>Note: the only package used is `beautifulsoup4`. the rest are related to the testing framework `pytest`</sub>

```
pip install -r requirements.txt
```
## Running the code 
You can run the code using : 
```
python main.py
```
the json result is stored under `output` folder 

## Running Tests
you can run all tests by running the following command :
```
pytest
```

## Project description
This is a very simple project that has a class Hotel that is responsible for extracting the hotel data from a given html. 
I used `Beautifulsoup4` since it's a very simple but powerful tool to access and read data from the DOM. I also had a look at the website booking.com , it may require using something a bit more advanced like Selenium to crawl the whole website, since it requires many browser interactions like for example filling forms.
