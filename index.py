#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from datetime import datetime, timedelta
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    trim_blocks=True
    )


class MainPage(webapp2.RequestHandler):
    def head(self):
        self.get

    def get(self):
        DEBUG = 0
        if DEBUG == 0:
            chinatime = datetime.now() + timedelta(hours=+8)
        else:
            chinatime = datetime(2015, 5, 10, 9, 29)
        dietime = datetime(2015, 6, 20, 9)
        reborntime = datetime(2015, 6, 21, 17, 30)
        helicoptertime = datetime(2015, 4, 25, 8, 20)
        landtime = datetime(2015, 4, 26, 9, 50)
        bustime = datetime(2015, 5, 10, 9, 15)  # Bus of Class 10 depart time
        returntime = datetime(2015, 5, 10, 12, 20)  # Approximate time. I forgot to log the time we got on the bus at Hongling

        template_values = {
            'DEBUG': DEBUG,
            'leftdays': dietime-chinatime,
            'reborning': reborntime-chinatime,
            'pastdays': chinatime-reborntime,
            'to_departure': helicoptertime-chinatime,
            'flying': landtime-chinatime,
            'have_land': chinatime-landtime,
            'to_bus': bustime-chinatime,
            'running': returntime-chinatime,
            'have_return': chinatime-returntime
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
