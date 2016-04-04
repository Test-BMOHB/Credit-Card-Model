login as: mrains
Using keyboard-interactive authentication.
PAM Authentication
Password:
Last login: Mon Apr 04 2016 11:20:24 -0400 from OCDT70451748.office.adroot.bmogc                                                                                                                                                             .net

###################################################################
# This is a private computer system and is the property of        #
# Bank of Montreal and its associated affiliates.                 #
# Individuals using this computer system without authority, or in #
# excess of their authority, are subject to having all of their   #
# activities on this system monitored and recorded by system      #
# personnel.                                                      #
#                                                                 #
# In the course of monitoring individuals improperly using this   #
# system, or in the course of system maintenance, the activities  #
# of authorized users may also be monitored.                      #
#                                                                 #
# Anyone using this system expressly consents to such monitoring  #
# and is advised that if such monitoring reveals possible         #
# evidence of criminal activity, system personnel may provide the #
# evidence of such monitoring to law enforcement officials.       #
###################################################################

[mrains@cmtoldelkkapp02 ~]$ ls
cc_hadoop  get-pip.py
[mrains@cmtoldelkkapp02 ~]$ ls -lart
total 1540
drw-r--r--  2 mrains mrains    4096 Jul 14  2010 .gnome2
-rw-r--r--  1 mrains mrains     124 Aug 17  2015 .bashrc
-rw-r--r--  1 mrains mrains      18 Aug 17  2015 .bash_logout
-rw-r--r--  1 mrains mrains     171 Aug 19  2015 .kshrc
-rw-rw-r--  1 mrains mrains 1522812 Mar  5 12:15 get-pip.py
-rw-------  1 mrains mrains      35 Mar 30 14:04 .lesshst
drwxr-xr-x 35 root   root      4096 Apr  1 12:03 ..
-rw-------  1 mrains mrains     186 Apr  4 11:12 .bash_history
drwx------  3 mrains mrains    4096 Apr  4 11:45 .cache
drwx------  4 mrains mrains    4096 Apr  4 11:45 .local
-rw-r--r--  1 mrains mrains     253 Apr  4 11:49 .bash_profile
-rw-------  1 mrains mrains     690 Apr  4 11:49 .viminfo
drwx------  6 mrains mrains    4096 Apr  4 11:50 .
drwxrwxr-x  3 mrains mrains    4096 Apr  4 11:51 cc_hadoop
[mrains@cmtoldelkkapp02 ~]$ rm -r .local/
[mrains@cmtoldelkkapp02 ~]$ ls -lart
total 1536
drw-r--r--  2 mrains mrains    4096 Jul 14  2010 .gnome2
-rw-r--r--  1 mrains mrains     124 Aug 17  2015 .bashrc
-rw-r--r--  1 mrains mrains      18 Aug 17  2015 .bash_logout
-rw-r--r--  1 mrains mrains     171 Aug 19  2015 .kshrc
-rw-rw-r--  1 mrains mrains 1522812 Mar  5 12:15 get-pip.py
-rw-------  1 mrains mrains      35 Mar 30 14:04 .lesshst
drwxr-xr-x 35 root   root      4096 Apr  1 12:03 ..
-rw-------  1 mrains mrains     186 Apr  4 11:12 .bash_history
drwx------  3 mrains mrains    4096 Apr  4 11:45 .cache
-rw-r--r--  1 mrains mrains     253 Apr  4 11:49 .bash_profile
-rw-------  1 mrains mrains     690 Apr  4 11:49 .viminfo
drwxrwxr-x  3 mrains mrains    4096 Apr  4 11:51 cc_hadoop
drwx------  5 mrains mrains    4096 Apr  4 16:33 .
[mrains@cmtoldelkkapp02 ~]$ python --version
Python 2.6.6
[mrains@cmtoldelkkapp02 ~]$ python get-pip.py --user
DEPRECATION: Python 2.6 is no longer supported by the Python core team, please u                                                                                                                                                             pgrade your Python. A future version of pip will drop support for Python 2.6
Collecting pip
/tmp/tmpWuhDes/pip.zip/pip/_vendor/requests/packages/urllib3/util/ssl_.py:315: S                                                                                                                                                             NIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indi                                                                                                                                                             cation) extension to TLS is not available on this platform. This may cause the s                                                                                                                                                             erver to present an incorrect TLS certificate, which can cause validation failur                                                                                                                                                             es. For more information, see https://urllib3.readthedocs.org/en/latest/security                                                                                                                                                             .html#snimissingwarning.
/tmp/tmpWuhDes/pip.zip/pip/_vendor/requests/packages/urllib3/util/ssl_.py:120: I                                                                                                                                                             nsecurePlatformWarning: A true SSLContext object is not available. This prevents                                                                                                                                                              urllib3 from configuring SSL appropriately and may cause certain SSL connection                                                                                                                                                             s to fail. For more information, see https://urllib3.readthedocs.org/en/latest/s                                                                                                                                                             ecurity.html#insecureplatformwarning.
  Using cached pip-8.1.1-py2.py3-none-any.whl
Collecting wheel
  Using cached wheel-0.29.0-py2.py3-none-any.whl
Collecting argparse (from wheel)
  Using cached argparse-1.4.0-py2.py3-none-any.whl
Installing collected packages: pip, argparse, wheel
Successfully installed argparse-1.2.1 pip wheel
[mrains@cmtoldelkkapp02 ~]$ ls
cc_hadoop  get-pip.py
[mrains@cmtoldelkkapp02 ~]$ ls -lart
total 1540
drw-r--r--  2 mrains mrains    4096 Jul 14  2010 .gnome2
-rw-r--r--  1 mrains mrains     124 Aug 17  2015 .bashrc
-rw-r--r--  1 mrains mrains      18 Aug 17  2015 .bash_logout
-rw-r--r--  1 mrains mrains     171 Aug 19  2015 .kshrc
-rw-rw-r--  1 mrains mrains 1522812 Mar  5 12:15 get-pip.py
-rw-------  1 mrains mrains      35 Mar 30 14:04 .lesshst
drwxr-xr-x 35 root   root      4096 Apr  1 12:03 ..
-rw-------  1 mrains mrains     186 Apr  4 11:12 .bash_history
drwx------  3 mrains mrains    4096 Apr  4 11:45 .cache
-rw-r--r--  1 mrains mrains     253 Apr  4 11:49 .bash_profile
-rw-------  1 mrains mrains     690 Apr  4 11:49 .viminfo
drwxrwxr-x  3 mrains mrains    4096 Apr  4 11:51 cc_hadoop
drwx------  6 mrains mrains    4096 Apr  4 16:33 .
drwx------  4 mrains mrains    4096 Apr  4 16:33 .local
[mrains@cmtoldelkkapp02 ~]$ pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output.
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup.
  --trusted-host <hostname>   Mark this host as trusted, even though it does
                              not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.
[mrains@cmtoldelkkapp02 ~]$ python
Python 2.6.6 (r266:84292, May 22 2015, 08:34:51)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-15)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> help()

Welcome to Python 2.6!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

