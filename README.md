[![publish](https://github.com/Mark7888/steelseries-sonar-py/actions/workflows/publish.yml/badge.svg?event=push)](https://github.com/Mark7888/steelseries-sonar-py/actions/workflows/publish.yml)
[![Downloads](https://static.pepy.tech/badge/steelseries-sonar-py)](https://pepy.tech/project/steelseries-sonar-py)

# SteelSeries Sonar Python API

## Overview

This Python package provides a convenient interface for interacting with the SteelSeries Sonar application API. The Sonar application allows users to control and display volumes for various audio channels.

## Installation

To use this package, follow these steps:

1. Install the package using pip:

   ```bash
   pip install steelseries-sonar-py
   ```

2. Import the `Sonar` class in your Python script or application:

   ```python
   from steelseries_sonar_py import Sonar
   ```

## Usage

### Initializing the Sonar Object

The Sonar class accepts two optional parameters during initialization:
`streamer_mode`: Set to True to use streamer mode (default is False).
`app_data_path`: Specify a custom path for the SteelSeries Engine 3 coreProps.json file (default is the default installation path: `C:\\ProgramData\\SteelSeries\\SteelSeries Engine 3\\coreProps.json`).

```python
sonar = Sonar(streamer_mode=True, app_data_path="C:\\path\\to\\coreProps.json")
```

### Retrieving Volume Information

Retrieve information about the current volume settings for all channels:

```python
volume_data = sonar.get_volume_data()
print(volume_data)
```

### Setting Volume for a Channel

Set the volume for a specific channel. The `channel` parameter should be one of the following: "master", "game", "chatRender", "media", "aux", "chatCapture". The `volume` parameter should be a float between 0 and 1:

```python
channel = "master"
volume = 0.75

result = sonar.set_volume(channel, volume)
print(result)
```

### Muting/Unmuting a Channel

Toggle mute status for a specific channel. The `channel` parameter should be one of the following: `master`, `game`, `chatRender`, `media`, `aux`, `chatCapture`. The `muted` parameter should be a boolean indicating whether to mute (`True`) or unmute (`False`) the channel:

```python
channel = "game"
muted = True

result = sonar.mute_channel(channel, muted)
print(result)
```

### Chatmix

Chatmix value between `-1 and 1` to focus sound from the `game` or `chatRender` channel:

```python
result = sonar.chat_mix(0.5)
print(result)
```

## Exceptions

The package introduces a set of exceptions that might be raised during usage. It is advisable to handle these exceptions accordingly in your code. You can import them from `steelseries_sonar_py.exceptions`. Here is the list of potential exceptions:

- `EnginePathNotFoundError`: Raised when SteelSeries Engine 3 is not installed or not in the default location.
- `ServerNotAccessibleError`: Raised when the SteelSeries server is not accessible. Provides the HTTP status code.
- `SonarNotEnabledError`: Raised when SteelSeries Sonar is not enabled.
- `ServerNotReadyError`: Raised when SteelSeries Sonar is not ready.
- `ServerNotRunningError`: Raised when SteelSeries Sonar is not running.
- `WebServerAddressNotFoundError`: Raised when the web server address is not found.
- `ChannelNotFoundError`: Raised when the specified channel is not found.
- `InvalidVolumeError`: Raised when an invalid volume value is provided.

## Example

Here is a complete example demonstrating the usage of the SteelSeries Sonar Python API:

```python
from steelseries_sonar_py import Sonar
from steelseries_sonar_py.exceptions import EnginePathNotFoundError

# Initialize Sonar object
try:
    sonar = Sonar(streamer_mode=False, app_data_path="C:\\path\\to\\coreProps.json")
except EnginePathNotFoundError:
    print("Engine not found!")
    quit()

# Retrieve volume data
volume_data = sonar.get_volume_data()
print("Volume Data:", volume_data)

# Set volume for the 'master' channel
channel = "master"
volume = 0.8
result = sonar.set_volume(channel, volume)
print(f"Set volume for {channel}:", result)

# Mute the 'game' channel
channel = "game"
muted = True
result = sonar.mute_channel(channel, muted)
print(f"Mute {channel}:", result)
```

## Special Thanks

Thanks to two contributors who made this package possible - [wex](https://github.com/wex/sonar-rev) for figuring out the API and [TotalPanther317](https://github.com/TotalPanther317/steelseries-sonar-py) for understanding streamer mode. Grateful for their efforts!
