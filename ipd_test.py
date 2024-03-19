from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import random
firefoxOptions = Options()
nrp = '5025221215'
password = 'RayanGant3ng'
komentar = ('Penjelasan dosen mudah dipahami, jadwal sesuai dengan perjanjian belajar yang dicantumkan di MyClassroom',
            'Dosen dapat mengajar dengan cara yang unik dan tidak membuat bosan, kelas berlangsung secara kondusif dengan materi yang tersampaikan',
            'Mudah memahami penjelasan dosen dengan materi yang diberikan yang ada di MyClassroom',
            'Pembelajaran baik dan kondusif, meskipun ada sedikit materi belum dijelaskan secara maksimal karena kurangnya waktu dan beberapa hal')

browser = webdriver.Firefox()

browser.get("https://akademik.its.ac.id/home.php")
browser.find_element("id", "username").send_keys(nrp)
browser.find_element("id", "continue").click()
browser.find_element("id", "password").send_keys(password)
browser.find_element("id", "login").click()
time.sleep(0.5)

# List all the mk
browser.get("https://akademik.its.ac.id/ipd_kuesionermk.php")
form_mk = browser.find_element("xpath",'//select[@id="mk_kuesioner"]')
matkul = [mk.get_attribute('value') for mk in form_mk.find_elements('tag name','option')]

# Fill the mk form and dosen form
browser.get("https://akademik.its.ac.id/ipd_kuesionermk.php")
for i in range(len(matkul)-1):
    choose = Select (browser.find_element("id", "mk_kuesioner"))
    choose.select_by_value (matkul[i+1])
    for j in range(10):
        random.seed(time.time())
        nilai = random.randint(3,4)
        score= "MK" + str(j+1) + str(nilai) 
        browser.find_element("id", score).click()
        print(score)
        time.sleep(0.1)
    isi_text=komentar[random.randint(0,3)]
    browser.find_element("id", "txtKomentar").send_keys(isi_text)
    checkbox = browser.find_element("name", "chkPermanent").click()
    print(matkul[i+1], isi_text)
    browser.find_element("name", "button").click()

    form_dosen = browser.find_element('id','form2')
    link_element = form_dosen.find_element("xpath",'.//a[@href]')
    link_dosen = link_element.get_attribute('href')

    browser.get(link_dosen)
    for j in range(10):
        random.seed(time.time())
        nilai = random.randint(3,4)
        score= "DO" + str(j+1) + str(nilai) 
        browser.find_element("id", score).click()
        print(score)
        time.sleep(0.1)
    isi_text=komentar[random.randint(0,3)]
    browser.find_element("id", "txtKomentar").send_keys(isi_text)
    checkbox = browser.find_element("name", "chkPermanent").click()
    print(nip[i], isi_text)
    browser.find_element("name", "button").click()

    browser.get("https://akademik.its.ac.id/ipd_kuesionermk.php")