/usr/lib/python2.6/site-packages/ambari_jinja2/__init__.py:31: UserWarning: Modu                                                                                                                                                             le argparse was already imported from /home/mrains/.local/lib/python2.6/site-pac                                                                                                                                                             kages/argparse.pyc, but /usr/lib/python2.6/site-packages is being added to sys.p                                                                                                                                                             ath
  __version__ = __import__('pkg_resources') \
BaseHTTPServer      binhex              ihooks              rexec
Bastion             bisect              imageop             rfc822
CDROM               bonobo              imaplib             rhn
CGIHTTPServer       bsddb               imghdr              rhsm
CORBA               bz2                 imp                 rlcompleter
ConfigParser        cPickle             imputil             robotparser
Cookie              cProfile            iniparse            rpm
Crypto              cStringIO           inspect             rpmUtils
DLFCN               cairo               io                  runpy
DocXMLRPCServer     calendar            iotop               sched
HTMLParser          cas                 itertools           select
IN                  cgi                 iwlib               sets
M2Crypto            cgitb               json                setuptools
MimeWriter          chunk               keyword             sgmllib
ORBit               cmath               lib2to3             sha
OpenSSL             cmd                 libproxy            shelve
PortableServer      code                libxml2             shlex
Queue               codecs              libxml2mod          shutil
SimpleHTTPServer    codeop              linecache           signal
SimpleXMLRPCServer  collections         linuxaudiodev       simplejson
SocketServer        colorsys            locale              site
StringIO            commands            logging             smtpd
TYPES               compileall          macpath             smtplib
UserDict            compiler            macurl2path         snack
UserList            contextlib          mailbox             sndhdr
UserString          cookielib           mailcap             socket
_LWPCookieJar       copy                markupbase          sos
_MozillaCookieJar   copy_reg            marshal             spwd
__builtin__         crypt               math                sqlite3
__future__          csv                 md5                 sqlitecachec
_abcoll             ctypes              mhlib               sre
_ast                curl                mimetools           sre_compile
_bisect             curses              mimetypes           sre_constants
_bsddb              datetime            mimify              sre_parse
_bytesio            dateutil            mmap                ssl
_codecs             dbhash              modulefinder        stat
_codecs_cn          dbm                 multifile           statvfs
_codecs_hk          dbus                multiprocessing     string
_codecs_iso2022     dbus_bindings       mutex               stringold
_codecs_jp          decimal             netrc               stringprep
_codecs_kr          difflib             new                 strop
_codecs_tw          dircache            nis                 struct
_collections        dis                 nntplib             subprocess
_crypt              distutils           nose                sunau
_csv                dl                  ntpath              sunaudio
_ctypes             dmidecode           nturl2path          symbol
_curses             dmidecodemod        numbers             symtable
_curses_panel       doctest             opcode              sys
_dbus_bindings      drv_libxml2         operator            syslog
_dbus_glib_bindings dsextras            optparse            tabnanny
_elementtree        dumbdbm             ordereddict         tarfile
_fileio             dummy_thread        os                  telnetlib
_functools          dummy_threading     os2emxpath          tempfile
_hashlib            easy_install        ossaudiodev         termios
_heapq              email               pango               test
_hotshot            encodings           pangocairo          textwrap
_json               errno               paramiko            this
_locale             ethtool             parser              thread
_lsprof             exceptions          pdb                 threading
_multibytecodec     fcntl               pickle              time
_multiprocessing    filecmp             pickletools         timeit
_random             fileinput           pip                 timing
_snack              fnmatch             pipes               toaiff
_socket             formatter           pkg_resources       token
_sqlite3            fpformat            pkgutil             tokenize
_sqlitecache        fractions           platform            trace
_sre                ftplib              plistlib            traceback
_ssl                functools           popen2              tty
_strptime           future_builtins     poplib              types
_struct             gc                  posix               unicodedata
_symtable           gdbm                posixfile           unittest
_threading_local    genericpath         posixpath           urlgrabber
_warnings           getopt              pprint              urllib
_weakref            getpass             problem             urllib2
_xmlplus            gettext             profile             urlparse
abc                 gio                 pstats              user
abrt_exception_handler glib                pty                 uu
acutil              glob                pwd                 uuid
aifc                gnome               py_compile          warnings
ambari_agent        gnomecanvas         pyclbr              wave
ambari_commons      gnomevfs            pycurl              weakref
ambari_jinja2       gobject             pydoc               webbrowser
ambari_simplejson   gpgme               pydoc_topics        wheel
anydbm              grp                 pyexpat             whichdb
argparse            gtk                 pygtk               wsgiref
array               gtkunixprint        pytz                xdrlib
ast                 gudev               quopri              xml
asynchat            gzip                random              xmllib
asyncore            hashlib             re                  xmlrpclib
atexit              heapq               readline            xxsubtype
atk                 hmac                report              yum
audiodev            hotshot             reportclient        yumutils
audioop             htmlentitydefs      repr                zipfile
base64              htmllib             resource            zipimport
bdb                 httplib             resource_management zlib
binascii            idlelib             resource_monitoring

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose descriptions contain the word "spam".

help> exit()
no Python documentation found for 'exit()'

help> quit()
no Python documentation found for 'quit()'

help> exit()
no Python documentation found for 'exit()'

help> exit

help> uit
no Python documentation found for 'uit'

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> quit()
[mrains@cmtoldelkkapp02 ~]$ pip install barnum --user
DEPRECATION: Python 2.6 is no longer supported by the Python core team, please u                                                                                                                                                             pgrade your Python. A future version of pip will drop support for Python 2.6
Collecting barnum
/home/mrains/.local/lib/python2.6/site-packages/pip/_vendor/requests/packages/ur                                                                                                                                                             llib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but t                                                                                                                                                             he SNI (Subject Name Indication) extension to TLS is not available on this platf                                                                                                                                                             orm. This may cause the server to present an incorrect TLS certificate, which ca                                                                                                                                                             n cause validation failures. For more information, see https://urllib3.readthedo                                                                                                                                                             cs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/home/mrains/.local/lib/python2.6/site-packages/pip/_vendor/requests/packages/ur                                                                                                                                                             llib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not                                                                                                                                                              available. This prevents urllib3 from configuring SSL appropriately and may cau                                                                                                                                                             se certain SSL connections to fail. For more information, see https://urllib3.re                                                                                                                                                             adthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Using cached barnum-0.5.1.tar.gz
Collecting future (from barnum)
  Using cached future-0.15.2.tar.gz
Collecting importlib (from future->barnum)
  Using cached importlib-1.0.3.tar.bz2
