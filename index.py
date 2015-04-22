#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import webapp2
from datetime import datetime, timedelta
class MainPage(webapp2.RequestHandler):
    def get(self):
        chinatime = datetime.now() + timedelta(hours=+8)
        helicoptertime = datetime(2015,4,25,8) #hour is guessed
        landtime = datetime(2015,4,26,12) #hour is guessed
        dietime = datetime(2015,6,20,9)
        reborntime = datetime(2015,6,21,17,30)
        leftdays = dietime-chinatime
        reborning = reborntime-chinatime
        pastdays = chinatime-reborntime
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
        if (helicoptertime-chinatime).days > 0: #leftdays to zhisheng
            self.response.write(
'''<p class="l">距离直升考开始还有<span class="rxxl">''' + str((helicoptertime-chinatime).days) + '''</span>天<span class="rxxl">''' + str(((helicoptertime-chinatime).seconds)//3600) + '''</span>时<span class="rxxl">''' + str((((helicoptertime-chinatime).seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str(((helicoptertime-chinatime).seconds)%60) + '''</span>秒</p>
''')
        if -1 < (chinatime-landtime).days < 0 | -1 < (pastdays).days < 0 :
            self.response.write(
'''<p class="rxxl">祝大家取得好成绩！</p>
''')
        if (landtime-chinatime).days > 0: #leftdays to landtime
            self.response.write('''<p class="l">距离直升考结束还有<span class="rxxl">''' + str((landtime-chinatime).days) + '''</span>天<span class="rxxl">''' + str(((landtime-chinatime).seconds)//3600) + '''</span>时<span class="rxxl">''' + str((((landtime-chinatime).seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str(((landtime-chinatime).seconds)%60) + '''</span>秒</p>
''')
        if leftdays.days > 0:
            self.response.write(
'''<p class="l">距离中考开始还有<span class="rxxl">''' + str(leftdays.days) + '''</span>天<span class="rxxl">''' + str((leftdays.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((leftdays.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((leftdays.seconds)%60) + '''</span>秒</p>
''')
        if reborning.days > 0:
            self.response.write(
'''<p class="l">距离中考结束还有<span class="rxxl">''' + str((reborning).days) + '''</span>天<span class="rxxl">''' + str((reborning.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((reborning.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((reborning.seconds)%60) + '''</span>秒</p>
''')
        if pastdays.days > 0:
            self.response.write(
'''<p class="l">中考已经过去了<span class="rxxl">''' + str((pastdays).days) + '''</span>天<span class="rxxl">''' + str((pastdays.seconds)//3600) + '''</span>时<span class="rxxl">''' + str(((pastdays.seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str((pastdays.seconds)%60) + '''</span>秒</p>
''')
        if (chinatime-landtime).days > 0:
            self.response.write(
'''<p class="l">直升考已经过去了<span class="rxxl">''' + str((chinatime-landtime).days) + '''</span>天<span class="rxxl">''' + str(((chinatime-landtime).seconds)//3600) + '''</span>时<span class="rxxl">''' + str((((chinatime-landtime).seconds)//60)%60) + '''</span>分<span class="rxxl">''' + str(((chinatime-landtime).seconds)%60) + '''</span>秒</p>
''')
        self.response.write(
'''<div style="font-size:xx-small">
<a target="_blank" href="https://github.com/zsdtj/sz2015zkcountdown">源码见此</a>
</div>
</div>
</body>
</html>''')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
