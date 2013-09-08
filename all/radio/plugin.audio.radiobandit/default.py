

import urllib,urllib2,re,xbmcplugin,xbmcgui,httplib,htmllib,xbmc

PLUGIN              ='plugin.audio.radiobandit'
VERSION             ='0.1'
USER_AGENT          ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

pl=xbmc.PlayList(1)
pl.clear()

listitem = xbmcgui.ListItem('radio_bandit',
thumbnailImage='special://home/addons/plugin.audio.radiobandit/icon.png')
url = 'http://stream-ice.mtgradio.com:8080/stat_bandit'

xbmc.PlayList(1).add(url, listitem)

xbmc.Player().play(pl)

xbmc.executebuiltin('XBMC.ActivateWindow(Music,MusicAdd-ons)')
xbmc.executebuiltin('XBMC.ActivateWindow(0)')


#url = 'http://79.136.100.244:80/banditsthlm?MSWMExt=.asf'