Requirement already satisfied (use --upgrade to upgrade): argparse in ./.local/l                                                                                                                                                             ib/python2.6/site-packages (from future->barnum)
Building wheels for collected packages: barnum, future, importlib
  Running setup.py bdist_wheel for barnum ... error
  Complete output from command /usr/bin/python -u -c "import setuptools, tokeniz                                                                                                                                                             e;__file__='/tmp/pip-build-wgxpNB/barnum/setup.py';exec(compile(getattr(tokenize                                                                                                                                                             , 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" bdis                                                                                                                                                             t_wheel -d /tmp/tmpyAXcI6pip-wheel- --python-tag cp26:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help

  error: invalid command 'bdist_wheel'

  ----------------------------------------
  Failed building wheel for barnum
  Running setup.py clean for barnum
  Running setup.py bdist_wheel for future ... error
  Complete output from command /usr/bin/python -u -c "import setuptools, tokeniz                                                                                                                                                             e;__file__='/tmp/pip-build-wgxpNB/future/setup.py';exec(compile(getattr(tokenize                                                                                                                                                             , 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" bdis                                                                                                                                                             t_wheel -d /tmp/tmptDWh2Qpip-wheel- --python-tag cp26:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help

  error: invalid command 'bdist_wheel'

  ----------------------------------------
  Failed building wheel for future
  Running setup.py clean for future
  Running setup.py bdist_wheel for importlib ... error
  Complete output from command /usr/bin/python -u -c "import setuptools, tokeniz                                                                                                                                                             e;__file__='/tmp/pip-build-wgxpNB/importlib/setup.py';exec(compile(getattr(token                                                                                                                                                             ize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" b                                                                                                                                                             dist_wheel -d /tmp/tmpHkA9Mrpip-wheel- --python-tag cp26:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help

  error: invalid command 'bdist_wheel'

  ----------------------------------------
  Failed building wheel for importlib
  Running setup.py clean for importlib
Failed to build barnum future importlib
Installing collected packages: importlib, future, barnum
  Running setup.py install for importlib ... done
  Running setup.py install for future ... done
  Running setup.py install for barnum ... done
Successfully installed barnum-0.5.1 future-0.15.2 importlib-1.0.3
[mrains@cmtoldelkkapp02 ~]$ python
Python 2.6.6 (r266:84292, May 22 2015, 08:34:51)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-15)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import barnum
>>> help()

Welcome to Python 2.6!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> exit()
no Python documentation found for 'exit()'

help> quit()
no Python documentation found for 'quit()'

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> exit()
[mrains@cmtoldelkkapp02 ~]$ pip install virtualenv --user
DEPRECATION: Python 2.6 is no longer supported by the Python core team, please u                                                                                                                                                             pgrade your Python. A future version of pip will drop support for Python 2.6
Collecting virtualenv
/home/mrains/.local/lib/python2.6/site-packages/pip/_vendor/requests/packages/ur                                                                                                                                                             llib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but t                                                                                                                                                             he SNI (Subject Name Indication) extension to TLS is not available on this platf                                                                                                                                                             orm. This may cause the server to present an incorrect TLS certificate, which ca                                                                                                                                                             n cause validation failures. For more information, see https://urllib3.readthedo                                                                                                                                                             cs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/home/mrains/.local/lib/python2.6/site-packages/pip/_vendor/requests/packages/ur                                                                                                                                                             llib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not                                                                                                                                                              available. This prevents urllib3 from configuring SSL appropriately and may cau                                                                                                                                                             se certain SSL connections to fail. For more information, see https://urllib3.re                                                                                                                                                             adthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Using cached virtualenv-15.0.1-py2.py3-none-any.whl
Installing collected packages: virtualenv
Successfully installed virtualenv-15.0.1
[mrains@cmtoldelkkapp02 ~]$ ls
cc_hadoop  get-pip.py
[mrains@cmtoldelkkapp02 ~]$ cd cc_hadoop/
[mrains@cmtoldelkkapp02 cc_hadoop]$ virutalenv -p /usr/local/bin/python2.7 venv
-bash: virutalenv: command not found
[mrains@cmtoldelkkapp02 cc_hadoop]$ virutalenv
-bash: virutalenv: command not found
[mrains@cmtoldelkkapp02 cc_hadoop]$ pip

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  list                        List installed packages.
  show                        Show information about installed packages.
  search                      Search PyPI for packages.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --isolated                  Run pip in an isolated mode, ignoring
                              environment variables and user configuration.
  -v, --verbose               Give more output. Option is additive, and can be
                              used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output.
  --log <path>                Path to a verbose appending log.
  --proxy <proxy>             Specify a proxy in the form
                              [user:passwd@]proxy.server:port.
  --retries <retries>         Maximum number of retries each connection should
                              attempt (default 5 times).
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists:
                              (s)witch, (i)gnore, (w)ipe, (b)ackup.
  --trusted-host <hostname>   Mark this host as trusted, even though it does
                              not have valid or any HTTPS.
  --cert <path>               Path to alternate CA bundle.
  --client-cert <path>        Path to SSL client certificate, a single file
                              containing the private key and the certificate
                              in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine
                              whether a new version of pip is available for
                              download. Implied with --no-index.
[mrains@cmtoldelkkapp02 cc_hadoop]$ cd ~/.local/
[mrains@cmtoldelkkapp02 .local]$ ls
bin  lib
[mrains@cmtoldelkkapp02 .local]$ cd bin
[mrains@cmtoldelkkapp02 bin]$ ls
futurize  pasteurize  pip  pip2  pip2.6  rebuild_barnum_data  virtualenv  wheel
[mrains@cmtoldelkkapp02 bin]$ cd ..
[mrains@cmtoldelkkapp02 .local]$ cd ..
[mrains@cmtoldelkkapp02 ~]$ echo $PATH
/usr/lib64/qt-3.3/bin:/usr/bin:/bin:/apps/git/bin:/usr/local/sbin:/apps/maven/bi                                                                                                                                                             n:/apps/ant/bin:/usr/sbin:/sbin:/home/mrains/bin:/home/mrains/.local/bin
[mrains@cmtoldelkkapp02 ~]$ virtualenv
You must provide a DEST_DIR
Usage: virtualenv [OPTIONS] DEST_DIR

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -v, --verbose         Increase verbosity.
  -q, --quiet           Decrease verbosity.
  -p PYTHON_EXE, --python=PYTHON_EXE
                        The Python interpreter to use, e.g.,
                        --python=python2.5 will use the python2.5 interpreter
                        to create the new environment.  The default is the
                        interpreter that virtualenv was installed with
                        (/usr/bin/python)
  --clear               Clear out the non-root install and start from scratch.
  --no-site-packages    DEPRECATED. Retained only for backward compatibility.
                        Not having access to global site-packages is now the
                        default behavior.
  --system-site-packages
                        Give the virtual environment access to the global
                        site-packages.
  --always-copy         Always copy files rather than symlinking.
  --unzip-setuptools    Unzip Setuptools when installing it.
  --relocatable         Make an EXISTING virtualenv environment relocatable.
                        This fixes up scripts and makes all .pth files
                        relative.
  --no-setuptools       Do not install setuptools in the new virtualenv.
  --no-pip              Do not install pip in the new virtualenv.
  --no-wheel            Do not install wheel in the new virtualenv.
  --extra-search-dir=DIR
                        Directory to look for setuptools/pip distributions in.
                        This option can be used multiple times.
  --download            Download preinstalled packages from PyPI.
  --no-download, --never-download
                        Do not download preinstalled packages from PyPI.
  --prompt=PROMPT       Provides an alternative prompt prefix for this
                        environment.
  --setuptools          DEPRECATED. Retained only for backward compatibility.
                        This option has no effect.
  --distribute          DEPRECATED. Retained only for backward compatibility.
                        This option has no effect.
