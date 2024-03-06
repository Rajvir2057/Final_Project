import csv

def zodiac_info():
    fields = ['zodiac_sign', 'lucky_color']

    rows = [
        {'zodiac_sign': 'Sagittarius', 'lucky_color': 'Purple, dark blue'},
        {'zodiac_sign': 'Capricorn', 'lucky_color': 'Brown, black'},
        {'zodiac_sign': 'Aquarius', 'lucky_color': 'Blue, turquoise'},
        {'zodiac_sign': 'Pisces', 'lucky_color': 'Mauve, sea green'},
        {'zodiac_sign': 'Aries', 'lucky_color': 'Red, orange'},
        {'zodiac_sign': 'Taurus', 'lucky_color': 'Green, pink'},
        {'zodiac_sign': 'Gemini', 'lucky_color': 'Yellow, light green'},
        {'zodiac_sign': 'Cancer', 'lucky_color': 'White, silver'},
        {'zodiac_sign': 'Leo', 'lucky_color': 'Gold, orange'},
        {'zodiac_sign': 'Virgo', 'lucky_color': 'Navy blue, gray'},
        {'zodiac_sign': 'Libra', 'lucky_color': 'Blue, pink'},
        {'zodiac_sign': 'Scorpio', 'lucky_color': 'Red, black'}
    ]

    file = 'zodiac_color_record.csv'

    with open(file, 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fields)

        csvwriter.writeheader()

        csvwriter.writerows(rows)
zodiac_info()

