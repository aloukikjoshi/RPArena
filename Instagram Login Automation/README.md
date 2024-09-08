# 📸 Instagram Login Automation

## 🎯 Purpose
This project automates the process of logging into Instagram using Selenium WebDriver. It also includes a feature to automatically close the browser when the user logs out manually.

## 🛠️ How It Works
1. The script uses Selenium WebDriver to open the Instagram login page.
2. It waits for the username and password fields to be present.
3. It enters the credentials and logs in.
4. It periodically checks if the user has logged out by looking for the presence of the login elements.
5. If the user logs out, the script closes the browser.

## 📋 Prerequisites
- Python 3.x
- Selenium
- `python-dotenv`
- Microsoft Edge WebDriver

## 📦 Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium python-dotenv
    ```

3. Download and install Microsoft Edge WebDriver from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).

4. Create a `.env` file in the project directory and add your Instagram credentials:
    ```plaintext
    INSTAGRAM_USERNAME=your_instagram_username
    INSTAGRAM_PASSWORD=your_instagram_password
    ```

## 🚀 Usage
1. Run the script:
    ```sh
    python login.py
    ```

2. The script will open the Instagram login page, enter your credentials, and log in.

3. It will periodically check if you have logged out. If you log out manually, the script will close the browser.

## 📝 Notes
- Ensure that the `.env` file is not committed to your repository by adding it to `.gitignore`:
    ```plaintext
    .env
    ```

## 🛠️ Troubleshooting
- If you encounter a `NoSuchElementException`, ensure that the page has fully loaded before the script tries to find the elements.
- Use `WebDriverWait` to wait for the elements to be present.