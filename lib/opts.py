import os


class AppOptions(object):
    rc_file_name = ".yandishrc"

    params = {
        "StartMinimized": "1",
        "HideOnMinimize": "1",
        "autorefresh": "15",
        "startServiceAtStart": "1",
        "yandex-cfg": ""
    }

    def __init__(self):
        self.read_params_from_rc_file()

    def get_rc_file_name(self):
        return self.rc_file_name

    def set_rc_file_name(self, fn):
        self.rc_file_name = fn

    def get_rc_path(self):
        return os.path.join(os.environ["HOME"], self.rc_file_name)

    def get_param(self, param):
        if param in self.params.keys():
            return self.params[param]

        else:
            return "-1"

    def set_param(self, param, value):
        if param in self.params.keys():
            self.params[param] = value

    def print_params(self):
        for k, v in self.params.items():
            print("'%s' -> '%s'" % (k, v))

    def read_params_from_rc_file(self):
        if not os.path.exists(self.get_rc_path()):
            self.save_params_to_rc_file()

        with open(self.get_rc_path(), "r") as f:
            for line in f:
                if line.strip() == "":
                    continue

                elements = line.split("=")
                if len(elements) != 2:
                    continue

                key, value = elements[0], elements[1]
                if key in self.params.keys():
                    self.params[key] = value

    def save_params_to_rc_file(self):
        fn = self.get_rc_path()
        fn_tmp = fn + ".tmp"
        with open(fn_tmp, "w") as f:
            for k, v in self.params.items():
                v = str(v)
                v = v.strip()
                line = k + "=" + v + "\n"
                f.write(line)

        if os.path.exists(fn):
            os.remove(fn)

        os.rename(fn_tmp, fn)
