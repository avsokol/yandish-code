# -*- coding: utf-8 -*-

import sys, os, re
from subprocess import Popen, PIPE

#############################################################################

def CheckLinks(dir,rootdir,exclude_dirs,cfgfile):

    if os.path.exists(dir) == 0:
        return

    elements = os.listdir(dir)

    for element in elements:
        element = os.path.join(dir,element)

        if os.path.isfile(element):
            continue

        if os.path.islink(element):
            target = os.readlink(element)
            if os.path.exists(target):
                pass
            elif os.path.isdir(target):
                print("ERR!")
            else:
                element = element.lstrip(rootdir)
                if element != "":
                    if element in exclude_dirs:
                        pass
                    else:
                        exclude_dirs.append(element)

        if os.path.isdir(element) and os.path.islink(element) == 0:
            CheckLinks(element,rootdir,exclude_dirs,cfgfile)
    return

#############################################################################

def GetParamFromCfgFile(param,cfgfile):

    with open(os.path.expanduser(cfgfile), "r") as f:
        for line in f:

            if line.strip() == "":
                continue
            elements = line.split("=")
            if elements[0] != param:
                continue
            return elements[1].strip().strip('"')
    
    return ""

#############################################################################

def replaceParamsInCfgFile(pvalues,cfgfile):

    tmp_file = cfgfile + ".tmp"

    seen_elements = []

    with open(os.path.expanduser(tmp_file), "w") as fw:
        with open(os.path.expanduser(cfgfile), "r") as fr:
            for line in fr:
                elements = line.split("=")

                if elements[0] == "#proxy":
                    fw.write(line)
                    continue

                el = elements[0].lstrip("#")

                if el in seen_elements:
                    continue

                if el in pvalues.keys():
                    seen_elements.append(el)
                    new_line = el + "=\"" + pvalues[el] + "\"\n"
                    fw.write(new_line)

                else:
                    fw.write(line)

            for key in pvalues.keys():
                if key in seen_elements:
                    continue
                if el == "proxy":
                    new_line = key + "=" + pvalues[key] + "\n"
                else:
                    new_line = key + "=\"" + pvalues[key] + "\"\n"
                fw.write(new_line)

    os.rename(os.path.expanduser(tmp_file),os.path.expanduser(cfgfile))

#############################################################################

def writeCfgFile(pvalues,cfgfile):
    with open(os.path.expanduser(cfgfile), "w") as fw:
        for key in pvalues.keys():
            new_line = key + "=\"" + pvalues[key] + "\"\n"
            fw.write(new_line)

#############################################################################

def SaveParamsInCfgFile(pvalues,cfgfile):

    if os.path.exists(os.path.expanduser(cfgfile)):
        replaceParamsInCfgFile(pvalues,cfgfile)
    else:
        writeCfgFile(pvalues,cfgfile)

#############################################################################

def GetYandexCfgFromCfgFile(cfgfile,raiseExcept=1):
    if os.path.exists(os.path.expanduser(cfgfile)) == False:
        if raiseExcept:
            raise Exception("Couldn't find config file:\n%s" % cfgfile)
        else:
            return ""

    return GetParamFromCfgFile("yandex-cfg",cfgfile)

#############################################################################

def GetAuthFromCfgFile(cfgfile,raiseExcept=1):
    if os.path.exists(os.path.expanduser(cfgfile)) == False:
        if raiseExcept:
            raise Exception("Couldn't find config file:\n%s" % cfgfile)
        else:
            return ""

    return GetParamFromCfgFile("auth",cfgfile)

#############################################################################

def GetRootDirFromCfgFile(cfgfile,raiseExcept=1):
    if os.path.exists(os.path.expanduser(cfgfile)) == False:
        if raiseExcept:
            raise Exception("Couldn't find config file:\n%s" % cfgfile)
        else:
            return ""

    return GetParamFromCfgFile("dir",cfgfile)

#############################################################################

