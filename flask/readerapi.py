
import ctypes
import sys
import os
import datetime


pc = ctypes.CDLL('libMMMReaderHighLevelAPI.so', ctypes.RTLD_GLOBAL)


Flag_end = False

#################################
## SDK - High Level API
#################################
def MMMReader_Initialise(aDataCallback, aEventCallback, aErrorCallback, aCertCallback, aProcessMessages, aProcessInputMessages, aParam):
	return pc.MMMReader_Initialise(aDataCallback, aEventCallback, aErrorCallback, aCertCallback, aProcessMessages, aProcessInputMessages, aParam)
def MMMReader_Shutdown():
	return pc.MMMReader_Shutdown()
def MMMReader_Reset():
	return pc.MMMReader_Reset()
def MMMReader_IsInitialised():
	return pc.MMMReader_IsInitialised()
def MMMReader_GetState():
	return pc.MMMReader_GetState()
def MMMReader_SetState(aNewState, aForceRedetect):
	return pc.MMMReader_SetState(aNewState, aForceRedetect)
def MMMReader_ForceRead():
	return pc.MMMReader_ForceRead()
def MMMReader_IsDocumentOnWindow():
	return pc.MMMReader_IsDocumentOnWindow()
def MMMReader_WaitForDocumentOnWindow(aTimeout):
	return pc.MMMReader_WaitForDocumentOnWindow(aTimeout)
def MMMReader_ReadDocument():
	return pc.MMMReader_ReadDocument()
def MMMReader_GetData(aDataType, aDataPtr, aDataLen, aIndex):
	return pc.MMMReader_GetData(int(aDataType), aDataPtr, aDataLen, aIndex)
def MMMReader_GetDataCount(aDataType, aItemCount):
	return pc.MMMReader_GetDataCount(aDataType, aItemCount)
def MMMReader_GetPluginData(aPluginName, aFeatureName, aPartNum, aDataPtr):
	return pc.MMMReader_GetPluginData(aPluginName, aFeatureName, aPartNum, aDataPtr)
def MMMReader_ClearData():
	return pc.MMMReader_ClearData()
def MMMReader_InitialisePositionCorrection(aPositionCorrectionCallback, aBoxCount, aBoxes):
	return pc.MMMReader_InitialisePositionCorrection(aPositionCorrectionCallback, aBoxCount, aBoxes)
def MMMReader_InitialiseSkipPlugin(aSkipPluginCallback):
	return pc.MMMReader_InitialiseSkipPlugin(aSkipPluginCallback)
def MMMReader_RFAbort():
	return pc.MMMReader_RFAbort()
def MMMReader_GetSettings(aSettings, aSize):
	return pc.MMMReader_GetSettings(aSettings, aSize)
def MMMReader_GetSettingValue(aSectionName, aSettingName, aSettingValue, aSize):
	return pc.MMMReader_GetSettings(aSectionName, aSettingName, aSettingValue, aSize)
def MMMReader_UpdateSettings(aNewSettings):
	return pc.MMMReader_UpdateSettings(aNewSettings)
def MMMReader_SaveSettings():
	return pc.MMMReader_SaveSettings()
def MMMReader_WriteTextfileSettings(aNewSettings, aPathFileName):
	return pc.MMMReader_WriteTextfileSettings(aNewSettings, aPathFileName)
def MMMReader_EnablePlugin(aPluginName, aEnabled):
	return pc.MMMReader_EnablePlugin(aPluginName, aEnabled)
def MMMReader_IsPluginEnabled(aPluginName, aEnabled):
	return pc.MMMReader_IsPluginEnabled(aPluginName, aEnabled)
def MMMReader_GetPluginName(aPluginName, aPluginNameLen, aPluginIndex):
	return pc.MMMReader_GetPluginName(aPluginName, aPluginNameLen, aPluginIndex)
def MMMReader_SetPluginOrder(aPluginName, aOrder):
	return pc.MMMReader_SetPluginOrder(aPluginName, aOrder)
def MMMReader_GetConnectedScanners(aSerialNumbers, aSerialNumbersLen, aNumScanners):
	return pc.MMMReader_GetConnectedScanners(aSerialNumbers, aSerialNumbersLen, aNumScanners)
def MMMReader_SelectScanner(aSerialNumber):
	return pc.MMMReader_SelecetScanner(aSerialNumber)
