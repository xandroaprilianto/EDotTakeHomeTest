import pytest
import time

@pytest.fixture
def scroll_to_bottom(driver):
    def _scroll():
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll ke bawah
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)  # beri waktu konten load

            # Hitung ulang tinggi halaman
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break  # sudah sampai paling bawah
            last_height = new_height

    return _scroll

@pytest.fixture
def scroll_once(driver):
    def _scroll():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    return _scroll