def GetProxyFromCfgFile(cfgfile,raiseExcept=1):
    if os.path.exists(os.path.expanduser(cfgfile)) == False:
        if raiseExcept:
            raise Exception("Couldn't find config file:\n%s" % cfgfile)
        else:
            return ""

    return GetParamFromCfgFile("proxy",cfgfile)

#############################################################################

def GetExcludeDirsFromCfgFile(cfgfile,raiseExcept=1):
    if os.path.exists(os.path.expanduser(cfgfile)) == False:
        if raiseExcept:
            raise Exception("Couldn't find default config file:\n%s" % cfgfile)
        else:
            return []

    return GetParamFromCfgFile("exclude-dirs",cfgfile).split(",")

#############################################################################

def SaveExcludeDirs(dirs,cfgfile):

    value = ",".join(dirs)
    params = {"exclude-dirs": value}
    SaveParamsInCfgFile(params,cfgfile)

#############################################################################

def DoAction(action,params):

    prg = params["prg"]
    cfgfile = params["config"]
    auth = params["auth"]
    rootdir = params["rootdir"]
    exclude_dirs = params["exclude-dirs"]

    CheckLinks(rootdir,rootdir,exclude_dirs,cfgfile)
    excludeOpt = ",".join(exclude_dirs)

    cfgOpt = os.path.expanduser(cfgfile)
    authParam = os.path.expanduser(auth)

    is_running,message = IsDaemonRunning(prg)

    err_messages = ["Error: option 'dir' is missing",
                    "Error: Indicated directory does not exist",
                    "Error: file with OAuth token hasn't been found.\nUse 'token' command to authenticate and create this file"]

    if message in err_messages :
        return 3,message        

    if action == "status":
        return is_running,message
    elif action == "stop":
        if is_running == 0:
            return 2,message
    elif action == "start":
        if is_running:
            return 2,message
    else:
        raise Exception("Unexpected action %s\n%s" % (action, 1))

    proc = Popen([prg, action,
                  "--exclude-dirs", excludeOpt,
                  "--config", cfgOpt,
                  "--auth", authParam,
                  "--dir", rootdir],
                 stdout=PIPE, stderr=PIPE)

    return_code = proc.wait()
    if return_code == 0:
        OUT = proc.stdout.read()
        OUT = OUT.strip()
        OUT = OUT.decode("utf8")
    else:
        raise Exception("Failure %s:\n'%s'\n'%s'" % (return_code, proc.stdout.read(), proc.stderr.read()))

    return return_code,OUT

#############################################################################

def ShowMsg(msg,type,title,icon,verbose):
    if verbose == 0:
        return

    print("%s" % msg)

#############################################################################

def ProcessResult(res,action,out,params,verbose=1):

    exclude_dirs = params["exclude-dirs"]
    prg = params["prg"]

    if res == 0:
        type = "ok"
        title = "Done"
        icon = "info"
        if action == "start":
            msg = "Yandex Disk service is started"
            if len(exclude_dirs):
                msg = msg + "\nDirectories excluded:\n" + "\n".join(exclude_dirs)
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
            if len(exclude_dirs):
                msg = msg + "\nDirectories excluded:\n" + "\n".join(exclude_dirs)
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
        elif action == "status":
            msg = "Yandex Disk is not running\n\n" + out

    elif res == 3:
        type = "error"
        title = "Error"
        icon = "error"
        msg = out

    else:
        raise Exception("Unexpected error code: '%s'" % res)

    ShowMsg(msg,type,title,icon,verbose)
    return msg

#############################################################################

def IsDaemonRunning(prg):

    proc = Popen([prg, "status"], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0 or return_code == 1:
        RES = proc.stdout.read()
        RES = RES.strip()
        RES = RES.decode("utf8")
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

def getStatusFromMsg(msg):

    status = "Unknown"

    pattern = "Synchronization core status: "

    for line in msg.split("\n"):
        if re.search(pattern, line):
            status = re.sub(pattern, "", line)
            break

    return status

