#!/usr/bin/env python
# coding: UTF-8
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
        self.response.write('''<!DOCTYPE html>
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
<div style="text-align:center">''')
        if (helicoptertime-chinatime).days > 0: #leftdays to zhisheng
            self.response.write('''<span class="l">距离直升考还有</span><span class="rxxl">''' + str((helicoptertime-chinatime).days) + '''</span><span class="l">天</span><span class="rxxl">''' + str((helicoptertime-chinatime).seconds) + '''</span><span class="l">秒</span>
<br>''')
        if -1 < ((chinatime-landtime).days < 0 | -1 < (pastdays).days) < 0 :
            self.response.write('''<span class="rxxl">祝大家取得好成绩！</span>
<br>''')
        if (landtime-chinatime).days > 0: #leftdays to landtime
            self.response.write('''<span class="l">距离直升考结束还有</span><span class="rxxl">''' + str((landtime-chinatime).days) + '''</span><span class="l">天</span><span class="rxxl">''' + str((landtime-chinatime).seconds) + '''</span><span class="l">秒</span>
<br>''')
        if (leftdays).days > 0:
            self.response.write('''<span class="l">距离中考还有</span><span class="rxxl">''' + str((leftdays).days) + '''</span><span class="l">天</span><span class="rxxl">''' + str((leftdays).seconds) + '''</span><span class="l">秒</span>
<br>''')
        if (reborning).days > 0:
            self.response.write('''<span class="l">距离中考结束还有</span><span class="rxxl">''' + str((reborning).days) + '''</span><span class="l">天</span><span class="rxxl">''' + str((reborning).seconds) + '''</span><span class="l">秒</span>
<br>''')
        if (pastdays).days > 0:
            self.response.write('''<span class="l">中考已经过去了</span><span class="rxxl">''' + str((pastdays).days) + '''</span><span class="l">天</span><span class="rxxl">''' + str((pastdays).seconds) + '''</span><span class="l">秒</span>
<br>''')
        if (chinatime-landtime).days > 0:
            self.response.write('''<span class="l">直升考已经过去了</span><span class="rxxl">''' + str((chinatime-landtime).days) + '''</span><span class="l">天</span><span class="rxxl">''' + str((chinatime-landtime).seconds) + '''</span><span class="l">秒</span>''')
        self.response.write('''<br>
<div style="font-size:xx-small">
<a target="_blank" href="https://github.com/zsdtj/sz2015zkcountdown">源码见此</a>
</div>
</div>
</body>
</html>''')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
