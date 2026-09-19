# Django-SkillSquad

**SkillSquad** is a Django **learning-management system (LMS) / student portal**: teachers publish courses made of modules, pages, quizzes and assignments; students enrol, work through the material, take quizzes, submit assignments, ask questions and track their progress. It also has direct messaging, paid courses through Stripe, and an interviewer area for live video sessions.

> Built on the open-source "django student portal" tutorial and extended for SkillSquad. A variant with role selection at sign-up lives in [SkillSquad-User-Roles](https://github.com/SanaAkram/SkillSquad-User-Roles).

## Features

| Area | What you can do |
|---|---|
| **Accounts** (`authy`) | Sign up / log in, profile with picture, banner, location, bio |
| **Courses** (`classroom`) | Create, edit and delete courses in **categories**; browse by category; enrol; "My courses" |
| **Course content** (`module`, `page`) | Modules containing rich-text **pages** (CKEditor, file uploads); students mark pages as done |
| **Quizzes** (`quiz`) | Teachers create quizzes with questions/answers; students take them and see graded attempts |
| **Assignments** (`assignment`) | Teachers set assignments; students submit files; teachers grade submissions (points, status) |
| **Progress** (`completion`) | Tracks completed pages/modules per student |
| **Q&A** (`question`) | Per-course questions and answers with voting and "mark as answer" |
| **Messages** (`direct`) | Direct messages between users |
| **Payments** (`payments`) | Stripe Checkout for paid courses (course `amount`) |
| **Interviewer** (`interviewer`) | Meeting links with a weekly schedule, and a video-meeting page built on the Zoom Meeting Web SDK 2.3.5 (a copy of the SDK sample is in `zoom-sdk-web-2.3.5/`) |

Teachers vs. students: a course's owner sees the teacher tools (`teacher_mode`); everyone else sees the student view.

## Architecture

```
Browser ─► student_portal/urls.py
              ├─ /user/…       authy        (auth + profiles)
              ├─ /course/…     classroom    ─┬─ module ─ page ─ completion
              │                             ├─ quiz  (Quizzes, Question, Answer, Attempt)
              │                             ├─ assignment (Assignment, Submission, Grade)
              │                             └─ question (Q&A: Question, Answer, Votes)
              ├─ /direct/…     direct       (Message)
              ├─ /payment/…    payments     (Stripe Checkout session)
              ├─ /inter/…      interviewer  (Zoom meeting links)
              └─ /ckeditor/…   rich-text uploads
                          │
                          ▼
              SQLite (default)  +  media/ (uploaded pictures, files)
```

## Stack

- Python 3.8+ and **Django 3.2**
- SQLite (default database)
- Pillow (images), **django-ckeditor** (rich text and uploads)
- **Stripe** (`stripe` Python library) for payments
- Zoom Meeting **Web SDK 2.3.5**
- HTML templates in `student_portal/templates/`

## Install

There is no `requirements.txt` yet; install what the code imports:

```bash
git clone https://github.com/SanaAkram/Django-SkillSquad.git
cd Django-SkillSquad

python -m venv venv
# Windows:      venv\Scripts\activate
# macOS/Linux:  source venv/bin/activate

pip install "Django>=3.2,<4" Pillow django-ckeditor stripe
```

## Configure

In `student_portal/settings.py`:

- **Database** — SQLite works out of the box (`db.sqlite3`). For PostgreSQL, install `psycopg2-binary` and set:

  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "<database>",
          "USER": "<user>",
          "PASSWORD": "<password>",
          "HOST": "localhost",
          "PORT": "5432",
      }
  }
  ```

- **Stripe** — set your own test keys (from the Stripe dashboard) and load them from the environment instead of the file:

  ```python
  import os
  STRIPE_PUBLIC_KEY = os.environ["STRIPE_PUBLIC_KEY"]
  STRIPE_SECRET_KEY = os.environ["STRIPE_SECRET_KEY"]
  ```

- **Media** — uploads go to `media/` (`MEDIA_URL = '/media/'`), CKEditor uploads to `media/uploads/`.
- **Login** — `LOGIN_URL = '/user/login'`, redirect to the site index after login.

Uncomment `'payments'` in `INSTALLED_APPS` if you want the payment flow enabled.

## Run

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/>, register a user, create a category in `/admin/`, then create a course from **New course**.

## Notes

- The default branch of this repository is `fitrsy`.
- Keep real Stripe/Zoom credentials out of git; rotate any key that was ever committed.
- `db.sqlite3` and `media/` in the repo hold development data only.
