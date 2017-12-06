import os
import jinja2
import logging
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))
# Yen-Ting Pan and Hung-Wen Chen contribution - SI 539 server side code 

class MainHandler(webapp2.RequestHandler):
    def get(self):
        title = "Paw Wow - Home"
        template_vars = {
            'title': title,
            'name':'index',
            'bodyid':"index",
            'map':"not"
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.out.write(template.render(template_vars))

class browseHandler(webapp2.RequestHandler):
    def get(self):        
        title = "Paw Wow - Browse Our Pets"
        template_vars = {
            'title': title,
            'name':'browse',
            'bodyid':"browsePage",
            'map':"not"
        }
        template = JINJA_ENVIRONMENT.get_template('browse.html')
        self.response.out.write(template.render(template_vars))

class processHandler(webapp2.RequestHandler):
    def get(self):
        title = "Paw Wow - Our Process"
        template_vars = {
            'title': title,
            'name':'howitworks',
            'bodyid':"ProcessPage",
            'map':"not"
        }
        template = JINJA_ENVIRONMENT.get_template('howitworks.html')
        self.response.out.write(template.render(template_vars))

class contactusHandler(webapp2.RequestHandler):
    def get(self):
        title = "Paw Wow - Contact Us"
        template_vars = {
            'title': title,
            'name':'contactus',
            'bodyid':"contactusPage",
            'map':"use"
        }
        template = JINJA_ENVIRONMENT.get_template('contactus.html')
        self.response.out.write(template.render(template_vars))

class petHandler(webapp2.RequestHandler):
    def get(self):
        title = "Paw Wow - Our Pets"
        if ('1' in self.request.path ):
            number = '1'
            template = JINJA_ENVIRONMENT.get_template('pet1.html')
        elif ('2' in self.request.path ):
            number = '2'
            template = JINJA_ENVIRONMENT.get_template('pet2.html')
        elif ('3' in self.request.path ):
            number = '3'
            template = JINJA_ENVIRONMENT.get_template('pet3.html')
        elif ('4' in self.request.path ):
            number = '4'
            template = JINJA_ENVIRONMENT.get_template('pet4.html')
        elif ('5' in self.request.path ):
            number = '5'
            template = JINJA_ENVIRONMENT.get_template('pet5.html')
        elif ('6' in self.request.path ):
            number = '6'
            template = JINJA_ENVIRONMENT.get_template('pet6.html')
        elif ('7' in self.request.path ):
            number = '7'
            template = JINJA_ENVIRONMENT.get_template('pet7.html')
        elif ('8' in self.request.path ):
            number = '8'
            template = JINJA_ENVIRONMENT.get_template('pet8.html')
        elif ('9' in self.request.path ):
            number = '9'
            template = JINJA_ENVIRONMENT.get_template('pet9.html')
        else:
            self.response.write('<h1>FILE NOT FOUND</h1>')
            self.response.write('<h2>Try a different URL</h2>')
        
        template_vars = {
            'title': title,
            'name':'browse',
            'bodyid':"browsePage",
            'map':"use",
            'number':number
        }
        self.response.write(template.render(template_vars))

class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>FILE NOT FOUND</h1>')
        self.response.write('<h2>Try a different URL</h2>')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/browse.html', browseHandler),
    ('/howitworks.html', processHandler),
    ('/contactus.html', contactusHandler),
    ('/pet.*', petHandler),
    ('/.*', MainHandler)
], debug=True)


