from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = []
@app.route("/posts")
def cont_posts():
        return "{} posts".format(len(posts))

@app.route("/")
def index():
    return render_template("index.html", num_posts=len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
        return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
        return render_template("admin/post_from.html", post_id=post_id)




@app.route('/hello')
def hello():
    return "Hello World!"

if __name__ == '__main__':
        app.run()
