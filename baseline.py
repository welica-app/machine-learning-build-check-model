from pathlib import Path

import pandas as pd
from sklearn.metrics import confusion_matrix


DATA_DIR = Path(__file__).resolve().parent
TARGET = "missed_scan"
QUEUE_LIMIT = 17
FALSE_ALARM_LIMIT = 0.15


def load_splits():
    parcels = pd.read_csv(DATA_DIR / "parcels.csv").drop_duplicates()
    split_ids = pd.read_csv(DATA_DIR / "split_ids.csv")

    if set(parcels["parcel_id"]) != set(split_ids["parcel_id"]):
        raise ValueError("Parcel IDs must match the supplied split.")
    if set(split_ids["split"]) != {"train", "held_out"}:
        raise ValueError("Expected train and held_out split labels.")

    rows = split_ids.merge(parcels, on="parcel_id", validate="one_to_one")
    train = rows.loc[rows["split"] == "train"]
    held_out = rows.loc[rows["split"] == "held_out"]
    return train, held_out


def print_scores(name, actual, predicted):
    tn, fp, fn, tp = confusion_matrix(actual, predicted, labels=[0, 1]).ravel()
    recall = tp / (tp + fn)
    false_alarm_rate = fp / (fp + tn)

    print(f"{name}: rows={len(actual)} TP={tp} FN={fn} FP={fp} TN={tn}")
    print(f"Recall: {tp}/{tp + fn} = {recall:.2%}")
    print(f"False alarm rate: {fp}/{fp + tn} = {false_alarm_rate:.2%}")
    within_limit = false_alarm_rate <= FALSE_ALARM_LIMIT
    print(f"Within false alarm limit ({FALSE_ALARM_LIMIT:.0%}): {within_limit}")


def main():
    _, held_out = load_splits()
    predicted = held_out["queue_length"] >= QUEUE_LIMIT
    print_scores("Baseline", held_out[TARGET], predicted)


if __name__ == "__main__":
    main()
