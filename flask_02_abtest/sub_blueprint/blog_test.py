from flask import Blueprint

blog_ab = Blueprint('blog', __name__)

# /blog/blog1
@blog_ab.route('/blog1')
def blog():
    return 'TEST BLUEPRINT'