# Home Furniture E-commerce

A Django-based e-commerce platform for furniture retail, featuring user authentication, product catalog, and shopping functionality.

## Features

- User authentication (login, registration, profile management)
- Product catalog with categories
- Search functionality with PostgreSQL full-text search
- Product filtering and sorting
- Responsive design with Bootstrap
- Admin interface for content management
- Static file handling with WhiteNoise
- Debug toolbar for development

## Tech Stack

- Python 3.x
- Django 5.1.5
- PostgreSQL
- Bootstrap
- WhiteNoise
- Django Debug Toolbar

## Prerequisites

- Python 3.x
- PostgreSQL
- pip (Python package manager)

## Installation

1. Clone the repository:
bash
git clone <repository-url>
cd <project-directory>

2. Create and activate virtual environment:
bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies:
bash
pip install -r requirements.txt

4. Configure environment variables:

    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/dbname

5. Run migrations:
bash
python manage.py migrate            

6. Create superuser:
bash
python manage.py createsuperuser    

7. Run development server:
bash
python manage.py runserver      




## Project Structure

- `app/` - Main project configuration
- `main/` - Home page and basic views
- `goods/` - Product catalog functionality
- `users/` - User authentication and profiles
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates
- `media/` - User-uploaded files

## Apps

### Main App
- Basic pages (home, about)
- Base templates

### Goods App
- Product catalog
- Categories
- Search functionality
- Product filtering and sorting

### Users App
- User authentication
- User profiles
- Custom user model

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

This README.md provides:
- A brief project description
- List of main features
- Technology stack
- Installation instructions
- Project structure overview
- Description of each app's functionality
- Contributing guidelines


 