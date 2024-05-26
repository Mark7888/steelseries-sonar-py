class EnginePathNotFoundError(Exception):
    def __str__(self):
        return "SteelSeries Engine 3 not installed or not in the default location!"


class ServerNotAccessibleError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code

    def __str__(self):
        return f"SteelSeries server not accessible! Status code: {self.status_code}"


class SonarNotEnabledError(Exception):
    def __str__(self):
        return "SteelSeries Sonar is not enabled!"


class ServerNotReadyError(Exception):
    def __str__(self):
        return "SteelSeries Sonar is not ready yet!"


class ServerNotRunningError(Exception):
    def __str__(self):
        return "SteelSeries Sonar is not running!"


class WebServerAddressNotFoundError(Exception):
    def __str__(self):
        return "Web server address not found"


class ChannelNotFoundError(Exception):
    def __init__(self, channel):
        self.channel = channel

    def __str__(self):
        return f"Channel '{self.channel}' not found"


class InvalidVolumeError(Exception):
    def __init__(self, volume):
        self.volume = volume

    def __str__(self):
        return f"Invalid volume '{self.volume}'! Value must be between 0 and 1!"

class InvalidMixVolumeError(Exception):
    def __init__(self, mix_volume):
        self.mix_volume = mix_volume

    def __str__(self):
        return f"Invalid mix volume '{self.mix_volume}'! Value must be between -1 and 1!"