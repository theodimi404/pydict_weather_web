import requests, bs4


def main(city):
    url = f'http://www.skaikairos.gr/main/{city}/position'

    res = requests.get(url)
    if res.status_code == 404:
        response = 'Your city of choise doesn\'t exist or you mispelled it.'
    else:
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        kairos = soup.find("div", {"id": "forecast-upper-seven"})
        data = list(kairos.stripped_strings)

        if data:
            response = {
                "one": "Η πρόγνωση του καιρού για {city} είναι:",
                "two": f"""{data[2]} \n
                {data[3]}{data[4]}
                {data[5]} {data[6]} Μποφόρ"""
            }
            """
            response = f\
                Η πρόγνωση του καιρού για {city} είναι:
                {data[2]}
                {data[3]}{data[4]}
                {data[5]} {data[6]} Μποφόρ
                ------
                {data[7]}
                {data[8]}
                {data[9]}{data[10]}
                {data[11]} {data[12]} Μποφόρ
                ------
                {data[13]}
                {data[14]}
                {data[15]}{data[16]}
                {data[17]} {data[18]} Μποφόρ
                ------
                {data[19]}
                {data[20]}
                {data[21]}{data[22]}
                {data[23]} {data[24]} Μποφόρ
                (Data from skaikairos.gr)
            """
        else:
            response = f'There are no weather data for {city}'

    return response
