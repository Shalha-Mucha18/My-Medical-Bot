import logging

def setup_logger(name="medicalbot"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(ch)
    return logger



logger = setup_logger()
logger.info("RAG server logger initialized")
logger.debug("Debugging information for RAG server")
logger.error("Error occurred in RAG server")
logger.warning("Warning in RAG server") 
logger.critical("Critical issue in RAG server")




