sitemap-generator
=================

* [What is this?](#what-is-this)
* [Assumptions](#assumptions)
* [What's in here?](#whats-in-here)
* [Bootstrap the project](#bootstrap-the-project)
* [Run the project](#run-the-project)
* [Deploy the sitemap](#deploy-the-sitemap)

What is this?
-------------

Generates and deploys a xml sitemap from a google spreadsheet for our standalone projects

Assumptions
-----------

The following things are assumed to be true in this documentation.
* You are running OSX.
* You are using Python 2.7. (Probably the version that came OSX.)
* You have virtualenv and virtualenvwrapper installed and working.
* You have postgres installed and running

For more details on the technology stack used with the app-template, see our [development environment blog post](http://blog.apps.npr.org/2013/06/06/how-to-setup-a-developers-environment.html).

This code should work fine in most recent versions of Linux, but package installation and system dependencies may vary.

What's in here?
---------------

The project contains the following folders and important files:

* ``fabfile`` -- Fabric tasks
* ``requirements.txt`` -- Python requirements.
* ``data`` -- Folder used to download the spreadsheet and store the xml sitemap
* `oauth.py`` -- OAuth flow to access google drive
* ``parse_copy.py`` -- parses the downloaded google spreadsheet using jinja2 templates
* ``app_config.py`` -- Application configuration
* ``render_utils.py`` -- Utils to generate jinja2 template context


Bootstrap the project
---------------------

To bootstrap the project:

```
git clone git@github.com:nprapps/sitemap-generator.git
cd sitemap-generator
mkvirtualenv sitemap-generator
pip install -r requirements.txt
```

Run the project
---------------

To generate the sitemap run (it automatically downloads the most recent version of the spreadsheet):

```
fab sitemap
```

This will write a new `sitemap_apps.xml` inside the data folder for the projects that are marked to be included in the sitemap on the google spreadsheet.

If you want to just download the copy and take a look prior to the sitemap generation then run:

```
fab text.update
```

Also if you want to navigate to the spreadsheet from the commandline....nice!!!!, run:

```
fab spreadsheet.open
```

Deploy the sitemap
------------------

In order to deploy the generated sitemap we will need to mount the samba folder in our computer, copy the local file to the server and finally unmount the server from our local filesystem.

Since all of this operations are somewhat convoluted we have left each one as an individual task.

To mount the server at the location where the sitemap should go run:

```
fab smb.mount
```

_The samba server we are connecting with should be defined as an environment variable named `sitemap_generator_DEFAULT_SERVER` or passed a the first parameter to the mount command like in the following example_

```
fab smb.mount:server="yoursambaserver"
```

To actually deploy the file to the server (it will overwrite the old file if it exists):

```
fab smb.deploy
```

**Finally do not forget to unmount the server from our local filesystem**, run:

```
fab smb.umount
```

Since the mounted point has a lot of information it takes a while to mount and you may get an error when unmounting. If so run it on force mode.

```
fab smb.umount:force=True
```
