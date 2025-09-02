# FPSO Equipment Failure Analysis

## Challenge:
Analysis focused on predicting equipment failures in an FPSO (Floating Production, Storage, and Offloading) vessel. Where it's need to:
1. Calculate how many times the equipment has failed.
2. Categorize equipment failures by setup configurations (Preset 1 and Preset 2)
3. Categorize equipment failures by their nature/root cause according to parameter readings (temperature, pressure, and others)
4. Create a model (or models) using the technique you think is most appropriate and measure its performance.
5. Analyze variable importance

## Dataset Description
- **Cycle**: Sequential identifier of measurement cycles
- **Preset_1 & Preset_2**: Variables that control a specific operating point of the machine.
- **Temperature**: Temperature recorded in the equipment.
- **Vibrations (X, Y & Z)**: Vibrations along the machine's axes.
- **Frequency**: Operating frequency of the machine.
- **Fail**: Variable indicating whether the machine is in a failure state at the given timestamp.