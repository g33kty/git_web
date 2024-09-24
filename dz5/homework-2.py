import aiohttp
import asyncio
import sys
from datetime import datetime, timedelta

class CurrencyRateFetcher:
    BASE_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='

    def __init__(self, days):
        self.days = days
        self.session = None

    async def fetch_rate_for_date(self, date):
        url = self.BASE_URL + date.strftime('%d.%m.%Y')
        async with self.session.get(url, ssl= False) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Failed to fetch data for {date}, status code: {response.status}")

    async def get_currency_rates(self):
        async with aiohttp.ClientSession() as self.session:
            tasks = []
            for i in range(self.days):
                date = datetime.now() - timedelta(days=i + 1)
                tasks.append(self.fetch_rate_for_date(date))

            return await asyncio.gather(*tasks)

class CurrencyRateProcessor:
    def __init__(self, rates):
        self.rates = rates

    def extract_currency_data(self):
        result = []
        for rate in self.rates:
            if rate:
                date = rate['date']
                eur_rate = next((item for item in rate['exchangeRate'] if item['currency'] == 'EUR'), None)
                usd_rate = next((item for item in rate['exchangeRate'] if item['currency'] == 'USD'), None)

                result.append({
                    date: {
                        'EUR': {
                            'sale': eur_rate['saleRate'] if eur_rate else 'N/A',
                            'purchase': eur_rate['purchaseRate'] if eur_rate else 'N/A'
                        },
                        'USD': {
                            'sale': usd_rate['saleRate'] if usd_rate else 'N/A',
                            'purchase': usd_rate['purchaseRate'] if usd_rate else 'N/A'
                        }
                    }
                })
        return result

async def main(days):
    if not 1 <= days <= 10:
        raise ValueError("The number of days should be between 1 and 10.")

    fetcher = CurrencyRateFetcher(days)
    rates = await fetcher.get_currency_rates()

    processor = CurrencyRateProcessor(rates)
    processed_data = processor.extract_currency_data()

    print(processed_data)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: py main.py <number_of_days>")
        sys.exit(1)

    try:
        days = int(sys.argv[1])
        asyncio.run(main(days))
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
