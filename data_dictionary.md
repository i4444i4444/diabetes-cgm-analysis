# Data dictionary

## Source
25 CSV files, separator `;`, one file per patient (`HUPA0001P.csv` -> `HUPA0001`).
Collection period: 2018-06 .. 2022-05. Timestamps are local time, timezone is not specified.

## Columns

| Column | Meaning | Units | Comment |
|---|---|---|---|
| patient_id | patient identifier | — | derived from the file name |
| time | measurement timestamp | — | exactly 5-minute grid |
| glucose | continuous glucose monitor reading | mg/dL | minimum is exactly 40 — looks clipped |
| calories | calories per 5 minutes | not verified | |
| heart_rate | heart rate | bpm | |
| steps | step count per 5 minutes | steps | |
| basal_rate | basal insulin rate | NOT VERIFIED | zero for 5 patients |
| bolus_volume_delivered | bolus insulin delivered | U | zero in almost all rows |
| carb_input | carbohydrate intake | NOT VERIFIED | 0-278 g per day across patients — inconsistent scale |

## Known issues
1. No missing values at all -> the data was already interpolated before we got it.
2. `carb_input` and `basal_rate`: units are unverified and empty for some patients.
3. HUPA0026-0028: 90-574 days versus 8-14 days for the rest; HUPA0027 alone is 53% of all rows.

## Decisions
- Timestamps are kept as local time, no timezone conversion.
- Units are not converted in the loader; any conversion will be added separately after verification.