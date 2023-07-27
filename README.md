# Qtile Configuration 🪟🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Qtile](https://github.com/qtile/qtile) is a lightweight, highly customizable, and user-friendly window manager (UI - user interface) for Linux. It empowers you to efficiently control and organize your desktop using Python scripts. 
Dynamic tiling window managers, like Qtile, automatically adjust the arrangement of open windows in response to one another.

What do we have here? My Qtile configuration file!

Who can use it? Anyone can use it!

Who should use it? those who want to start learning about tiling window managers in Linux, as well as advanced users.

![system_pic](https://github.com/YanivZalach/qtile-config/assets/131461377/6a9460f3-54a3-4087-918f-759057a085c4)

## Requirements 🛠️

Before using this Qtile configuration, if you don't want to start configuring the config file, make sure you have the following programs installed on your system:

- Qtile (of course!) 🪶
- Python (required for Qtile configuration) 🐍
- Picom (to allow applications to be transparent) ✨
- Amixer (to display and change volume in the widgets) 🎧
- Kitty (terminal emulator, can be replaced with other terminal emulators) 🐱
- Alacritty (another terminal emulator option, can be canceled) 🍃
- Terminator (yet another terminal emulator option, can be canceled) ⚙️
- Zathura (PDF viewer, used for displaying keybindings, can be replaced with other PDF viewer) 📜
- Rofi (application launcher and menu) 🚀
- Thunar (file manager, can be replaced with your preferred file manager) 📂
- Google Chrome (or any web browser of your choice) 🌐
- Visual Studio Code (or any code editor of your choice) 💻
- Font Noto Sans font (used for widgets) ✒️
- Font Lilex Nerd Font Mono Regular font (used for widgets) 🖋️
- FPDF Python library (used for generating the keybindings PDF) 📚

## Installation 📦

1. Install the required programs listed above using your package manager or download them from their respective websites.

2. Open a terminal emulator by pressing:
  ```
  Super + Enter
  ```
  Note: The Super key is typically the "Windows" key on most keyboards.
  
3. Copy the config file, by copy and paste the following command into the terminal and press 'enter':

  ```bash
  git clone https://github.com/YanivZalach/qtile.git ~/.config/qtile
  ```

4. Restart Qtile to apply the new configuration by pressing:

  ```
  Super + control + r
  ```

5. Enable the autostart applications and the shutdown menu, by copy and paste the following command into the terminal and press 'enter':
  ```bash
  chmod +x ~/.config/qtile/autostart.sh
  chmod +x ~/.config/qtile/ro_sd.sh
  ```

## Usage 🚀

Use keybindings to navigate and control the window manager efficiently. 
Check the keybindings in the generated Mqtile.pdf file for a quick reference, by clicking on the date widget in the bar,
or by pressing:

```
Super + shift + i 
```

## Troubleshooting 🔧

The installation is not working:

* Make sure you have Git installed on your computer.
  Open the terminal and run the following command:
  ```bash
  git --version
  ```
  If Git is installed, you will see the installed version. If not, you need to install it using your package manager.
  Then retry the Installation.
  
* Check if the ~/.config/qtile directory already exists.
  Open the terminal and run the following command to check if the directory exists:
  ```bash
  ls ~/.config/qtile
  ```
  If the directory is found, you need to proceed with backing it up or renaming it.
  Do so by open the terminal and run the following command:
  ```bash
  mv ~/.config/qtile ~/.config/qtile_backup
  ```
  This will rename the existing 'qtile' directory to 'qtile_backup'.
  Retry the Installation.

Don't see a background? / See something other than "Home" in the first group?
* Check if your system path is /home/yaniv. Open the terminal and run the following command to check:
  ```bash
  pwd
  ```
  If the path is /home/yaniv, run the following command in the terminal:
  ```bash
  nano ~/.config/qtile/config.py
  ```
  Find the myWallpaper() function and replace it with the one below:
  
  ```
  def myWallpaper():
    return f"{home}/.config/qtile/dmirlea_norway.jpg"
  ```

  Find the myHomeGroup() function and replace it with the one below:
  
  ```
  def myHomeGroup():
    return "Home"
  ```

  Save the changes, then restart Qtile to apply the new updates.

I hope this helps! 😊

## Acknowledgments 🙏
thanks to the Qtile community for their support.


### Happy tiling! 🪶💻🐍
