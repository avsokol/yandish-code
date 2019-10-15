import os
import re
from subprocess import Popen, PIPE


def check_links(dir, rootdir, exclude_dirs, cfgfile):

    if os.path.exists(dir) == 0:
        return

    elements = os.listdir(dir)

    for element in elements:
        element = os.path.join(dir, element)

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
            check_links(element, rootdir, exclude_dirs, cfgfile)
    return


def get_param_from_cfg_file(param, cfg_file):

    with open(os.path.expanduser(cfg_file), "r") as f:
        for line in f:

            if line.strip() == "":
                continue
            elements = line.split("=")
            if elements[0] != param:
                continue
            return elements[1].strip().strip('"')
    
    return ""


def replace_params_in_cfg_file(p_values, cfg_file):

    tmp_file = cfg_file + ".tmp"

    seen_elements = []

    with open(os.path.expanduser(tmp_file), "w") as fw:
        with open(os.path.expanduser(cfg_file), "r") as fr:
            for line in fr:
                elements = line.split("=")

                if elements[0] == "#proxy":
                    fw.write(line)
                    continue

                el = elements[0].lstrip("#")

                if el in seen_elements:
                    continue

                if el in p_values.keys():
                    seen_elements.append(el)
                    new_line = el + "=\"" + p_values[el] + "\"\n"
                    fw.write(new_line)

                else:
                    fw.write(line)

            for key in p_values.keys():
                if key in seen_elements:
                    continue
                if el == "proxy":
                    new_line = key + "=" + p_values[key] + "\n"
                else:
                    new_line = key + "=\"" + p_values[key] + "\"\n"
                fw.write(new_line)

    os.remove(os.path.expanduser(cfg_file))
    os.rename(os.path.expanduser(tmp_file), os.path.expanduser(cfg_file))


def write_cfg_file(p_values, cfg_file):

    cfg_dir = os.path.dirname(cfg_file)
    if not os.path.exists(cfg_dir):
        os.mkdir(cfg_dir)

    with open(os.path.expanduser(cfg_file), "w") as fw:
        for key in p_values.keys():
            new_line = key + "=\"" + p_values[key] + "\"\n"
            fw.write(new_line)


def save_params_in_cfg_file(p_values, cfg_file):

    if os.path.exists(os.path.expanduser(cfg_file)):
        replace_params_in_cfg_file(p_values, cfg_file)

    else:
        write_cfg_file(p_values, cfg_file)


def get_yandex_cfg_from_cfg_file(cfg_file, raise_except=1):
    if not os.path.exists(os.path.expanduser(cfg_file)):
        if raise_except:
            raise Exception("Couldn't find config file:\n%s" % cfg_file)

        else:
            return ""

    return get_param_from_cfg_file("yandex-cfg", cfg_file)


def get_auth_from_cfg_file(cfg_file, raise_except=1):
    if not os.path.exists(os.path.expanduser(cfg_file)):
        if raise_except:
            raise Exception("Couldn't find config file:\n%s" % cfg_file)

        else:
            return ""

    return get_param_from_cfg_file("auth", cfg_file)


def get_root_dir_from_cfg_file(cfg_file, raise_except=1):
    if not os.path.exists(os.path.expanduser(cfg_file)):
        if raise_except:
            raise Exception("Couldn't find config file:\n%s" % cfg_file)

        else:
            return ""

    return get_param_from_cfg_file("dir", cfg_file)


def get_proxy_from_cfg_file(cfg_file, raise_except=1):
    if not os.path.exists(os.path.expanduser(cfg_file)):
        if raise_except:
            raise Exception("Couldn't find config file:\n%s" % cfg_file)

        else:
            return ""

    return get_param_from_cfg_file("proxy", cfg_file)


def get_exclude_dirs_from_cfg_file(cfg_file, raise_except=1):
    if not os.path.exists(os.path.expanduser(cfg_file)):
        if raise_except:
            raise Exception("Couldn't find default config file:\n%s" % cfg_file)

        else:
            return []

    return get_param_from_cfg_file("exclude-dirs", cfg_file).split(",")


def save_exclude_dirs(dirs, cfg_file):
    value = ",".join(dirs)
    params = {"exclude-dirs": value}
    save_params_in_cfg_file(params, cfg_file)


def do_action(action, params):
    prg = params["prg"]
    cfg_file = params["config"]
    auth = params["auth"]
    root_dir = params["rootdir"]
    exclude_dirs = params["exclude-dirs"]

    check_links(root_dir, root_dir, exclude_dirs, cfg_file)
    exclude_opt = ",".join(exclude_dirs)

    cfg_opt = os.path.expanduser(cfg_file)
    auth_param = os.path.expanduser(auth)

    is_running, message = is_daemon_running(prg)

    err_messages = [
        "Error: option 'dir' is missing",
        "Error: Indicated directory does not exist",
        "Error: file with OAuth token hasn't been found."
        "\nUse 'token' command to authenticate and create this file"
    ]

    if message in err_messages:
        return 3, message

    if action == "status":
        return is_running, message
    elif action == "stop":
        if is_running == 0:
            return 2, message
    elif action == "start":
        if is_running:
            return 2, message
    else:
        raise Exception("Unexpected action %s\n%s" % (action, 1))

    proc = Popen(
        [
            prg,
            action,
            "--exclude-dirs", exclude_opt,
            "--config", cfg_opt,
            "--auth", auth_param,
            "--dir", root_dir
        ],
        stdout=PIPE,
        stderr=PIPE
    )

    return_code = proc.wait()
    if return_code == 0:
        out = proc.stdout.read()
        out = out.strip()
        out = out.decode("utf8")
    else:
        raise Exception("Failure %s:\n'%s'\n'%s'" % (return_code, proc.stdout.read(), proc.stderr.read()))

    return return_code, out


def show_msg(msg, type, title, icon, verbose):
    if verbose == 0:
        return

    print("%s" % msg)


def process_result(res, action, out, params, verbose=1):

    exclude_dirs = params["exclude-dirs"]
    prg = params["prg"]

    msg = type = title = icon = None

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

    show_msg(msg, type, title, icon, verbose)
    return msg


def is_daemon_running(prg):
    proc = Popen([prg, "status"], stdout=PIPE, stderr=PIPE)
    return_code = proc.wait()
    if return_code == 0 or return_code == 1:
        res = proc.stdout.read()
        res = res.strip()
        res = res.decode("utf8")
    else:
        raise Exception("Failure %s:\n'%s'\n'%s'" % (return_code, proc.stdout.read(), proc.stderr.read()))

    message = res

    if return_code == 0:
        is_running = 1
    elif return_code == 1:
        is_running = 0
    else:
        raise Exception("Unexpected error code: %s", return_code)

    return is_running, message


def get_status_from_msg(msg):
    # TODO: to be refactored
    status = "Unknown"

    pattern = dict()

    pattern["english"] = "Synchronization core status: "
    pattern["russian"] = u"Статус ядра синхронизации: "
    pattern["russian_error"] = u"Ошибка: "

    for line in msg.split("\n"):
        if re.search(pattern["english"], line):
            status = re.sub(pattern["english"], "", line)
            break

        if re.search(pattern["russian"], line):
            status = re.sub(pattern["russian"], "", line)
            break

        if re.search(pattern["russian_error"], line):
            status = re.sub(pattern["russian_error"], "", line)
            break

    return status
