import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,datetime
clogo = "http://epgstatic.sky.com/epgdata/1.0/newchanlogos/500/500/skychb"
whatson = "http://epgservices.sky.com/5.1.1/api/2.0/channel/json/"
whatsonimage = "http://epgstatic.sky.com/epgdata/1.0/paimage/121/0/"
AddonID = 'plugin.video.SGUIDE'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")
HOME       =  xbmc.translatePath('special://home/addons/%s/channels.txt'%(AddonID))
SPORTSA =  ('http://cdn.phoenix.intergi.com/21772/videos/')
SPORTSB = ('/video-sd.mp4?hosting_id=21772')
date= datetime.datetime.today().strftime('%Y%m%d%H%M')
date5= datetime.datetime.today().strftime('%Y-%m-%d')
date3= datetime.datetime.today().strftime('%Y%m')
date4= datetime.datetime.today().strftime('%d')
date2= datetime.datetime.today().strftime('%Y-%m-%d')
dateshort= datetime.datetime.today().strftime('%Y')
time= datetime.datetime.today().strftime('%H%M')
time2= datetime.datetime.today().strftime('%H:%M')
def CATEGORIES():
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        addDir('SKY','http://epgservices.sky.com/tvlistings-proxy/TVListingsProxy/init.json',4,'')
        addDir('FILMON','http://thaisatellite.tv/ftv/guide_filmon.xmltv',13,'')
        addDir('Catch Up Sports','http://www.fullmatchesandshows.com',10,'http://i1.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2015/01/Premier-League-World.png?resize=700%2C500')
        addDir('Catch Up Movies','http://tv.pubfilmhd.com',80,'http://i1.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2015/01/Premier-League-World.png?resize=700%2C500')
        addDir('GERMANY','http://m.tvtv.de/api/v1/channel_groups.json',15,'')
        addDir('FRANCE','http://www.skysiertv.com/stv/index2.php',18,'')
        addDir('VIRGIN','http://www.tvguide.co.uk/mobile/?systemid=25',20,'')
        addDir('SKY2','http://www.tvguide.co.uk/mobile/?systemid=5',20,'')
        addDir('BT','http://www.tvguide.co.uk/mobile/?systemid=22',20,'https://img01.bt.co.uk/s/assets/170815/tve/img/BT-Logo.png')
        addDir('Radio Times','http://www.radiotimes.com/rt-service/schedule/get?startdate=30-08-2015%2016:00:00&hours=3&totalWidthUnits=858&channels=94,105,26,132,248,197,2685,11820,288,2050,1061,180,2212,45,47,11741,185,1859,1961,40,11680,1461,5076,1201,922,292,158,1959,2056,11314,1994,2179,11740,2586,2178,2177,1963,1882,11595,5097,11771,134,2189,2008,2062,11708,2603,5074,11816,2134,2195,2139,11450,2185,249,2210,260,5093,258,2204,257,2206,2208,2168,253,160,271,2476,2059,2058,300,262,264,265,2200,11693,2700,2174,123,1876,11150,11791,11568,2142,2175,2176,11774,256,48,49,147,213,182,1601,10008,2668,801,2165,156,482,483,1981',60,'https://img01.bt.co.uk/s/assets/170815/tve/img/BT-Logo.png')
        addDir('BT TEST','https://voila.metabroadcast.com/1.0/schedules/?annotations=broadcasts,locations,description&apiKey=public:64a03c33f9a64c2b80b6f58cd218e5c8&from=now&count=10&id=hkwh',50,'https://img01.bt.co.uk/s/assets/170815/tve/img/BT-Logo.png')
        addDir('NETHERLANDS','https://www.ziggo.tv/tv-gids',21,'')
        addDir('ITALY','http://www.tvtoday.de/programm/standard/',22,'')
        addDir('IPTV','http://i-ptv.blogspot.co.uk',29,'')
        addDir('RUSSIA','https://tv.mail.ru/go-mobile/',31,'')
        addDir('POLAND','http://tv.wp.pl/kanaly-lista.html',31,'')
        addDir('INDIA [COLOR yellow]Requested[/COLOR]','http://tv.burrp.com/channels.html',40,'')
