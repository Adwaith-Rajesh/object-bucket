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
  All the things mentioned above will not be added or saved permanently, to do so it is necessary to save the bucket.
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
 Trying to get a droplet that does not exists will cause an error.

 - Get all the runtime droplets
 ```python
 drop1 = [1, 2, 3, 4]
 drop2 = "Hello"
 drop3 = {1: "a", 2: "b"}
 test_bucket.add_droplet("drop1", drop1)
 test_bucket.add_droplet("drop2", drop2)
 test_bucket.add_droplet("drop3", drop3)

 # to get all the droplets
 a = test_bucket.get_all_droplets()
 print(a)

 # output
 {"drop1": [1, 2, 3, 4], "drop2": "Hello", "drop3": {1: "a", 2: "b"}}
 ```
 - Deleting a bucket
 To delete the bucket and to clear the runtime storage of all the droplets.
 ```python
 test_bucket.delete_bucket()
 ```

 ## Using the context manager.
 It might be a hastle to remember to save to bucket, so you can use the context manager to avoid using the ```save_bucket``` method.

 **Note**: Using ```Bucket().delete_bucket``` inside the context manager is useless as at the end the file will be saved automatically.

 ```python
 from object_bucket import Bucket
 
 with Bucket("name-of-the-bucket") as b:
   # code to execute
   b.add_droplet("name", 1)
   # ...etc
   b.delete_bucket()  # wont work as the file will be again saved,
   # but the runtime contents will be cleared
 ```