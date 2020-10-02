import configparser


def create_config(settings):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "IP_address", '127.0.0.1')
    config.set("Settings", "PORT", '5080')

    with open(settings, "w") as config_file:
        config.write(config_file)


def load_config():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    ip_address = config.get('Settings', 'ip_address')
    port = config.get('Settings', 'port')

    return ip_address, port


settings = "settings.ini"
create_config(settings)

