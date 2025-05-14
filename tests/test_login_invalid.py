from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Login sayfasına git
driver.get("https://the-internet.herokuapp.com/login")

# Kullanıcı adı ve şifre alanlarını bul
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Geçerli giriş bilgilerini gir
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")

# Giriş butonunu bul ve tıkla
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Sayfanın yüklenmesini bekle
time.sleep(2)

# Başarılı giriş sonrası yönlendirme kontrolü
if driver.current_url == "https://the-internet.herokuapp.com/secure":
    print("Giriş başarılı!")
else:
    # Hatalı giriş testi
    driver.get("https://the-internet.herokuapp.com/login")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("tomsmith")
    password_field.send_keys("Yanlışşifre")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(2)
    error_message = driver.find_element(By.ID, "flash")
    if "Your username is invalid!" in error_message.text:
        print("Hatalı giriş testi başarılı!")
    else:
        print("Hatalı giriş testi başarısız!")

# Tarayıcıyı kapat
driver.quit()
