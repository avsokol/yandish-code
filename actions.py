# -*- coding: utf-8 -*-

import sys, os, re
from subprocess import Popen, PIPE
from init import IsDaemonRunning, GetPrg, GetCfgFile, GetExcludedDirs, AppendExcludedDir

#############################################################################

def CheckLinks(dir):

    elements = os.listdir(dir)

    for element in elements:
        element = os.path.join(dir,element)

        if os.path.isfile(element):
            pass

        if os.path.islink(element):
            target = os.readlink(element)
            if os.path.exists(target):
                pass
            elif os.path.isdir(target):
                print("ERR!")
            else:
                root_dir = FindRootDir()
                element = element.lstrip(root_dir)
                excl_dirs = GetExcludedDirs()
                if element != "":
                    AppendExcludedDir(element)

        if os.path.isdir(element) and os.path.islink(element) == 0:
            CheckLinks(element)
    return

#############################################################################

def GetParamFromCfgFile(param):

    CFGFILE = GetCfgFile()

    with open(os.path.expanduser(CFGFILE), "r") as f:
        for line in f:

            if line.strip() == "":
                continue
            elements = line.split("=")
            if elements[0] != param:
                continue
            return elements[1].strip().strip('"')
    
    return ""

#############################################################################

def SaveParamsInCfgFile(pvalues):
    CFGFILE = GetCfgFile()

    tmp_file = CFGFILE + ".tmp"

    with open(os.path.expanduser(tmp_file), "w") as fw:
        with open(os.path.expanduser(CFGFILE), "r") as fr:
            for line in fr:
                elements = line.split("=")

                if elements[0] in pvalues.keys():
                    new_line = elements[0] + "=\"" + pvalues[elements[0]] + "\"\n"
                    fw.write(new_line)

                else:
                    fw.write(line)

    os.rename(os.path.expanduser(tmp_file),os.path.expanduser(CFGFILE))


#############################################################################

def FindRootDir():

    CFGFILE = GetCfgFile()

    if os.path.exists(os.path.expanduser(CFGFILE)) == False:
        raise Exception("Couldn't find default config file:\n%s" % CFGFILE)

    path = GetParamFromCfgFile("dir")
    if path == "":
        raise Exception("Couldn't get parameter 'dir' from config file")

    return path

#############################################################################

def FindExcludedDirs():

    CFGFILE = GetCfgFile()

    if os.path.exists(os.path.expanduser(CFGFILE)) == False:
        raise Exception("Couldn't find default config file:\n%s" % CFGFILE)

    return GetParamFromCfgFile("exclude-dirs").split(",")

#############################################################################

def SaveExcludedDirs(dirs):
    CFGFILE = GetCfgFile()

    value = ",".join(dirs)
    params = {"exclude-dirs": value}
    SaveParamsInCfgFile(params)

#############################################################################

def DoAction(action):

    PRG = GetPrg()
    params=""
    is_running,message = IsDaemonRunning()

    if action == "status":
        return is_running,message
    elif action == "stop":
        if is_running == 0:
            return 2,message
    elif action == "start":
        if is_running:
            return 2,message
        excl_dirs = FindExcludedDirs()
        CheckLinks(FindRootDir())

        if len(excl_dirs):
            params = "--exclude-dirs=" + "\"" + ",".join(excl_dirs) + "\""

    else:
        raise Exception("Unexpected action %s\n%s:\n'%s'" % (action, return_code, proc.stderr.read()))

    proc = Popen([PRG, action, params], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0:
        OUT = proc.stdout.read()
        OUT = OUT.strip()
    else:
        raise Exception("Failure %s:\n'%s'" % (return_code, proc.stderr.read()))

    return return_code,OUT

#############################################################################

def ShowMsg(msg,type,title,icon,verbose):
    if verbose == 0:
        return

    print("%s" % msg)

#############################################################################

def ProcessResult(res,action,out,verbose=1):

    excl_dirs = GetExcludedDirs()

    PRG = GetPrg()

    if res == 0:
        type = "ok"
        title = "Done"
        icon = "info"
        if action == "start":
            msg = "Yandex Disk service is started"
            if len(excl_dirs):
                msg = msg + "\nDirectories excluded:\n" + "\n".join(excl_dirs)
        elif action == "stop":
            msg = "Yandex Disk service is stopped"
        elif action == "status":
            msg = "Yandex Disk service is not running\n\n" + out

    elif res == 1:
        if action == "start" or action == "stop":
            msg = "Error: " + out
            type = "ok"
            title = "Error"
            icon = "error"
        elif action == "status":
            msg = "Yandex Disk service is running"
            if len(excl_dirs):
                msg = msg + "\nDirectories excluded:\n" + "\n".join(excl_dirs)
            msg = msg + "\n\n" + out
            type = "ok"
            title = "Info"
            icon = "info"

    elif res == 2:
        type = "ok"
        title = "Done"
        icon = "info"
        if action == "start":
            msg = "Yandex Disk is already running"
        elif action == "stop":
            msg = "Yandex Disk is not running"
        elif action == status:
            raise Exception("Unexpected code for status command")
    else:
        raise Exception("Unexpected error code: '%s'" % res)

    ShowMsg(msg,type,title,icon,verbose)
    return msg

#############################################################################
