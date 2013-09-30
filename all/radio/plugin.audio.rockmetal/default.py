

import urllib,urllib2,re,xbmcplugin,xbmcgui,httplib,htmllib,xbmc

PLUGIN              ='plugin.audio.rockmetal'
VERSION             ='0.1'
USER_AGENT          ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

pl=xbmc.PlayList(1)
pl.clear()

listitem = xbmcgui.ListItem('Rock Antenne Metal',
thumbnailImage='special://home/addons/plugin.audio.rockmetal/icon.png')
url = 'http://mp3channels.webradio.rockantenne.de/heavy-metal.aac'

xbmc.PlayList(1).add(url, listitem)

xbmc.Player().play(pl)

xbmc.executebuiltin('XBMC.ActivateWindow(Music,MusicAdd-ons)')
xbmc.executebuiltin('XBMC.ActivateWindow(0)')


#url = 'http://mp3channels.webradio.rockantenne.de/heavy-metal.aac'