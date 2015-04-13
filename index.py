#!/usr/bin/env python
# coding: UTF-8
import webapp2
from datetime import datetime, timedelta
class MainPage(webapp2.RequestHandler):
    def get(self):
        chinatime = datetime.now() + timedelta(hours=+8)
        helicoptertime = datetime(2015,4,25,8) #hour is guessed
        downtime = datetime(2015,4,26,12) #hour is guessed
        dietime = datetime(2015,6,20,9) #date is guessed. Hasn't been published
        reborntime = datetime(2015,6,21,18) #date is guessed. Hasn't been published
        leftdays = (dietime-chinatime).days
        reborning = (reborntime-chinatime).days
        pastdays = (chinatime-reborntime).days
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
            self.response.write('''<span class="l">距离直升考还有</span><span class="rxxl">''' + str((helicoptertime-chinatime).days) + '''</span><span class="l">天</span><br>
<span class="l">距离直升考结束还有</span><span class="rxxl">''' + str((downtime-chinatime).days) + '''</span><span class="l">天</span><br>
<span class="l">距离中考还有</span><span class="rxxl">''' + str(leftdays) + '''</span><span class="l">天</span><br>
<span class="l">距离中考结束还有</span><span class="rxxl">''' + str(reborning) + '''</span><span class="l">天</span>''')
        elif (chinatime-downtime).days < 0: #pastdays to zhisheng
            self.response.write('''<span class="rxxl">祝大家取得好成绩！</span><br>
<span class="l">距离中考还有</span><span class="rxxl">''' + str(leftdays) + '''</span><span class="l">天</span><br>
<span class="l">距离中考结束还有</span><span class="rxxl">''' + str(reborning) + '''</span><span class="l">天</span>''')
        elif leftdays > 0:
            self.response.write('''<span class="l">距离中考还有</span><span class="rxxl">''' + str(leftdays) + '''</span><span class="l">天</span><br>
<span class="l">距离中考结束还有</span><span class="rxxl">''' + str(reborning) + '''</span><span class="l">天</span>
<span class="l">直升考已经过去了</span><span class="rxxl">''' + str((chinatime-downtime).days) + '''</span><span class="l">天</span>''')
        elif pastdays < 0:
            self.response.write('''<span class="rxxl">祝大家取得好成绩！</span><br>
<span class="l">距离中考结束还有</span><span class="rxxl">''' + str(reborning) + '''</span><span class="l">天</span><br>
<span class="l">直升考已经过去了</span><span class="rxxl">''' + str((chinatime-downtime).days) + '''</span><span class="l">天</span>''')
        elif pastdays == 0:
            self.response.write('''<span class="rxxl">考完了！</span><br>
<span class="l">直升考已经过去了</span><span class="rxxl">''' + str((chinatime-downtime).days) + '''</span><span class="l">天</span>''')
        else:
            self.response.write('''<span class="l">中考已经过去了</span><span class="rxxl">''' + str(pastdays) + '''</span><span class="l">天</span><br>
<span class="l">直升考已经过去了</span><span class="rxxl">''' + str((chinatime-downtime).days) + '''</span><span class="l">天</span>''')
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
