# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

#############################################################################

def Init():
    global PRG
    global CFGFILE
    global EXCLUDED_DIRS
    PRG = ""
    CFGFILE = "~/.config/yandex-disk/config.cfg"
    EXCLUDED_DIRS = []
    CheckPrg()
    return IsDaemonRunning()

#############################################################################

def CheckPrg():
    global PRG

    executable = "yandex-disk"

    proc = Popen(["which", executable], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0:
        PRG = proc.stdout.read()
        PRG = PRG.strip()
    else:
        raise Exception("Error %s: Couldn't find '%s' executable\n%s" % (return_code, executable, proc.stderr.read()))

#############################################################################

def GetPrg():
    global PRG

    return PRG

#############################################################################

def GetCfgFile():
    global CFGFILE

    return CFGFILE

#############################################################################

def ClearExcludedDirs():
    global EXCLUDED_DIRS

    EXCLUDED_DIRS = []

#############################################################################

def GetExcludedDirs():
    global EXCLUDED_DIRS

    return EXCLUDED_DIRS

#############################################################################

def AppendExcludedDir(element):
    global EXCLUDED_DIRS

    if element in EXCLUDED_DIRS:
        pass
    else:
        EXCLUDED_DIRS.append(element)

#############################################################################

def IsDaemonRunning():
    global PRG

    proc = Popen([PRG, "status"], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0 or return_code == 1:
        RES = proc.stdout.read()
        RES = RES.strip()
    else:
        raise Exception("Failure %s:\n'%s'\n'%s'" % (return_code, proc.stdout.read(), proc.stderr.read()))

    message = RES

    if return_code == 0:
        is_running = 1
    elif return_code == 1:
        is_running = 0
    else:
        raise Exception("Unexpected error code: %s", return_code)

    return is_running,message

#############################################################################
