from src.steelseries_sonar_py.sonar import Sonar
from src.steelseries_sonar_py.exceptions import *

import time

def test_classic_mode():
    try:
        sonar = Sonar()
        
        print("Disabling streamer mode: ", not sonar.set_streamer_mode(False))        
        
        volume_data = sonar.get_volume_data()
        print("Classic Mode - Volume Data:", volume_data)

        channel = "master"
        volume = 0.5
        result = sonar.set_volume(channel, volume)
        print(f"Classic Mode - Set volume for {channel}:", result)

        channel = "game"
        muted = True
        result = sonar.mute_channel(channel, muted)
        print(f"Classic Mode - Mute {channel}:", result)

    except EnginePathNotFoundError:
        print("Engine not found!")
    except ServerNotAccessibleError as e:
        print(f"Server not accessible, status code: {e.status_code}")

def test_streamer_mode():
    try:
        sonar = Sonar()
        
        print("Enabling streamer mode: ", sonar.set_streamer_mode(True))
        
        for slider in ["streaming", "monitoring"]:
            volume_data = sonar.get_volume_data()
            print(f"Streamer Mode ({slider}) - Volume Data:", volume_data)

            channel = "master"
            volume = 0.5
            result = sonar.set_volume(channel, volume, streamer_slider=slider)
            print(f"Streamer Mode ({slider}) - Set volume for {channel}:", result)

            channel = "game"
            muted = True
            result = sonar.mute_channel(channel, muted, streamer_slider=slider)
            print(f"Streamer Mode ({slider}) - Mute {channel}:", result)

    except EnginePathNotFoundError:
        print("Engine not found!")
    except ServerNotAccessibleError as e:
        print(f"Server not accessible, status code: {e.status_code}")

if __name__ == "__main__":
    test_classic_mode()
    print("\n\n--------------------------------\n\n")
    test_streamer_mode()
