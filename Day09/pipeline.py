from extract import extract_data
from transform import transform_data
from load import load_data
from save_rejected import save_rejected_data
from logger import get_logger


logger = get_logger()


def run_pipeline():

    try:

        logger.info("Starting ETL pipeline")

        # Extract
        employees = extract_data("employee_source.csv")

        logger.info(f"Extracted records: {len(employees)}")

        # Transform and validate
        valid_employees, rejected_employees = transform_data(employees)

        logger.info(f"Valid records: {len(valid_employees)}")
        logger.warning(f"Rejected records: {len(rejected_employees)}")

        # Load valid records
        load_data(valid_employees)

        logger.info("Valid data loaded successfully")

        # Save rejected records
        save_rejected_data(
            rejected_employees,
            "rejected_data.csv"
        )

        logger.info("Rejected data saved successfully")

        logger.info("ETL pipeline completed")

    except Exception as error:

        logger.exception(
            f"ETL pipeline failed: {error}"
        )

        raise


if __name__ == "__main__":
    run_pipeline()