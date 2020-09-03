# edx_azure_profile_picture

## Features

- This plugin is to download and set user profile picture from Microsoft API

## Installation

### Open edX devstack

- Clone this repo in the src folder of your devstack.
- Open a new Lms/Devstack shell.
- Install the plugin as follows: pip install -e git+https://github.com/thinhvo-groove/edx-get-profile-picture-from-ms-plugin#egg=edx_azure_profile_picture_plugin
- Add edx_azure_profile_picture to the list of social auth pipline

```
SOCIAL_AUTH_PIPELINE = [
        ...
        'edx_azure_profile_picture.pipeline.download_profile_image',
    ]
```

- Restart Lms service.

## Usage

Include a usage description for your plugin.

## Contributing

Add your contribution policy. (If required)
