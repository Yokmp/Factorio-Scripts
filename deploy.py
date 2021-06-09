#!/usr/bin/env python3

""" Factorio mod deployement script """

import os ,sys, shutil, zipfile, json, platform

#region ----------------------------------- Boring Settings
deploy_mod  = True       # create a zip file or not

## Blacklist
exclude     = ["vscode", ".git", ".py", "workspace", ".xcf", "_release_"]

## Get information from filesystem
workspace   = "."
user_dir    = os.path.expanduser('~')
deploy_dir  = ""
mod_name    = ""
mod_title   = ""
version     = ""

## Path settings - deploy_dir should end in factorio/mods so a new version can be tested easily
if platform.system() == "Windows":
  deploy_dir = os.path.join("F:\\", "Games", "Factorio_ModTest", "mods") # os.path.join(user_dir, "AppData", "Roaming", "Factorio", "mods")
else:
  deploy_dir = os.path.join(user_dir, ".factorio", "mods")
#endregion -----------------------------------

if not os.path.exists(deploy_dir):
  print("\nNo Factorio mod directory found. Aborting.")
  sys.exit(-1)

## Get informations from info.json TODO: update json depending on user settings
with open("info.json") as info:
  js = json.load(info)
  version = js["version"] if version == "" else version
  mod_name = js["name"] if mod_name == "" else mod_name
  mod_title = js["title"] if mod_title == "" else mod_title

if (mod_name == ""):
  print("\nNo name found. Aborting.")
  sys.exit(-1)

if (mod_title == ""):
  print("\nNo title found. Aborting.")
  sys.exit(-1)

if (version == ""):
  print("\nNo version found. Aborting.")
  sys.exit(-1)

text = " Generating files for: " + mod_title + " - version: " + version + " "
print("\n"+text.center(len(text)+22, "-"))

## ----------------------------------- Secret Settings
mod_name_full   = mod_name + "_" + version
mod_deploy_dir  = os.path.join(deploy_dir, mod_name_full)
zip_name        = mod_name_full + '.zip'
zip_file_path   = os.path.join(workspace, "_release_")
zip_file        = os.path.join(zip_file_path, mod_name + "_" + version+".zip")
zip_temp_dir    = os.path.join(workspace, mod_name_full)
## -----------------------------------

def match_pattern(string):
  for e in exclude:
    if string.find(e) != -1: return True
  return False
## ----------------------------------- COLLECTING
for root, subdirs, files in os.walk(workspace):
  if match_pattern(root): continue

  for filename in files:
    if match_pattern(filename): continue

    file_path = os.path.join(root, filename)

    if os.path.isfile(file_path):
      print('File: %s \t %s' % (mod_name_full, filename))
      os.makedirs(os.path.join(zip_temp_dir, os.path.dirname(file_path[2:])), exist_ok=True)
      shutil.copy(file_path, os.path.join(zip_temp_dir, os.path.dirname(file_path[2:])))

## ----------------------------------- ZIPING
if os.path.exists(zip_file):
  print("\n%s already exists." %zip_file)
  quest = input("[R]emove or [A]bort? ")
  if quest == "r" or quest == "R":
    os.remove(zip_file)
  else:
    shutil.rmtree(zip_temp_dir)
    sys.exit("\n\tScript aborted with '"+quest+"'\n\tNo changes where made.\n")

print('\nCreating\t %s' % zip_name)
zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

for root, subdirs, files in os.walk(zip_temp_dir):
  for filename in files:
    f = os.path.join(root, filename)
    zipf.write(f)
zipf.close()

shutil.rmtree(zip_temp_dir)
os.makedirs(zip_file_path, exist_ok=True)
shutil.move(zip_name, zip_file_path)

if deploy_mod:
  print("Deploying\t %s%s" %(deploy_dir, zip_name))
  shutil.copy(zip_file, deploy_dir)

success = " Release " + version + " completed "
print("\n"+success.center(len(text)+22, "-")+"\n")
