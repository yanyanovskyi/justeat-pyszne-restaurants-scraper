import requests
import pandas as pd

headers = {
    'accept': 'application/json;v=3',
    'accept-language': 'en-PL',
    'origin': 'https://www.pyszne.pl',
    'priority': 'u=1, i',
    'referer': 'https://www.pyszne.pl/',
    'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
    'x-je-auser': '86576186-af1f-40aa-ab71-4574c1cdfd01',
    'x-jet-analytical-session-id': '58f9ad06-6526-4c81-99ca-c85a58e23095',
    'x-jet-application': 'OneWeb',
    'x-jet-braze-device-id': '5d0e6a86-4239-423d-b75f-2c9a8a9018ba',
    'x-jet-essential-session-id': '58f9ad06-6526-4c81-99ca-c85a58e23095',
    'x-jet-functional-session-id': '58f9ad06-6526-4c81-99ca-c85a58e23095',
    'x-jet-personalised-session-id': '58f9ad06-6526-4c81-99ca-c85a58e23095',
}

params = {
    'latitude': '53.123482',
    'longitude': '18.008438',
    'serviceType': 'delivery',
    'ratingsOutOfFive': 'true',
    'je-tgl-ops_include_closed': 'true',
    'je-tgl-tmp_banners': 'false',
}

response = requests.get(
    'https://rest.api.eu-central-1.production.jet-external.com/discovery/pl/restaurants/enriched',
    params=params,
    headers=headers,
)

data = response.json()

restaurants = []
for rest in data.get("restaurants", []):
    restaurants.append({
        "name": rest.get("name"),
        "rank": rest.get("rating", {}).get("starRating", "нет рейтинга"),
    })

df = pd.DataFrame(restaurants)
df.to_excel("City pyszne.xlsx", index=False)
print("✅ Successfully saved.xlsx")




