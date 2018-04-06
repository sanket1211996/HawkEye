import json
from  firebase import firebase

# your variables are already assigned before this
#
# firebase = firebase.FirebaseApplication('https://my-travel-junction.firebaseio.com/Location', None)
#
#
# firebase.put('/LocationUpdate',"latitude",54)
# firebase.put('/LocationUpdate',"longitude",64)
#
# latitude= firebase.get('/LocationUpdate','latitude')
# print (latitude)
# longitude = firebase.get('/LocationUpdate','longitude')
# print (longitude)




#result = firebase.post("/-L9R1cMDzq4RjLZhOzd_", {'lat':'4' , 'long': '5'})
#result = firebase.post("/-L9R1cMDzq4RjLZhOzd_", {'lat':'1.324' , 'long': '10.455'})

#print(result)


#
# from pyfcm import FCMNotification
#
# push_service = FCMNotification(api_key="AIzaSyA9lDAhCrQbo03msu0FE5TFd145guNWOSg")
#
#
#
#
# # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
#
# registration_id = "<device registration_id>"
# message_title = "Uber update"
# message_body = "Hi john, your customized news for today is ready"
# result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
#
# # Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
#
# print result