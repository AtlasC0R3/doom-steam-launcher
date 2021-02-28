"""
MIT License

Copyright (c) 2021 atlas_core

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import sys
import subprocess
import shutil
import glob
import requests
import zipfile

wad = "DOOM2.WAD"
# If you wanted Doom 2 compatibility, you could put "DOOM2.WAD" instead.


def pause():
    os.system('pause')
    return


def download_extract(url: str, dir: str):
    print(f"Downloading {url}")
    r = requests.get(url)
    print("Downloaded, saving...")
    if not os.path.exists(dir):
        os.mkdir(dir)
    fpath = dir + 'downloaded.zip'
    open(fpath, 'wb+').write(r.content)
    print("Extracting...")
    zipref = zipfile.ZipFile(fpath)
    zipref.extractall(dir)
    print("Extracted.")
    zipref.close()
    os.remove(fpath)


def update_brutality():
    print("Downloading Project Brutality... This might take a while.")
    r = requests.get("https://github.com/pa1nki113r/Project_Brutality/archive/master.zip")
    print("Downloaded, saving... This might also take a while.")
    if os.path.exists('base/gz/Project_Brutality.pk3'):
        os.remove('base/gz/Project_Brutality.pk3')
    open('base/gz/Project_Brutality.pk3', 'wb+').write(r.content)
    print("Project Brutality downloaded and saved.")


if len(sys.argv) == 1:
    print("Please run this script in Steam (by selecting \"Launch DOS Version\", with classic controls or not).")
    pause()
    exit(1)

print("1: Original DOSBox version\n"
      "2: GZDoom/LZDoom\n"
      "3: Chocolate Doom\n"
      "4: Brutal Doom")
while True:
    how = input("How do you want to run your Doom? ")
    possible = [1, 2, 3, 4]
    if how.isnumeric():
        how = int(how)
        if how in possible:
            break
        else:
            print("That's, uh, not in the options.\n")
    else:
        print("That's not even a number.\n")
    

if how == 1:
    args = []  # ['E:\\Steam\\steamapps\\common\\Ultimate Doom\\base\\dos\\dosbox.exe', '-conf', 'base\\dos\\ultimatem.conf', '-fullscreen', '-exit']
    for arg in sys.argv:
        args.append(arg.replace('base\\', 'base\\dos\\'))
    cfgpath = args[2]
    with open(cfgpath, 'r+') as conf:
            newconf = conf.read().replace('mount c .\\base\n', 'mount c .\\base\\dos\n')
            open(cfgpath, 'w').write(newconf)
    saves = glob.glob('base\\DOOMSAV*.DSG', recursive=True)
    for savefile in saves:
        dest = savefile.replace('base\\', 'base\\dos\\')
        if os.path.isfile(dest):
            os.remove(dest)
        os.rename(savefile, dest)
    subprocess.run(args)  # dooming time
    # user done gaming
    print("Moving saves to somewhere Steam Cloud will work")
    saves = glob.glob('base\\dos\\DOOMSAV*.DSG', recursive=True)
    for savefile in saves:
        os.rename(savefile, savefile.replace('base\\dos\\', 'base\\'))
elif (how == 2) or (how == 4):
    args = []
    if not (os.path.exists('base/gz/gzdoom.exe') or os.path.exists('base/gz/lzdoom.exe')):
        print("\nSeems like you're missing GZDoom. Which version would you like to download?\n"
              "(If you do not want to download GZDoom/LZDoom, you can close this window)\n"
              "1: GZDoom\n2: LZDoom\n")
        possible = ["1", "2"]
        while True:
            choice = input()
            if choice in possible:
                break
            else:
                print("What? What is that?\n")
        if choice == "1":
            url = "https://github.com/coelckers/gzdoom/releases/download/g4.5.0/gzdoom-4-5-0-Windows-64bit.zip"
        else:
            url = "https://github.com/drfrag666/gzdoom/releases/download/3.87c/LZDoom_3.87c_x64.zip"
        download_extract(url, 'base\\gz\\')
    if how == 4:
        if not os.path.exists('base/gz/Project_Brutality.pk3'):
            # download project bruality, typo intended
            update_brutality()
        if os.path.exists('base/gz/gzdoom.exe'):
            args = ['base/gz/gzdoom.exe', 'base/gz/Project_Brutality.pk3']
            thing = input("If you would like to update Brutal Doom, please enter 'y'\nIf not, just press Enter.\n")
            if thing.lower().startswith('y'):
                update_brutality()
        else:
            print("Please install GZDoom before launching Brutal Doom.")
            pause()
            exit(0)
    # Because of the way GZDoom saves things, it is incompatible with Steam Cloud.
    # So all we have to do is just copy the WAD then delete it once the user is done.
    shutil.copyfile(f'base/dos/{wad}', f'base/gz/{wad}')
    if not args:
        # not brutal doom
        if os.path.exists('base/gz/gzdoom.exe'):
            args = ['base/gz/gzdoom.exe']
        else:
            args = ['base/gz/lzdoom.exe']
    subprocess.run(args)
    # user done gaming
    os.remove(f'base/gz/{wad}')
elif how == 3:
    if not os.path.exists('base/choco/chocolate-doom.exe'):
        download_extract('https://www.chocolate-doom.org/downloads/3.0.1/chocolate-doom-3.0.1-win32.zip', 'base\\choco\\')
    subprocess.run(["choco\\chocolate-doom.exe", "-iwad",  f"dos\\{wad}"], cwd="base\\")
    # as easy as that. my job here is done.
