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

    $ ovfexport -h
    usage: amiupload [-h] -r AWS_REGIONS [AWS_REGIONS ...] -a AWS_PROFILE -b
                 S3_BUCKET -f VMDK_UPLOAD_FILE [-n AMI_NAME] [-d DIRECTORY]

    Uploads specified VMDK file to AWS s3 bucket, and converts to AMI

    optional arguments:
      -h, --help            show this help message and exit
      -r AWS_REGIONS [AWS_REGIONS ...], --aws_regions AWS_REGIONS [AWS_REGIONS ...]
                            list of AWS regions where uploaded ami should be
                            copied. Available regions: ['us-east-1', 'us-east-2',
                            'us-west-1', 'us-west-2', 'ca-central-1', 'eu-west-1',
                            'eu-central-1', 'eu-west-2', 'ap-northeast-1', 'ap-
                            northeast-2', 'ap-southeast-2', 'ap-south-1', 'sa-
                            east-1'].
      -a AWS_PROFILE, --aws_profile AWS_PROFILE
                            AWS profile name to use for aws cli commands
      -b S3_BUCKET, --s3_bucket S3_BUCKET
                            The aws_bucket of the profile to upload and save vmdk
                            to
      -f VMDK_UPLOAD_FILE, --vmdk_upload_file VMDK_UPLOAD_FILE
                            The file to upload if executing
      -n AMI_NAME, --ami_name AMI_NAME
                            The name to give to the uploaded ami. Defaults to the
                            name of the file
      -d DIRECTORY, --directory DIRECTORY
                            Directory to save temp aws config upload files
