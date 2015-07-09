CrunchyRoll Auto Ripper V1.0
Released:    2015/07/09

This is a composite of various scripts required to download the latest videos from CrunchyRoll. This script was not made entirely by me(X).
I took the premade CrunchyRoll Downloader Toolkit DX v0.98 and incorporated a python script which rips the latest video from crunchyroll without you having to enter the url.

DEPEDENCIES :-

   This script requires you to install a few libraries (easily and freely available of internet)
     1.) Feedparser
     2.) binascii
     3.) ctypes
     4.) time
     5.) Subprocess
  Most of these will be pre-installed, otherwise, you'll get the error showing which module you need to install.You can find the setup of feedparser in this package itself.

INSTRUCTIONS:

    Pre-Setup (Only need to do these once.):
    1.  Install Python 2.7.5.
    2.  Set your default video resolution and language in "settings.ini".
    3.  If a premium member, run "_make-cookies.bat" and sign in.

    Per-Video Process:
    1. Start "ExecuteMe.py".
    2. Download will start automatically. Everything is automated.
    3. Browse to the 'export' folder to view the completed file.

    SPECIAL NOTE: There are 2 other Batch files that you should know about...
       1.)  _start_subs-only.bat :- Just want the subtitles to an episode? OK.. fair 'nuff. Use this.
       2.) cleaner.bat :- Sometimes, you might be getting login errors,video corruptions and stuff, it's mainly because of cache in your system.So, execute this script and it will solve 99% of your problem(s).


WHAT IS THE POINT OF THIS SCRIPT? WHAT IS IT ACTUALLY DOING?:

    The process of getting a working download from CrunchyRoll is effectively doing the following:
        - First it fetches the entried from the Crunchyroll's RSS
        - Extracts the link of the latest episode
        - Passes the link to _start.bat
        - Downloading and decrypting subtitles
        - Downloading the video as FLV
        - Splitting the FLV file into 264 video and aac audio
        - Merging video, audio, and subtitles into a mkv file
        - Naming the new video something other than 'video.mkv'


NOTES FROM THE AUTHORS:

    From Author of Latest Crunchyroll video ripper (Author = X) :
        Hey, I know this might be of no use to most of the people.But,if you want to rip/download some crunchyroll show and know when it is going to air, then you can put this script in "scheduled tasks" of your system and at the particular time, it will start automatically.You don't need to visit crunchyroll to get the link of their latest video.Just execute this and BOOM!. No, this is not what HorribleSubs use to rip videos, But, the idea is pretty much the same, I guess.Please, anyone who thinks who can improve this script and make it even better,do so.. just let me know when you update it by emailing me at :- x@psychoticelites.com

    From the DX author:
        Yeah, I wrote the basis for this "new 'n' improved version". Basically, I monitored the traffic
        to and from Crunchyroll while a video was loading, found a few (read: a lot of) similarities, and
        basically wrote the script to do the same thing, but parse the file and call upon RTMPdump to
        dump the video (RTMPexplorer was doing the same thing basically).

    From the anonymous original author:
        I did not write these programs, and I didn't even come up with this method. All I have done is 
        created a few little bat files to bring them together. Original instructions on how this is 
        done can be found here: 
        http://www.darkztar.com/forum/showthread.php?219034-Ripping-videos-amp-subtitles-from-Crunchyroll-%28noob-friendly%29


DISCLAIMER:

    This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.
    To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/deed.en_US.

    The software is provided "AS IS", without any warranty, either expressed or implied, including, but 
    not limited to, the implied warranties of merchantability and fitness for a particular purpose. 
    The author(s) will not be liable for any special, incidental, consequential or indirect damages due 
    to loss of data or any other reason. This is a free tool for educational (yes, educational >.>) use only.

    If you you think you can make a better script, you're probably right. Feel free to use this as a 
    basis for your creation if it helps, which is what I did. ;-)

    Please note that all bundled applications (i.e. everything other than these batch files, decode.py, and ultimate.py) were 
    created by others, and are subject to their applicable Terms, Conditions, and Copyright. At time of 
    release, all included scripts/applications were freely avaliable, however that is up to the 
    respective authors to decide.

    Any questions or requests for assistance should be directed to your nearest geek who looks like they
    know more about this than you. While individual components of this toolkit may be supported by their
    creators and previously no original author-support was provided, as he's enjoying the isolation granted
    by his pious fortress of solitude, the current author is more than happy to answer any questions or fix
    bugs (damn bugs). But then again, educational tools are more about the self-learning process anyway :-)
