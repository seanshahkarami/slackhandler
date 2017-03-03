from distutils.core import setup

setup(
    name='slackhandler',
    version='0.1.0',
    description='Posts logs to Slack webhooks.',
    author='Sean Shahkarami',
    author_email='sean.shahkarami@gmail.com',
    url='https://github.com/seanshahkarami/slackhandler',
    install_requires=['requests'],
    packages=['slackhandler'],
)
