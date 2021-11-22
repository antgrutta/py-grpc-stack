import logging
import sys
import grpc
from config import Config

# Logging Settings
logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=Config.LOGLEVEL,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()


class RequestHeaderInterceptor(grpc.ServerInterceptor):

    def intercept_service(self, continuation, handler_call_details):
        logger.debug(handler_call_details)

        return continuation(handler_call_details)
