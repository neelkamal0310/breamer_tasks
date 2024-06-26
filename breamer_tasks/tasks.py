from .app import app
import logging

logger = logging.getLogger(__name__)


@app.task
def say_wtf():
    logger.warning("WHAT THE FUCK MAN")
