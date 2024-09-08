import os
from dotenv import load_dotenv
import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import matplotlib.pyplot as plt

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
recipient_email = os.getenv('RECIPIENT_EMAIL')
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')

def scrape_stock_prices(url, stock_symbols):
    driver = webdriver.Edge()  # Ensure Edge WebDriver is in your PATH
    driver.get(url)
    prices = {}
    for symbol in stock_symbols:
        try:
            # CSS Selector to find the price based on the data-symbol attribute
            css_selector = f'fin-streamer[data-symbol="{symbol}"]'
            element = driver.find_element(By.CSS_SELECTOR, css_selector)
            price_text = element.get_attribute('value').strip('$').replace(',', '')
            price = float(price_text)  # Convert to float
            prices[symbol] = price
        except Exception as e:
            print(f"Error retrieving data for {symbol}: {e}")
    driver.quit()
    return prices

def analyze_prices(current_prices, historical_prices, threshold=0.25):
    alerts = {}
    for symbol, current_price in current_prices.items():
        if symbol in historical_prices:
            historical_price_entry = historical_prices[symbol]
            print(f"Data for {symbol}: {historical_price_entry}")  # Debugging statement
            if isinstance(historical_price_entry, list) and historical_price_entry:
                last_entry = historical_price_entry[-1]
                if isinstance(last_entry, dict) and 'price' in last_entry:
                    historical_price = last_entry['price']
                    price_change = (current_price - historical_price) / historical_price * 100
                    if price_change >= threshold or price_change <= -threshold:
                        alerts[symbol] = {
                            'price_change': price_change,
                            'last_price': historical_price,
                            'current_price': current_price,
                            'last_timestamp': last_entry['timestamp'],
                            'current_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        }
                else:
                    print(f"Unexpected data format for {symbol} in historical prices.")
            else:
                print(f"Unexpected data format for {symbol} in historical prices.")
    return alerts

def save_prices_to_json(prices, filename='historical_prices.json'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(filename, 'r') as f:
            historical_data = json.load(f)
    except FileNotFoundError:
        historical_data = {}

    for symbol, price in prices.items():
        if symbol not in historical_data or not isinstance(historical_data[symbol], list):
            historical_data[symbol] = []
        historical_data[symbol].append({'timestamp': timestamp, 'price': price})

    with open(filename, 'w') as f:
        json.dump(historical_data, f)

def load_historical_prices_from_json(filename='historical_prices.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def load_prices_for_symbol(symbol, filename='historical_prices.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data.get(symbol, [])

def plot_alert_prices(symbol, last_price, current_price, last_timestamp, current_timestamp):
    timestamps = [last_timestamp, current_timestamp]
    prices = [last_price, current_price]
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, prices, marker='o')
    plt.title(f'Stock Price Alert for {symbol}')
    plt.xlabel('Timestamp')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'{symbol}_alert_price_trend.png')
    plt.close()

def send_email_alerts(alerts, recipient_email, sender_email, sender_password):
    if not alerts:
        print("No alerts to send.")
        return
    subject = "Stock Price Alert"
    body = "Significant stock price changes:\n\n"
    for symbol, data in alerts.items():
        body += f"{symbol}: {data['price_change']:.2f}%\n"
        plot_alert_prices(symbol, data['last_price'], data['current_price'], data['last_timestamp'],
                          data['current_timestamp'])
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    for symbol in alerts.keys():
        with open(f'{symbol}_alert_price_trend.png', 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=f'{symbol}_alert_price_trend.png')
        msg.attach(image)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()

# Main script
historical_prices = load_historical_prices_from_json()
stock_symbols = [
    "AAPL", "GOOGL", "MSFT", "TSLA", "TCS.NS", "WIT", "NVD.F", "NOK", "VUG", "DIS", "PARA", "SUNPHARMA.BO",
    "DELL", "ADANIPOWER.NS", "RELI", "JIOFIN.BO", "AMZN", "BSE-MIDCAP.BO", "^NSEI", "^BSESN", "^NSEBANK", "^DJI",
    "HFCL.NS", "HFCL.BO", "ADANIPOWER.BO", "RNFI-ST.NS", "NIBL.NS", "NIBL.BO", "RHL.BO", "RHL.NS", "ASAHISONG.BO",
    "ASAHISONG.NS", "UNIINFO.NS", "IDEA.NS"
]
url = (
    "https://finance.yahoo.com/quotes/AAPL,GOOGL,MSFT,TSLA,TCS.NS,WIT,NVD.F,NOK,VUG,DIS,PARA,SUNPHARMA.BO,DELL,"
    "ADANIPOWER.NS,RELI,JIOFIN.BO,AMZN,BSE-MIDCAP.BO,%5ENSEI,%5EBSESN,%5ENSEBANK,%5EDJI,HFCL.NS,HFCL.BO,"
    "ADANIPOWER.BO,RNFI-ST.NS,NIBL.NS,NIBL.BO,RHL.BO,RHL.NS,ASAHISONG.BO,ASAHISONG.NS,UNIINFO.NS,IDEA.NS/view/v1"
)

while True:
    current_prices = scrape_stock_prices(url, stock_symbols)
    alerts = analyze_prices(current_prices, historical_prices)
    if alerts:
        send_email_alerts(alerts, recipient_email, sender_email, sender_password)
    save_prices_to_json(current_prices)
    historical_prices = load_historical_prices_from_json()
    time.sleep(1800)
