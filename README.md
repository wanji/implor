# implor
Image Explorer


Example:

```
# start the image server
cd $working_dir
run_implor 8080
```

```
# Create a symbol link to your image folder under `$working_dir/static`
cd $working_dir/static
ln -sv path_to_your_image_folder link_name
```

Then you can explorer the image folder via:
```
http://0.0.0.0:8080/link_name
```
