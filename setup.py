from distutils.core import setup

setup(
    name='slackhandler',
    version='0.1.0',
    description='Posts logs to Slack webhooks.',
    install_requires=['requests'],
    packages=['slackhandler'],
)
