import logging
import requests
import json


class SlackHandler(logging.Handler):

    colors = {
        'CRITICAL': '#e01765',
        'ERROR': '#e01765',
        'WARNING': '#e8a723',
        'INFO': '#3eb890',
        'DEBUG': '#70cadb',
    }

    def __init__(self, webhook, **kwargs):
        logging.Handler.__init__(self)
        self.webhook = webhook
        self.url = 'https://hooks.slack.com/services/{}'.format(webhook)

    def emit(self, record):
        params = record.__dict__
        timestamp = params['created']
        name = params['name']
        level = params['levelname']
        msg = params['msg']

        color = self.colors.get(level, '#000000')

        data = {
            'attachments': [
                {
                    'ts': timestamp,
                    'text': msg,
                    'color': color,
                    'author_name': name,
                    'fallback': '{} {}'.format(level, msg),
                }
            ]
        }

        requests.post(self.url, data=json.dumps(data))
