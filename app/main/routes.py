from . import main_bp
from flask import render_template, request, redirect, url_for, flash

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Processar a informação de contato aqui
        flash('Contact request submitted successfully.', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html')
