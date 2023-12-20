import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from getpass import getpass
from selenium.webdriver.common.keys import Keys
import os


"""
##############################################################
############                                ##################
############      CLASS FOR INSTAGRAM       ##################
############                                ##################
##############################################################

"""


class Instagram():
    def __init__(self) -> None:
        self.username = ""
        self.password = ""
        self.followerCount = 0
        self.followingCount = 0
        self.followers = []
        self.following = []
        self.userNotFollowingBack = []

    def login(self):
        driver.get('https://www.instagram.com/')
        time.sleep(3)
        while True:
            try:
                self.username = input("Kullanıcı adı: ")
                self.password = getpass(prompt="Şifre (görünmez):")

                usernameTb = driver.find_element(
                    by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
                usernameTb.send_keys(Keys.CONTROL, "a")
                usernameTb.send_keys(Keys.DELETE)
                usernameTb.send_keys(self.username)

                passwordTb = driver.find_element(
                    by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
                passwordTb.send_keys(Keys.CONTROL, "a")
                passwordTb.send_keys(Keys.DELETE)
                passwordTb.send_keys(self.password)

                # Login button click
                time.sleep(0.2)
                driver.find_element(
                    by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()
                time.sleep(5)
            except:
                print("Bir hata oluştu tekrar deneyin")
                continue

            try:
                driver.find_element(
                    by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/span")
                print("Yanlış kullanıcı adı veya şifre.")
                continue

            except:
                print("Kullanıcı adı ve şifre doğru")
                break

        # --- END OF LOGIN SCREEN ---
        time.sleep(5)

        try:
            twoFactorTb = driver.find_element(
                by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input")

            if (twoFactorTb != None):
                twoFactorCode = input("Kimlik doğrulama kodunuzu girin : ")
                twoFactorTb = driver.find_element(
                    by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input")
                twoFactorTb.send_keys(twoFactorCode)

                # Confirm button click
                driver.find_element(
                    by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[2]/button").click()
        except:
            print("Çift doğrulama etkin değil giriş başarılı")

        time.sleep(5)

    def findFollowers(self):
        os.system("cls")
        driver.get(f'https://www.instagram.com/{self.username}/?next=%2F')
        time.sleep(3)

        # -- Get follower count --
        followerCountStr = driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span").text
        self.followerCount = int(followerCountStr)
        print(self.followerCount, "tane takipçi bulundu.")

        # -- Load all followers --
        driver.get(
            f"https://www.instagram.com/{self.username}/followers/?next=%2F")
        time.sleep(4)

        for i in range(1, self.followerCount + 1):
            os.system("cls")
            print(
                f"Takipçiler alınıyor... {'{:.2%}'.format(i/self.followerCount)}")
            while True:
                try:
                    lastElement = driver.find_element(
                        by=By.XPATH, value=f"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]")
                    break
                except:
                    continue

            ActionChains(driver).move_to_element(lastElement).perform()

        # -- Get all followers and user not following back--
        for i in range(1, self.followerCount + 1):
            followerUser = driver.find_element(
                by=By.XPATH, value=f"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[{i}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span").text
            self.followers.append(followerUser)

            # -- Get user not following back --
            try:
                notFollowingUserButton = driver.find_element(
                    by=By.XPATH, value=f"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[2]/div/div/div/button")
                self.userNotFollowingBack.append(followerUser)
            except:
                pass

        print("Tüm takipçiler başarıyla alındı.")
        time.sleep(1.5)

    def findFollowings(self):
        driver.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)

        # -- Get following count --
        followingCount = driver.find_element(
            by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a/span/span").text
        self.followingCount = int(followingCount)
        print(self.followingCount, "tane takip edilen hesap bulundu.")

        driver.get(f"https://www.instagram.com/{self.username}/following/")
        time.sleep(3)

        # -- Scroll to bottom --
        for i in range(1, self.followingCount + 1):
            os.system("cls")
            print(
                f"Takip edilen hesaplar alınıyor... {'{:.2%}'.format(i/self.followingCount)}")
            while True:
                try:
                    lastElement = driver.find_element(
                        by=By.XPATH, value=f"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[{i}]")
                    break
                except:
                    continue

            ActionChains(driver).move_to_element(lastElement).perform()

        for i in range(1, self.followingCount + 1):
            followedByUser = driver.find_element(
                by=By.XPATH, value=f"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div/div/div[{i}]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span").text
            self.following.append(followedByUser)

        print("Takip edilen hesaplar başarıyla alındı.")

    def followUsers(self, users):
        os.system("cls")
        print("Seçilen hesaplar takip ediliyor.")
        for user in users:
            print(f'{user} takip ediliyor...', end=" ")
            driver.get(f"https://www.instagram.com/{user}")
            time.sleep(2)
            while True:
                try:
                    driver.find_element(
                        by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]").click()
                    break
                except:
                    print(".", end=" ")
                    continue

            print("✔")

        input("Menüye dönmek için entera basın")

    def userNotFollowingBackMain(self):
        usersToFollow = []
        while True:
            os.system("cls")
            print("Geri takip etmediğiniz hesaplar :")
            for i, user in enumerate(self.userNotFollowingBack):
                print("\t", i, "-", user)
            print("Takipt edilecek hesaplar :")
            for i, user in enumerate(usersToFollow):
                print("\t", i, "-", user)
            n = input("\nTakip etmek istediğniz hesapların sayılarını aralarında virgül olacak şekilde yazın\nÖrnek : 1,3,4,6,11\nSeçiminizi sıfırlamak için 'r'\nSeçiminizi onaylamak için 'y'\nÇıkış yapmak için 'n'\nSeçiminiz : ")
            if (n == "n"):
                break
            elif (n == "r"):
                usersToFollow.clear()
                continue
            elif (n == "y"):
                self.followUsers(usersToFollow)
                break
            inputUsersToFollow = n.split(",")
            for index in inputUsersToFollow:
                usersToFollow.append(self.userNotFollowingBack[int(index)])

    def unfollowUsers(self, users):
        os.system("cls")
        print("Seçilen hesaplar takipten çıkılıyor.")
        for user in users:
            print(f'{user} takipten çıkılıyor...', end=" ")
            driver.get(f"https://www.instagram.com/{user}")
            time.sleep(2)
            while True:
                try:
                    driver.find_element(
                        by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]").click()
                    break
                except:
                    print("hata")
                    continue

            while True:
                try:
                    driver.find_element(

                        by=By.XPATH, value="/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]").click()
                    break
                except:
                    continue

            print("✔")
            # ilk button /html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button
            # ikinci button /html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div/div/div

        input("Menüye dönmek için entera basın")

    def notFollowingUserBackMenu(self, result):
        usersToUnfollow = []
        while True:
            os.system("cls")
            print("Sizi gerip takip etmeyen hesaplar :")
            for i, user in enumerate(result):
                print("\t", i, "-", user)
            print("Takipten çıkılacak hesaplar :")
            for i, user in enumerate(usersToUnfollow):
                print("\t", i, "-", user)
            n = input("\nTakipten çıkmak istediğniz hesapların sayılarını aralarında virgül olacak şekilde yazın\nÖrnek : 1,3,4,6,11\nSeçiminizi sıfırlamak için 'r'\nSeçiminizi onaylamak için 'y'\nÇıkış yapmak için 'n'\nSeçiminiz : ")
            if (n == "n"):
                break
            elif (n == "r"):
                usersToUnfollow.clear()
                continue
            elif (n == "y"):
                self.unfollowUsers(usersToUnfollow)
                break
            inputUsersToUnfollow = n.split(",")
            for index in inputUsersToUnfollow:
                usersToUnfollow.append(result[int(index)])

    def notFollowingUserBackMain(self):
        os.system("cls")
        set_followers = set(self.followers)
        set_following = set(self.following)
        set_result = set_following - set_followers
        result = list(set_result)
        self.notFollowingUserBackMenu(result)

    def menu(self):
        os.system("cls")
        print(
            f'Hoşgeldiniz {self.username}, yapmak istediğiniz işlemi seçiniz')
        n = input("1 - Takip edenleri tekrardan bul\n2 - Takip ettiklerimi tekrardan bul\n3 - Benim geri takip etmediklerim\n4 - Beni geri takip etmiyenler\nn - Çıkış\nSeçiminiz : ")
        return n


"""
##############################################################
############                                ##################
############        WEBDRIVER OPTIONS       ##################
############                                ##################
##############################################################

"""

# --- Options ----
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("log-level=3")

# -- Driver Neccessary --
webdriver_service = service.Service(
    '')
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url,
                          webdriver.DesiredCapabilities.OPERA, options=chrome_options)
driver.maximize_window()


"""
##############################################################
############                                ##################
############        DRIVER CODE             ##################
############                                ##################
##############################################################

"""

instagram = Instagram()
instagram.login()
instagram.findFollowers()
instagram.findFollowings()
while True:
    n = instagram.menu()
    match n:
        case "1":
            instagram.findFollowers()
        case "2":
            instagram.findFollowings()
        case "3":
            instagram.userNotFollowingBackMain()
        case "4":
            instagram.notFollowingUserBackMain()
        case "n":
            break
        case _:
            print("Geçersiz giriş yaptınız.")
            time.sleep(1.5)
