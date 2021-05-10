import requests
import lxml.html as lh
from re import findall
from django.core.management.base import BaseCommand
from core.models import CurrencyRateParseData

class Command(BaseCommand):

    def handle(self, *args, **options):
#        response = requests.get('https://kurs.com.ua/visa/uah#main_table_cards')
#        if response.status_code == 200:
#            tree = lh.fromstring(response.content)
#            for index in range(1, 155):
#                obj = CurrencyRateParseData.objects.create()
#                name_elem = tree.xpath(f'//*[@id="main_table_cards"]/table/tbody/tr[{index}]/td[contains(@class, "fsz-20 hide-767 text-left")]')
#                for field in name_elem:
#                    obj.name = 'Монобанк, ' + field.text_content()
#                rate_elem = tree.xpath(f'//*[@id="main_table_cards"]/table/tbody/tr[146]/td[4]/div')
#                for field in rate_elem:
#                    obj.rate = field.text_content()
#                obj.save()
#            print('Currency exchange rates from Monobank parsed successfully')
#        response = requests.get('http://vkurse.dp.ua/course.json')
#        if response.status_code == 200:
#            rates = str(response.content)
#            usd = str(findall(r'Dollar" : \{\\n\\t\\t"buy" : "\d{2}\.\d{2}', rates))[-7:-2]
#            eur = str(findall(r'Euro" : \{\\n\\t\\t"buy" : "\d{2}\.\d{2}', rates))[-7:-2]
#            rub = str(findall(r'Rub" : \{\\n\\t\\t"buy" : "\d{1}\.\d{3}', rates))[-7:-2]
#            CurrencyRateParseData.objects.create(name='Доллар, vkurse.dp.ua', rate=usd)
#            CurrencyRateParseData.objects.create(name='Евро, vkurse.dp.ua', rate=eur)
#            CurrencyRateParseData.objects.create(name='Рубль, vkurse.dp.ua', rate=rub)
#            print('Currency exchange rates from vkurse.dp.ua parsed successfully')
#        response = requests.get('http://www.finmarket.ru/currency/rates/?id=10134')
#        if response.status_code == 200:
#            tree = lh.fromstring(response.content)
#            for index in range(1, 35):
#                obj = CurrencyRateParseData.objects.create()
#                name_elem = tree.xpath(f'/html/body/div[6]/div[7]/div[2]/div[7]/table[2]/tbody/tr[{index}]/td[2]/a')
#                for field in name_elem:
#                    obj.name = 'finmarket.ru, ' + field.text_content()
#                rate_elem = tree.xpath(f'/html/body/div[6]/div[7]/div[2]/div[7]/table[2]/tbody/tr[{index}]/td[4]')
#                for field in rate_elem:
#                    obj.rate = field.text_content()
#                obj.save()
#            print('Currency exchange rates from finmarket.ru parsed successfully')
#        response = requests.get('https://finance.i.ua/')
#        if response.status_code == 200:
#            tree = lh.fromstring(response.content)
#            obj = CurrencyRateParseData.objects.create(name = 'finance.i.ua, доллар')
#            usd = tree.xpath('/html/body/div[3]/div[3]/div/div[1]/div[1]/div[1]/div/table/tbody/tr[1]/td[3]/span/span[1]')
#            for field in usd:
#                    obj.rate = field.text_content()
#            obj.save()
#            obj = CurrencyRateParseData.objects.create(name = 'finance.i.ua, евро')
#            eur = tree.xpath('/html/body/div[3]/div[3]/div/div[1]/div[1]/div[1]/div/table/tbody/tr[2]/td[3]/span/span[1]')
#            for field in eur:
#                    obj.rate = field.text_content()
#            obj.save()
#            obj = CurrencyRateParseData.objects.create(name = 'finance.i.ua, рубль')
#            rub = tree.xpath('/html/body/div[3]/div[3]/div/div[1]/div[1]/div[1]/div/table/tbody/tr[3]/td[3]/span/span[1]')
#            for field in rub:
#                    obj.rate = field.text_content()
#            obj.save()
#            obj = CurrencyRateParseData.objects.create(name = 'finance.i.ua, злотый')
#            pln = tree.xpath('/html/body/div[3]/div[3]/div/div[1]/div[1]/div[1]/div/table/tbody/tr[4]/td[3]/span/span[1]')
#            for field in pln:
#                    obj.rate = field.text_content()
#            obj.save()
#        print('Currency exchange rates from finance.i.ua parsed successfully')
        response = requests.get('https://ubr.ua/kurs')
        if response.status_code == 200:
            tree = lh.fromstring(response.content)
            obj = CurrencyRateParseData.objects.create(name = 'ubr.ua, доллар')
            usd = tree.xpath('//*[@id="js-tb-currency"]/tbody/tr[1]/td[5]/strong')
            for field in usd:
                    obj.rate = field.text_content()
            obj.save()
            obj = CurrencyRateParseData.objects.create(name = 'ubr.ua, евро')
            eur = tree.xpath('//*[@id="js-tb-currency"]/tbody/tr[2]/td[5]/strong')
            for field in eur:
                    obj.rate = field.text_content()
            obj.save()
            obj = CurrencyRateParseData.objects.create(name = 'ubr.ua, рубль')
            rub = tree.xpath('//*[@id="js-tb-currency"]/tbody/tr[3]/td[5]/strong')
            for field in rub:
                    obj.rate = field.text_content()
            obj.save()
        print('Currency exchange rates from ubr.ua parsed successfully')

