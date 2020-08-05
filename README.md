# Nba Streams Kodi Addon

**NOTICE: The authors of this plugin do not actually create the streams. They created an addon that lets you view the streams inside of Kodi**

This repository contains the code required to create a video add-on for [Kodi](https://kodi.tv/).

This plugin pulls the stream information from [nba-streams.xyz](http://nba-streams.xyz/schedule/).


## Development

Make sure to:
`pip install -r requirements.txt`

The actual plugin can be found inside of the `kodi-addon` directory and any files not in that directory are used to test and debug the code that parses [nba-streams.xyz](http://nba-streams.xyz/schedule/).

To debug Kodi, the log files on a Mac can be found at `/Users/{username}/Library/Logs/kodi.log`, replace {username} with your user.

Verify that the plugin code works by running:

`kodi-addon-checker plugin.video.nbastreams --branch=leia`

NOTE: Make sure that the branch is correct for the version of kodi being used.


## [MACOS] Creating the zip file for the addon

Run the following commands inside of the terminal:

Create the zip file:
`zip -r plugin.video.nbastreams.zip ./plugin.video.nbastreams/ -x ".*" -x "*.DS_Store" -x "__MACOSX"`


## Installing the zip file

Instructions on how to install the zip file can be found [here](https://kodi.wiki/view/HOW-TO:Install_add-ons_from_zip_files).