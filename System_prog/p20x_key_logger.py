# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:44:39 2013

@author: kansi
"""
import pyHook, pythoncom

# create a keyboard hook
def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'
    if event.Key.lower() in ['lwin', 'tab', 'lmenu']:
         return False    # block these keys
    elif event.Ascii == 3:
         exit(0)
    else:
         return True
         
'''    else:
        # return True to pass the event to other handlers
        return True'''

# create a hook manager
hm = pyHook.HookManager()
# watch for all keyboard events
hm.KeyDown = OnKeyboardEvent
# set the hook
hm.HookKeyboard()

pythoncom.PumpMessages()