def MMMReader_EnableLogging(aEnabled, aLogLevel, aLogMask, aFilename):
	return pc.MMMReader_EnableLogging(aEnabled, aLogLevel, aLogMask, aFilename)
def MMMReader_GetLastError(aErrorCode, aErrorString, aStrLen):
	return pc.MMMReader_GetLastError(aErrorCode, aErrorString, aStrLen)
def MMMReader_LogMessage(aLevel, aMask, aLocation, aMessage):
	return pc.MMMReader_LogMessage(aLevel, aMask, aLocation, aMessage)
#def MMMReader_LogFormatted(aLevel, aMask, aLocation, aFormat, *args):
#	return pc.MMMReader_LogFormatted(aLevel, aMask, aLocation, aFormat, args)
def MMMReader_GetErrorMessage(aErrorCode, aErrorString, aStrLen):
	return pc.MMMReader_GetErrorMessage(aErrorCode, aErrorString, aStrLen)
def MMMReader_GetItemData(aDataFormat, aLocationInfo, aProcessName, aDataItemName, aDataPtr, aDataLen):
	return pc.MMMReader_GetItemData(aDataFormat, aLocationInfo, aProcessName, aDataItemName, aDataPtr, aDataLen)
def MMMReader_SetItemData(aDataFormat, aProcessName, aDataItemName, aBuffer, aBufferSize):
	return pc.MMMReader_SetItemData(aDataFormat, aProcessName, aDataItemName, aBuffer, aBufferSize)
def MMMReader_CaptureImage(alight, aImageFormat, aCompression, aCropWithExistingLocate, aRaw, aAntiGlare):
	return pc.MMMReader_CaptureImage(alight, aImageFormat, aCompression, aCropWithExistingLocate, aRaw, aAntiGlare)
def MMMReader_IsImageCroppingEnabled(aDataType, aEnabled):
	return pc.MMMReader_IsImageCroppingEnabled(aDataType, aEnabled)
def MMMReader_EnableImageCropping(aDataType, aEnabled):
	return pc.MMMReader_EnableImageCropping(aDataType, aEnabled)
def MMMReader_SignalEventEx(aAssumeControl, aSoundSettings, aLedSettings, aEvent):
	return pc.MMMReader_SignalEventEx(aAssumeControl, aSoundSettings, aLedSettings, aEvent)

#######################################
## Python API
#######################################
def IsInitialised():
	return MMMReader_IsInitialised() == 1

def Shutdown():
	return MMMReader_Shutdown()

def Reset():
	return MMMReader_Reset()

def IsDocumentOnWindow():
	return MMMReader_IsDocumentOnWindow == 1

def EnableLogging(aEnabled = True, aLogLevel = 1, aLogMask = -1, aFilename = b'reader.log'):
	return MMMReader_EnableLogging(aEnabled, aLogLevel, aLogMask, ctypes.create_string_buffer(aFilename))

def GetData(aDataType, aIndex = 0):
	pDataLen = (ctypes.c_int32 * 1)()
	MMMReader_GetData(int(aDataType), None, pDataLen, int(aIndex))
	print(pDataLen[0])
	raw_dat_tmp = (ctypes.c_ubyte * pDataLen[0])()
	MMMReader_GetData(int(aDataType), raw_dat_tmp, pDataLen, int(aIndex))
	return raw_dat_tmp

def GetState():
	return MMMReader_GetState()

def Get_IRImage():
	return GetData(4)

def Get_IRImageRear():
	return Get_Data(5)

def Get_VisibleImage():
	return GetData(6)

def Get_VisibleImageRear():
	return GetData(7)

def Get_PhotoImage():
	return GetData(10)

def Get_UVImage():
	return GetData(11)

def Get_UVImageRear():
	return GetData(12)

def GetConnectedScanners():
	aSerialNumbersLen = (ctypes.c_int * 1)()
	aNumScanners = (ctypes.c_int * 1)()
	MMMReader_GetConnectedScanners(None, aSerialNumbersLen, aNumScanners)
	if aSerialNumbersLen[0] > 0:
		aSerialNumbers = (ctypes.c_ubyte * aSerialNumbersLen[0])()
		MMMReader_GetConnectedScanners(aSerialNumbers, aSerialNumbersLen, aNumScanners)
		return (aNumScanners[0], aSerialNumbers)
	else:
		return (aNumScanners[0], None)
