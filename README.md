# Motion Analysis – 1D Kinematics (Python)

This project models and visualizes 1D motion using analytical functions for
position, velocity, and acceleration.

It was developed as part of Physics coursework and refined into a clean,
reproducible visualization tool.

## Physics Model
- Position: x(t) = 3t² − 4t + 2
- Velocity: v(t) = dx/dt = 6t − 4
- Acceleration: a(t) = dv/dt = 6

The script highlights the **direction-change event** where velocity crosses zero
(at t = 2/3 s).

## Project Structure
- `physics/kinematics_motion_analysis/motion_analysis.py`  
  Final, cleaned version of the model and plots

- `physics/kinematics_motion_analysis/prototypes/`  
  Early iterations showing development of plotting, annotation, and event detection

## Output
The script generates:
- Position vs Time
- Velocity vs Time
- Acceleration vs Time  
with annotated sample points and key events.

## How to Run
```bash
pip install numpy matplotlib
python physics/kinematics_motion_analysis/motion_analysis.py
