# A small tool collection which will grow over time when i think the code is somewhat presentable ...


If you have any suggestion then please let me know.

## deploy.py

A small script to help zip and copy your mod.

<img src=deploy_01.jpg>

### The default folder structure is like:

Your_Mod  
|- \_release_ (youll find your zip files here)  
|- all   
|- other  
'- folders (like graphics, locale, etc)

There are some settings on top of the file like paths and exclude.
Excluding files and folders goes by name and are read as literals so a dot is just a dot.  
This means, you should be as exact as possible. So look into your zip and check just to be shure ;)

Mod-version and name are read from the info.json file.  

### Args:
- *-h* help: prints a short usage and description of all available arguments.
- *-v* verbose: shows some additional informations like the filenames and paths. It the also asks you if an existing zip should be overwritten or not (default False)
- *-d* deploy: wether or not to deploy (copy to Factorio/mods/) or not. In both cases a zip is generated and copied to \_release_ (default True)

### Usage:  
``C:\Path\To\Mod_Name> python deploy.py`` or  
``PS C:\Path\To\Mod_Name> .\deploy.py`` (no output as it will launch another terminal instance and close it afterwards)


## mipmap.py

Generates mipmaps from png

<img src=mipmap_01.jpg>

Have a look at the presets section in the file to change like the in/out folders.  
It can read the info.json but will work in any folder.

### Args:
- *-h*       help: prints a short usage and description of all available arguments.
- *-v*       verbose: shows every processed file (default False)
- *-c*       crop: crop the canvas (default False)
- *-s*       set icon size to the specified size _-s 128_ (min 32; default 64)
- *-m*       set mipmap amount _-m 2_ (default 4)
- *-i --in*  input Folder (default graphics/\_single/)
- *-o --out* output Folder (default graphics/\_single/)

### Usage:  
``C:\Path\To\Mod_Name> python mipmap.py`` or  
``PS C:\Path\To\Mod_Name> .\mipmap.py`` (no output as it will launch another terminal instance and close it afterwards)
