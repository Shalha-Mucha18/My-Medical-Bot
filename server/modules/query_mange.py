from logger import logger


def quey_chain(chain, user_input:str):

    try:
        logger.info(f"Running chain for input: {user_input}")
        result = chain({'query': user_input})
        response = {
          "response": result['result'],
          "sources":[doc.metadata.get("source","") for doc in result['source_documents']]
        }
        logger.debug(f"Chain result: {response}")
        return response
    except Exception as e:
        logger.error(f"Error running chain: {e}")   
        return {"response": "An error occurred while processing your request."}
