# 17-1 review exercise

# This script needs to be placed in a project folder with
# the appropriate YAML configuration file

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("myName")
        if username == "":
            welcome_string = ""
        else:
            welcome_string = "Hi there, {}!".format(username)

        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Enter your name...</title></head>
            <body>
              {}<br />
              <form action="/" method="get">
                <input type="text" name="myName"><br>
                <input type="submit" value="Greet me!">
              </form>
            </body>
          </html>""".format(welcome_string))

routes = [('/', MainPage)]
my_app = webapp2.WSGIApplication(routes, debug=True)
