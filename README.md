# Object Bucket
An easy and fun way to store python objects

____

## Table of contents
  - [Description](#DESCRIPTION)
  - [Installation](#INSTALLATION)
  - [Usage](#USAGE)


___
## Description
Object Bucket is a python package that allows you to store python packages permanently in a more user friendly way.

___
## Installation

The object-bucket package can be installed by using pip
```bash
pip install object-bucket
```

___
## Usage

  - Creating new bucket.
  ```python
  from object_bucket import Bucket
  
  test_bucket = Bucket("name-of-the-bucket")
  ```
  - Adding droplets to the bucket, droplets are considered as objects that you want to save permanently

  ```python
  test_obj = [1, 2, 3, 4]
  test_bucket.add_droplet("droplet-name", test_obj)
  ```
  Trying to add a droplet with the same name will cause an error

  - Modifying a droplet
  ```python
  new_obj = {1: "a"}
  test_bucket.modify_droplet("droplet-name", new_obj)
  ```
  Trying to modify a droplet that does not exists will cause an error

  - Saving a bucket
  All the things mentioned above will not added or saved permanently to do so it is necessary to save the bucket
  ```python
  test_bucket.save_bucket()
  ```
 - Retrieving values from a bucket
 ```python
 from object_bucket import Bucket
 test_bucket = Bucket("name-of-the-bucket")
 a = test.bucker.get_droplet("droplet-name")
 print(a)  # {1: "a"}
 ```

 Trying to get a droplet that does nor exists will cause an error.