def Fixture(url):
        addDir('[B]See Fixtures Week 1[/B]','1',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 2[/B]','2',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 3[/B]','3',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 4[/B]','4',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 5[/B]','5',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 6[/B]','6',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 7[/B]','7',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 8[/B]','8',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 9[/B]','9',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 10[/B]','10',25,'%s/CTH_1.png'%(addonDir))
        addDir('[B]See Fixtures Week 11[/B]','11',25,'%s/CTH_1.png'%(addonDir))
def two_e(str):
  count = 0
  for ch in str:  ## this loops over each char in the string
    if ch == 'e':
      count = count + 1

  if count == 100:
    return True
  else:
    return False
  ## this last if/else can be written simply as "return (count == 2)"
def FOOTBALLCATS(url):
        addDir('League Table','http://www.msn.com/en-gb/sport/football/premier-league/table',32,'')
        addDir('[COLOR yellow]Fixtures[/COLOR]','3',24,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2015/08/VIDEO-Dynamo-Dresden-vs-Bayern-Munich-Highlights.png?resize=700%2C500')
        addDir('[COLOR yellow]View League Tables[/COLOR]','%s/matches'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2015/08/VIDEO-Dynamo-Dresden-vs-Bayern-Munich-Highlights.png?resize=700%2C500')
        addDir('[COLOR yellow]Up And Comming Matches[/COLOR]','%s/matches'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2015/08/VIDEO-Dynamo-Dresden-vs-Bayern-Munich-Highlights.png?resize=700%2C500')
        addDir('Latest','%s/matches'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2015/08/VIDEO-Dynamo-Dresden-vs-Bayern-Munich-Highlights.png?resize=700%2C500')
        addDir('Shows','%s/category/show/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('Premier League','%s/premier-league-2/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('Champions League','%s/category/champions-league/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('Womens World Cup','%s/category/full-match/women-world-cup/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('Germany','%s/category/germany-2/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('Copa America','%s/copa-america-2015/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('La Liga','%s/category/spain/la-liga/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('Serie A','%s/category/italy/serie-a/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
        addDir('Concacaf','%s/category/concacaf/'%(url),11,'http://i0.wp.com/www.fullmatchesandshows.com/wp-content/uploads/2014/11/MOTD-2.png?resize=700%2C500')
def FULLMATCHES(url):
        link = OPEN_URL(url)
        match=re.compile('<div class="td-module-thumb"><a href="(.+?)" rel="bookmark" title="(.+?)"><img width="" height="" itemprop="image" class="entry-thumb" src="(.+?)" alt=".+?" title=".+?"/></a></div>').findall(link)
        for url,event,image in match:
            addDir2('[B]%s[/I]'%(event).replace('&amp;', '&').replace('&#8211;', '[/B]-[I]').replace('|', '[/B]-[I]'),'%s'%(url),12,'%s'%(image).replace('265%2C198','700%2C500'))
def NL(url):
        link = OPEN_URL(url)
        match=re.compile('"name":"(.+?)",.+?image":"(.+?)".+?description":"(.+?)"').findall(link)
        for name,icon,de in match:
            addDir('[COLOR yellow]%s[/COLOR] - %s'%(name,de),'',19,'https://static.ziggo-apps.nl/images/channels/%s'%(icon))
def BTTEST(url):
        link = OPEN_URL(url)
        match=re.compile('{"id":".+?","type":"(.+?)","title":"(.+?)","description":"(.+?)","image":"(.+?)","specialization":".+?","broadcasts":\[{"transmission_time":"%sT(.+?)","transmission_end_time":".+?"'%(date2)).findall(link)
        match2=re.compile('{"channel":{"title":"(.+?)","image":"(.+?)"').findall(link)
        for name,image in match2:
            addDir('CHANNEL [%s]'%name,'',50,'%s'%image)
            addDir('--------------------------------------','',50,'')
        for type,name,description,image,start in match:
            addDir5('[COLOR yellow]%s[/COLOR] - %s [%s]'%(start.replace('%sT'%(date2),'').replace('Z',''),name,type),'%s'%(id),19,'%s'%(image),'',description)
def GERMANY2(url):
        link = OPEN_URL(url)
        match=re.compile('<span class="zc-st-c"><a class="zc-st-a" href="(.+?)">(.+?)</a></span>').findall(link)
        for url,name in match:
            addDir('[COLOR yellow]%s[/COLOR] - '%(name),'%s'%(url),19,'https://static.ziggo-apps.nl/images/channels/%s')
def Radiotime(url):
        addDir5('[COLOR yellow]Press I For Mor Info[/COLOR]','',61,'','','')
        link = OPEN_URL(url)
        match=re.compile('{"DisplayName":"(.+?)",".+?"Image":"(.+?)","Description":"(.+?)",".+?","StartTime":".+?","FilmStarRating".+?"Title":"(.+?)"').findall(link)
        for channel,image,description,name in match:
            addDir5('%s - [Now: %s]'%(channel,name),'',61,image,'',description)
def Radiotime2(name):
        link = OPEN_URL(url)
        match=re.compile('"DisplayName":"(.+?)"').findall(link)
        for name in match:
            addDir('%s - '%(name),'',61,'')
def ITALY(url):
        link = OPEN_URL(url)
        match=re.compile('href=".+?">(.+?)</a>').findall(link)
        for name in match:
            addDir('%s'%(name),'%s'%(url),19,'%s'%(name))
def TB2(url):
        link = OPEN_URL(url)
        match=re.compile('<tr class="rowlink" data-link=".+?"><td class="index hide1 rankvalue">(.+?)</td><td class="teamlogo"><img alt="(.+?)" height="30" src="(.+?)" width="30" /></td><td class="teamname"><a href=".+?">.+?</a></td><td class="teamtla"><a href="(.+?)">(.+?)</a></td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td class="hide12">(.+?)</td><td class="hide12">(.+?)</td><td class="hide12">(.+?)</td><td class="points">(.+?)</td>').findall(link)
        for rank,name,logo,url,shortname,played,win,draw,lose,GF,GA,GD,PTS in match:
            addDir('%s%s%s%s%s%s%s%s%s%s%s%s%s'%(rank,name,logo,url,shortname,played,win,draw,lose,GF,GA,GD,PTS),url,19,logo)
def TABLE():
        url = 'http://m.premierleague.com/en-gb/league-table.html'
        link = OPEN_URL(url)
        match=re.compile('/en-gb/clubs/club-profile.html/(.+?)"').findall(link)
        for name in match:
                addDir('[COLOR white]%s [/COLOR]'%(name),'','','')
def TB(url):
        addDir('[R]       [TEAM]                         [P]    [W]    [D]    [L]    [GF]    [GA]   [GD]   [PTS]','',5,'')
        link = OPEN_URL(url)
        match=re.compile('data-link=".+?football/(.+?)/.+?"><td class="index.+?">(.+?)</td><td class="teamlogo"><img alt=".+?" src="\/(.+?)"').findall(link)
        for name,rank,image in match:
                addDir('[COLOR white][B]%s)[/B][/COLOR] %s '%(rank,name),name,5,'http:/%s'%image)
def FIXTURES(url):
        num = url
        url = 'http://m.premierleague.com/pa-services/api/football/mobile/competition/fandr/api/gameweek/%s.json'%(num)
        link = OPEN_URL(url)
        match=re.compile('"awayTeamScore":(.+?),"homeTeamScore":(.+?),"liveMatch":(.+?),".+?status":"(.+?)".+?"koTime":"(.+?)",".+?displayShortDate":"(.+?)","awayTeamClubURL":"(.+?)","homeTeamClubURL":"(.+?)"').findall(link)
        for s1,s2,live,name,l1,l2,l3,l4 in match:
            if name == "fulltime":
                if s1 > s2:
                    addDir('[COLOR red]%s [/COLOR][COLOR gold]%s [B]%s[/B][/COLOR][COLOR red]   Vs      [B]%s[/B] %s   %s[/COLOR]'%(name.replace('fulltime','FT: '),l3,s1,s2,l4,live.replace('false',' ')),'%s %s'%(l1,l2),'','')
                if s1 < s2:
                    addDir('[COLOR red]%s %s [B]%s[/B]   Vs      [B]%s[/B] [/COLOR][COLOR gold]%s[/COLOR]  [COLOR red]%s[/COLOR]'%(name.replace('fulltime','FT: '),l3,s1,s2,l4,live.replace('false',' ')),'%s %s'%(l1,l2),'','')
                if s1 == s2:
                    addDir('[COLOR blue]%s %s [B]%s[/B]   Vs      [B]%s[/B] %s  %s[/COLOR]'%(name.replace('fulltime','FT: '),l3,s1,s2,l4,live.replace('false',' ')),'%s %s'%(l1,l2),'','')
            else:
                if s1 == "null":
                    addDir('[COLOR red]%s[/COLOR] %s %s %s %s VS %s %s  '%(name.replace('FIXTURE',' '),l1,l2,l3,s1.replace('null',' '),s2.replace('null',' '),l4),'%s'%(live),'','')
                else:
                    if l2 == dateshort:
                        addDir('[COLOR red]%s[/COLOR] %s %s %s %s VS %s %s    %s'%(name.replace('FIXTURE',' '),l1,l2.replace('%s'%(dateshort),''),l3,s1,s2,l4,live.replace('false',' ').replace('true','[COLOR green]LIVE![/COLOR]')),'','','')
                    else:
                        addDir('[COLOR red]%s[/COLOR] %s %s %s %s VS %s %s    %s'%(l2,name.replace('FIXTURE',' '),l1,l3,s1,s2,l4,live.replace('false',' ').replace('true','[COLOR green]LIVE![/COLOR]')),'','','')
def FRENCH(url):
        link = OPEN_URL(url)
        match=re.compile('<A HREF="index2\.php\?chaine=(.+?)" TARGET="2"><IMG SRC="(.+?)" ALT=".(.+?) -').findall(link)
        for url,icon,name in match:
            addDir('%s'%(name.replace('<b>','').replace('</b>','')),'http://www.skysiertv.com/stv/chaines/%s/%s/%s.html'%(url,date3,date4),19,'http://www.skysiertv.com/stv/%s'%(icon))
def FRENCH2(url):
        link = OPEN_URL(url)
        match=re.compile('<p align="JUSTIFY">(\d\d\.\d\d)</b></font>\n<td width="92%" valign="TOP"><table border="0" width="100%"><tr><td width="100%">\n<b><font face="Arial" size="3"><p align="JUSTIFY">(.+?)<').findall(link)
        for name,title in match:
            addDir('[%s] - %s'%(name,title),'',12,'')
def VIRGIN(url):
        link = OPEN_URL(url)
        match=re.compile('img-channel-logo" width="50" src="http://my.tvguide.co.uk/channel_logos/60x35/(.+?).png" alt="(.+?) TV Listings"+|<div class="div-time">(.+?)</div>.+?\n.+?<div class="div-title">(.+?)<').findall(link)
        for icon,channel,programme,title in match:
            addDir('%s [COLOR yellow]%s[/COLOR] - %s'%(channel,programme,title),'http://www.tvguide.co.uk/mobile/channellisting.asp?ch=%s'%(icon),26,'http://my.tvguide.co.uk/channel_logos/60x35/%s.png'%(icon))
def VIRGIN2(url):
        link = OPEN_URL(url)
        match=re.compile('<a class="prog-link" href="(.+?)" id=".+?" >.+?\n.+?\n.+?time">(.+?)</div>.+?\n.+?\n(.+?)</div>.+?\n.+?\n.+?\n(.+?)\n').findall(link)
        for programme,time,name,de in match:
            addDir('[%s] - [COLOR yellow]%s[/COLOR] - %s'%(time,name,de),'%s'%(programme),26,'http://cdn.tvguide.co.uk/HighlightImages/Large/%s.jpg'%(name.replace(' ', '_').replace('!', '')))
def PLAYVIDEOFULLMATCHES(url):
    link = OPEN_URL(url)
    match=re.compile('//config.playwire.com/21772/videos/v2/(.+?)/zeus.json').findall(link)
    for url in match:
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Opening ','Opening %s '%(channelno))
        dp.update(10)
        play.play('%s%s%s'%(SPORTSA,url,SPORTSB))
        dp.update(100)
        dp.close()
		
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
def ALLCHANNELS(url):
        link = OPEN_URL(url)
        match=re.compile('{"channelno":"(.+?)","epggenre":".+?","title":"(.+?)","channeltype":".+?","channelid":"(.+?)","genre":".+?"}').findall(link)
        for channelno,title,channelid in match:
            addDir3('[COLOR yellow]%s[/COLOR] - %s'%(channelno,title),'%s%s/now/nnl/4'%(whatson,channelid),6,'%s%s.png'%(clogo,channelid),'%s'%(channelno))
def INDIA(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('href="(.+?)" title="(.+?)">\n.+?<img src="(.+?)"').findall(link)
        for url,title,image in match:
            addDir(title,url,41,image)
def INDIA2(url):
        link = OPEN_URL(url)
        match=re.compile('(\d\d:\d\d)<sup class="ap">(.+?)</sup>\n.+?</b>\n.+?</td>\n.+?<td class="resultThumb">\n.+?\n.+?<a href="(.+?)" title="(.+?)">\n.+?\n.+?<img src="(.+?)"/>').findall(link)
        for time3,time4,url,name,image in match:
            addDir('[COLOR yellow]%s%s[/COLOR]  - %s   '%(time3,time4,name),url,41,image)
def FILMON(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('<display-name lang="en">(.+?)</display-name>.+?\n.+?<icon src="(.+?)" />').findall(link)
        match2=re.compile('<display-name lang="en">(.+?)</display-name>').findall(link)
        for name,icon in match:
            addDir('%s'%(name),'http://thaisatellite.tv/ftv/guide_filmon.xmltv',14,'%s'%(icon))
        for name in match2:
            addDir('%s'%(name),'http://thaisatellite.tv/ftv/guide_filmon.xmltv',14,'')
def FILMON2(url,name):
        link = OPEN_URL(url)
        match=re.compile('<programme start="(.+?)\s\+.+?" stop="(.+?)\s\+.+?" channel="%s">.+?\n.+?<title lang="en">(.+?)</title>'%(name)).findall(link)
        for start,stop,title in match:
            if start > '%s'%date:
                addDir3('[COLOR yellow]%s[/COLOR] - %s - %s '%(title,start,stop),'',6,'','')
            if start == '%s'%time:
                addDir3('[COLOR green]%s[/COLOR] - %s - %s '%(title,start,stop),'',6,'','')
            else:
                addDir3('[COLOR red]%s[/COLOR] - %s - %s '%(title,start,stop),'',6,'','')
def GERMANYCAT(url):
        link = OPEN_URL(url)
        match=re.compile('"id":"(.+?)","name":"(.+?)"').findall(link)
        for id,name in match:
            addDir('%s'%(name),'http://m.tvtv.de/api/v1/channels/%s.json?date=%s&range=00:00-24:00'%(id,date2),16,'http://m.tvtv.de/ng-assets/channel_logos/%s_w.png'%(id))
def GERMANY(url):
        link = OPEN_URL(url)
        match=re.compile('title":"(.+?)","cover_image_uri":(.+?),.+?"time":"(.+?)".+?play_time":"(.+?)"').findall(link)
        for name,icon,start,playtime in match:
            start = start.replace(' Uhr','')
            if start > time2:
                addDir('%s %s'%(playtime,name),'%s'%(start.replace(' Uhr','')),14,'%s'%(icon.replace('"', '')))
            if start < time2:
                addDir('[COLOR red]%s %s[/COLOR]'%(playtime,name),'%s'%(start.replace(' Uhr','')),14,'%s'%(icon.replace('"', '')))

def GERMANY2(url):
        link = OPEN_URL(url)
        match=re.compile('<tr><td class="uhrzeit">(.+?)<br />.+?</td><td class="sendung"><div><a href="(.+?)".+?false;" title=".+?">(.+?)<.+uhrzeit">(.+?)<br /><img src="(.+?)"').findall(link)
        for start,url,name,end,icon in match:
                addDir('[%s]- [%s] - [B]%s[/B] -'%(start,end,name),'%s'%(url),6,'http://www.tvtv.de/%s'%(icon))
def GERMANY3(url):
        link = OPEN_URL(url)
        match=re.compile('<tr><td class="uhrzeit">(.+?)<br />.+?</td><td class="sendung"><div><a href="(.+?)".+?false;" title=".+?">(.+?)<.+uhrzeit">(.+?)<br /><img src="(.+?)"').findall(link)
        for start,url,name,end,icon in match:
                addDir('[%s]- [%s] - [B]%s[/B] -'%(start,end,name),'%s'%(url),6,'http://www.tvtv.de/%s'%(icon))
def GENRESELECT(url,iconimage):
        link = OPEN_URL(url)
        match=re.compile('{"channelno":"(.+?)","epggenre":".+?","title":"(.+?)","channeltype":".+?","channelid":"(.+?)","genre":"%s"}'%(iconimage)).findall(link)
        for channelno,title,channelid,genre in match:
            addDir('[COLOR yellow]%s[/COLOR] - %s  %s'%(channelno,title,genre),'%s%s/now/nnl/4'%(whatson,channelid),6,'%s%s.png'%(clogo,channelid))
def MOVIES(url):
        link = OPEN_URL(url)
        match=re.compile("<li><a href='/search/label/.+?' title='.+?'><span>(.+?)</span></a></li>").findall(link)
        for name in match:
            addDir('%s'%(name),'http://tv.pubfilmhd.com/feeds/posts/default/-/%s?alt=json-in-script&callback=numberOfPosts'%(name),81,'')
def MOVIES2(url):
        link = OPEN_URL(url)
        match=re.compile('"rel":"alternate","type":"text/html","href":"(.+?)","title":"(.+?)"').findall(link)
        for url,name in match:
            addDir('%s'%(name),'%s'%(url.replace('\/','/')),82,'')
def MOVIES3(url):
        link = OPEN_URL(url)
        match=re.compile('<iframe allowfullscreen="" frameborder="1" width="950" height="520" src="(.+?)" frameborder="0" style="background-color: black;">').findall(link)
        for url in match:
            addDir('Play','%s'%(url),83,'')
def MOVIES4(url):
        link = OPEN_URL(url)
        match=re.compile('<iframe allowfullscreen="" frameborder="1" width="950" height="520" src="(.+?)" frameborder="0" style="background-color: black;">').findall(link)
        for url in match:
            addDir('Play','%s'%(url),84,'')
def MOVIES5(url):
        link = OPEN_URL(url)
        match=re.compile('file: "(.+?)", label: "(.+?)"').findall(link)
        for url,name in match:
            addDir(name,'%s'%(url),84,'')
def GENRES(url):
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE)
        link = OPEN_URL(url)
        match=re.compile('{"genreid":"(.+?)","name":"(.+?)"}').findall(link)
        for genreid,genrename in match:
            addDir('%s'%(genrename),'http://epgservices.sky.com/tvlistings-proxy/TVListingsProxy/init.json',7,'%s'%(genreid))
def IPTV(url):
        link = OPEN_URL(url)
        match=re.compile('#EXTINF:.+?,(.+?)\n(.+?)\n').findall(link)
        for name,url in match:
            addDir2(name,url,30,'')
def RUSSIA(url):
        link = OPEN_URL(url)
        match=re.compile('<a href="/name,(.+?),stid,.+?,program\.html" data-stid=".+?">.+?</a></li>').findall(link)
        for name in match:
            addDir2('%s'%(name),'https://tv.mail.ru/london/%s'%(name),30,'')
def RUSSIA2(url):
        link = OPEN_URL(url)
        match=re.compile('<option value="\d+">(.+?)</option>').findall(link)
        for name in match:
            addDir2('%s'%(name),'https://tv.mail.ru/london/%s'%(name),30,'')
def EPG(url,channelno):
        link = OPEN_URL(url)
        match=re.compile('.+?"d":"(.+?)","img":"(.+?)".+?"t":"(.+?)"').findall(link)
        match2=re.compile('":{"(.+?)"').findall(link)
        for channelid in match2:
            addDir4('[B]Play [/B]','%s'%(channelno),8,'%s'%(channelid),'%s'%(channelno))
            addLink('------------------------------------------','','','')
        for description,icon,name in match:
            addLink('[COLOR yellow][B]%s[/B][/COLOR] - [I][B]%s[/B][/I]'%(name,description),'','%s%s'%(whatsonimage,icon),'%s'%(description))
def EPG3(url,channelno):
        url=('http://live.tvgenius.net/accessible/text/index.html?colour=one&tvgRegion=London&tvgFlagFilter=&tvgBegin=0&tvgChannel=BDS%7C%7C')
        link = OPEN_URL(url)
        match=re.compile('<a\sclass="rbm_title"\shref="(.+?)">(.+?)</a><p\sclass="rbm_timing">(.+?)</p><p\sclass="rbm_description">(.+?)</p>').findall(link)
        for dlink,time,description in match:
            addLink('[COLOR yellow][B]%s[/B][/COLOR] - [I][B]%s[/B][/I]'%(name,description),'','%s%s'%(whatsonimage,icon),'%s'%(description))
def EPG2(url,channelno):
        link = OPEN_URL(url)
        match=re.compile('.+?"d":"(.+?)","img":".+?".+?"t":"(.+?)"').findall(link)
        names = ['[COLOR yellow]Play Channel[/COLOR]',]
        links = ['PLAYVIDEO(%s?&url=%s&channelno=%s)'% (sys.argv[0],url,channelno),]
        for name,link in match:
            names.append(name)
            links.append(link)
            dialog = xbmcgui.Dialog()
        index = dialog.select('Choose a video source', names)

def PLAYVIDEO(url,channelno):
    link = OPEN_URL('file:///%s/channels.txt'%(addonDir))
    match = re.findall('%s":".+?":"(.+?)"'%(channelno), link)
    for url in match:
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Opening ','Opening %s '%(channelno))
        dp.update(10)
        play.play(url)
        dp.update(100)
        dp.close()
def PLAYVIDEO2(url,name):
        play=xbmc.Player(GetPlayerCore())
        dp = xbmcgui.DialogProgress()
        dp.create('Opening ','Opening %s '%(name))
        dp.update(10)
        play.play(url)
        dp.update(100)
        dp.close()
def DownloaderClass(url,dest):
    dp = xbmcgui.DialogProgress()
    dp.create("Iptv Manager","Downloading")
    urllib.urlretrieve(url,dest,lambda nb, bs, fs, url=url: _pbhook(nb,bs,fs,url,dp))
def _pbhook(numblocks, blocksize, filesize, url=None,dp=None):
    try:
        percent = min((numblocks*blocksize*100)/filesize, 100)
        print percent
        dp.update(percent)
    except:
        percent = 100
        dp.update(percent)
    if dp.iscanceled(): 
        print "DOWNLOAD CANCELLED" # need to get this part working
        dp.close()
def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
			
def RESOLVE(url): 
    import urlresolver
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    play=xbmc.Player(GetPlayerCore())
    url=urlresolver.HostedMediaFile(url).resolve() 
    try: play.play(url)
    except: pass
    try: ADDON.resolve_url(url) 
    except: pass 
def RESOLVE2(url): 
    play=xbmc.Player(GetPlayerCore())
    dp = xbmcgui.DialogProgress()
    dp.create('Featching Your Video','Opening %s Ready'%(name))
    dp.update(10)
    play.play(url)
    dp.update(100)
    dp.close()

def VIDEOLINKS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('file: "(.+?)",').findall(link)
        for url in match:
                addLink(name,url,'',"")
        

                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def addLink(name,url,iconimage,plot):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setProperty('IsPlayable','true')
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
        return ok

def addSearch():
	searchStr = ''
	keyboard = xbmc.Keyboard(searchStr, 'Search')
	keyboard.doModal()
	if (keyboard.isConfirmed()==False):
	  return
	searchStr=keyboard.getText()
	if len(searchStr) == 0:
	  return
	else:
	  return searchStr
	  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir3(name,url,mode,iconimage,channelno):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&channelno="+urllib.quote_plus(channelno)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
def addDir4(name,url,mode,iconimage,channelno):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&channelno="+urllib.quote_plus(channelno)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
def addDir5(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty( "Fanart_Image", fanart )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
               
params=get_params()
url=None
name=None
iconimage=None
mode=None
plot=None
channelno=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:
        plot=urllib.unquote_plus(params["plot"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        channelno=urllib.unquote_plus(params["channelno"])
except:
        pass
try:        
        fanart=urllib.unquote_plus(params["fanart"])
except:
        pass
try:        
        description=urllib.unquote_plus(params["description"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Plot: "+str(plot)
print "channelno: "+str(channelno)
print "IconImage: "+str(iconimage)
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        INDEX(url)
        
elif mode==2:
        print ""+url
        addSearch()

elif mode==3:
          MVLOADCAT(url)
elif mode==4:
          ALLCHANNELS(url)
elif mode==5:
          GENRES(url)
elif mode==6:
          EPG(url,channelno)
elif mode==7:
          GENRESELECT(url,iconimage)
elif mode==8:
          PLAYVIDEO(url,channelno)
elif mode==9:
          EPG2(url,channelno)
elif mode==10:
          FOOTBALLCATS(url)
elif mode==11:
          FULLMATCHES(url)
elif mode==12:
          PLAYVIDEOFULLMATCHES(url)
elif mode==13:
          FILMON(url)
elif mode==14:
          FILMON2(url,name)
elif mode==15:
          GERMANYCAT(url)
elif mode==16:
          GERMANY(url)
elif mode==17:
          GERMANY2(url)
elif mode==18:
          FRENCH(url)
elif mode==19:
          FRENCH2(url)
elif mode==20:
          VIRGIN(url)
elif mode==21:
          NL(url)
elif mode==22:
          ITALY(url)
elif mode==23:
          TABLE()
elif mode==24:
          Fixture(url)
elif mode==25:
          FIXTURES(url)
elif mode==26:
          VIRGIN2(url)
elif mode==29:
          IPTV(url)
elif mode==30:
          PLAYVIDEO2(url,name)
elif mode==31:
          RUSSIA(url)
elif mode==32:
          TB(url)
elif mode==40:
          INDIA(url)
elif mode==41:
          INDIA2(url)
elif mode==50:
          BTTEST(url)
elif mode==60:
          Radiotime(url)
elif mode==61:
          Radiotime2(name)
elif mode==80:
          MOVIES(url)
elif mode==81:
          MOVIES2(url)
elif mode==82:
          MOVIES3(url)
elif mode==83:
          MOVIES4(url)
elif mode==84:
          MOVIES5(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
