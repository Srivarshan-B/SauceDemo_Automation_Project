import os
from datetime import datetime


def take_screenshot(driver, test_name):
    os.makedirs("reports/screenshots", exist_ok=True)
    file_name = f"reports/screenshots/{test_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    driver.save_screenshot(file_name)