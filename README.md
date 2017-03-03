# Slack Handler

## Installation

```
pip install git+https://github.com/seanshahkarami/slackhandler
```

## Example

```python
import logging
from slackhandler import SlackHandler

logger = logging.getLogger('cool-program')
logger.setLevel(logging.DEBUG)
logger.addHandler(SlackHandler('T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'))

logger.info('What! Are you wasting my time!? Get out of here!')
logger.warn('Oh! I should pay attention to this one.')
logger.error('Uhhh...sorry...I should have listened earlier...')
```
