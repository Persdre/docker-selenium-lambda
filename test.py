from selenium import webdriver
from selenium.webdriver.common.by import By
from tempfile import mkdtemp
import time


def handler(event=None, context=None):
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome("/opt/chromedriver",
                              options=options)
    # get to login page
    driver.get("https://www.twitter.com/i/flow/login")
    time.sleep(10)
    user_name_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
    next_button = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div'
    driver.find_element(By.XPATH, user_name_path).send_keys("persdre")
    time.sleep(10)
    driver.find_element(By.XPATH, next_button).click()
    
#     # upload password
#     password_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
#     login_path = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div'
#     driver.find_element(By.XPATH, password_path).send_keys("!8328Ilovelina")
#     time.sleep(0.5)
#     driver.find_element(By.XPATH, login_path).click()
#     time.sleep(1)
    
    # # to get celebrities' list
    # celebrities_list = []
    # with open("NFTCelebrities.txt") as f:
    #     for line in f:
    #         celebrities_list.append(line.strip())
    
    # # to read celebrities' following list from twitter
    # textfile = open("following_complete_list.txt", "w")

    # # initial a following list to store all following people
    # following_list = []
    
    # for person in celebrities_list:
    #     url = "https://twitter.com/" + person + "/following"
    #     print(url)
    #     driver.get(url)
    #     # counter for the person's following people
    #     counter = 0
    #     # read first page of following list
    #     usernames = driver.find_elements_by_class_name(
    #         "css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg")

    #     for username in usernames:
    #         username = username.find_element_by_class_name("css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l").get_attribute("href")
    #         if username not in following_list:
    #             following_list.append(username)
    #             counter += 1
        
    #     last_height = driver.execute_script("return document.body.scrollHeight")
    #     while True:
    #         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #         # Wait to load page
    #         time.sleep(5)
    #         # Calculate new scroll height and compare with last scroll height
    #         new_height = driver.execute_script("return document.body.scrollHeight")
    #         if new_height == last_height:
    #             break
    #         last_height = new_height

    #         #get usernames element
    #         usernames = driver.find_elements_by_class_name(
    #                 "css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg")
    #         for username in usernames:
    #             username = username.find_element_by_class_name("css-4rbku5.css-18t94o4.css-1dbjc4n.r-1loqt21.r-1wbh5a2.r-dnmrzs.r-1ny4l3l").get_attribute("href")
    #             if username not in following_list:
    #                 following_list.append(username)
    #                 counter += 1

    #     for elem in following_list:
    #         textfile.write(elem + "\n")
    #     print(counter)
    # textfile.close()
    
    return 0
