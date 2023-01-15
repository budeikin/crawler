from bs4 import BeautifulSoup


class Advertisement:
    def __init__(self):
        self.soup = None

    @property
    def title(self):
        title_tag = self.soup.find('h1', attrs={'id': 'pdp_product_title'})
        if title_tag:
            return title_tag.text
        return None

    @property
    def price(self):
        price = self.soup.find('div', attrs={'class': 'product-price'})
        if price:
            return price.text
        return None

    @property
    def shown(self):
        shown = self.soup.find('li', attrs={'class': 'description-preview__color-description'})
        if shown:
            return shown.text.replace('Shown: ', '')
        return None

    @property
    def style_color(self):
        style = self.soup.find('li', attrs={'class': 'description-preview__style-color'})
        if style:
            return style.text.replace('Style: ', '')
        return None

    def parse(self, html_file):
        self.soup = BeautifulSoup(html_file, 'html.parser')
        data = dict(title=self.title, price=self.price, shown=self.shown, style=self.style_color)

        return data
