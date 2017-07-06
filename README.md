# vCenter vmdk/Ovf Exporter

## About
ovexport is a script which will log in to vCenter, search for a vm by name, then download all vmdks of that vm, as well
as create an ovf descriptor.

## Requirements
- vCenter user should have permissions to export a vm

## Installation
Ensure you have the local silo repository in your .pip config and:

```
$ pip install ovfexporter
```


## Running
All arguments and parameters are specified in the help menu when running the script

    $ ovfexport -i 10.3.2.5 -u <vc_user> -p <vc_password> -n <vm_name> -d <download_directory>
