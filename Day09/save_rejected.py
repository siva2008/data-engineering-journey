import csv


def save_rejected_data(rejected_employees, filename):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "id",
            "name",
            "department",
            "salary",
            "reason"
        ])

        for rejected in rejected_employees:

            employee = rejected["employee"]
            reason = rejected["reason"]

            writer.writerow([
                employee["id"],
                employee["name"],
                employee["department"],
                employee["salary"],
                reason
            ])

    print(f"Rejected data saved to {filename}")