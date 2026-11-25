from sklearn.pipeline import Pipeline

from baseline import load_splits


AVAILABLE_WHEN = {
    "queue_length": "before_departure",
    "scanner_retries": "before_departure",
    "minutes_until_departure": "before_departure",
    "scan_receipt_count": "after_departure",
}
DRAFT_FEATURES = [
    "queue_length",
    "scanner_retries",
    "minutes_until_departure",
    "scan_receipt_count",
]


def validate_inputs(columns):
    unknown = [column for column in columns if column not in AVAILABLE_WHEN]
    if unknown:
        raise ValueError(f"Unknown model inputs: {', '.join(unknown)}")


def build_pipeline() -> Pipeline:
    # TODO: Add preprocessing and classification steps.
    raise NotImplementedError


def main():
    validate_inputs(DRAFT_FEATURES)
    train_rows, held_out_rows = load_splits()

    # TODO: Fit on train_rows and score predictions on held_out_rows.
    print(f"Training rows: {len(train_rows)}")
    print(f"Held-out rows: {len(held_out_rows)}")
    print("Pipeline: TODO")


if __name__ == "__main__":
    main()
