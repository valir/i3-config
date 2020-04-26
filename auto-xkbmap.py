#!/usr/bin/env python3

from argparse import ArgumentParser
import i3ipc

i3 = i3ipc.Connection()

# parser = ArgumentParser(description="""Open the given application each time the
#     given workspace is created. For instance, running 'app-on-ws-init.py 6
#     i3-sensible-terminal' should open your terminal as soon as you create the
#     workspace 6.
#     """)
#
# parser.add_argument('--workspace', metavar='WS_NAME', nargs='+', required=True,
#                     help='The name of the workspaces to run the command on')
# parser.add_argument('--command', metavar='CMD', required=True,
#                     help='The command to run on the newly initted workspace')
#
# args = parser.parse_args()
#

def on_window_focus(i3, e):
    print(e.change)
    print(e.container.__dict__)

def on_window_close(i3, e):
    print(e.change)

i3.on('window', on_window_focus)
i3.on('window::close', on_window_close)

i3.main()
