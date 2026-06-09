# URL Shortener - Django Application

A full-featured URL shortener web application built with Django. Create short, memorable links, track clicks, and manage your URLs with user authentication.

## ✨ Features

- ✅ **User Authentication** – Register, login, logout functionality
- ✅ **URL Shortening** – Convert long URLs into short, shareable links
- ✅ **User Dashboard** – View, edit, and delete your created short URLs
- ✅ **User-Specific URLs** – Each user sees only their own URLs
- ✅ **Responsive Design** – Works on desktop, tablet, and mobile devices
- ✅ **Copy to Clipboard** – One-click copy of short URLs
- ✅ **Custom Short Keys** – Option to create custom short URLs

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Django 6.0 |
| **Database** | PostgreSQL / SQLite |
| **Frontend** | Bootstrap 5, HTML5, CSS3 |
| **Icons** | Font Awesome 6 |
| **JavaScript** | AJAX for async operations |

## 📋 Prerequisites

- Python 3.10+
- pip
- virtualenv (recommended)
- PostgreSQL (optional, SQLite works for development)

## 🚀 Installation
### Prerequisites
- Python 3.8 or higher
- PostgreSQL (optional, SQLite works for development)
- Git

### Step-by-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/suyog123-hub/E-learning-platform.git
cd shortner

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up database
python manage.py migrate

# 6. Create superuser (admin account)
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver
