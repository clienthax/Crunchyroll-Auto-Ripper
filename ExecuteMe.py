#------------------------------------------------------------------------------------------------------------------------------#
#                                                DISCLAIMER:                                                                   #
#------------------------------------------------------------------------------------------------------------------------------#
#                                                                                                                              # 
#    This work is licensed under the Creative Commons Attribution-ShareAlike 3.0 Unported License.                             #
#    To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/deed.en_US.                           #           
#                                                                                                                              # 
#    The software is provided "AS IS", without any warranty, either expressed or implied, including, but                       #
#    not limited to, the implied warranties of merchantability and fitness for a particular purpose.                           #
#    The author(s) will not be liable for any special, incidental, consequential or indirect damages due                       #
#    to loss of data or any other reason. This is a free tool for educational (yes, educational >.>) use only.                 #
#                                                                                                                              #
#    If you you think you can make a better script, you're probably right. Feel free to use this as a                          #
#    basis for your creation if it helps, which is what I did. ;-)                                                             #
#                                                                                                                              # 
#    Please note that all bundled applications (i.e. everything other than these batch files, decode.py, and ultimate.py) were # 
#    created by others, and are subject to their applicable Terms, Conditions, and Copyright. At time of                       #
#    release, all included scripts/applications were freely avaliable, however that is up to the                               #
#    respective authors to decide.   																						   #
#                                                                                                                              #
#    Any questions or requests for assistance should be directed to your nearest geek who looks like they                      #
#    know more about this than you. While individual components of this toolkit may be supported by their                      #
#    creators and previously no original author-support was provided, as he's enjoying the isolation granted                   #
#    by his pious fortress of solitude, the current author is more than happy to answer any questions or fix                   #
#    bugs (damn bugs). But then again, educational tools are more about the self-learning process anyway :-)                   #
#------------------------------------------------------------------------------------------------------------------------------#


		# ---------------------------------------------------------------------------------------------------- #
		#                                                                                                      #
		#  Please edit this only if you know what you are doing. Otherwise it could mess up the input process. #
		#                                                                                                      #
		# ---------------------------------------------------------------------------------------------------- #



# -------------- Libraries Importing Starts --------------
import feedparser
import ctypes
import time
import subprocess
import binascii

# -------------- Libraries Importing Done --------------

# -------------- Feed Checking and Parsing Started --------------

feed = feedparser.parse('http://www.crunchyroll.com/rss/anime') #checks the crunchyroll for latest videos.
URL = feed['entries'][0]['link']            # gets the link of the latest episode
# -------------- Feed Checking and Parsing  Done --------------

print feed['entries'][0]['title']  #Prints the title of the episode being ripped!

# ------------ Parsing URL to Crunchy DX Tool Start ------------

if __name__ =="__main__":
    response = URL

    p = subprocess.Popen("_start.bat", stdin = subprocess.PIPE)
    #time.sleep(1)

    p.stdin.write(response) #Answer the question
    #print(response)
    time.sleep(20)

# ------------ Parsing URL to Crunchy DX Tool Done ------------