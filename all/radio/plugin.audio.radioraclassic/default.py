

import urllib,urllib2,re,xbmcplugin,xbmcgui,httplib,htmllib,xbmc

PLUGIN              ='plugin.audio.radioraclassic'
VERSION             ='0.1'
USER_AGENT          ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

pl=xbmc.PlayList(1)
pl.clear()

listitem = xbmcgui.ListItem('radio_raclassic',
thumbnailImage='special://home/addons/plugin.audio.radioraclassic/icon.png')
url = 'http://mp3channels.webradio.rockantenne.de/classic-perlen.aac'

xbmc.PlayList(1).add(url, listitem)

xbmc.Player().play(pl)

xbmc.executebuiltin('XBMC.ActivateWindow(Music,MusicAdd-ons)')
xbmc.executebuiltin('XBMC.ActivateWindow(0)')

