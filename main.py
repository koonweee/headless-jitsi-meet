from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# get cmd line args
import sys
args = sys.argv

# check if 'headless' is in args
headless = True if 'headless' in args else False

# URL parameters added with https://shawnchin.github.io/jitsi-url-generator/
URL = 'https://meet.jit.si/MutualDecembersAverageCheaply#config.disableAP=true#userInfo.displayName=%22pi%22&config.prejoinConfig.enabled=false&config.startWithVideoMuted=true&config.faceLandmarks.enableFaceCentering=false&config.disableTileEnlargement=true&config.notifications=[]'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('use-fake-ui-for-media-stream')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-features=AudioServiceSandbox')
if headless:
    print('headless')
    chrome_options.add_argument("--headless=new")

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# for pi
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
print('running')

while(True):
    pass