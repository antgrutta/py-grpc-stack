import os


class Config:
    LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG')
    SERVICE_PORT = os.environ.get('SERVICE_PORT', '50051')
