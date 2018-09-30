import configparser
import os
import platform
from os.path import join

__os_type = platform.system()
__home = os.path.join(os.path.expanduser("~"), "Chat Server")

if "Windows" in __os_type:
    try:
        os.makedirs(__home)
    except FileExistsError as err:
        pass
    finally:
        pass

default_config = {
    "timestamp": {
        "default": 'False'
    },
    "default_paths": {
        "database": join(__home, "database", "chat.sqlite"),
    },
    "default_ip": {
        "ip": "127.0.0.1"
    },
    "default_host": {
        "host": '5005'
    }
}

default_name = "default_config.ini"


def create_config(name: str = join(__home, default_name), default_con: dict = default_config):
    from os import mkdir
    try:
        mkdir("\\".join(name.split("\\")[:-1]))
    except FileExistsError:
        pass
    with open(name, "w+") as file:
        temp = configparser.ConfigParser()
        for header in default_con.keys():
            temp.add_section("{}".format(header))
            for opt in default_con[header].keys():
                temp.set(header, opt, str(default_con[header][opt]))
        temp.write(file)


def open_config(file: str = join(__home, default_name)):
    _config = configparser.ConfigParser()
    _config.read(file)
    return _config


def config_selection(file: str = join(__home, default_name), selection: str = None):
    _dict = {}
    _file = open_config(file)
    if selection is not None:
        options = _file.options(selection)
        for opt in options:
            try:
                _dict[opt] = _file.get(selection, opt)
                if _dict[opt] == -1:
                    print("skip: {}".format(opt))
            except Exception as r:
                print("Exception on {}\n{}".format(opt, r))
    else:
        for section in _file:
            if section is not "DEFAULT":
                _dict[section] = dict()
                for opt in _file.options(section):
                    _dict[section][opt] = _file[section][opt]
    return _dict


if __name__ == "__main__":
    create_config()
    config = open_config()
    print(config_selection())