[mrains@cmtoldelkkapp02 ~]$ cd cc_hadoop/
[mrains@cmtoldelkkapp02 cc_hadoop]$ virutalenv venv
-bash: virutalenv: command not found
[mrains@cmtoldelkkapp02 cc_hadoop]$ virtualenv venv
New python executable in /home/mrains/cc_hadoop/venv/bin/python
Installing setuptools, pip, wheel...done.
[mrains@cmtoldelkkapp02 cc_hadoop]$ ls
ENV  venv
[mrains@cmtoldelkkapp02 cc_hadoop]$ rm -r ENV
[mrains@cmtoldelkkapp02 cc_hadoop]$ ls
venv
[mrains@cmtoldelkkapp02 cc_hadoop]$ . ./venv/bin/activate
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python --version
Python 2.6.6
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ deactivate
[mrains@cmtoldelkkapp02 cc_hadoop]$ rm -r venv/
[mrains@cmtoldelkkapp02 cc_hadoop]$ virtualenv -p /usr/local/bin/python2.7 venv
Running virtualenv with interpreter /usr/local/bin/python2.7
New python executable in /home/mrains/cc_hadoop/venv/bin/python2.7
Also creating executable in /home/mrains/cc_hadoop/venv/bin/python
Installing setuptools, pip, wheel...done.
[mrains@cmtoldelkkapp02 cc_hadoop]$ ls
venv
[mrains@cmtoldelkkapp02 cc_hadoop]$ source ./venv/bin/activate
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python --version
Python 2.7.11
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ pip install barnum
Collecting barnum
  Using cached barnum-0.5.1.tar.gz
Collecting future (from barnum)
  Using cached future-0.15.2.tar.gz
Building wheels for collected packages: barnum, future
  Running setup.py bdist_wheel for barnum ... done
  Stored in directory: /home/mrains/.cache/pip/wheels/f0/67/9d/2cdd3d61c0cd0d05f                                                                                                                                                             33a496b2323744598b2f944b69b95a9b1
  Running setup.py bdist_wheel for future ... done
  Stored in directory: /home/mrains/.cache/pip/wheels/d9/04/36/6bd807b5148e7c929                                                                                                                                                             d8f0991cc943a81f3287030a1b352e3fc
Successfully built barnum future
Installing collected packages: future, barnum
Successfully installed barnum-0.5.1 future-0.15.2
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python
Python 2.7.11 (default, Apr  4 2016, 15:02:03)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import barnum
>>>
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ pip install faker
Collecting faker
  Downloading Faker-0.1.4.tar.gz
Building wheels for collected packages: faker
  Running setup.py bdist_wheel for faker ... done
  Stored in directory: /home/mrains/.cache/pip/wheels/94/aa/b5/e762f92c9f0bf12f8                                                                                                                                                             18618d7638b23734390486b84997c5b85
Successfully built faker
Installing collected packages: faker
Successfully installed faker-0.1.4
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python
Python 2.7.11 (default, Apr  4 2016, 15:02:03)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import faker
/home/mrains/cc_hadoop/venv/lib/python2.7/site-packages/faker/__init__.py:23: Pe                                                                                                                                                             ndingDeprecationWarning:
This faker package is being deprecated September 15, 2016.

You should switch to using https://pypi.python.org/pypi/fake-factory instead.
After September 15, 2016 the PyPi faker package will be changing to that!

  warnings.warn(deprecation_message, PendingDeprecationWarning)
>>>
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ pyspark
Python 2.7.11 (default, Apr  4 2016, 15:02:03)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
16/04/04 16:45:39 INFO SparkContext: Running Spark version 1.3.1
16/04/04 16:45:40 WARN NativeCodeLoader: Unable to load native-hadoop library fo                                                                                                                                                             r your platform... using builtin-java classes where applicable
16/04/04 16:45:40 INFO SecurityManager: Changing view acls to: mrains
16/04/04 16:45:40 INFO SecurityManager: Changing modify acls to: mrains
16/04/04 16:45:40 INFO SecurityManager: SecurityManager: authentication disabled                                                                                                                                                             ; ui acls disabled; users with view permissions: Set(mrains); users with modify                                                                                                                                                              permissions: Set(mrains)
16/04/04 16:45:41 INFO Slf4jLogger: Slf4jLogger started
16/04/04 16:45:41 INFO Remoting: Starting remoting
16/04/04 16:45:41 INFO Remoting: Remoting started; listening on addresses :[akka                                                                                                                                                             .tcp://sparkDriver@cmtoldelkkapp02:52502]
16/04/04 16:45:41 INFO Utils: Successfully started service 'sparkDriver' on port                                                                                                                                                              52502.
16/04/04 16:45:41 INFO SparkEnv: Registering MapOutputTracker
16/04/04 16:45:41 INFO SparkEnv: Registering BlockManagerMaster
16/04/04 16:45:41 INFO DiskBlockManager: Created local directory at /tmp/spark-9                                                                                                                                                             475a2b5-f102-4873-88e7-5d7361e2e6d8/blockmgr-b2b07b26-c76b-4444-b98e-c8843b2bde4                                                                                                                                                             1
16/04/04 16:45:41 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
16/04/04 16:45:41 INFO HttpFileServer: HTTP File server directory is /tmp/spark-                                                                                                                                                             dc999c3a-8389-45f8-bbbb-b3c07fbb2852/httpd-c6958128-fcd4-46a6-bc17-ec8e92e2403a
16/04/04 16:45:41 INFO HttpServer: Starting HTTP Server
16/04/04 16:45:42 INFO Server: jetty-8.y.z-SNAPSHOT
16/04/04 16:45:42 INFO AbstractConnector: Started SocketConnector@0.0.0.0:49351
16/04/04 16:45:42 INFO Utils: Successfully started service 'HTTP file server' on                                                                                                                                                              port 49351.
16/04/04 16:45:42 INFO SparkEnv: Registering OutputCommitCoordinator
16/04/04 16:45:42 INFO Server: jetty-8.y.z-SNAPSHOT
16/04/04 16:45:42 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0                                                                                                                                                             :4040
16/04/04 16:45:42 INFO Utils: Successfully started service 'SparkUI' on port 404                                                                                                                                                             0.
16/04/04 16:45:42 INFO SparkUI: Started SparkUI at http://cmtoldelkkapp02:4040
16/04/04 16:45:42 INFO Executor: Starting executor ID <driver> on host localhost
16/04/04 16:45:42 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sp                                                                                                                                                             arkDriver@cmtoldelkkapp02:52502/user/HeartbeatReceiver
16/04/04 16:45:42 INFO NettyBlockTransferService: Server created on 45521
16/04/04 16:45:42 INFO BlockManagerMaster: Trying to register BlockManager
16/04/04 16:45:42 INFO BlockManagerMasterActor: Registering block manager localh                                                                                                                                                             ost:45521 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 45521)
16/04/04 16:45:43 INFO BlockManagerMaster: Registered BlockManager
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.3.1
      /_/

Using Python version 2.7.11 (default, Apr  4 2016 15:02:03)
SparkContext available as sc, HiveContext available as sqlContext.
>>> print 'Hi;
  File "<stdin>", line 1
    print 'Hi;
             ^
SyntaxError: EOL while scanning string literal
>>> print 'hi'
hi
>>>
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/me                                                                                                                                                             trics/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/stage/kill,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/,n                                                                                                                                                             ull}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             atic,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors/threadDump/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors/threadDump,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/en                                                                                                                                                             vironment/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/en                                                                                                                                                             vironment,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage/rdd/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage/rdd,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/pool/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/pool,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/stage/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/stage,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs/job/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs/job,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs/json,null}
16/04/04 16:46:09 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs,null}
16/04/04 16:46:09 INFO SparkUI: Stopped Spark web UI at http://cmtoldelkkapp02:4                                                                                                                                                             040
16/04/04 16:46:09 INFO DAGScheduler: Stopping DAGScheduler
16/04/04 16:46:09 INFO MapOutputTrackerMasterActor: MapOutputTrackerActor stoppe                                                                                                                                                             d!
16/04/04 16:46:09 INFO MemoryStore: MemoryStore cleared
16/04/04 16:46:09 INFO BlockManager: BlockManager stopped
16/04/04 16:46:09 INFO BlockManagerMaster: BlockManagerMaster stopped
16/04/04 16:46:09 INFO OutputCommitCoordinator$OutputCommitCoordinatorActor: Out                                                                                                                                                             putCommitCoordinator stopped!
16/04/04 16:46:09 INFO SparkContext: Successfully stopped SparkContext
16/04/04 16:46:09 INFO RemoteActorRefProvider$RemotingTerminator: Shutting down                                                                                                                                                              remote daemon.
16/04/04 16:46:09 INFO RemoteActorRefProvider$RemotingTerminator: Remote daemon                                                                                                                                                              shut down; proceeding with flushing remote transports.
16/04/04 16:46:09 INFO RemoteActorRefProvider$RemotingTerminator: Remoting shut                                                                                                                                                              down.
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ deactivate
[mrains@cmtoldelkkapp02 cc_hadoop]$ pyspark
Python 2.6.6 (r266:84292, May 22 2015, 08:34:51)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-15)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
16/04/04 16:46:18 INFO SparkContext: Running Spark version 1.3.1
16/04/04 16:46:19 WARN NativeCodeLoader: Unable to load native-hadoop library fo                                                                                                                                                             r your platform... using builtin-java classes where applicable
16/04/04 16:46:19 INFO SecurityManager: Changing view acls to: mrains
16/04/04 16:46:19 INFO SecurityManager: Changing modify acls to: mrains
16/04/04 16:46:19 INFO SecurityManager: SecurityManager: authentication disabled                                                                                                                                                             ; ui acls disabled; users with view permissions: Set(mrains); users with modify                                                                                                                                                              permissions: Set(mrains)
16/04/04 16:46:19 INFO Slf4jLogger: Slf4jLogger started
16/04/04 16:46:19 INFO Remoting: Starting remoting
16/04/04 16:46:19 INFO Remoting: Remoting started; listening on addresses :[akka                                                                                                                                                             .tcp://sparkDriver@cmtoldelkkapp02:49737]
16/04/04 16:46:19 INFO Utils: Successfully started service 'sparkDriver' on port                                                                                                                                                              49737.
16/04/04 16:46:19 INFO SparkEnv: Registering MapOutputTracker
16/04/04 16:46:20 INFO SparkEnv: Registering BlockManagerMaster
16/04/04 16:46:20 INFO DiskBlockManager: Created local directory at /tmp/spark-0                                                                                                                                                             0c542df-1af7-494e-830e-db34d91a2b8b/blockmgr-1b21667f-52d3-44ce-b90e-3a7488f5604                                                                                                                                                             6
16/04/04 16:46:20 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
16/04/04 16:46:20 INFO HttpFileServer: HTTP File server directory is /tmp/spark-                                                                                                                                                             33499a2a-b45d-4f20-9ed8-3b47e3ff0a43/httpd-54b90fdb-8344-4bf0-b739-2dcd3b815482
16/04/04 16:46:20 INFO HttpServer: Starting HTTP Server
16/04/04 16:46:20 INFO Server: jetty-8.y.z-SNAPSHOT
16/04/04 16:46:20 INFO AbstractConnector: Started SocketConnector@0.0.0.0:47923
16/04/04 16:46:20 INFO Utils: Successfully started service 'HTTP file server' on                                                                                                                                                              port 47923.
16/04/04 16:46:20 INFO SparkEnv: Registering OutputCommitCoordinator
16/04/04 16:46:20 INFO Server: jetty-8.y.z-SNAPSHOT
16/04/04 16:46:20 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0                                                                                                                                                             :4040
16/04/04 16:46:20 INFO Utils: Successfully started service 'SparkUI' on port 404                                                                                                                                                             0.
16/04/04 16:46:20 INFO SparkUI: Started SparkUI at http://cmtoldelkkapp02:4040
16/04/04 16:46:20 INFO Executor: Starting executor ID <driver> on host localhost
16/04/04 16:46:20 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sp                                                                                                                                                             arkDriver@cmtoldelkkapp02:49737/user/HeartbeatReceiver
16/04/04 16:46:20 INFO NettyBlockTransferService: Server created on 41207
16/04/04 16:46:20 INFO BlockManagerMaster: Trying to register BlockManager
16/04/04 16:46:20 INFO BlockManagerMasterActor: Registering block manager localh                                                                                                                                                             ost:41207 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 41207)
16/04/04 16:46:20 INFO BlockManagerMaster: Registered BlockManager
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 1.3.1
      /_/

