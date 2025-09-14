# MyBlog

A simple Flask blog application with user authentication and CRUD functionality for posts.
The app uses MySQL for storing user and post data, managed via SQL Workbench.

## Features
- User registration and login/logout
- User session management
- Create, read, update, and delete blog posts
- Flash messages for feedback (errors)
- Responsive layout with basic CSS styling

## Installation

1. Clone the repository:
   git clone https://github.com/Acosta381/Blog-Flask.git
2. Navigate to the project folder:
   cd myblog
3. Create a virtual environment:
   python -m venv env
4. Activate the virtual environment:
   - Windows: env\Scripts\activate
   - Mac/Linux: source env/bin/activate
5. Install dependencies:
   pip install -r requirements.txt
6. Run the app:
   #Windows
   $env:FLASK_APP="main"
   flask run

   #Linux
   export FLASK_APP=main
   flask run
  
## Usage
- Go to `/auth/register` to create a new user.
- Go to `/auth/login` to log in.
- Once logged in, access `/blog/create` to create a new post.
- You can edit or delete your posts from the main page.

## Screenshots
<img width="947" height="405" alt="image" src="https://github.com/user-attachments/assets/aed2e063-8f85-43ef-9f16-f7a66f29dd52" />

<img width="958" height="406" alt="image" src="https://github.com/user-attachments/assets/582b0e8d-3656-4521-963b-d8eb4503a286" />

<img width="954" height="399" alt="image" src="https://github.com/user-attachments/assets/4f675869-a644-42fc-ac53-691c2d68bd29" />

<img width="942" height="395" alt="image" src="https://github.com/user-attachments/assets/492e5e37-43f8-4fff-a5b9-87ca9b8a9c35" />





## Technologies
- Python
- Flask
- SQLAlchemy
- SQL Workbench
- Jinja2 templates
- HTML/CSS
