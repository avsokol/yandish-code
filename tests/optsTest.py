#!/usr/bin/python

import sys
import os
cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.dirname(cur_dir))

from lib.opts import AppOptions

app_opts = AppOptions()

app_opts.set_rc_file_name(".yadisktest")

print("Test cfg file: '%s'" % app_opts.get_rc_file_name())

# ya.save_params_to_rc_file()
# ya.read_params_from_rc_file()

app_opts.print_params()

app_opts.set_param("StartMinimized", 0)
app_opts.set_param("HideOnMinimize", 0)
app_opts.set_param("autorefresh", 30)


app_opts.save_params_to_rc_file()
app_opts.read_params_from_rc_file()

app_opts.print_params()
