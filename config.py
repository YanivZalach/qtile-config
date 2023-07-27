
#__/\\\________/\\\______________________/\\\_______________/\\\\\\\\\\\\\\\_        
# _\///\\\____/\\\/_____________________/\\\\\______________\////////////\\\__       
#  ___\///\\\/\\\/_____________________/\\\/\\\________________________/\\\/___      
#   _____\///\\\/_____________________/\\\/\/\\\______________________/\\\/_____     
#    _______\/\\\____________________/\\\/__\/\\\____________________/\\\/_______    
#     _______\/\\\__________________/\\\\\\\\\\\\\\\\_______________/\\\/_________   
#      _______\/\\\_________________\///////////\\\//______________/\\\/___________  
#       _______\/\\\___________________________\/\\\_______________/\\\\\\\\\\\\\\\_ 
#        _______\///____________________________\///_______________\///////////////__

# Import necessary modules from libqtile library
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import os

# Import FPDF module for generating a PDF of key bindings
from fpdf import FPDF

# Define the modifier key (mod key) for keybindings
mod = "mod4"

# Guess the terminal to be used (default terminal if not specified)
terminal = guess_terminal()
#The user home path
home = os.path.expanduser('~')
# Function to run at startup once. It is used to run commands specified in the 'autostart.sh'
@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])
        
# Define the key bindings
keys = [
    # Launches Zathura with a specific PDF file
    Key([mod,"shift"],"i", lazy.spawn("setsid zathura ~/Mqtile.pdf"),desc="Info system keybindings"),
    
    # Shutdown or reboot the PC using a custom bash script
    Key([mod, "shift"], "x", lazy.spawn(f'{home}/.config/qtile/bash_scripts/ro_sd.sh'), desc="Shutdown || Reboot"),
    
    # Switch between US and IL keyboard layouts
    Key(["mod1"],"shift_L",  lazy.widget["keyboardlayout"].next_keyboard(), desc="Keyboard layout (US || IL)"),
    
    # Terminal emulators
    Key([mod], "t", lazy.spawn("kitty"), desc="Terminal kitty -> bash"),
    Key([mod], "a", lazy.spawn("alacritty"), desc="Terminal alacritty ->fish"),
    Key([mod], "m", lazy.spawn("terminator"), desc="Terminal terminator ->zsh"),
    
    # Close the focused window
    Key([mod], "c", lazy.window.kill(), desc="Close focused window"),
    
    # Launch different rofi menus for application, commands, windows, and ssh
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Launch rofi dmenu (all apps)"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Launch rofi menu (commands)"),
    Key([mod], "w", lazy.spawn("rofi -show window"), desc="Launch rofi windows (active windows)"),
    Key([mod], "s", lazy.spawn("rofi -show ssh"), desc="Launch rofi ssh"),
    
    # Launch Ranger file browser using kitty terminal
    Key([mod], "b", lazy.spawn("kitty -e ranger"), desc="Ranger file browser"),
    
    # Launch commonly used applications
    Key([mod], "e", lazy.spawn("thunar"), desc="Thunar file manager"),
    Key([mod], "i", lazy.spawn("/usr/bin/google-chrome-stable"), desc="Google Chrome"),
    Key([mod], "v", lazy.spawn("code"), desc="VS code"),
    
    # Toggle between different layouts or fullscreen
    Key([mod], "f", lazy.next_layout(), desc="Toggle tiling or fullscreen"),
    
    # Toggle floating layout for the focused window
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle floating layout\n\tSuper + Left_mouse_click\t:-)\t\tDrag floating windows\n\tSuper + Right_mouse_click\t:-)\t\tChange size of floating windows"),
    
    # Move focus between windows
    Key([mod], "space", lazy.layout.next(), desc="Move focus to next window"),
    
    # Volume control bindings (using function keys and XF86Audio keys)
    Key([mod], "f7", lazy.spawn("amixer -q sset Master 5%-"),desc="Lower volume"),
    Key([mod], "f8", lazy.spawn("amixer -q sset Master 5%+"),desc="Raise volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-"),desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+"),desc="Raise volume"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -q sset Master toggle"),desc="Mute volume toggle"),
    
    # Reload Qtile configuration and logout Qtile
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the Qtile config"),
    Key([mod, "control"], "g", lazy.shutdown(), desc="Logout Qtile"),
    
    # Reset the size of windows to default layout size
    Key([mod], "n", lazy.layout.normalize(), desc="Reset to default layout size"),
    
    # Toggle between split and unsplit sides of the stack
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    Key([mod, "shift"],"Return",lazy.layout.toggle_split(),desc="Toggle split or unsplit sides of stack",),
    
    # Move focus between windows in different directions
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    
    # Move windows between left/right columns or move up/down in the current stack
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow or shrink windows in different directions
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    ]

