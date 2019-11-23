# implor - Image Explorer

Suppose you have images under `./images`, you can start the image server via:
```
run_implor -p 8080 -d ./images
```

Then you can explorer the image folder via:
```
http://0.0.0.0:8080
```

There are some GET opts
```
w: image width
h: image height
n: images per page
s: show the s-th ~ (s+n-1)-th images 
```

Example:
```
http://0.0.0.0:8080?s=4&n=4&w=1024
```
This will show the 4th~7th images with `width=1024`;

Alternatively, you can put images under `sub-directory`, suppose you have directory structure like this:
```
images/
├── imgs001
│   ├── 0000.jpg
│   └── 0001.jpg
└── imgs002
```
after starting the image server via `run_implor -p 8080 -d ./images`, you can access images from `images/imgs001` by
```
http://0.0.0.0:8080/imgs001?s=4&n=4&w=1024
```
