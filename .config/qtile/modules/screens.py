from libqtile import bar
from .widgets import *
from libqtile.config import Screen
import os


colors = {
    "violet": "#932191",
    "ruby": "#AD3D6F",
    "cedar": "#C7594B",
    "deep-orange": "#E17327",
    "orange": "#FF9300",
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(
                    filename="~/.config/qtile/eos-c.png",
                    margin=3,
                    background="#2f343f",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn("rofi -show combi")
                    },
                ),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"),
                widget.GroupBox(
                    highlight_method="line",
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f",
                ),
                widget.TextBox(text="", padding=0, fontsize=28, foreground="#2f343f"),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground="#ffffff", fmt="{}"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            "xfce4-terminal '-e yay -Syu'"
                        )
                    },
                    background="#2f343f",
                ),
                widget.Systray(icon_size=20),
                widget.Spacer(length=10),
                left_half_circle(colors["violet"]),
                widget.Backlight(
                    background=colors["violet"],
                    backlight_name="amdgpu_bl0",
                    change_comands="",
                ),
                right_half_circle(colors["violet"]),
                widget.Spacer(length=10),
                left_half_circle(colors["ruby"]),
                widget.Battery(background=colors["ruby"]),
                widget.Spacer(length=5, background=colors["ruby"]),
                widget.BatteryIcon(icon_size=20, background=colors["ruby"]),
                right_half_circle(colors["ruby"]),
                widget.Spacer(length=10),
                left_half_circle(colors["cedar"]),
                widget.Volume(
                    background=colors["cedar"],
                ),
                widget.Spacer(length=5, background=colors["cedar"]),
                MyVolume(
                    fontsize=18,
                    font="Font Awesome 5 Free",
                    foreground="#000000",
                    background=colors["cedar"],
                    mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("pavucontrol")},
                ),
                right_half_circle(colors["cedar"]),
                widget.Spacer(length=10),
                left_half_circle(colors["deep-orange"]),
                widget.Clock(
                    format=" %Y-%m-%d %a %I:%M %p",
                    background=colors["deep-orange"],
                ),
                right_half_circle(colors["deep-orange"]),
                widget.Spacer(length=15),
                widget.TextBox(
                    text="",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(
                            os.path.expanduser("~/.config/rofi/powermenu.sh")
                        )
                    },
                ),
                widget.Spacer(length=15),
            ],
            margin=[3, 10, 3, 10],
            background="#00000000",
            opacity=1,
            size=25,
        ),
    ),
]