# Mouse bindings for dragging floating windows
mouse = [#This doesn't have a desc attribute, so its description is set in the 'Toggle floating layout' above manually.
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

 
#We call the function after we have defined the key bindings for the groups
def Mqtile_info(keys):
    """
    Description:
        This function takes a list of key bindings and creates a text file ('Mqtile.txt')
        and a PDF file ('Mqtile.pdf') containing a formatted representation of the key bindings.
        The generated files will contain the key modifiers, key, and description for each key binding.
    """
    # Create the 'Mqtile.txt' file
    with open("Mqtile.txt","w") as file:
        # ASCII art title to be included in the files
        ascii_art = '''
#    #   #   #   #####
 #  #    #####      #
  #          #    #
 #           #   #####
'''
        file.write(ascii_art)
        for key in keys:
            mainK=""
            for k in key.modifiers:
                p=k # the text that is simple for the user that we're putting
                if(k=='mod4'):
                    p='Super'
                elif(k=='mod1'):
                    p='Alt'
                mainK+=f" {p} +"
            keyk=key.key
            if keyk.startswith("XF86"):
                keyk = keyk[4:]
            add=mainK+"\t"+str(keyk)+"\t:-)\t\t"+str(key.desc)+"\n"
            file.write(add) 
        file.write(ascii_art)
    
    # Convert the 'Mqtile.txt' file to a PDF file
    pdf = FPDF() # Save FPDF() class into a variable 'pdf'
    pdf.add_page() # Add a page
    pdf.set_font("Courier", size = 13) # Set style and size of font
    f = open("Mqtile.txt", "r") # Open the text file in read mode
    for x in f:    # Insert the texts in to the PDF
        pdf.cell(200, 10, txt = x, ln = 1, align = 'L')
    pdf.output("Mqtile.pdf") # Save the PDF with name 'Mqtile.pdf'



# Function to set the Home Grop based on the user's home path
def myHomeGroup():
    # Check if the home directory path is '/home/yaniv' (the creator of the config)
    if(home == "/home/yaniv"):
        # If the user is 'yaniv' (the creator of the code),
        # return the desired Home Grop for personal use
        return "Y4Z"
    # If the user is not 'yaniv' (new user cloning the repo),
    # set the Home Grop to a default one for a pleasant initial experience
    return "Home"

#layout of windows
layout_in_init='Max'
def init_group_names():
    """
        This function sets up the names and layout preferences for different groups.
        Each group is represented as a tuple with the format (name, layout_preferences).
        The 'layout_preferences' variable is set to the 'layout_in_init' value defined earlier.
        Modify the 'layout_in_init' variable to change the default layout for all groups.
    """
    return [
        (myHomeGroup(),{'layout':layout_in_init}),
        ("Terminal",{'layout':layout_in_init}),
        ("www",{'layout':layout_in_init}),
        ("Code",{'layout':layout_in_init}),
        ("Static",{'layout':layout_in_init}),]
    
def init_groups():
    """
        This function creates Group objects based on the group names and layout preferences
        defined in the 'group_names' variable. It uses the 'init_group_names()' function
        to get the necessary information. The 'init_group_names()' function should be called
        before calling this function.
    """
    return [Group(name, **kwargs) for name, kwargs in group_names]

# When the script is run as the main window manager configuration, not the main itself
if __name__ in ["config", "__main__"]:
    # Set up group names and create Group objects
    group_names = init_group_names()
    groups = init_groups()

# Key bindings to switch between groups and move windows between groups
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen(),desc=f"Switch to group '{name}'")) # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name),desc=f"Send current window to group '{name}'")) # Send current window to another group



# Call the function to generate the files with the provided keys
Mqtile_info(keys)



# Define available layouts
layouts = [
    layout.Columns(border_focus=["#1353e8", "#8d69db"],border_normal=["#96e4fa", "#ffffff"], border_width=4, margin=11),
    layout.Max(),
]

widget_defaults = dict(
    font="Lilex Nerd Font Mono Regular",
    fontsize=15,
    padding=15,
)
extension_defaults = widget_defaults.copy()


# Function to set the wallpaper based on the user's home path
def myWallpaper():
    # Check if the home directory path is '/home/yaniv' (the creator of the config)
    if(home == "/home/yaniv"):
        # If the user is 'yaniv' (the creator of the code),
        # return the desired wallpaper path for personal use
        return f"{home}/Pictures/b_g/hlightbulb_greece.jpg"
    # If the user is not 'yaniv' (new user cloning the repo),
    # set the wallpaper to a default one for a pleasant initial experience
    return f"{home}/.config/qtile/dmirlea_norway.jpg"


