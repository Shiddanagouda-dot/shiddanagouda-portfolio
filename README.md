# Shiddanagouda Patil — Portfolio Site

A single-page portfolio backed by a small Django app. All the content (profile,
education, experience, skills, projects, certifications) lives in a SQLite
database and is editable from the Django admin — no need to touch HTML to
update your projects later. A read-only JSON API is included via Django REST
Framework, and the contact form saves messages straight into the database.

## Tech stack

- **Backend:** Django (server-rendered HTML templates)
- **Database:** SQLite (built in, zero setup)
- **API (optional/bonus):** Django REST Framework — `/api/projects/`, `/api/skills/`, `/api/certifications/`
- **Frontend:** plain HTML/CSS/JS (no framework, no build step)

## 1. Set up a virtual environment

```bash
cd portfolio_site
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

## 3. Create the database and tables

```bash
python manage.py makemigrations core
python manage.py migrate
```

## 4. Load your portfolio content

This fills the database with the content already on your resume (profile,
education, the QSpiders training, all 6 projects, skills, and certifications):

```bash
python manage.py seed_data
```

You can re-run this command any time to reset the content back to the
defaults in `core/management/commands/seed_data.py`.

## 5. (Optional) Create an admin login

So you can edit content — new projects, updated skills, etc. — from a
browser instead of editing code:

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/` after starting the server.

## 6. Run the site

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## Adding your resume PDF

Drop your resume file into `core/static/core/files/resume.pdf` (that exact
name) and the "Résumé" link in the navigation will download it. You can
change the expected file name in the `Profile` row via the admin panel
(`resume_file_name` field) if you'd rather use a different file name.

## Editing content later

Go to `http://127.0.0.1:8000/admin/` and log in with the superuser you
created. You can add/edit:

- **Profile** — name, tagline, summary, contact links
- **Education** / **Experience** — timeline entries
- **Skill categories & Skills** — grouped skill chips
- **Projects** — title, tech stack (comma-separated), bullet points, link
- **Certifications**
- **Contact messages** — everything submitted through the contact form

## Project structure

```
portfolio_site/
├── manage.py
├── requirements.txt
├── portfolio_site/          # Django project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── core/                    # The portfolio app
    ├── models.py            # Profile, Education, Experience, Skill, Project, Certification, ContactMessage
    ├── views.py             # Home page + contact form handling
    ├── forms.py             # Contact form
    ├── admin.py             # Admin panel registrations
    ├── serializers.py       # DRF serializers (API)
    ├── api_views.py         # DRF viewsets (API)
    ├── api_urls.py          # /api/... routes
    ├── urls.py              # Page routes
    ├── management/commands/seed_data.py   # Loads your resume content into the DB
    ├── templates/core/home.html           # The whole one-page site
    └── static/core/
        ├── css/style.css    # All styling — warm paper background, green/amber accents
        ├── js/script.js     # Active-section nav highlighting + mobile menu
        └── files/           # Put resume.pdf here
```

## Deploying somewhere public later

This ships with `DEBUG = True` and a placeholder `SECRET_KEY`, which is fine
for running locally. Before putting it on a public host (Render, PythonAnywhere,
Railway, etc.):

1. Set `DEBUG = False` in `portfolio_site/settings.py`.
2. Set a real, private `SECRET_KEY` (e.g. via an environment variable).
3. Set `ALLOWED_HOSTS` to your actual domain.
4. Run `python manage.py collectstatic`.
