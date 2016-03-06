# Ubuntu Download Organizer

I just made a simple Python script to organize my Downloads directory on my Ubuntu Desktop :D

## How does it work?
For example, your download directory located at /home/superman/Downloads with structure like
```
Dowloads/
	d-- data/
	d-- nginx/
	--- bootstrap.zip
	--- MD5 Specs.pdf
	--- Security_Guide.pdf
	--- tinymce_4.3.0.zip
	--- webzash-v2.6.tar.gz
	--- Testing.docx
```

After running my script, all files you downloaded would be organized, group all file with the same file extension into a directory, something like below structure
```
Dowloads/
	d-- UDO_Office/
	---------- Testing.docx
	d-- UDO_Portable_Document/
	---------- MD5 Specs.pdf
	---------- Security_Guide.pdf
	d-- UDO_Compressed/
	---------- bootstrap.zip
	---------- tinymce_4.3.0.zip
	---------- webzash-v2.6.tar.gz
```
You can change the **"UDO_"** prefix by modifying DIR_PREFIX variable (It is default value, stand for Ubuntu Download Organizer)

## How to run?

```
$ git clone https://github.com/doantranhoang/udownload_organizer.git
$ cd udownload_organizer
$ python main.py
+-------------------+
|2016-03-05 10:06:36|
+-------------------+
[+] Make directory /home/superman/Downloads/UDO_Office
---> Move file Testing.docx to UDO_Office/Testing.docx
[+] Make directory /home/superman/Downloads/UDO_Portable_Document
---> Move file MD5 Specs.pdf to UDO_Portable_Document/MD5 Specs.pdf
---> Move file MD5 Security_Guide.pdf to UDO_Portable_Document/Security_Guide.pdf
[+] Make directory /home/superman/Downloads/UDO_Compressed
---> Move file bootstrap.zip to UDO_Compressed/bootstrap.zip
---> Move file tinymce_4.3.0.zip to UDO_Compressed/tinymce_4.3.0.zip
---> Move file webzash-v2.6.tar.gz to UDO_Compressed/webzash-v2.6.tar.gz
```
## Running this script daily

For example, your main.py located at /home/superman/Scripts/udownload_organizer/main.py and you want it run every hours. Using a cronjob to make it automatic sorting your files
```
0 * * * * /usr/bin/python /home/superman/Scripts/udownload_organizer/main.py >> /home/superman/Scripts/udownload_organizer/log.txt
```
*Note: You should append script activity log into '>> /home/superman/Scripts/udownload_organizer/log.txt' for auditing.*
