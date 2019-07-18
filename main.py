import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('index.html')
        self.response.write(template.render())

class Bloghandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('new_post.html')
        self.response.write(template.render())
    def post(self):
        Title_answer: self.request.get('Title')
        Name_answer: self.request.get('Name')
        Content_answer: self.request.get('Content')

        template_vars = {
        "Title_answer" : Title_answer,
        "Name_answer" : Name_answer,
        "Content_answer" : Content_answer
        }
        template = jinja_env.get_template('templates/view_post.html')
        self.response.write(template.render(template_vars))


app = webapp2.WSGIApplication([
        ('/', MainHandler),
        ('/blogpost', Bloghandler),
        ('/view', Bloghandler)
] ,debug=True)
