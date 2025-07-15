from bruce import init, bracks, bruceformatter
import logging

init() # initialize bruce

logger = logging.getLogger("bruce-demo")
handler = logging.StreamHandler()
handler.setFormatter(bruceformatter("%(levelname)s: %(message)s")) # input modified formatter
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info(f"this is a test log! {bracks('test brackets')}") # logger message
