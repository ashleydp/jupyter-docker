import sys
from notebook.auth import passwd

if len(sys.argv) < 2:
    sys. exit("You must define a password")
elif len(sys.argv[1]) < 5:
    sys.exit("Password must have at least 8 characters!")

pwd = passwd(sys.argv[1])

jupyter_row = "c.NotebookApp.password = u'{}'".format(pwd)

jconfig = open("/root/.jupyter/jupyter_notebook_config.py", "a+")

jconfig.write(jupyter_row)

jconfig.close()

print("Password set successfully")