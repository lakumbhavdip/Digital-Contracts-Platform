
# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAA5LS_Q2E:APA91bEl-inXQwB-OrfEIT0k34patsZwicmujZay4a0lZoopkGEuxDfQp6KCHmP07tOIKzVdJGHPLaAt469F8N9tU4vcV_f8wEizbuUMSmgJ6xXav0RBKa_Hqd_4d1fMCsrtVYly6g6S")

# Send to multiple devices by passing a list of ids.

registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]

message_title = "Uber update"

message_body = "Hope you're having fun this weekend, don't forget to check today's news"

result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print(result)