screens = [
            Screen(
                        top=bar.Bar(
                        [
                            # GroupBox widget to display group names and windows
                            widget.GroupBox(
                                highlight_method='line',                    # Set the highlight method to 'line'
                                highlight_color=['#63c0c2', '#63c0c2'],      # Set the text color when selected and not selected
                                ),

                            # Widget to display the name of the currently focused window
                            widget.WindowName(foreground='#fcf8c0',),

                            # Custom TextBox widget for 'Lay' (Layout) text display
                            widget.TextBox(
                                font="Noto Sans",
                                text="Lay:",
                                padding = 0,
                                fontsize=13
                            ),
                            # CurrentLayout widget to display the current layout
                            widget.CurrentLayout(
                                font = "Noto Sans Bold",
                            ),

                            # Custom TextBox widget for 'Mem' (Memory) text display
                            widget.TextBox(
                                font="Noto Sans",
                                text="Mem:",
                                padding = 0,
                                fontsize=13
                            ),
                            # Memory widget to display memory usage and launch htop on click
                            widget.Memory(
                                font="Noto Sans Bold",
                                format='{MemUsed:.1f}M / {MemTotal:.1f}M',
                                update_interval = 1,
                                fontsize = 12,
                                mouse_callbacks={'Button1':lazy.spawn("kitty -e htop")}
                            ),

                            # Custom TextBox widget for 'Net' (Network) text display
                            widget.TextBox(
                                font="Noto Sans",
                                text="Net:",
                                padding = 2,
                                fontsize=13
                            ),
                            # Net widget to display network interface information and launch connection editor on click
                            widget.Net(
                                font="Noto Sans Bold",
                                interface="enp2s0",#how to find it:   run in terminal: ifconfig, find the value
                                format="{down} ↓↑ {up}",
                                padding = 7,
                                mouse_callbacks={'Button1':lazy.spawn("nm-connection-editor")}
                            ),

                            # Custom TextBox widget for 'Vol' (Volume) text display
                            widget.TextBox(
                                font="Noto Sans",
                                text="Vol:",
                                padding = 2,
                                fontsize=13
                            ),
                            # Volume widget to display volume level and control with mouse scroll and click
                            widget.Volume(font="Noto Sans Bold",padding = 4,),
                            widget.Volume(emoji=True,padding = 2,),

                            # Custom TextBox widget for 'Key' (Keyboard Layout) text display
                            widget.TextBox(
                                font="Noto Sans",
                                text="Key:",
                                padding = 7,
                                fontsize=13
                            ),
                            # KeyboardLayout widget to display and switch between configured keyboard layouts
                            widget.KeyboardLayout(
                                configured_keyboards=['us', 'il'], 
                                foreground='#ffffff',
                                font = "Noto Sans Bold",
                                padding = 5,
                                ),

                        # Commented out Battery widget (uncomment to use in a laptop)     
                        #    widget.TextBox(# Widget to display text
                        #        font="Noto Sans",
                        #        text="Battery:",
                        #        padding = 7,
                        #        fontsize=13
                        #   ),
                        #   widget.Battery(# Battery widget to display battery status
                        #       font="Noto Sans Bold",
                        #       update_interval = 10,
                        #       fontsize = 12,
                        #       padding = 5,
                        #   ),

                            # Sep widget to add a separator between widgets
                            widget.Sep(
                                linewidth=2,
                                padding=10,
                                foreground="#fcf8c0",
                                size_percent=65,
                            ),

                            # Clock widget to display date and time and launch Zathura on click -> open the file Mqtile.pdf -> key bindings map
                            widget.Clock(
                                format="%Y-%m-%d %a %H:%M",
                                foreground='#ffffff',
                                font = "Noto Sans Bold",
                                mouse_callbacks={'Button1':lazy.spawn(f"setsid zathura {home}/Mqtile.pdf")}
                                ),
                            

                        ],
                        27,
                        background='#2f9fb5', # Set the background color of the bar
                        opacity=0.8,            # Set the opacity of the bar (optional)
                    ),
                    # Set the wallpaper path
                    wallpaper=myWallpaper(), # Call the function to set the window wallpaper
                    wallpaper_mode='fill', # Set the wallpaper mode
                ),
            ]


#WM bhiver

# Key bindings for dynamic groups are not used in this configuration
dgroups_key_binder = None

# Application rules for dynamic groups (currently empty)
dgroups_app_rules = []  # type: list

# When enabled, the focus will follow the mouse pointer
follow_mouse_focus = False

# Determines if windows should be brought to the front on click
bring_front_click = False

# When set to True, the cursor will warp to the center of the focused window.
cursor_warp = False

# Floating layout settings with custom float rules for specific applications
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# Automatically set windows to fullscreen when they are created
auto_fullscreen = True

# Choose how to focus on windows when they are activated
focus_on_window_activation = "smart"

# When enabled, the screens will be reconfigured automatically
reconfigure_screens = True


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# LG3D: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

