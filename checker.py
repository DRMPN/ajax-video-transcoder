import logging
import os
import sys
import time
import traceback
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from src.helpers import random_gen

logging.basicConfig(level=logging.INFO)

if len(sys.argv) != 4:
    print("usage: checker.py [IP] [PORT] check")
    sys.exit(1)

IP = sys.argv[1]
PORT = sys.argv[2]
COMMAND = sys.argv[3]
URL = f"http://{IP}:{PORT}/hello"

CWD = os.path.abspath(os.getcwd())
CHECK_FILE = "small.webm"
if not [x for x in Path(CWD).iterdir() if "small" in x.name]:
    logging.error("No file to upload")
    exit(102)
else:
    logging.info("Completed - Check file is found")

logging.info(f"Recieved: IP - {IP}; PORT - {PORT}; COMMAND - {COMMAND}; URL - {URL}")

time.sleep(3)
logging.info("Sleeping 3 seconds")

if COMMAND.lower() == "check":
    logging.info("Begin check")
    try:
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_service = Service(log_path=Path("/dev/null"))
        driver = webdriver.Firefox(options=firefox_options, service=firefox_service)

        username = random_gen()
        password = random_gen()

        """
        SIGN UP
        """
        driver.get(URL)
        driver.find_element(By.XPATH, '//*[@id="gotoreg"]').click()
        logging.info("Completed - clicked Sign Up")
        driver.find_element(By.XPATH, '//*[@id="reguser"]').send_keys(username)
        password_field = driver.find_element(By.XPATH, '//*[@id="regpass1"]').send_keys(
            password
        )
        confirmation_field = driver.find_element(
            By.XPATH, '//*[@id="regpass2"]'
        ).send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="makereg"]').click()
        logging.info("Completed - Sign up")
        """
        SIGN IN
        """
        driver.find_element(By.XPATH, '//*[@id="logform"]/form/div[1]/input').send_keys(
            username
        )
        driver.find_element(By.XPATH, '//*[@id="logform"]/form/div[2]/input').send_keys(
            password
        )
        driver.find_element(By.XPATH, '//*[@id="makelog"]').click()
        logging.info("Completed - Sign in")
        """
        FILE UPLOAD
        """
        driver.find_element(By.XPATH, '//*[@id="upfile"]').send_keys(
            f"{CWD}/{CHECK_FILE}"
        )
        driver.find_element(By.XPATH, '//*[@id="upform"]/button').click()
        logging.info("Completed - File upload")
        """
        FILE DOWNLOAD
        """
        driver.find_element(By.XPATH, "/html/body/main/div[2]/div[2]/div/a").click()
        logging.info("Completed - File download")
        driver.close()

        [f.unlink() for f in Path(f"{CWD}/src/uploads").iterdir() if f.is_file()]
        logging.info("Completed - File removed")
    except Exception as e:
        logging.error(traceback.format_exc())
        exit(102)

    print("OK")
    exit(101)

else:
    print("usage: checker.py [IP] [PORT] check")
    sys.exit(1)
