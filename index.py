#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import webapp2
from datetime import datetime, timedelta
class MainPage(webapp2.RequestHandler):
    def get(self):
        DEBUG = 0
        if DEBUG == 0 :
            chinatime = datetime.now() + timedelta(hours=+8)
        else:
            chinatime = datetime(2015,6,21,9,29)
        dietime = datetime(2015,6,20,9)
        reborntime = datetime(2015,6,21,17,30)
        leftdays = dietime-chinatime
        reborning = reborntime-chinatime
        pastdays = chinatime-reborntime
        helicoptertime = datetime(2015,4,25,8,20)
        landtime = datetime(2015,4,26,9,50)
        departuredays = helicoptertime-chinatime
        flying = landtime-chinatime
        landdays = chinatime-landtime
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(
'''<!DOCTYPE html>
<html>
<head>
<meta name=viewport content="width=device-width, initial-scale=1">
<meta charset="UTF-8">
<title>2015深圳中考倒计时</title>
<style type="text/css">
.l{font-size:large}.rxxl{font-size:xx-large;color:#f00}.rl{font-size:large;color:#f00}
</style>
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-16653627-12', 'auto');
ga('send', 'pageview');
</script>
</head>
<body>
<div style="text-align:center">
<h1>2015年深圳实验学校<del style="font-size:xx-small">直升考</del>两部联考和<abbr title="深圳市2015年高中阶段学校招生考试">2015年深圳中考</abbr>的倒计时</h1>
''')
        if departuredays.days >= 0:
            self.response.write(
'''<p class="l">距离直升考开始还有<span class="rxxl">''' + str(departuredays.days) + '''</span>天<span class="rxxl">''' + str((departuredays.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((departuredays.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((departuredays.seconds)%60) + '''</span>秒</p>
''')
        if ((-2 <= landdays.days <= -1) and (-2 <= departuredays.days <= -1)) or ((-2 <= pastdays.days <= -1) and (0 <= reborning.days <= 1)) :
            self.response.write(
'''<p class="rxxl">祝大家取得好成绩！</p>
''')
        if flying.days >= 0:
            self.response.write('''<p class="l">距离直升考结束还有<span class="rxxl">''' + str(flying.days) + '''</span>天<span class="rxxl">''' + str((flying.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((flying.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((flying.seconds)%60) + '''</span>秒</p>
''')
        if leftdays.days >= 0:
            self.response.write(
'''<p class="l">距离中考开始还有<span class="rxxl">''' + str(leftdays.days) + '''</span>天<span class="rxxl">''' + str((leftdays.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((leftdays.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((leftdays.seconds)%60) + '''</span>秒</p>
''')
        if reborning.days >= 0:
            self.response.write(
'''<p class="l">距离中考结束还有<span class="rxxl">''' + str((reborning).days) + '''</span>天<span class="rxxl">''' + str((reborning.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((reborning.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((reborning.seconds)%60) + '''</span>秒</p>
''')
        if pastdays.days >= 0:
            self.response.write(
'''<p class="l">中考已经过去了<span class="rxxl">''' + str((pastdays).days) + '''</span>天<span class="rxxl">''' + str((pastdays.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((pastdays.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((pastdays.seconds)%60) + '''</span>秒</p>
''')
        if landdays.days >= 0:
            self.response.write(
'''<p class="l">直升考已经过去了<span class="rxxl">''' + str(landdays.days) + '''</span>天<span class="rxxl">''' + str((landdays.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((landdays.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((landdays.seconds)%60) + '''</span>秒</p>
''')
        self.response.write(
'''<div style="font-size:xx-small">
<a target="_blank" href="https://github.com/zsdtj/sz2015zkcountdown">源码见此</a>
</div>
''')
        if DEBUG == 1 :
            self.response.write(
'''<p>departuredays.days: ''' + str(departuredays.days) + '''</p>
<p>landdays.days: ''' + str(landdays.days) + '''</p>
<p>pastdays.days: ''' + str(pastdays.days) + '''</p>
<p>flying.days: ''' + str(flying.days) + '''</p>
<p>leftdays.days: ''' + str(leftdays.days) + '''</p>
<p>reborning.days: ''' + str(reborning.days) + '''</p>
<p>pastdays.days: ''' + str(pastdays.days) + '''</p>
<p>landdays.days: ''' + str(landdays.days) + '''</p>
''')
        self.response.write(
'''</div>
</body>
</html>''')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
