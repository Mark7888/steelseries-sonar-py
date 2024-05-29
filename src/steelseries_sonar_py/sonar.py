import requests
import json
import os

from . import exceptions as ex


def streamer_mode_status(self):
    try:
        # get the "web server address" from "https://127.0.0.1:6327/subApps" (default address)
        web_server_address_raw = requests.get("https://127.0.0.1:6327/subApps", verify=False)

        # get the raw web server address
        web_server_address = web_server_address_raw.json()["subApps"]["sonar"]["metadata"]["webServerAddress"]

        # check if streamer mode is enabled (returns true or false)
        streamer_mode_raw = requests.get(web_server_address + "/mode/", verify=False).text

        # clear the string from brackets
        streamer_mode = streamer_mode_raw.replace('"', '')

        # check mode ("stream", "classic")
        if streamer_mode == "stream":
            streamer_mode = True
        else:
            streamer_mode = False
    
    except:
        # revert to the default "streamer_mode = False" (not fatal)
        return False
    
    finally:
        # return result
        return streamer_mode


class Sonar:
    # chatCapture = mic
    channel_names = ["master", "game", "chatRender", "media", "aux", "chatCapture"]
    volume_path = "/volumeSettings/classic"
    app_data_path = os.path.join(
        os.environ["ProgramData"],
        "SteelSeries",
        "SteelSeries Engine 3",
        "coreProps.json",
    )

    def __init__(self, streamer_mode=None, app_data_path=None):
        requests.packages.urllib3.disable_warnings()

        if app_data_path is not None:
            self.app_data_path = app_data_path

        self.load_base_url()
        self.load_server_address()

        if streamer_mode is None:
            # get the streamer mode using a request to the server
            self.streamer_mode = streamer_mode_status(self)
        if self.streamer_mode:
            self.volume_path = "/volumeSettings/streamer/streaming/master/volume"

    def load_base_url(self):
        if not os.path.exists(self.app_data_path):
            raise ex.EnginePathNotFoundError()

        with open(self.app_data_path, "r") as rf:
            common_app_data = json.load(rf)
            self.base_url = f'https://{common_app_data["ggEncryptedAddress"]}'

    def load_server_address(self):
        app_data = requests.get(self.base_url + "/subApps", verify=False)
        if app_data.status_code != 200:
            raise ex.ServerNotAccessibleError(app_data.status_code)

        app_data_json = json.loads(app_data.text)

        if not app_data_json["subApps"]["sonar"]["isEnabled"]:
            raise ex.SonarNotEnabledError()

        if not app_data_json["subApps"]["sonar"]["isReady"]:
            raise ex.ServerNotReadyError()

        if not app_data_json["subApps"]["sonar"]["isRunning"]:
            raise ex.ServerNotRunningError()

        self.web_server_address = app_data_json["subApps"]["sonar"]["metadata"][
            "webServerAddress"
        ]
        if self.web_server_address in ["", None, "null"]:
            raise ex.WebServerAddressNotFoundError()

    def get_volume_data(self):
        # "volumeSettings/streamer" displays streamer and classic volume (everything)
        volume_info_url = self.web_server_address + "/volumeSettings/streamer"
        volume_data = requests.get(volume_info_url)
        if volume_data.status_code != 200:
            raise ex.ServerNotAccessibleError(volume_data.status_code)
        volume_data_json = json.loads(volume_data.text)

        return volume_data_json

    def set_volume(self, channel, volume):
        if channel not in self.channel_names:
            raise ex.ChannelNotFoundError(channel)

        if volume < 0 or volume > 1:
            raise ex.InvalidVolumeError(volume)

        url = f"{self.web_server_address}{self.volume_path}/{channel}/Volume/{json.dumps(volume)}"
        volume_data = requests.put(url)

        return json.loads(volume_data.text)

    def mute_channel(self, channel, muted):
        if channel not in self.channel_names:
            raise ex.ChannelNotFoundError(channel)

        muted = muted == True

        url = f"{self.web_server_address}{self.volume_path}/{channel}/Mute/{json.dumps(muted)}"
        mute_data = requests.put(url)

        return json.loads(mute_data.text)

    def chat_mix(self, mix_volume):
        if mix_volume < -1 or mix_volume > 1:
            raise ex.InvalidMixVolumeError(mix_volume)
        
        url = f"{self.web_server_address}/chatMix?balance={json.dumps(mix_volume)}"
        chat_mix_data = requests.put(url)

        return json.loads(chat_mix_data.text)
