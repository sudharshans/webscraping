import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.forbes.com/lists/cloud100/?sh=52a181287d9c'

driver = webdriver.Chrome()

driver.get(url)

driver.implicitly_wait(5)

html_text = driver.page_source

driver.quit()

soup = BeautifulSoup(html_text, 'html.parser')
links = soup.find_all('div', class_='table-row-group')

with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(['Company Name', 'Company Link', 'Location'])

    for tag in links:
        company_names = tag.find_all('div', class_='organizationName second table-cell company')
        companies = tag.find_all('a', href=True)
        locations = tag.find_all('div', class_='headquarters table-cell country headquarters')

        for company_name, company, location in zip(company_names, companies, locations):
            name = company_name.text.strip()
            link = company['href']
            loc = location.text.strip()

            csv_writer.writerow([name, link, loc])
            print(f'Company Name: {name}, Company Link: {link}, Location: {loc}')
print('Data has been written to output.csv')
