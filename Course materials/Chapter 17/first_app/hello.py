import webapp2
import cgi


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Enter your name...</title></head>
            <body>
              <form action="/welcome" method="post">
                <input type="text" name="myName"><br>
                <input type="submit" value="Sign In">
              </form>
            </body>
          </html>""")


class Greeting(webapp2.RequestHandler):
    def post(self):
        username = cgi.escape(self.request.get("myName"))
        welcome_string = """<html><body>
                        Hi there, {}!
                        </body></html>""".format(username)
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(welcome_string)

routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)