Using Python version 2.6.6 (r266:84292, May 22 2015 08:34:51)
SparkContext available as sc, HiveContext available as sqlContext.
>>>
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/me                                                                                                                                                             trics/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/stage/kill,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/,n                                                                                                                                                             ull}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             atic,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors/threadDump/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors/threadDump,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/ex                                                                                                                                                             ecutors,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/en                                                                                                                                                             vironment/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/en                                                                                                                                                             vironment,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage/rdd/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage/rdd,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             orage,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/pool/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/pool,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/stage/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/stage,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/st                                                                                                                                                             ages,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs/job/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs/job,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs/json,null}
16/04/04 16:46:23 INFO ContextHandler: stopped o.s.j.s.ServletContextHandler{/jo                                                                                                                                                             bs,null}
16/04/04 16:46:23 INFO SparkUI: Stopped Spark web UI at http://cmtoldelkkapp02:4                                                                                                                                                             040
16/04/04 16:46:23 INFO DAGScheduler: Stopping DAGScheduler
16/04/04 16:46:23 INFO MapOutputTrackerMasterActor: MapOutputTrackerActor stoppe                                                                                                                                                             d!
16/04/04 16:46:23 INFO MemoryStore: MemoryStore cleared
16/04/04 16:46:23 INFO BlockManager: BlockManager stopped
16/04/04 16:46:23 INFO BlockManagerMaster: BlockManagerMaster stopped
16/04/04 16:46:23 INFO SparkContext: Successfully stopped SparkContext
16/04/04 16:46:23 INFO OutputCommitCoordinator$OutputCommitCoordinatorActor: Out                                                                                                                                                             putCommitCoordinator stopped!
16/04/04 16:46:23 INFO RemoteActorRefProvider$RemotingTerminator: Shutting down                                                                                                                                                              remote daemon.
16/04/04 16:46:23 INFO RemoteActorRefProvider$RemotingTerminator: Remote daemon                                                                                                                                                              shut down; proceeding with flushing remote transports.
16/04/04 16:46:23 INFO RemoteActorRefProvider$RemotingTerminator: Remoting shut                                                                                                                                                              down.
[mrains@cmtoldelkkapp02 cc_hadoop]$ . ./venv/bin/activate
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ hdsf dsf -ls /sandbox
-bash: hdsf: command not found
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ hdsf dfs -ls /sandbox
-bash: hdsf: command not found
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ hdfs dfs -ls /sandbox
Found 6 items
drwxrwxr-x+  - vwei02  hdfs          0 2016-03-02 13:52 /sandbox/AML
drwxrwxr-x+  - vwei02  hdfs          0 2016-03-02 13:55 /sandbox/Data_Governance
drwxrwxr-x+  - kkalr01 hdfs          0 2016-03-21 15:29 /sandbox/kkalr01
drwxrwxr-x+  - vpanshe hdfs          0 2016-03-08 15:17 /sandbox/tmp
drwxrwxr-x+  - vpanshe hdfs          0 2016-04-04 15:20 /sandbox/vpanshe
drwxrwxr-x+  - vwei02  hdfs          0 2016-03-29 14:22 /sandbox/vwei02
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ hdfs dfs -ls /sandbox/AML/mrains
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ df -h /
Filesystem            Size  Used Avail Use% Mounted on
/dev/mapper/vg_os_00-Root
                       12G  6.5G  4.7G  59% /
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ sudo yum install git-all
[sudo] password for mrains:
mrains is not in the sudoers file.  This incident will be reported.
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ yum install git-all
Loaded plugins: product-id, rhnplugin, subscription-manager
*Note* Red Hat Network repositories are not listed below. You must run this comm                                                                                                                                                             and as root to access RHN repositories.
You need to be root to perform this command.
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ pip install git
Collecting git
  Could not find a version that satisfies the requirement git (from versions: )
No matching distribution found for git
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ pip install git-all
Collecting git-all
  Could not find a version that satisfies the requirement git-all (from versions                                                                                                                                                             : )
No matching distribution found for git-all
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ dir
Airlines.py             Transaction_DistLoc.py
Branch_Zip.py           Transaction_Type.py
Country.py              uber_cust_hadoop.py
Detection_Scenarios     uber_cust_multithreading.py
geo_data.py             uber_cust.py
Hotels.py               uber_transactions_multithreading.py
Merchant_Category.py    uber_transactions.py
NAICS.py                venv
python_merchant_cat.py  zips.py
README.md
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python -v
# installing zipimport hook
import zipimport # builtin
# installed zipimport hook
# /home/mrains/cc_hadoop/venv/lib/python2.7/site.pyc matches /home/mrains/cc_had                                                                                                                                                             oop/venv/lib/python2.7/site.py
import site # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/site.py                                                                                                                                                             c
# /home/mrains/cc_hadoop/venv/lib/python2.7/os.pyc matches /home/mrains/cc_hadoo                                                                                                                                                             p/venv/lib/python2.7/os.py
import os # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/os.pyc
import errno # builtin
import posix # builtin
# /home/mrains/cc_hadoop/venv/lib/python2.7/posixpath.pyc matches /home/mrains/c                                                                                                                                                             c_hadoop/venv/lib/python2.7/posixpath.py
import posixpath # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/po                                                                                                                                                             sixpath.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/stat.pyc matches /home/mrains/cc_had                                                                                                                                                             oop/venv/lib/python2.7/stat.py
import stat # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/stat.py                                                                                                                                                             c
# /home/mrains/cc_hadoop/venv/lib/python2.7/genericpath.pyc matches /home/mrains                                                                                                                                                             /cc_hadoop/venv/lib/python2.7/genericpath.py
import genericpath # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/                                                                                                                                                             genericpath.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/warnings.pyc matches /home/mrains/cc                                                                                                                                                             _hadoop/venv/lib/python2.7/warnings.py
import warnings # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/war                                                                                                                                                             nings.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/linecache.pyc matches /home/mrains/c                                                                                                                                                             c_hadoop/venv/lib/python2.7/linecache.py
import linecache # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/li                                                                                                                                                             necache.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/types.pyc matches /home/mrains/cc_ha                                                                                                                                                             doop/venv/lib/python2.7/types.py
import types # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/types.                                                                                                                                                             pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/UserDict.pyc matches /home/mrains/cc                                                                                                                                                             _hadoop/venv/lib/python2.7/UserDict.py
import UserDict # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/Use                                                                                                                                                             rDict.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/_abcoll.pyc matches /home/mrains/cc_                                                                                                                                                             hadoop/venv/lib/python2.7/_abcoll.py
import _abcoll # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/_abc                                                                                                                                                             oll.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/abc.pyc matches /home/mrains/cc_hado                                                                                                                                                             op/venv/lib/python2.7/abc.py
import abc # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/abc.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/_weakrefset.pyc matches /home/mrains                                                                                                                                                             /cc_hadoop/venv/lib/python2.7/_weakrefset.py
import _weakrefset # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/                                                                                                                                                             _weakrefset.pyc
import _weakref # builtin
# /home/mrains/cc_hadoop/venv/lib/python2.7/copy_reg.pyc matches /home/mrains/cc                                                                                                                                                             _hadoop/venv/lib/python2.7/copy_reg.py
import copy_reg # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/cop                                                                                                                                                             y_reg.pyc
import encodings # directory /home/mrains/cc_hadoop/venv/lib/python2.7/encodings
# /home/mrains/cc_hadoop/venv/lib/python2.7/encodings/__init__.pyc matches /home                                                                                                                                                             /mrains/cc_hadoop/venv/lib/python2.7/encodings/__init__.py
import encodings # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/en                                                                                                                                                             codings/__init__.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/codecs.pyc matches /home/mrains/cc_h                                                                                                                                                             adoop/venv/lib/python2.7/codecs.py
import codecs # precompiled from /home/mrains/cc_hadoop/venv/lib/python2.7/codec                                                                                                                                                             s.pyc
import _codecs # builtin
# /home/mrains/cc_hadoop/venv/lib/python2.7/encodings/aliases.pyc matches /home/                                                                                                                                                             mrains/cc_hadoop/venv/lib/python2.7/encodings/aliases.py
import encodings.aliases # precompiled from /home/mrains/cc_hadoop/venv/lib/pyth                                                                                                                                                             on2.7/encodings/aliases.pyc
# /home/mrains/cc_hadoop/venv/lib/python2.7/encodings/utf_8.pyc matches /home/mr                                                                                                                                                             ains/cc_hadoop/venv/lib/python2.7/encodings/utf_8.py
import encodings.utf_8 # precompiled from /home/mrains/cc_hadoop/venv/lib/python                                                                                                                                                             2.7/encodings/utf_8.pyc
Python 2.7.11 (default, Apr  4 2016, 15:02:03)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
# clear __builtin__._
# clear sys.path
# clear sys.argv
# clear sys.ps1
# clear sys.ps2
# clear sys.exitfunc
# clear sys.exc_type
# clear sys.exc_value
# clear sys.exc_traceback
# clear sys.last_type
# clear sys.last_value
# clear sys.last_traceback
# clear sys.path_hooks
# clear sys.path_importer_cache
# clear sys.meta_path
# clear sys.flags
# clear sys.float_info
# restore sys.stdin
# restore sys.stdout
# restore sys.stderr
# cleanup __main__
# cleanup[1] encodings
# cleanup[1] site
# cleanup[1] abc
# cleanup[1] _weakrefset
# cleanup[1] _codecs
# cleanup[1] _warnings
# cleanup[1] zipimport
# cleanup[1] encodings.utf_8
# cleanup[1] codecs
# cleanup[1] signal
# cleanup[1] posix
# cleanup[1] encodings.aliases
# cleanup[1] exceptions
# cleanup[1] _weakref
# cleanup[2] copy_reg
# cleanup[2] posixpath
# cleanup[2] errno
# cleanup[2] _abcoll
# cleanup[2] types
# cleanup[2] genericpath
# cleanup[2] stat
# cleanup[2] warnings
# cleanup[2] UserDict
# cleanup[2] os.path
# cleanup[2] linecache
# cleanup[2] os
# cleanup sys
# cleanup __builtin__
# cleanup ints: 19 unfreed ints
# cleanup floats
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python uber_cust_hadoop.py
/home/mrains/cc_hadoop/venv/lib/python2.7/site-packages/faker/__init__.py:23: Pe                                                                                                                                                             ndingDeprecationWarning:
This faker package is being deprecated September 15, 2016.

