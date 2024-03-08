from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

app = Flask(__name__)

def convert_excel_to_json(excel_url):
    response = requests.get(excel_url)
    filename = "spisak.xlsx"
    with open(filename, "wb") as f:
        f.write(response.content)
    data_frame = pd.read_excel(filename, engine='openpyxl')
    json_data = data_frame.to_dict(orient="records")
    for record in json_data:
        if "Генеричко име лека                                             (INN)" in record:
            record["product_name"] = record.pop("Генеричко име лека                                             (INN)")
    
    return json_data

@app.route('/api/crawler', methods=['POST'])
def excel_to_json():
    baseurl = "https://www.zdravlje.gov.rs"
    url = "https://www.zdravlje.gov.rs/tekst/335366/najvise-cene-lekova.php"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    hrefs = soup.find_all("a", href=True, title=True)

    excel_hrefs = []

    for href in hrefs:
        title_attribute = href["title"]
        if title_attribute.lower() == "excel":
            if href["href"].startswith("http"):
                excel_hrefs.append(href["href"])
            else:
                excel_hrefs.append(baseurl + href["href"])

    first_excel_href = excel_hrefs[0]
    json_data = convert_excel_to_json(first_excel_href)

    with open('pricing_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    return jsonify(json_data)

@app.route('/api/pricing_data', methods=['GET'])

def get_pricing_data():
    product_name = request.args.get('product_name')

    with open('pricing_data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if product_name:
        filtered_data = [item for item in data if item.get('product_name') == product_name]
        return jsonify(filtered_data)
    else:
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
