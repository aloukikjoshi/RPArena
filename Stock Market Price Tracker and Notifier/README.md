# 📈 Stock Market Price Tracker and Notifier

## 🎯 Purpose
This project tracks stock prices from Yahoo Finance and sends email alerts when significant price changes occur. It also saves historical prices to a JSON file and generates plots for price trends.

## 🛠️ How It Works
1. The script scrapes stock prices from Yahoo Finance using Selenium WebDriver.
2. It compares the current prices with historical prices and identifies significant changes.
3. It sends email alerts with the details of the price changes and attaches plots of the price trends.
4. It saves the current prices to a JSON file for future reference.

## 📋 Prerequisites
- Python 3.x
- Selenium
- `python-dotenv`
- `matplotlib`
- Microsoft Edge WebDriver

## 📦 Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium python-dotenv matplotlib
    ```

3. Download and install Microsoft Edge WebDriver from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

4. Create a `.env` file in the project directory and add your email credentials:
    ```plaintext
    RECIPIENT_EMAIL=recipient_email@example.com
    SENDER_EMAIL=your_email@example.com
    SENDER_PASSWORD=your_email_password
    ```

## 🚀 Usage
1. Run the script:
    ```sh
    python all.py
    ```

2. The script will scrape stock prices, analyze them, and send email alerts if significant changes are detected.

3. It will save the current prices to `historical_prices.json` and generate plots for price trends.

## 📝 Notes
- Ensure that the `.env` file is not committed to your repository by adding it to `.gitignore`:
    ```plaintext
    .env
    ```

## 🛠️ Troubleshooting
- If you encounter a `TimeoutError`, check your internet connection, firewall settings, and ensure that "Less secure app access" is enabled in your Google account settings.
- Use a simple script to test the SMTP connection if needed.