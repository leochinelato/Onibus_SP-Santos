from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import date
import time

service = Service(ChromeDriverManager().install())
navigator = webdriver.Chrome(service=service)
today = date.today()
today = today.strftime("%d/%m/%Y")


def open_navigator(link):
    navigator.get(link)


def fields_filling(origin, destination, date):
    origin_element = navigator.find_element(
        "xpath",
        "/html/body/main/div[1]/div[2]/div/div[5]/main/div/div/div/div/section/div/form/div/div[1]/div[1]/div/input",
    )
    destination_element = navigator.find_element(
        "xpath",
        "/html/body/main/div[1]/div[2]/div/div[5]/main/div/div/div/div/section/div/form/div/div[1]/div[3]/div/input",
    )
    departure_date = navigator.find_element(
        "xpath",
        "/html/body/main/div[1]/div[2]/div/div[5]/main/div/div/div/div/section/div/form/div/div[2]/div[1]/div[1]/div/div/input",
    )

    origin_element.click()
    time.sleep(1)
    origin_element.send_keys(origin)
    time.sleep(1)
    navigator.find_element(
        "xpath", "/html/body/div[4]/ul/li[2]/a/p"
    ).click()
    time.sleep(1)
    destination_element.click()
    time.sleep(1)
    destination_element.send_keys(destination)
    time.sleep(1)
    navigator.find_element(
        "xpath", "/html/body/div[4]/ul[2]/li[5]/a/p"
    ).click()
    time.sleep(1)
    departure_date.click()
    time.sleep(1)
    navigator.find_element(
        "xpath",
        "/html/body/main/div[1]/div[2]/div/div[5]/main/div/div/div/div/section/div/form/div/div[2]/div[1]/div[1]/div/div/input",
    ).send_keys(date)
    time.sleep(1)
    navigator.find_element(
        "xpath",
        "/html/body/main/div[1]/div[2]/div/div[5]/main/div/div/div/div/section/div/form/div/div[2]/div[4]/button",
    ).click()
    time.sleep(4)


def verify_next_bus():
    next_bus_departure = navigator.find_element(
        "xpath",
        "/html/body/main/div[1]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[9]/div/div/div[1]/div[1]/div/div/div[2]/ul/li[1]/div/div[1]/div/header/div/div/div[1]/div[2]/span[2]",
    ).text
    return next_bus_departure


def main():
    open_navigator("https://www.viacaocometa.com.br")
    fields_filling("Jabaquara", "Santos", today)
    next_bus = verify_next_bus()
    print(f"O próximo onibus SP -> Santos é: {next_bus}")


if __name__ == "__main__":
    main()
