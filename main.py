#!/usr/bin/env python

import webapp2

form="""
<form method="post" action="/testform">
	<input name="q">
	<input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)
        
class TestHandler(webapp2.RequestHandler):
	def get(self):
		q = self.request.get("q")
		self.response.out.write(q)
		#self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(self.request)
		
app = webapp2.WSGIApplication([('/', MainPage),
								('/testform', TestHandler)],
								debug=True)
