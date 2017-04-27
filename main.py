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
		
app = webapp2.WSGIApplication([('/', MainPage)], 
			      debug=True)