You should switch to using https://pypi.python.org/pypi/fake-factory instead.
After September 15, 2016 the PyPi faker package will be changing to that!

  warnings.warn(deprecation_message, PendingDeprecationWarning)
Traceback (most recent call last):
  File "uber_cust_hadoop.py", line 309, in <module>
    CC_NO=gen_data.cc_number()
AttributeError: 'module' object has no attribute 'cc_number'
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ pip install fake-factory
Collecting fake-factory
  Downloading fake_factory-0.5.7-py2.py3-none-any.whl (484kB)
    100% |████████████████████████████████| 491kB 1.5MB/s
Collecting python-dateutil>=2.4 (from fake-factory)
  Downloading python_dateutil-2.5.2-py2.py3-none-any.whl (201kB)
    100% |████████████████████████████████| 204kB 2.3MB/s
Collecting six (from fake-factory)
  Downloading six-1.10.0-py2.py3-none-any.whl
Collecting ipaddress (from fake-factory)
  Downloading ipaddress-1.0.16-py27-none-any.whl
Installing collected packages: six, python-dateutil, ipaddress, fake-factory
Successfully installed fake-factory-0.5.7 ipaddress-1.0.16 python-dateutil-2.5.2                                                                                                                                                              six-1.10.0
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python uber_cust_hadoop.py
Traceback (most recent call last):
  File "uber_cust_hadoop.py", line 309, in <module>
    CC_NO=gen_data.cc_number()
AttributeError: 'module' object has no attribute 'cc_number'
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python uber_cust_hadoop.py
Traceback (most recent call last):
  File "uber_cust_hadoop.py", line 309, in <module>
    CC_NO=gen_data.cc_number()
AttributeError: 'module' object has no attribute 'cc_number'
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python
Python 2.7.11 (default, Apr  4 2016, 15:02:03)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import barnum
>>> exit()
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ python
Python 2.7.11 (default, Apr  4 2016, 15:02:03)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from barnum import gen_data
>>> gen_data.cc_number()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'cc_number'
>>> gen_data.DIRNAME
'/home/mrains/cc_hadoop/venv/lib/python2.7/site-packages/barnum'
>>> ^C
KeyboardInterrupt
>>> ^C
KeyboardInterrupt
>>> '/home/mrains/cc_hadoop/venv/lib/python2.7/site-packages/barnum'
'/home/mrains/cc_hadoop/venv/lib/python2.7/site-packages/barnum'
>>> exit()
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ dir
Airlines.py             Transaction_DistLoc.py
Branch_Zip.py           Transaction_Type.py
Country.py              uber_cust.csv
Detection_Scenarios     uber_cust_hadoop.py
geo_data.py             uber_cust_multithreading.py
geo_data.pyc            uber_cust.py
Hotels.py               uber_transactions_multithreading.py
Merchant_Category.py    uber_transactions.py
NAICS.py                venv
NAICS.pyc               zips.py
python_merchant_cat.py  zips.pyc
README.md
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ pwd
/home/mrains/cc_hadoop
(venv) [mrains@cmtoldelkkapp02 cc_hadoop]$ cd venv
(venv) [mrains@cmtoldelkkapp02 venv]$ cd lib
(venv) [mrains@cmtoldelkkapp02 lib]$ ls
python2.7
(venv) [mrains@cmtoldelkkapp02 lib]$ cd py*
(venv) [mrains@cmtoldelkkapp02 python2.7]$ ls
_abcoll.py    genericpath.py               posixpath.pyc      stat.py
_abcoll.pyc   genericpath.pyc              re.py              stat.pyc
abc.py        lib-dynload                  re.pyc             types.py
abc.pyc       linecache.py                 site-packages      types.pyc
codecs.py     linecache.pyc                site.py            UserDict.py
codecs.pyc    locale.py                    site.pyc           UserDict.pyc
config        locale.pyc                   sre_compile.py     warnings.py
copy_reg.py   no-global-site-packages.txt  sre_compile.pyc    warnings.pyc
copy_reg.pyc  ntpath.py                    sre_constants.py   _weakrefset.py
distutils     orig-prefix.txt              sre_constants.pyc  _weakrefset.pyc
encodings     os.py                        sre_parse.py
fnmatch.py    os.pyc                       sre_parse.pyc
fnmatch.pyc   posixpath.py                 sre.py
(venv) [mrains@cmtoldelkkapp02 python2.7]$ cd site-p*
(venv) [mrains@cmtoldelkkapp02 site-packages]$ ls
Airlines.py                   past
barnum                        pip
barnum-0.5.1.dist-info        pip-8.1.1.dist-info
Branch_Zip.py                 pkg_resources
builtins                      python_dateutil-2.5.2.dist-info
configparser                  python_merchant_cat.py
copyreg                       queue
Country.py                    README.md
dateutil                      reprlib
Detection_Scenarios           setuptools
_dummy_thread                 setuptools-20.6.7.dist-info
easy_install.py               six-1.10.0.dist-info
easy_install.pyc              six.py
fake_factory-0.5.7.dist-info  six.pyc
faker                         socketserver
Faker-0.1.4.dist-info         _thread
future                        tkinter
future-0.15.2.dist-info       Transaction_DistLoc.py
geo_data.py                   Transaction_Type.py
Hotels.py                     uber_cust_hadoop.py
html                          uber_cust_multithreading.py
http                          uber_cust.py
ipaddress-1.0.16.dist-info    uber_transactions_multithreading.py
ipaddress.py                  uber_transactions.py
ipaddress.pyc                 wheel
libfuturize                   wheel-0.29.0.dist-info
libpasteurize                 winreg
_markupbase                   xmlrpc
Merchant_Category.py          zips.py
NAICS.py
(venv) [mrains@cmtoldelkkapp02 site-packages]$ python uber_cust_hadoop.py
Traceback (most recent call last):
  File "uber_cust_hadoop.py", line 309, in <module>
    CC_NO=gen_data.cc_number()
