# CONSTANTS
__author__ = 'Tridex'
__version__ = '0.0.1'
__url__ = 'http://tridex.net'
__date__ = '3/2015'

# imports
import sys
import xbmc
import xbmcaddon
import xbmcgui

import telnetlib
import time
import json

# custom imports
import xb_events
import log
import event_actions

# load settings
denonip = "10.0.0.6"

# create xbmc event handler
xEvents = xb_events.xbmcEvents()
# add handlers
node_events = {
    'onVolumeChanged': delVolume()
}
xEvents.AddHandlers(node_events)

# start events engine
xEvents.RunMainLoop()

def delVolume():
        tn = telnetlib.Telnet(denonIp)
        tn.write("MVDOWN\r")
        tn.close()

