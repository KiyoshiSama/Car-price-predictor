from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time

import re
import csv


def save_to_csv(data, filename='./cars_data.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # writer.writerow(['Company', 'Name', 'Model', 'Year', 'Price', 'Mileage', 'Location'])
        writer.writerow(['Location', 'Mileage', 'Price', 'Year', 'Model', 'Name', 'Company'])
        writer.writerows(data)





def main():

    url = 'https://bama.ir/car?price=1/'

    options = ChromeOptions()
    service = ChromeService(executable_path='/usr/bin/chromedriver')

    options.add_argument("--headless")

    browser = webdriver.Chrome(service=service, options=options)

    browser.get(url)

    browser.execute_script("window.scrollBy(0,1000)")

    time.sleep(5)

    cars = browser.find_elements(By.CLASS_NAME, 'bama-ad.listing')
    car_data = []

    for car in cars:
        car_company, car_name = car.find_element(By.CLASS_NAME, "text").text.split("،")
        details = car.find_element(By.CLASS_NAME, "bama-ad__detail-row").text.split("\n")
        car_year =details[0].strip()
        car_mileage=details[1].strip() if 'km' in details[1] else '0 km'
        car_model = details[2].strip() 

        car_price = car.find_element(By.CLASS_NAME, "bama-ad__price").text.strip()
        car_location = car.find_element(By.CLASS_NAME, "bama-ad__address").text.strip()

        car_year = int(car_year)
        car_mileage = int(re.sub(r'\D', '', car_mileage))
        car_price = int(re.sub(r'\D', '', car_price))

        car_data.append([car_company.strip(), car_name.strip(), car_model.strip(), car_year, car_price, car_mileage, car_location.strip()])

    save_to_csv(car_data)
    browser.quit()

if __name__ == "__main__":
    main()