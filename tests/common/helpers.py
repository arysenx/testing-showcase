def parse_config_value(value, config_data):
    if isinstance(value, str) and value.startswith('[CONF:') and value.endswith(']'):
        keys = value[6:-1].split('.')
        result = config_data
        try:
            for key in keys:
                result = result[key]
            return result
        except KeyError:
            raise KeyError(f"Configuration key not found: {value}")
    return value
