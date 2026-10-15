import requests
from bs4 import BeautifulSoup
import openpyxl
def oppp():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Author","Quotes"])
    for page in range(1,10):
        url = f"https://quotes.toscrape.com/page/{page}/"
        q = requests.get(url)
        soup = BeautifulSoup(q.text, "html.parser")
        qu = soup.find_all("span", class_="text")
        au = soup.find_all("small", class_="author")
        for authors,quotes in zip(au,qu):
            ws.append([authors.text,quotes.text])
        print(f"Page {page} Done")
    return wb,au
def tifo(au,wb):
    ws2 = wb.create_sheet("Author Stats")
    ws2.append(["Author","Count"])
    acount = {}
    for acc in au:
        name = acc.text
        if name in acount:
            acount[name] += 1
        else:
            acount[name] = 1
    for author, count in acount.items():
        ws2.append([author, count])
    wb.save("Quotes.xlsx")
    print("All done")
    return wb
wb, au = oppp()
tifo(au, wb)