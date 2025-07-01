# UWL Nepalese Society Website 🏛️

A Django-based website for the University of West London’s Nepalese Society, showcasing events, blog posts, and member profiles.

---

## 📌 Table of Contents

- [About](#about)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Database Setup](#database-setup)  
  - [Environment Variables](#environment-variables)  
  - [Run Locally](#run-locally)  
- [Project Structure](#project-structure)  
- [Usage](#usage)  
- [Contributing](#contributing)  
- [License](#license)  
- [Credits](#credits)

---

## 🌟 About

This site was developed by Rusz Baidhya and team for the Nepalese Society at UWL. It offers:

- Presentation of past & upcoming **cultural events**
- Dynamic **member profiles**
- Integrated **blog** area for community contributions

Acting as both **lead developer** and **project manager**, the site was built using Python/Django, with a custom responsive frontend. The project followed a structured Waterfall methodology from requirement gathering through deployment.

---

## 🔧 Features

- ✅ Responsive, custom UI with HTML/CSS & JavaScript  
- ✅ Admin dashboard for CRUD management of members, events, and posts  
- ✅ SQLite3 integration (development-ready)  
- ✅ Blog module for member-contributed content  
- ✅ Static/media inclusion for photos and event assets  

---

## 🛠️ Tech Stack

- **Backend**: Python, Django  
- **Frontend**: HTML5, CSS3, JavaScript  
- **Database**: SQLite3  

---

## 🧩 Getting Started

### Prerequisites

- Python 3.8+  
- Git

### Installation

1. Clone this repo:
    ```bash
    git clone https://github.com/Rusz01/UWL-Nepalese-Society-Website.git
    cd UWL-Nepalese-Society-Website
    ```

2. (Recommended) Create & activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### 🗄️ Database Setup

- By default, the app uses **SQLite3**, ideal for development.
- To set up:
  ```bash
  python manage.py migrate
  python manage.py createsuperuser
