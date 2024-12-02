#Funkcija, skirta istraukti is interneto duomenis:pavadinimus ir kainas.

from requests import get
from lxml.html import fromstring



def gintarine_vaistine(timeoutvaistine = 10):
    response = get("https://www.gintarine.lt/maistas-ir-papildai-sportininkams",timeout=timeoutvaistine)
    html_content = response.text

    tree = fromstring(html_content)

# Fetch all product items
    products = tree.xpath("//div[contains(@class, 'product-item')]")
    pavadinimu_sarasas=[]
    kainu_sarasas=[]

    for product in products:
        product_name = product.xpath(".//input[@name='productName']/@value")[0]
        product_price = product.xpath(".//input[@name='productPrice']/@value")[0]

        pavadinimu_sarasas.append(product_name)
        kainu_sarasas.append(product_price)
        print(f"Product Name: {product_name}")
        print(f"Product Price: {product_price}")

    return pavadinimu_sarasas, kainu_sarasas

    print(len(products))

#Funkcija, skirta gauti duomenis txt formatu
def irasyti_i_faila(pavadinimu_sarasas,kainu_sarasas):
    with open ("failas.txt", 'w') as failas:
        failas.write(str(pavadinimu_sarasas))
        failas.write("\n") #Nauja eilute
        failas.write(str(kainu_sarasas))

    with open("failas.txt", 'r') as failas:
     print(failas.read())
