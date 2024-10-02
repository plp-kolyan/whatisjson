from pprint import pprint
from unittest import TestCase
import requests


class ExampleTestCase(TestCase):
    def test_1(self):
        """ Пример запроса с читабельным видом ответа """

        url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
        response = requests.get(url)
        pprint(response.json())

    def setUp(self):
        """ Ответ из запроса выше захардкоден в self.response_json для его доступа во всех остальных тестах
            теперь он доступен из всех остальных тестов
        """

        self.response_json = {'bpi': {'EUR': {'code': 'EUR',
                                             'description': 'Euro',
                                             'rate': '55,561.504',
                                             'rate_float': 55561.5035,
                                             'symbol': '&euro;'},
                                     'GBP': {'code': 'GBP',
                                             'description': 'British Pound Sterling',
                                             'rate': '46,309.182',
                                             'rate_float': 46309.1816,
                                             'symbol': '&pound;'},
                                     'USD': {'code': 'USD',
                                             'description': 'United States Dollar',
                                             'rate': '61,462.928',
                                             'rate_float': 61462.928,
                                             'symbol': '&#36;'}},
                             'chartName': 'Bitcoin',
                             'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index '
                                           '(USD). Non-USD currency data converted using hourly conversion '
                                           'rate from openexchangerates.org',
                             'time': {'updated': 'Oct 2, 2024 06:10:47 UTC',
                                      'updatedISO': '2024-10-02T06:10:47+00:00',
                                      'updateduk': 'Oct 2, 2024 at 07:10 BST'}}

    def test_2(self):
        """ Способ полученния значения ключа EUR, подходит только в случаях когда точно уверенн что такой ключ есть"""
        print(self.response_json['bpi'])

    def test_3(self):
        """ Пример взятия несуществующего ключа, поднимет исключение KeyError"""
        print(self.response_json['pi'])

    def test_4(self):
        """ Пример получения вложенного ключа"""
        print(self.response_json['bpi']['EUR']['code'])

    def test_5(self):
        """ Способ полученния значения ключа EUR """
        print(self.response_json.get('bpi'))

    def test_6(self):
        """ Пример взятия несуществующего ключа, вернет None """
        print(self.response_json.get('pi'))

    def test_7(self):
        """Пример получения вложенного ключа"""
        print(self.response_json.get('bpi').get('EUR').get('code'))


class SpeciesTestCase(TestCase):
    """ Самые распрастраненные структуры json"""

    def test_1(self):
        """ Cамый простой пример """
        response_json = {"key": "value"}
        print(response_json['key'])

    def test_2(self):
        """ В виде значения список """
        response_json = {"key": [1, 2, 3]}
        for value in response_json['key']:
            print(value)

    def test_3(self):
        """ В виде значения список словарей"""
        response_json = {"key": [{"number": 1}, {"number": 2}, {"number": 3}]}
        for value in response_json['key']:
            print(value['number'])


class AddTestCase(TestCase):
    """ Заполнение словаря, обычно используется для заполнения заголовков или тела запроса"""
    def setUp(self):
        """ определение dict"""
        self.empty_dict = {}
        self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36"}
        self.dict_with_list = {"key": [1, 2, 3]}

    def test_0(self):
        """ Добавление данных """
        self.empty_dict.update({"key": "value"})
        print(self.empty_dict)

    def test_2(self):
        """ Удаление данных """
        self.headers.pop("user-agent")
        print(self.headers)

    def test_3(self):
        """ Добавление данных в список"""
        self.dict_with_list["key"].append(4)
        print(self.dict_with_list)

    def test_4(self):
        headers_copy = self.headers.copy()
        self.headers.update({"key": "value"})
        print(headers_copy)
        print(self.headers)


