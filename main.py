from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://meet.jit.si/MutualDecembersAverageCheaply#userInfo.displayName=%22pi%22&config.prejoinConfig.enabled=false&config.startWithVideoMuted=true&config.faceLandmarks.enableFaceCentering=false&config.disableTileEnlargement=true&config.notifications=[]'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('use-fake-ui-for-media-stream')
chrome_options.add_argument("--headless=new")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(URL)
print('running')

while(True):
    pass