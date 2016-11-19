#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS 
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
from com.xebialabs.xlrelease.plugin.overthere import RemoteScript

if taskPasswordToken and taskPassword:
    script = task.pythonScript.getProperty("script")
    script = script.replace(taskPasswordToken, taskPassword)
    task.pythonScript.setProperty("script",script)

rs = RemoteScript(task.pythonScript)

exitCode = rs.execute()

output = rs.getStdout()
err = rs.getStderr()

if (exitCode == 0):
    print output
else:
    print "Exit code "
    print exitCode
    print
    print "#### Output:"
    print output

    print "#### Error stream:"
    print err
    print
    print "----"

    sys.exit(exitCode)
