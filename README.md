# vCenter vmdk/Ovf Exporter

## About
ovexport is a script which will log in to vCenter, search for a vm by name, then download all vmdks of that vm, as well
as create an ovf descriptor.

## Requirements
- vCenter user should have permissions to export a vm

## Installation
It's in the public pypi repository. Simply run:

```
$ pip install ovfexporter
```


## Running
All arguments and parameters are specified in the help menu when running the script

    $ usage: ovfexport [-h] -i VCENTER_HOST -u VCENTER_USER -p VCENTER_PASS -n
                 VM_NAME [-d DIRECTORY] [-w VCENTER_PORT]

    Converts, and downloads a vm by name from vCenter to OVF in specified
    directory, then uploads the image as an AMI. AMI will be uploaded using
    specified AWS profile, to specified regions.

    optional arguments:
      -h, --help            show this help message and exit
      -i VCENTER_HOST, --vcenter_host VCENTER_HOST
                            Hostname or Ip of vCenter API of VM
      -u VCENTER_USER, --vcenter_user VCENTER_USER
                            Username for vCenter authentication
      -p VCENTER_PASS, --vcenter_pass VCENTER_PASS
                            Password for authentication to vCenter API
      -n VM_NAME, --vm_name VM_NAME
                            Name of the VM in vCenter
      -d DIRECTORY, --directory DIRECTORY
                            Directory to save the vmdk temp file (defaults to temp
                            location
      -w VCENTER_PORT, --vcenter_port VCENTER_PORT
                            Port to use for communication to vcenter api. Default
                            is 443
