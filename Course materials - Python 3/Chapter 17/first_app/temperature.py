import webapp2


def convertTemp(celTemp):
    ''' convert Celsius temperature to Fahrenheit temperature '''
    if celTemp == "":
        return ""
    try:
        farTemp = float(celTemp) * 9/5 + 32
        farTemp = round(farTemp, 3)  # round to three decimal places
        return str(farTemp)
    except ValueError:  # user entered non-numeric temperature
        return "invalid input"


class MainPage(webapp2.RequestHandler):
    def get(self):
        celTemp = self.request.get("celTemp")
        farTemp = convertTemp(celTemp)

        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>
            <head><title>Temperature Converter</title></head>
            <body>
              <form action="/" method="get">
                Celsius temperature: <input type="text"
                                        name="celTemp" value={}>
                <input type="submit" value="Convert"><br>
                Fahrenheit temperature: {}
              </form>
            </body>
          </html>""".format(celTemp, farTemp))

routes = [('/', MainPage)]
myApp = webapp2.WSGIApplication(routes, debug=True)
