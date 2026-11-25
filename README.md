# Build and check a model

You build a model that warns a parcel depot, while a van is being loaded, when a parcel may leave without its departure scan. You fix a check that lets in a field only known after departure, prove the fix with a test, and compare your model with the depot's simple queue rule on parcels the model has never seen.

## The files

| File | What it holds |
|---|---|
| `requirements.txt` | The exact versions of pandas, scikit-learn and pytest to install. |
| `parcels.csv` | Parcel records made up for this project. Each parcel ID stands for one chance to scan a parcel on an outbound trip. Some inputs are blank, and some rows appear twice, exactly the same. |
| `split_ids.csv` | The fixed split of parcels into training rows and held-out rows, by `parcel_id`. No parcel is in both. Training rows are the parcels the model learns from. Held-out rows are kept back, to test the model on parcels it has never seen. |
| `baseline.py` | Loads the data and the split, removes the exact copies, and checks that every parcel in the split is there exactly once. Then it runs the queue rule and prints its scores. Its `print_scores(name, actual, predicted)` function can score your model too. Give it the name to print, the held-out outcomes, and your predictions for the same parcels in the same order. |
| `train.py` | The candidate inputs and when each becomes known, the draft check on which inputs the model may use, and the unfinished pipeline. |
| `test_inputs.py` | Two passing tests of the input check, for an allowed input and an unknown one. A third test is skipped, ready for you to finish. Replace its skip line with a test that gives the check an input recorded after departure. Use the test for an unknown input, which expects a refusal, as a pattern. |
| `review_note.md` | Empty headings for your input checks, the held-out results and your recommendation. |

## The data

| Field | What it means |
|---|---|
| `parcel_id` | The parcel's key. Use it to match each parcel to the split. |
| `queue_length` | How many parcels were waiting at the moment of the decision, during loading. |
| `scanner_retries` | How many times the scanner at the loading desk had to try again, in the five minutes before the decision. |
| `minutes_until_departure` | How many minutes were left before the van's planned departure, at the moment of the decision. |
| `scan_receipt_count` | Zero or one departure scan receipts, counted ten minutes after departure. |
| `missed_scan` | The outcome, from the count ten minutes after departure. `1` means the scan is missing. `0` means a receipt is there. |

## The rules

- A model input must be known at the moment of the decision, before departure.
- The parcel ID and the outcome are never inputs.
- Keep the rows with blank inputs. Your model must handle the blanks itself.
- Fit the preparation steps and the classifier together, as one pipeline, on the training rows only. The classifier is the part that decides, for each parcel, whether to flag it as a likely missed scan. The pipeline keeps the preparation and the classifier together, so every parcel is prepared the same way before the classifier decides.
- Keep the split as it is. Use the held-out rows only for the final score.
- The queue rule flags a parcel when `queue_length` is 17 or more. A blank queue length gives no alert.
- Both your model and the rule are scored on all 60 held-out parcels, in the same order.

## How your model is judged

- **Recall** is the number of missed scans that were flagged, divided by all the missed scans.
- **The false alarm rate** is the number of flagged parcels that did have a scan, divided by all the parcels that had a scan.

Your model must have a higher recall than the queue rule, and a false alarm rate of 15% or less. Compare the rates before you round them. The held-out rows hold 19 missed scans and 41 parcels that had a scan. So your model must flag at least 10 of the 19 missed scans, with at most six false alarms among the 41.

## What to hand in

- `train.py`, with the fixed input check and the pipeline.
- `test_inputs.py`, with the finished test that fails if the old check comes back.
- `review_note.md`, filled in.

## How to start

1. Open https://github.com/welica-app/machine-learning-build-check-model in your browser.
2. Choose **Code**, then **Download ZIP**. Save the file and unzip it. You do not need Git for this project.
3. Open a terminal in the unzipped folder. A terminal is the window where you type commands to your computer.
4. Find Python 3.13 on your computer. Type `python --version`. If it does not show Python 3.13, try `python3 --version`, then `python3.13 --version`. On Windows, also try `py -3.13 --version`. Stop at the first one that shows Python 3.13. If none does, install Python 3.13 first, then try again.
5. Make an environment and turn it on. An environment is a folder that holds its own Python and its own packages for one project. On some computers, the Python that came installed refuses to install packages outside such an environment, and shows an error when you try. If you already have a Python 3.13 environment turned on, skip to the check at the end of this step.

   To make it, type the command that worked in step 4 without `--version`, then `-m venv .venv`. For example, type `python3.13 -m venv .venv` or `py -3.13 -m venv .venv`.

   Then turn it on. The command depends on your terminal:
   - In the Terminal app on a Mac, or a terminal on Linux, type `source .venv/bin/activate`.
   - In PowerShell on Windows, type `.venv\Scripts\Activate.ps1`. If PowerShell refuses to run it, open the Command Prompt in the same folder and use the next line.
   - In the Command Prompt on Windows, type `.venv\Scripts\activate.bat`.

   Now check the Python inside the environment. Type `python --version`. It must show Python 3.13. If it does not, the environment is not turned on, so type the command that turns it on again. From here on, type `python` in every command, whichever command you used in step 4. If you open a new terminal later, open it in the same folder and turn the environment on again.
6. Type `python -m pip install -r requirements.txt`. This installs the exact versions of pandas, scikit-learn and pytest that the project was built with.
7. Type `python baseline.py`. It prints how the queue rule did on the held-out parcels.
8. Type `python train.py`. It prints 180 training rows, 60 held-out rows and `Pipeline: TODO`.
9. Type `python -m pytest -q`. It runs the tests and reports two passed and one skipped.

If the last four commands run like this, you are ready.
