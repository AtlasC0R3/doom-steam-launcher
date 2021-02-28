# doom-steam-launcher
A simple Python 3 launcher, used to facilitate installing Doom source ports for Steam.

This should also be compatible with the Steam overlay if possible.

Tested with [The Ultimate DOOM](https://store.steampowered.com/app/2280/) and [DOOM II: Hell on Earth](https://store.steampowered.com/app/2300/) in the Steam launcher on Windows 10,
though it will probably be compatible with Proton for Linux *(I have not tested yet)*.

![Screenshot of the launcher in action](https://user-images.githubusercontent.com/39468657/109404115-0fc72580-7931-11eb-8b57-58b234472158.png)

## Installation

1. Make sure you have installed a Doom game (that uses the old `*.wad` format). For example, [The Ultimate DOOM](https://store.steampowered.com/app/2280/).
The `base` folder should contain all of the DOS game files.

2. Move all game files (`dosbox.exe`, `DOOM.WAD`, `dosbox.conf`, etc.) to a folder called `dos`.
Your file structure should be `C:\Program Files (x86)\Steam\steamapps\common\Ultimate Doom\base\dos\dosbox.exe` *(if you're using The Ultimate DOOM, though DOOM II should look similar)*.

3. Drop the launcher in the base folder (**not** the folder named `dos`), and rename it `dosbox.exe`
If you downloaded the `*.exe` file from the releases, `doom.exe` will be for [The Ultimate DOOM](https://store.steampowered.com/app/2280/), `doom2.exe` will be for [DOOM II: Hell on Earth](https://store.steampowered.com/app/2300/).
If you wish to add compatibility to another game, please check the `Compiling` section

4. Run your Doom game on Steam
If your game received the Unity engine port, launch the DOS versions.

You *should* receive a terminal window that lists things like "Original DOSBox version", "GZDoom/LZDoom", "Chocolate Doom", etc.
If you do, that means you have installed this launcher correctly!

## Usage
This launcher should be pretty straightforward.

`Original DOSBox version` will simply launch DOSBox and run Doom, as it normally would without this launcher.
If you launched Doom with "classic controls", the classic controls will apply.
This is compatible with Steam cloud saves, but not with the Steam overlay.

`GZDoom/LZDoom` will launch GZDoom or LZDoom, depending on which is currently downloaded.
If it is not downloaded, you will have the option to download either GZDoom or LZDoom.
This is compatible with the Steam overlay however is not compatible with Steam cloud saves.

`Chocolate Doom` will launch, well, Chocolate Doom, and download it, if not already done.
This is both compatible with the Steam overlay and Steam cloud saves.

`Brutal Doom` will require GZDoom to already be downloaded.
If Brutal Doom isn't already downloaded, it will do so.
If it is already downloaded, it will give the user the opportunity to update it.

## Compiling
To compile, use `pyinstaller` to compile `main.py` to an \*.exe file that can be launched by Steam.
If you wanted to change which `*.wad` file that would be used, change the `wad` variable inside the `main.py` script.

This is the default command:
`pyinstaller --noconfirm --onefile --console  main.py -n dosbox.exe`
Your file should be in dist/dosbox.exe. I named it "dosbox.exe" because Steam will attempt launching base/dosbox.exe, 
so naming the executable dosbox.exe right after it's compiled is just some convenience step.

You could also use the VSCode build tasks that are in `.vscode/`, if you use VSCode/VSCodium.
