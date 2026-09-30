import logging

def get_logger():
    logging.basicConfig(
        filename="etl_pipeline.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger("etl_pipeline")