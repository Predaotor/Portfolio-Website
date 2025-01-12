from flask import render_template, request, redirect, url_for
from .forms import ContactForm
from .models import Project, BlogPost

def home():
    return render_template('index.html')

def about():
    return render_template('about.html')

def projects():
    projects_list = Project.query.all()
    return render_template('projects.html', projects=projects_list)

def blog():
    blog_posts = BlogPost.query.all()
    return render_template('blog.html', posts=blog_posts)

def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Handle form submission logic here
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)