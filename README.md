# 📚 Random Topic Quote App

A simple and fun desktop application built with Python (v3.12) and PySide6 (Qt for Python).

Pick a topic from the dropdown menu and get a random quote, joke, movie info, or historical event — all loaded from a local SQLite database.

---

## ✨ Features

- 🎯 Choose from four topics via a ComboBox
- 🎲 Get a random item from the selected topic
- 💾 SQLite-powered persistent storage
- 🪟 Clean and simple PySide6 UI with gradient background
- 🎨 Styled buttons with hover and pressed effects
- 📝 Multi-line label with rounded corners
- ⚡ Instant loading from database

---

## 🎯 How It Works

The app uses a single ComboBox to select the topic. When the user clicks the "Next" button, the app:

1. Reads the selected topic from the ComboBox
2. Loads all rows from the matching database table
3. Picks a random item using `random.choice()`
4. Displays it in the label (skipping the `id` column)

### 📋 Topics and Tables

| Topic (in ComboBox) | Database Table |
|----------------------|----------------|
| جوک | `joke` |
| انگیزشی / اندرزی | `motivational` |
| اطلاعات فیلم | `Film_Information` |
| رخداد تاریخی | `Historical_event` |

All logic is handled in the `Main` class, and database operations are in the `SQl` class.

---

## 🗂️ Project Structure

```
project-folder/
│── main.py
│── main_window.py
│── database.py
│── databaseDB.db
│── ui_main_window.ui
│── README.md
```

---

## 🛠️ How to Run

Install dependencies:

```bash
pip install PySide6
```

Run the application:

```bash
python main.py
```

---

## 📦 Database

The SQLite database contains four tables:

| Table | Fields |
|-------|--------|
| `joke` | id, joke_text |
| `motivational` | id, text, author |
| `Film_Information` | id, name, Director, Year_of_construction, Film_Synopsis |
| `Historical_event` | id, history, event1, event2, event3 |

All data is read manually using SQL queries.

---

## 🚀 Future Improvements

- 🌙 Dark / Light theme switch
- 📝 Show author name in a separate label
- 🔍 Search and filter
- 🖼️ Movie poster display
- 🎨 Custom themes

---

## 👨‍💻 Author

Created by **Ali Asghari**
