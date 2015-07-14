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
        debug = 0
        if debug == 0:
            chinatime = datetime.now() + timedelta(hours=+8)
        else:
            chinatime = datetime(2015, 5, 16, 1, 29)
        dietime = datetime(2015, 6, 20, 9)
        reborntime = datetime(2015, 6, 21, 17, 30)
        helicoptertime = datetime(2015, 4, 25, 8, 20)
        landtime = datetime(2015, 4, 26, 9, 50)
        bustime = datetime(2015, 5, 10, 9, 15)  # Bus of Class 10 depart time
        returntime = datetime(2015, 5, 10, 12, 20)
        # Approximate time. I forgot to log the time we got on the bus at Hongling
        listentime = datetime(2015, 5, 16, 8, 30)  # The First Test start time
        throwtime = datetime(2015, 5, 16, 17, 45)  # The Last Test end time. Guessed
        # It started at 17:30
        # The test finished approximately 12min after it started.
        # But I was allowed to exit 15min after it started.
        # Actually, this test lasted for two days.
        # But my school finished it the first day,
        # and I don't know the schedule for the second day.
        scoretime = datetime(2015, 7, 8, 12, 0)
        # Shenzhen Enrolment and Examination Office began to send SMS at about 11:00.
        # The page is open at 11:45? Or 11:40?
        # No matter how, I failed it.
        firstlinetime = datetime(2015, 7, 14, 11, 0)
        # http://www.51a.gov.cn/show.asp?id=4838
        # Keep for reference: "special ability" student list:
        # http://www.51a.gov.cn/show.asp?id=4836

        template_values = {
            'debug': debug,
            'to_departure': helicoptertime-chinatime,
            'flying': landtime-chinatime,
            'have_land': chinatime-landtime,
            'to_bus': bustime-chinatime,
            'running': returntime-chinatime,
            'have_return': chinatime-returntime,
            'to_listen': listentime-chinatime,
            'listening': throwtime-chinatime,
            'have_spoken': chinatime-throwtime,
            'leftdays': dietime-chinatime,
            'reborning': reborntime-chinatime,
            'pastdays': chinatime-reborntime,
            'to_score': scoretime-chinatime,
            'scored': chinatime-scoretime,
            'to_firstline': firstlinetime-chinatime,
            'firstlined': chinatime-firstlinetime
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

# This "application", is based on a badly written one I wrote in 2012
# (Primary 6). After using the jinja2 template engine, I made tons of ugly
# ifes to make words show up correctly.
# I got the ever worst score since my graduation of primary. But, it's the most
# important one. My junior high life, just ended, in such.
# All have gone, let them go.
