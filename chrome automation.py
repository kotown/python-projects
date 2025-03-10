import webbrowser as wb

def auto():
    chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
    URLS=(
        "https://google.com",
        "https://youtube.com",
        "https://udemy.com"
    )
    
    browser = wb.get(chrome_path)
    for url in URLS:
        print(f"Opening {url}")
        browser.open(url)

auto()
