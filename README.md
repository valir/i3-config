# My own i3 / ArchLinux configuration

This is my current configuration, placed here for my own future reference but
also for sharing. I really appreciated others sharing their i3 configuration on
githib, so this is my turn to do it.

## The specifis

I wanted a clean looking terminal (urxvt) nice fonts in Firefox and a minimal but
informative statusbar. The Firefox fonts where a bit of a challenge, as it
tends to switch to ttf-embedded bitmaps. But now it's sorted out using
fontconfig - see the relevant configuration files. The fonts listed in the
configuration files must be installed on your system.

## Usage

Here is an usage example:

```
cd ~/.config
git clone https://github.com/valir/i3-config.git i3
ln -s /home/<youruser>/.config/i3/fontconfig .
ln -s /home/<youruser>/.config/i3/dunst .
ln -s /home/<youruser>/.config/i3/gtk-3.0 .
ln -s /home/<youruser>/.config/i3/gtkrc-2.0 .
ln -s /home/<youruser>/.config/i3/gtkrc .
ln -s /home/<youruser>/.config/i3/.Xdefaults ~/
# now reload your i3 configuration
```

Have fun!

