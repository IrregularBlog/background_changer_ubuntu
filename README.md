# A python script which automagically sets your background in Ubuntu (and every other distribution using Gnome) on a daily basis
A simple ubuntu (Gnome) background changer. It will fetch images from picsum.photos and sets them as your new backgroundpicture. There is an optional parameter which can be passed in the commandline: "daily". This will create a file where it saves the img-urls and the date the script was used. When daily is active, it will only change the background once a day.

Clone this repo by using
```
git clone https://github.com/IrregularBlog/background_changer_ubuntu.git
```

Now make it executable by

```
chmod +rwx ./background_changer.py
```

If you are using Ubuntu you can now add this script to the Ubuntu startup applications, this will give you a different background whenever you start your PC (if daily is active, it only changes the background once a day):

```
<python-path> <whole-path-to-background_changer.py> <optional:daily>
```
For example:

![image](https://github.com/IrregularBlog/background_changer_ubuntu/assets/27814043/6dbc0d3e-7574-4a9a-8f87-9bc7536cec61)

the current python directory can be found by using
```
where python
```
in your terminal.

### Crontab
This script will currently not be executable in cron due to the limited environment variable, the command gsettings does not work.
