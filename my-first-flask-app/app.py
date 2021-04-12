from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
posts = {
    0: {
        'id': 0,
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id: int):
    the_post = posts.get(post_id)
    if the_post is None:
        return render_template('404.html', message=f'A post with id {post_id} was not found.')
    return render_template('post.html', post=the_post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    title = request.form.get('title')
    content = request.form.get('content')
    post_id = len(posts)
    posts[post_id] = {'id': post_id, 'title': title, 'content': content}
    return redirect(url_for('post', post_id=post_id))


if __name__ == '__main__':
    app.run(debug=True)
