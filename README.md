# XL Release Remote Script Task Password plugin v1.0.0

[![Build Status][xlr-remotescript-taskpassword-plugin-travis-image]][xlr-remotescript-taskpassword-plugin-travis-url]
[![License: MIT][xlr-remotescript-taskpassword-plugin-license-image]][xlr-remotescript-taskpassword-plugin-license-url]
![Github All Releases][xlr-remotescript-taskpassword-plugin-downloads-image]

[xlr-remotescript-taskpassword-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-remotescript-taskpassword-plugin.svg?branch=master
[xlr-remotescript-taskpassword-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-remotescript-taskpassword-plugin
[xlr-remotescript-taskpassword-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-remotescript-taskpassword-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-remotescript-taskpassword-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-remotescript-taskpassword-plugin/total.svg

## Preface

This document describes the functionality provided by the XL Release Remote Script Task Password plugin.

See the [XL Release reference manual](https://docs.xebialabs.com/xl-release) for background information on XL Release and release automation concepts.  


## Overview

This plugin provides a way to supply a password on the command line without exposing it in the XL Release GUI.

## Requirements

XL Release 6.0+

## Usage ##

* Set taskPasswordToken to the token to be replaced on the command line
* Set taskPassword to a password or password variable
* Both items must be specified for the replacement to occur

![task config](images/task-config.png)