##################
# ANDROPYINFO.PY #
##################

import android
import time
import string
import sys
import subprocess

droid = android.Android()

def SignalstrenghtInfo():
 rt='[SIGNALSTRENGHT INFO] \n'
 droid.startTrackingSignalStrengths()
 time.sleep(5)
 droid.stopTrackingSignalStrengths()
 result =droid.readSignalStrengths()
 rt=rt+'SIGNALSTRENGHT_INFO:'+str(result.result)+';\n'
 return rt

def WifiInfo():
 rt='[WI-FI INFO] \n'
 #
 result=droid.checkWifiState ()
 rt=rt+'WIFI_STATE:'+str(result.result)+';\n'
 if result.result == True:
		result=droid.wifiGetConnectionInfo()
		rt=rt+'ACCESSPOINT_INFO:'+str(result.result)+';\n'
 return rt


def CellInfo():
 rt='[PHONE INFO] \n'
 droid.startTrackingPhoneState()
 #events=droid.eventPoll (5)
 #print (events)
 result=droid.getSimState ()
 rt=rt+'SIM_STATE:'+result.result+';\n'
 #
 result=droid.getDeviceId ()
 rt=rt+'DEVICE_ID:'+result.result+';\n'
 #
 result=droid.getDeviceSoftwareVersion()
 rt=rt+'DEVICE_SW_VER:'+result.result+';\n'
 #
 u=droid.getPhoneType ()
 rt=rt+'PHONE_TYPE:'+result.result+';\n'
 #
 result=droid.getSimCountryIso ()
 rt=rt+'SIM_COUNTRY:'+result.result+';\n'
 #
 result=droid.getSimOperator ()
 rt=rt+'SIM_OPERATOR:'+result.result+';\n'
 #
 result=droid.getSimOperatorName ()
 rt=rt+'SIM_OPERATOR_NAME:'+result.result+';\n'
 #
 result=droid.getSimSerialNumber ()
 rt=rt+'SIM_S/N:'+result.result+';\n'
 #
 result=droid.getSimState ()
 rt=rt+'SIM_STATE:'+result.result+';\n'
 #
 droid.stopTrackingPhoneState()
 return rt


def BatteryInfo():
 rt='[BATTERY INFO] \n'
 droid.batteryStartMonitoring()
 #
 result=droid.batteryGetStatus ()
 rt=rt+'BATTERY_STATUS:'+str(result.result)+';\n'
 #
 result=droid.batteryGetHealth ()
 rt=rt+'BATTERY_HEALTH:'+str(result.result)+';\n'
 #
 result=droid.batteryGetLevel ()
 rt=rt+'BATTERY_LEVEL:'+str(result.result)+';\n'
 #
 result=droid.batteryGetPlugType ()
 rt=rt+'BATTERY_PLUGTYPE:'+str(result.result)+';\n'
 #
 result=droid.batteryGetTechnology ()
 rt=rt+'BATTERY_TECHNOLOGY:'+str(result.result)+';\n'
 #
 result=droid.batteryGetTemperature ()
 rt=rt+'BATTERY_TEMPERATURE:'+str(result.result)+';\n'
 #
 result=droid.batteryGetVoltage ()
 rt=rt+'BATTERY_VOLTAGE:'+str(result.result)+';\n'
 
 droid.batteryStopMonitoring()
 return rt

def LocationInfo():
 rt='[LOCATION INFO] \n'
 lastaddr =''
 address=''
 droid.startLocating()
 time.sleep(30) 
 loc = droid.readLocation().result 
 if loc =={}:
  lastloc = droid.getLastKnownLocation().result
  print 'no current position'
  if lastloc != {}:
   try:
    n = lastloc ['gps'] 
   except KeyError:
    n = lastloc ['network']
    print n
    la = n['latitude']
    print la
    lo = n['longitude']
    print lo
    lastaddr =str(la)+'/'+str(lo)
   else :
    print 'no last position'
    
 if loc != {}:
  try:
   n = loc['gps'] 
  except KeyError:
   n = loc['network']
   la = n['latitude']
   lo = n['longitude']
   address =str(la)+'/'+str(lo)
   
 droid.stopLocating()
 rt=rt+'LOCATION: '+str(address)+';\n'
 rt=rt+'LAST_LOCATION: '+str(lastaddr)+';\n'
 return rt
 
#Apro file
try:
 out_file=open("Res.txt","w")
 print 'File Open'
 text=str(CellInfo())
 out_file.write(text)
 text=str(SignalstrenghtInfo())
 out_file.write(text)
 text=str(BatteryInfo())
 out_file.write(text)
 text=str(LocationInfo())
 out_file.write(text)
 text=str(WifiInfo())
 out_file.write(text)
 out_file.close
 print 'File Close'

except:
  print 'Error!',sys.exc_info ()[0], sys.exc_info ()[1]



