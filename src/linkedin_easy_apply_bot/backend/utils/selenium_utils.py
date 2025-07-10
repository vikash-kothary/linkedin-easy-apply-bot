import os
import pickle
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


driver = None


def get_driver():
    global driver

    if driver is None:
        options = browser_options()
        chrome_driver_path = os.getenv("CHROME_DRIVER_PATH")
        # ChromeDriverManager().install()
        driver = webdriver.Chrome(
            service=ChromeService(chrome_driver_path), options=options
        )

    return driver


def browser_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    # options.add_argument(r'--remote-debugging-port=9222')
    # options.add_argument(r'--profile-directory=Person 1')

    # Disable webdriver flags or you will be easily detectable
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Load user profile
    # options.add_argument(r"--user-data-dir={}".format(self.profile_path))

    return options


def save_cookies():
    driver = get_driver()
    # Save cookies to file

    try:
        with open("instances/cookies.json", "w") as f:
            json.dump(driver.get_cookies(), f, indent=1)
    except:
        pass


def load_cookies():
    driver = get_driver()
    # Load cookies from file

    try:
        with open("instances/cookies.json", "r") as f:
            print("opened file, loading json..")
            cookies = json.load(f)
            print("loaded json, getting cookie...")
            for cookie in cookies:
                try:
                    driver.add_cookie(cookie)
                    print(f"Cookie added: {cookie['name']} = {cookie['value']}")
                except Exception as e:
                    print(f"Error adding cookie: {e}")
    except Exception as e:
        print(f"Error loading cookies: {e}")
        pass

    driver.refresh()  # Apply cookies


def start_new_browser():
    driver = get_driver()
    session_url = driver.command_executor._conn.url
    session_id = driver.session_id

    # Save session info
    with open("session.json", "w") as f:
        json.dump({"session_url": session_url, "session_id": session_id}, f, indent=2)

    print(f"Session saved: {session_url} | {session_id}")
    return driver


def attach_to_existing_browser():
    global driver
    # Load session info
    with open("session.json", "r") as f:
        data = json.load(f)
        session_url = data["session_url"]
        session_id = data["session_id"]

    # Dummy driver for stealing session
    temp_driver = get_driver()
    temp_driver.quit()

    # Attach to the original session
    driver = RemoteWebDriver(command_executor=session_url, desired_capabilities={})
    driver.session_id = session_id

    print(f"Attached to session: {session_url} | {session_id}")
    return driver


def has_cookies():
    # Check if cookies file exists
    return (
        os.path.exists("instances/cookies.json")
        and os.path.getsize("instances/cookies.json") > 0
    )


if __name__ == "__main__":
    start_new_browser()
