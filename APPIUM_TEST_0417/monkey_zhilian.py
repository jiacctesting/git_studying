from com.android.monkeyrunner import MonkeyRunner as mr

from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

device=mr.waitForConnection()
package='com.zhaopin.social'
activity=".SplashActivity"
runComponent=package+"/"+activity
device.startActivity(component=runComponent)


