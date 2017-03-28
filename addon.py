import xbmc,xbmcgui,xbmcaddon

SKINS = [["White Snow - Default Font", "WhiteSnowDefaultFont"],
         ["White Snow - Custom Font",  "WhiteSnowCustomFont"]]


d = xbmcgui.Dialog()
names = [s[0] for s in SKINS]
skin = d.select("TV Guide Fullscreen - Set Default Skin", names)
if skin > -1:
    tvgf = xbmcaddon.Addon("script.tvguide.fullscreen")
    if tvgf:
        tvgf.setSetting('skin.source', '2')
        tvgf.setSetting('skin.folder', 'special://home/addons/script.tvguide.fullscreen.skin.tycoo/')
        tvgf.setSetting('skin.user', SKINS[skin][1])
        tvgf.setSetting('action.bar', 'true')
        tvgf.setSetting('down.action', 'true')
        tvgf.setSetting('channels.per.page', '8')
        tvgf.setSetting('epg.box.spacing', '4')
        tvgf.setSetting('epg.focus.color', '[COLOR ff606060]black[/COLOR]')
        if skin in [1]:
            tvgf.setSetting('epg.font', 'TVGuide29')
        else:
            tvgf.setSetting('epg.font', 'font13')
        tvgf.setSetting('epg.nofocus.color', '[COLOR ff696969]dimgrey[/COLOR]')
        tvgf.setSetting('last.channel.popup', '1')
        tvgf.setSetting('redraw.epg', 'false')
        tvgf.setSetting('up.cat.mode', 'no')
