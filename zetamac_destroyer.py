from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(chrome_options)

zetamac_url = "https://arithmetic.zetamac.com/game?key=a7220a92"

browser.get(zetamac_url)

game = browser.find_element(by=By.ID, value="game")

timer = 300

while timer > 0:

    timer = int(browser.find_element(by=By.CLASS_NAME, value="left").text.split(":")[-1])

    if timer == 0:

        break

    problem = browser.find_element(by=By.CLASS_NAME, value="problem").text

    prob_components = problem.split(" ")

    if prob_components[1] == "+":

        solution = int(prob_components[0]) + int(prob_components[2])

    elif prob_components[1] == "\u2013":

        solution = int(prob_components[0]) - int(prob_components[2])

    elif prob_components[1] == "\u00D7":

        solution = int(prob_components[0]) * int(prob_components[2])

    else:

        solution = int(int(prob_components[0]) / int(prob_components[2]))

    browser.find_element(by=By.CLASS_NAME, value="answer").send_keys(solution)

# Optional: Add a delay to see the opened page (you might want to remove this in production code)
input("Press Enter to close the browser...")

# Close the browser
browser.quit()