####################################
## Utils
####################################

def Save_TextFile(filename, text):
	print("path: " + filename)
	with open(filename, 'w') as file:
		file.write(text)

def Save_DataBin(filename, data):
	print("path: " + filename)
	with open(filename, 'wb') as file:
		file.write(data)

####################################
## Callbacks 
####################################
def processEventCallback(aEventCode):
	print("Event: " + str(aEventCode))
	if (aEventCode == 9): #SETTINGS_INITIALISED
		print("SETTINGS_INITIALISED")
	elif (aEventCode == 2):
		print("START_OF_DOCUMENT_DATA")
	elif (aEventCode == 3):
		print("END_OF_DOCUMENT_DATA")
		global Flag_end
		Flag_end = True
		Save_TextFile(os.path.join(path, "Successful.txt"), "OK - " + str(datetime.datetime.now()))
	elif (aEventCode == 27):
		print("READER_STATE_CHANGED")
	
def ProcessErrorCallback(aErrorCode, aErrorMessage):
	print("Error code:" + str(aErrorCode))
	print(aErrorMessage);


def ProcessDataCallback(aDataType, aDataLen, aDataPtr):
	print("Data Callback:")
	print("Type: " + str(aDataType))
	print("Len: " + str(aDataLen))
	if aDataType == 4:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		Save_DataBin(os.path.join(path, 'CD_IMAGEIR.jpg'), data)
	elif aDataType == 5:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		Save_DataBin(os.path.join(path, 'CD_IMAGEIRREAR.jpg'), data)
	elif aDataType == 6:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		Save_DataBin(os.path.join(path, 'CD_IMAGEVIS.jpg'), data)
	elif aDataType == 7:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		Save_DataBin(os.path.join(path, 'CD_IMAGEVISREAR.jpg'), data)
	elif aDataType == 11:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		Save_DataBin(os.path.join(path, 'CD_IMAGEUV.jpg'), data)
	elif aDataType == 12:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		Save_DataBin(os.path.join(path, 'CD_IMAGEUVREAR.jpg'), data)

#########################################################
## Initialise modes
#########################################################
def Initialise_blocking(aProcessMessages = True, aProcessInputMessages = True, aParam = None):
	return MMMReader_Initialise(None, None, None, None, aProcessMessages, aProcessInputMessages, aParam)

def Initialise_callback(aDataCallback = None, aEventCallback = None, aErrorCallback = None, aCertCallback = None, aParam = None):
	@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int32, ctypes.c_int, ctypes.c_void_p)
	def _StaticDataCallback(aParam, aDataType, aDataLen, aDataPtr):
		if aDataCallback != None:
			aDataCallback(aDataType, aDataLen, aDataPtr)
	@ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int32)
	def _StaticEventCallback(aParam, aEventCode):
		if aEventCallback != None:
			aEventCallback(aEventCode)
		return
	@ctypes.CFUNCTYPE(None, ctypes.c_int32, ctypes.c_wchar_p, ctypes.c_void_p)
	def _StaticErrorCallback(aErrorCode, aErrorMessage, aParam):
		if aErrorCallback != None:
			aErrorCallback(aErrorCode, aErrorMessage);
	#@ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_int, ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int_p)
	#def StaticCertificateCallback(aParam, aCertIdentifier, aCertIdentifierLen, aCertType, aCertBuffer, aCertBufferLen):
	#	if aCertCallback != None:
	#		return aCertCallback(aParam, aCertIdentifier, aCertIdentifierLen, aCertType, aCertBuffer, aCertBufferLen);		
	return MMMReader_Initialise(_StaticDataCallback, _StaticEventCallback, _StaticErrorCallback, None, False, False, aParam)

#########################################################
## Main
#########################################################
if __name__ == '__main__':

	if len(sys.argv) < 2:
		print('You must specify a path')
		exit()

	path = sys.argv[1]

	print('Path: ' + path)

	isExist = os.path.exists(path)
	if not isExist:
		os.makedirs(path) 

	EnableLogging(True, 1, -1, b"reader.log")
	Initialise_callback(aDataCallback = ProcessDataCallback, aEventCallback = processEventCallback)

	if IsInitialised() == False:
		Shutdown()
		exit()

	#input("Press any key to close the application...\r\n")
	try:
		while Flag_end == False:
			pass
	except KeyboardInterrupt:
		print("Interrupted!")
	Shutdown()