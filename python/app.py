from urllib.request import urlopen, Request
import re
import threading
import json

empty_array = []

def write_to_file(data):
    empty_array.append(data)



# Function to scrape data from a given URL
def scrape_data(page):
    url = f'https://www.auto24.ee/kasutatud/nimekiri.php?bn=2&a=100&l1=1&l2=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999&ae=8&af=50&ssid=131599877&ak={page}'
    print(page)
    headers = {
        'Cookie': 'PHPSESSID=cc5cc7aa6425315cc3a22bf245f6bfe6; CID=1710153745094726; my_searches_notif=0; OptanonAlertBoxClosed=2024-03-11T10:42:27.253Z; eupubconsent-v2=CP7TcXAP7TcXAAcABBENArEsAP_gAAAAAChQg1QpYAAgAEAAQAA0ACAAQgAqADIAHIAPABDACQAJYATgBQACqAFgAWgAvgBiAGUANAA1gByAHwAQoAiACMAEkAJgATgAoABVgC0AL8AYQBigDIAMoAaIA2ADaAG-AOQA5wB3AHiAPwBCwCIAIuARwBHgCTgEqAS0AmQCbAE6AKEAUgAqIBWgFcALKAXABcgC-gGAAYIAwwBjgDLAGdANIA1YBrgGyAOCAcQByADrgHiAecA-AD5gH2AfsA_wEAgIMAg8BEAERgIsAjUBHAEdAJFASUBJoCWgJcATAAnABOoCegJ-AUWApACkgFNAKgAVmArwCvgFmALgAXMAuwBeQC-gGBAMUAZIAzUBnAGdANAAaKA0wDUAG0ANsAbgA4QB2wDvgHmgPUA9YB7wD5QH1AfYA_cB_wIAgQIBAoCCQEGQISAhOBC4EMAIbARFAiUCJoEUgRUAiwBF4CMQEagI4AR2Aj0BIgCSwEqAJWgSyBLQCXgExQJkAmWBNIE1AJsgTiBOQCdIE7ATuAn-BQwFEwKMAo2BSAFIgKTgUsBS4CogFSQKpAqoBVkCrgKvAVkAruBXwFfwLDAsWBZAFkgLMAWeAtEBasC1wLYgW6Bb0C4QLigXIBc0C6ALqgXYBd8C8gLzgXsBe4C-oF-gX9AwADAwJvQTgBOEINQAAAEAkCsABAACwAKgAcAA8ACAAF8AMgA1AB4AEQAJgAVQA3gB-AEJAIgAiQBHACWAE0AMAAYYAywBsgD4gH2AfsA_wEAgIuAjABGoCRAJKAT8AqABcwDFAG0ANxAj0CRAE7AKHAUiAtgBcgC7wF5hAB4ADgAMgAkADaAQcAjgBfQElgJWATKApABS4CxAF5BBqDABwAVAAvgDuAPABAACMAJLAXIIAFAAqABeAHcAgABGADUAI7ASWAt0BcgoAEACoAPAwACACocAcAARAA4ADwALgAZABIAD8AKAAaAA2gCOAHIAQAAg4BEQCOAFQAOkAksBKwCYgEygKTAVUAsQBdADAgGCBBqHQLwAFgAVAA4ACAAF8AMQA1AB4AEQAJgAVYAuAC6AGIAN4AfoBEAESAJYATQAwABhgDZgH2AfoA_4CLAIxAR0BJQCfgFzALyAYoA2gBuAD7AIvgR6BIgCZAE7AKHAUgAsUBbAC3QFyALtAXeAvMBfQE3gJwkABgACAAHgAZADQAOQAjgBfQFJgLEAXkAwIBghCAkAAsAGIANQAmABVAC4AGIAN4AjgBgAD_ALmAYoA2gCPQFigLRAXISgMAAIAAWABwAGIAPAAiABMACqAFwAMUAiACJAEcAMAAbIA_AC5gGKARMAi-BHoEiALFAWwAvMCcJIAaABcADIANQA8AEAAIOARwAqAB2wErAJiAUmAwIoAWAAUABcADIAJAA2gB4AEcAOQAfYBAACDgGvAO2Af8BJYCYgFSALoAXkAwIBggE4SkCUABYAFQAOAAggBiAGoAPAAiABMACqAGIAP0AiACJAGAANmAfgB-gEWAIxAR0BJQC5gF5AMUAbQA3AB9gETAIvgR6BIgCdgFDgKQAWKAtgBcgC7QF5gL6Am8WgCAA1AEcAMAA-xYAIAMsAjgCPQExA.f_wAAAAAAAAA; _ga=GA1.1.1462978314.1710153751; __gfp_64b=ayAnHSJ31bJ8Wj6PSjAAGg409B1DC7Rw.87Q08LC2Nn.j7|1710153751; __cf_bm=RH..vadvgHY24vimPXvLL5MCF8MDd4AOrN3kga4RbLk-1710155270-1.0.1.1-o1rY__rQib8EF_nOf5mQRVvN49kgRx6JI2B0T.v9N6IoTtbn8SSfqlePC.0LCLKR9_BiwXF.h0MPSDTiB2a2og; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Mar+11+2024+13%3A07%3A51+GMT%2B0200+(Eastern+European+Standard+Time)&version=202310.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=4d2c0fec-13d1-434b-ba5f-7412c518c40f&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0004%3A1%2CC0002%3A1%2CV2STACK42%3A1&geolocation=%3B&AwaitingReconsent=false; _ga_FP634TYM36=GS1.1.1710153751.1.1.1710155271.0.0.0',
        'Referer': 'https://www.auto24.ee/kasutatud/nimekiri.php?',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }

    request = Request(url, headers=headers)

    with urlopen(request) as response:
        baidid = response.read()
        tekst = baidid.decode()

        img = re.findall(r'<span\s+class="thumb"\s+style="background-image:\s+url\(\'(.*)\'\)\">', tekst)
        description = re.findall(r'<div class="extra">\s*<span class="year">(\d+)</span>\s*<span class="mileage">([^<]*)</span>\s*<span class="fuel sm-none">([^<]+)</span>\s*<span class="fuel_short_icon sm-show"><img[^>]+>([^<]+)</span>\s*<span class="transmission sm-none">([^<]+)</span>\s*<span class="transmission_short_icon sm-show"><img[^>]+>([^<]+)</span>\s*<span class="bodytype">([^<]+)</span>\s*<span class="drive">([^<]+)</span>\s*</div>', tekst)
        title = re.findall(r'<a href="/soidukid/(.*)" class="main">\s*<span>([^<]*)</span>\s*<span class="model">([^<]*)</span>\s*<span class="model-short" style="display: none">([^<]*)</span>\s*<span class="engine">([^<]*)</span>\s*</a>', tekst)
        
        for i1, i2, i3 in zip(title, description, img):
            i1 = list(i1)
            i2 = list(i2)
            i1 = i1[1:]
            i1.pop(2)
            i1 = ' '.join(i1)

            replace1 = i2[1].replace('&nbsp;', '')
            i2[1] = replace1
            i2.pop(3)
            i2.pop(4)
            
            obj = {
                'title': i1,
                'description': i2,
                'image': i3
            }
            write_to_file(obj)
            
            # You can process the scraped data here
            print(obj)

# Main function to start multithreading
def main():
    amount = 0
    page = 0
    num_threads = 50  # Number of threads to run concurrently

    # Create and start threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=scrape_data, args=(page,))
        threads.append(thread)
        thread.start()
        page += 50
        amount += 1

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    with open("scraped_data.txt", "a") as file:
        file.write(str(empty_array))  # Write the updated array to the file

if __name__ == "__main__":
    main()
