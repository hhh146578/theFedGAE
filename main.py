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
        number = ''
        if ('/pet1.html' == self.request.path ):
            number = '1'
            template = JINJA_ENVIRONMENT.get_template('pet1.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet2.html' == self.request.path ):
            number = '2'
            template = JINJA_ENVIRONMENT.get_template('pet2.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet3.html' == self.request.path ):
            number = '3'
            template = JINJA_ENVIRONMENT.get_template('pet3.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet4.html' == self.request.path ):
            number = '4'
            template = JINJA_ENVIRONMENT.get_template('pet4.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet5.html' == self.request.path ):
            number = '5'
            template = JINJA_ENVIRONMENT.get_template('pet5.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet6.html' == self.request.path ):
            number = '6'
            template = JINJA_ENVIRONMENT.get_template('pet6.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet7.html' == self.request.path ):
            number = '7'
            template = JINJA_ENVIRONMENT.get_template('pet7.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet8.html' == self.request.path ):
            number = '8'
            template = JINJA_ENVIRONMENT.get_template('pet8.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif ('/pet9.html' == self.request.path ):
            number = '9'
            template = JINJA_ENVIRONMENT.get_template('pet9.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        else:
            title = "Paw Wow - Home"
            template_vars = {
                'title': title,
                'name':'index',
                'bodyid':"index",
                'map':"not"
            }
            template = JINJA_ENVIRONMENT.get_template('index.html')
            self.response.out.write(template.render(template_vars))
            return
    def post(self):
        breed = self.request.get('name').upper()
        title = "Paw Wow - Our Pets"
        number = ''
        if(breed == "LABRADOR RETRIEVER"):
            number = '1'
            template = JINJA_ENVIRONMENT.get_template('pet1.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "WELSH CORGI PEMBROKE" or breed == "WELSH CORGI CARDIGAN"):
            number = '2'
            template = JINJA_ENVIRONMENT.get_template('pet2.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "MIGUELO"):
            number = '3'
            template = JINJA_ENVIRONMENT.get_template('pet3.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "PUG"):
            number = '4'
            template = JINJA_ENVIRONMENT.get_template('pet4.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "GIANT SCHNAUZER" or breed == "SCHNAUZER" or breed == "MINIATURE SCHNAUZER"):
            number = '5'
            template = JINJA_ENVIRONMENT.get_template('pet5.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "DOLMATIAN"):
            number = '6'
            template = JINJA_ENVIRONMENT.get_template('pet6.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "GOLDEN RETRIEVER"):
            number = '7'
            template = JINJA_ENVIRONMENT.get_template('pet7.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "POODLE" or breed == "TOY POODLE"):
            number = '8'
            template = JINJA_ENVIRONMENT.get_template('pet8.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        elif (breed == "SHIH TZU"):
            number = '9'
            template = JINJA_ENVIRONMENT.get_template('pet9.html')
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"use",
                'number':number
            }
            self.response.write(template.render(template_vars))
        else:
            title = "Paw Wow - Browse Our Pets"
            template_vars = {
                'title': title,
                'name':'browse',
                'bodyid':"browsePage",
                'map':"not"
            }
            template = JINJA_ENVIRONMENT.get_template('browse.html')
            self.response.out.write(template.render(template_vars))
            return
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/browse.html', browseHandler),
    ('/howitworks.html', processHandler),
    ('/contactus.html', contactusHandler),
    ('/pet.*', petHandler),
    ('/.*', MainHandler)
], debug=True)
