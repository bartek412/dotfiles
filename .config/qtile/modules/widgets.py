from libqtile import widget
from libqtile import qtile

colors = [
    ["#282c34", "#282c34"],  # panel background
    ["#3d3f4b", "#434758"],  # background for current screen tab
    ["#ffffff", "#ffffff"],  # font color for group names
    ["#ff5555", "#ff5555"],  # border line color for current tab
    [
        "#74438f",
        "#74438f",
    ],  # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"],  # color for the 'even widgets'
    ["#e1acff", "#e1acff"],  # window name
    ["#ecbbfb", "#ecbbfb"],  # backbround for inactive screens
]


widget_defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ""
        elif self.volume <= 15:
            self.text = ""
        elif self.volume < 50:
            self.text = ""
        else:
            self.text = ""
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ""
        elif self.volume <= 15:
            self.text = ""
        elif self.volume < 50:
            self.text = ""
        else:
            self.text = ""
        self.draw()

        if wob:
            with open(self.wob, "a") as f:
                f.write(str(self.volume) + "\n")


def left_half_circle(fg_color="#7daea3"):
    return widget.TextBox(text="\uE0B6", fontsize=28, foreground=fg_color, padding=0)


def right_half_circle(fg_color="#7daea3"):
    return widget.TextBox(text="\uE0B4", fontsize=28, foreground=fg_color, padding=0)
