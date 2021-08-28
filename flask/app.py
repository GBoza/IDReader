
import ctypes
import threading
import time
import datetime
import os
from flask import Flask, request, render_template
from flask import json
from flask import send_file
import glob
import readerapi as api

app = Flask(__name__)

path = './'

####################################
## Callbacks
####################################

def processEventCallback(aEventCode):
	print("Event Callback:")
	print("Event Code: " + str(aEventCode))
	if (aEventCode == 9): #SETTINGS_INITIALISED
		print("SETTINGS_INITIALISED")
	elif (aEventCode == 10):
		print("PLUGINS_INITIALISED")
	elif (aEventCode == 2):
		print("START_OF_DOCUMENT_DATA")
	elif (aEventCode == 3):
		print("END_OF_DOCUMENT_DATA")
	elif (aEventCode == 27):
		print("READER_STATE_CHANGED")
	elif (aEventCode == 37):
		print("READER_CONNECTED")
	elif (aEventCode == 38):
		print("READER_DISCONNECTED")

def ProcessDataCallback(aDataType, aDataLen, aDataPtr):
	print("Data Callback:")
	print("Data Type: " + str(aDataType))
	print("Len: " + str(aDataLen))
	if aDataType == 4:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		api.Save_DataBin(os.path.join(path, 'CD_IMAGEIR.jpg'), data)
	elif aDataType == 5:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		api.Save_DataBin(os.path.join(path, 'CD_IMAGEIRREAR.jpg'), data)
	elif aDataType == 6:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		api.Save_DataBin(os.path.join(path, 'CD_IMAGEVIS.jpg'), data)
	elif aDataType == 7:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		api.Save_DataBin(os.path.join(path, 'CD_IMAGEVISREAR.jpg'), data)
	elif aDataType == 11:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		api.Save_DataBin(os.path.join(path, 'CD_IMAGEUV.jpg'), data)
	elif aDataType == 12:
		data = (ctypes.c_byte * aDataLen)()
		ctypes.memmove(data, ctypes.cast(aDataPtr, ctypes.POINTER(ctypes.c_byte)), aDataLen)
		api.Save_DataBin(os.path.join(path, 'CD_IMAGEUVREAR.jpg'), data)

############################################
## Reader thread
############################################

def thread_function():
	try:
		print('Start thread.')
		api.EnableLogging()
		while True:
			print('Initialise...')
			api.Initialise_callback(aDataCallback = ProcessDataCallback, aEventCallback = processEventCallback)
			if api.IsInitialised():
				print('Initialised.')
				while True:
					if api.IsDocumentOnWindow():
						print('DocumentOnWindow')
					time.sleep(10)
			api.Shutdown()
			time.sleep(5)
			#initiliase again
	except:
		api.Shutdown()
		print("End thread.")
		time.sleep(1)
		threading.Thread(target = thread_function, args = ()).start() #run forever

###########################################
## Flask
###########################################

@app.route('/api/SetPath', methods=['GET'])
def _setPath():
	try:
		_path = request.args.get('path')
		isExist = os.path.exists(_path)
		if not isExist:
			os.makedirs(_path)
		global path
		path = _path
		return {'success': True, 'path' : os.path.abspath(path)}
	except:
		return {'success' : False, 'path' : os.path.abspath(path)}

@app.route('/api/IsInitialised')
def _isInitialised():
	return {'value': api.IsInitialised()}

@app.route('/api/IsDocumentOnWindow')
def _IsDocumentOnWindow():
    return {'value': api.IsDocumentOnWindow()}

@app.route('/api/GetState')
def _GetState():
    return {'value': api.GetState()}

@app.route('/api/GetImage', methods=['GET'])
def _GetImage():
	file = request.args.get('file')
	return send_file(os.path.join(path, file))

@app.route('/api/ListImages')
def _listImages():
	print(glob.glob(os.path.join(path,'*.jpg')))
	_listjpg = glob.glob(os.path.join(path,'*.jpg'))
	imagedic = {}
	for i in range(len(_listjpg)):
		imagedic[str(i)] = os.path.basename(_listjpg[i])
	return {'path': os.path.abspath(path), 'images' : imagedic}

@app.route('/api/Images/<imagefile>')
def _getImage2(imagefile):
	return send_file(os.path.join(path, str(imagefile)))

######################################################
## Main
######################################################

if __name__ == '__main__':
	threading.Thread(target = thread_function, args = ()).start()
	app.run(host='0.0.0.0', port = 7080)
	print("Shutdown...")
	api.Shutdown()