AttributeError: 'module' object has no attribute 'cc_number'
(venv) [mrains@cmtoldelkkapp02 site-packages]$ python uber_cust_hadoop.py
  File "uber_cust_hadoop.py", line 16
    from fake-factory import Faker
             ^
SyntaxError: invalid syntax
(venv) [mrains@cmtoldelkkapp02 site-packages]$ python uber_cust_hadoop.py
(venv) [mrains@cmtoldelkkapp02 site-packages]$ python uber_transactions.py
(venv) [mrains@cmtoldelkkapp02 site-packages]$ ls -l
total 3864388
-rw-r--r--  1 mrains mrains      20204 Apr  4 14:55 Airlines.py
-rw-r--r--  1 mrains mrains      17610 Apr  4 17:24 Airlines.pyc
drwxrwxr-x  3 mrains mrains       4096 Apr  4 16:42 barnum
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 barnum-0.5.1.dist-info
-rw-r--r--  1 mrains mrains       7714 Apr  4 14:55 Branch_Zip.py
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 builtins
-rw-rw-r--  1 mrains mrains 3839025798 Apr  4 17:37 cc_trans.csv
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 configparser
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 copyreg
-rw-r--r--  1 mrains mrains       1483 Apr  4 14:55 Country.py
-rw-r--r--  1 mrains mrains       2634 Apr  4 17:24 Country.pyc
drwxrwxr-x  4 mrains mrains       4096 Apr  4 17:09 dateutil
-rw-r--r--  1 mrains mrains      12014 Apr  4 14:55 Detection_Scenarios
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 _dummy_thread
-rw-rw-r--  1 mrains mrains        126 Apr  4 16:42 easy_install.py
-rw-rw-r--  1 mrains mrains        315 Apr  4 16:42 easy_install.pyc
drwxrwxr-x  2 mrains mrains       4096 Apr  4 17:09 fake_factory-0.5.7.dist-info
drwxrwxr-x  6 mrains mrains       4096 Apr  4 17:09 faker
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:43 Faker-0.1.4.dist-info
drwxrwxr-x  9 mrains mrains       4096 Apr  4 16:42 future
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 future-0.15.2.dist-info
-rw-r--r--  1 mrains mrains    9710704 Apr  4 14:55 geo_data.py
-rw-r--r--  1 mrains mrains    5279280 Apr  4 17:19 geo_data.pyc
-rw-r--r--  1 mrains mrains      19816 Apr  4 14:55 Hotels.py
-rw-r--r--  1 mrains mrains      17433 Apr  4 17:24 Hotels.pyc
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 html
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 http
drwxrwxr-x  2 mrains mrains       4096 Apr  4 17:09 ipaddress-1.0.16.dist-info
-rw-rw-r--  1 mrains mrains      79904 Apr  4 17:09 ipaddress.py
-rw-rw-r--  1 mrains mrains      75360 Apr  4 17:09 ipaddress.pyc
drwxrwxr-x  3 mrains mrains       4096 Apr  4 16:42 libfuturize
drwxrwxr-x  3 mrains mrains       4096 Apr  4 16:42 libpasteurize
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 _markupbase
-rw-r--r--  1 mrains mrains       7718 Apr  4 14:55 Merchant_Category.py
-rw-r--r--  1 mrains mrains      11775 Apr  4 17:24 Merchant_Category.pyc
-rw-r--r--  1 mrains mrains    1042070 Apr  4 14:55 NAICS.py
-rw-r--r--  1 mrains mrains    1157761 Apr  4 17:19 NAICS.pyc
drwxrwxr-x  7 mrains mrains       4096 Apr  4 16:42 past
drwxrwxr-x 10 mrains mrains       4096 Apr  4 16:42 pip
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 pip-8.1.1.dist-info
drwxrwxr-x  4 mrains mrains       4096 Apr  4 16:42 pkg_resources
drwxrwxr-x  2 mrains mrains       4096 Apr  4 17:09 python_dateutil-2.5.2.dist-info
-rw-r--r--  1 mrains mrains      29238 Apr  4 14:55 python_merchant_cat.py
-rw-r--r--  1 mrains mrains      26787 Apr  4 17:24 python_merchant_cat.pyc
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 queue
-rw-r--r--  1 mrains mrains        108 Apr  4 14:55 README.md
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 reprlib
drwxrwxr-x  4 mrains mrains       4096 Apr  4 16:42 setuptools
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 setuptools-20.6.7.dist-info
drwxrwxr-x  2 mrains mrains       4096 Apr  4 17:09 six-1.10.0.dist-info
-rw-rw-r--  1 mrains mrains      30098 Apr  4 17:09 six.py
-rw-rw-r--  1 mrains mrains      29545 Apr  4 17:09 six.pyc
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 socketserver
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 _thread
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 tkinter
-rw-r--r--  1 mrains mrains       7600 Apr  4 14:55 Transaction_DistLoc.py
-rw-r--r--  1 mrains mrains       5873 Apr  4 17:24 Transaction_DistLoc.pyc
-rw-r--r--  1 mrains mrains       4651 Apr  4 14:55 Transaction_Type.py
-rw-r--r--  1 mrains mrains       2511 Apr  4 17:24 Transaction_Type.pyc
-rw-rw-r--  1 mrains mrains   95576885 Apr  4 17:23 uber_cust.csv
-rw-r--r--  1 mrains mrains      36200 Apr  4 17:22 uber_cust_hadoop.py
-rw-r--r--  1 mrains mrains      21570 Apr  4 14:55 uber_cust_multithreading.py
-rw-r--r--  1 mrains mrains      36201 Apr  4 14:55 uber_cust.py
-rw-r--r--  1 mrains mrains      35523 Apr  4 14:55 uber_transactions_multithrea
-rw-r--r--  1 mrains mrains      31205 Apr  4 14:55 uber_transactions.py
drwxrwxr-x  5 mrains mrains       4096 Apr  4 16:42 wheel
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 wheel-0.29.0.dist-info
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 winreg
drwxrwxr-x  2 mrains mrains       4096 Apr  4 16:42 xmlrpc
-rw-r--r--  1 mrains mrains    2790782 Apr  4 14:55 zips.py
-rw-r--r--  1 mrains mrains    1760570 Apr  4 17:19 zips.pyc
(venv) [mrains@cmtoldelkkapp02 site-packages]$ python uber_transactions.py

