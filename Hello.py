from flask import Flask, redirect, url_for, request

app = Flask(__name__)


##*****************set up web***********
@app.route('/hello')
def hello_world():
   return 'Hello World'

app.add_url_rule('/', 'hello', hello_world)

if __name__ == '__main__':
   app.run()



####*****************   open debug mode    ***********
##@app.route('/hello')
##def hello_world():
##   return 'Hello World'
##
##app.add_url_rule('/', 'hello', hello_world)
##
##if __name__ == '__main__':
####   app.run()
##   app.run(Debug = True)




####*****************  change port     ***********
##@app.route('/hello')
##def hello_world():
##   return 'Hello World'
##
##app.add_url_rule('/', 'hello', hello_world)
##
##if __name__ == '__main__':
####   app.run()
##   app.run(debug = True, port = 3000)
##



   

####*****************  passing web title        ***********
##
##@app.route('/hello/<name>')
##def hello_name(name):
##   return 'Hello %s!' % name
##
##if __name__ == '__main__':
##   app.run(debug = True)



######*****************  try different variables      ***********
####
##@app.route('/blog/<int:postID>')
##def show_blog(postID):
##   return 'Blog Number %d' % postID
##
##@app.route('/rev/<float:revNo>')
##def revision(revNo):
##   return 'Revision Number %f' % revNo
##
##if __name__ == '__main__':
##   app.run()
##   



########*****************  url_for()     ***********
##
##@app.route('/admin')
##def hello_admin():
##   return 'Hello Admin'
##
##@app.route('/guest/<guest>')
##def hello_guest(guest):
##   return 'Hello %s as Guest' % guest
##
##@app.route('/user/<name>')
##def hello_user(name):
##   if name =='admin':
##      return redirect(url_for('hello_admin'))
##   else:
##      return redirect(url_for('hello_guest',guest = name))
####      return redirect(url_for('hello_guest',guest = 'Henry'))
##
##if __name__ == '__main__':
##   app.run(debug = True)




##########*****************  POST    ***********
##
##@app.route('/success/<name>')
##def success(name):
##   return 'welcome %s' % name
##
##@app.route('/login',methods = ['POST', 'GET'])
##def login():
##   if request.method == 'POST':
##      user = request.form['nm']
##      return redirect(url_for('success',name = user))
##   else:
##      user = request.args.get('nm')
##      return redirect(url_for('success',name = user))
##
##if __name__ == '__main__':
##   app.run(debug = True)






##########*****************  GET     ***********
##
##@app.route('/success/<name>')
##def success(name):
##   return 'welcome %s' % name
##
##@app.route('/login',methods = ['POST', 'GET'])
##def login():
##   if request.method == 'GET':
##      user = request.args.get('nm')
##      return redirect(url_for('success',name = user))
##   else:
##      user = request.args.get('nm')
##      return redirect(url_for('success',name = user))
##
##if __name__ == '__main__':
##   app.run(debug = True)


##
############*****************  html format     ***********
##
##@app.route('/')
##def index():
##   return '<html><body><br><br><h1>Hello World</h1></body></html>'
##
##if __name__ == '__main__':
##   app.run(debug = True)

















