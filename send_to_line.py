import requests


def send_msg(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = 'omRcr27V8Ev2n8J86qPUgeGScGwB0GJbPGrBOwMoN7F'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    print('LINEに通知を送信しました')
    requests.post(line_notify_api, headers = headers, data = data)

