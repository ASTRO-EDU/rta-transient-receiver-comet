from distutils.core import setup

setup(
    name="rta-transient-receiver",
    author="Antonio Addis, Luca Babboni",
    version="2.0.0",
    packages=['comet/plugins', "comet/plugins/test", 'comet/plugins/extractors'],
    data_files=[('comet_voevent_reciver_config', ['./config.json'])],
    license='GPL-3.0'
)
