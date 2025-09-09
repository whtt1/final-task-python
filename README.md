# 📱 Phone Directory Web App

A simple web application built with **Python** and **Flask** to manage and display a phone directory. Users can register/login, check phone numbers for valid Lithuanian format, view a list of valid numbers, and leave comments on numbers.

---

## 🚀 Features

- **User Registration/Login** with phone number and password.
- **Phone Number Validation**: Checks if numbers start with `+370` and have 8 digits after.
- **Phone Directory**: View all valid numbers.
- **Comments System**: Registered and anonymous users can leave comments on phone numbers.
- **Track Checks**: The app tracks how many times a phone number was checked.

---

## 🛠️ Technologies Used

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite (`instance/telefono_numeriai.db`)
- **Frontend**: HTML, CSS
- **Utilities**: Custom Python utility functions for validation

---

## 📂 Project Structure

```
├── app.py                 # Main Flask application
├── db_populate.py         # Script to populate the database with sample data
├── models.py              # SQLAlchemy models for User, PhoneNumber, Comment
├── utility.py             # Utility functions (phone validation)
├── instance/
│   └── telefono_numeriai.db # SQLite database file
├── static/
│   └── styles.css         # CSS for styling
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── numbers.html
│   └── number_detail.html
├── .dmm                   # (Optional/unused project file)
└── .gitignore             # Git ignore file
```

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/whtt1/final-task-python.git
cd final-task-python
```

2. **Set up a virtual environment (recommended)**

```bash
python -m venv venv
# Activate the environment
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac
```

3. **Install dependencies**

```bash
pip install flask sqlalchemy
```

> Note: `sqlite3` is built into Python, no extra installation needed.

4. **Populate the database (optional)**

```bash
python db_populate.py
```

5. **Run the application**

```bash
python app.py
```

6. **Open in browser**

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the app.

---

## 📝 Usage

- **Login/Register**: Enter a phone number (starting with `+370`), password, and select a network.
- **Check a Phone Number**: Enter a number on the home page to validate it.
- **View Numbers**: Go to the "Numeriai" page to see all valid numbers.
- **Comment on a Number**:
  - **Logged-in users**: Comments show your phone number (partially hidden) and network.
  - **Not logged-in users**: Comments appear as **"Anonimas"** (anonymous).

---

## 💡 Notes

- The application is **designed for Lithuanian phone numbers**.
- Database resets when running `db_populate.py`, so be careful if you have data you want to keep.
- The `.dmm` file is not used in the main application.

---

## 🔗 Repository

[GitHub Repository](https://github.com/whtt1/final-task-python)

