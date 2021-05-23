#!/usr/bin python

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# test

@app.route("/")
def index():
    message = "Query /getlocation to get your location!"
    return render_template('index.html', message=message)

@app.route('/getlocation')
def return_location():
    URL = 'https://www.geodatatool.com/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    string_list = []

    for div in soup.findAll('div', {'class': 'data-item'}):
        # print(div.prettify())

        for string in soup.strings:
            # print(string)
            if string != '\n':
                string_list.append(string)

    string_dict = {}

    string_dict["longitude"] = string_list[string_list.index('Longitude:') + 1]
    string_dict["latitude"] = string_list[string_list.index('Latitude:') + 1]
    string_dict["IP address"] = string_list[string_list.index('IP Address:') + 1]
    string_dict["City"] = string_list[string_list.index('City:') + 1]
    string_dict["Region"] = string_list[string_list.index('Region:') + 1]
    string_dict["Zip"] = string_list[string_list.index('Postal Code:') + 1]
    string_dict["Country"] = string_list[string_list.index('Country Code:') + 1]

    # print("The longitude is " + string_list[string_list.index('Longitude:') + 1])
    # print("The latitude is " + string_list[string_list.index('Latitude:') + 1])
    # print("The IP address is " + string_list[string_list.index('IP Address:') + 1])
    # print("The City is " + string_list[string_list.index('City:') + 1])
    # print("The Region is " + string_list[string_list.index('Region:') + 1])
    # print("The Zip is " + string_list[string_list.index('Postal Code:') + 1])
    # print("The Country is " + string_list[string_list.index('Country Code:') + 1])

    return jsonify(string_dict)
    # Some internal stuff with processed text


if __name__ == '__main__':
    app.run()