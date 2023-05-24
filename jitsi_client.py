from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('use-fake-ui-for-media-stream')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

# additional URL parameters to optimize call
JITSI_PARAMS =  \
    '#config.disableAP=true' \
    '#userInfo.displayName=%22pi%22' \
    '&config.prejoinConfig.enabled=false' \
    '&config.startWithVideoMuted=true' \
    '&config.faceLandmarks.enableFaceCentering=false' \
    '&config.disableTileEnlargement=true' \
    '&config.notifications=[]'


def join_call(call_url):
    appended_url = call_url + JITSI_PARAMS
    driver.get(appended_url)

    print('call initiated to url: ' + call_url)

def leave_call():
    driver.get('about:blank')
    print('call ended')