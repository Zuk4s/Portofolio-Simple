from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./comment.db'
db = SQLAlchemy(app)

class Comment(db.Model):
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String, nullable=False)
  comment = Column(String, nullable=False)

with app.app_context():
  db.create_all()

@app.route('/', methods=['GET', 'POST'])
def main_route():
  if request.method == 'POST':
    input_name = request.form.get('username')
    input_comment = request.form.get('comment')
    new_comment = Comment(username=input_name, comment=input_comment)
    
    db.session.add(new_comment)
    db.session.commit()
    return redirect('/')
  else:
    comments = Comment.query.all()
    return render_template('main.html', comments=comments)

if __name__ == '__main__':
  app.run(debug=True)