# NFL Fourth-Down Decision Making & Win Probability

This project builds an interpretable win-probability model from NFL play-by-play data
and evaluates 4th-down coaching decisions (punt vs field goal vs go-for-it).

It includes a focused Miami Dolphins (MIA) case study.

## Why this matters
NFL teams care about:
- calibrated probability models
- decision support under uncertainty
- translating analytics into coaching insight

This project demonstrates that end-to-end.

## Notebooks
1. 01_data_exploration.ipynb  
   Load pbp, clean plays, label 4th-down decisions

2. 02_win_probability.ipynb  
   Train a home-win probability model and evaluate calibration

3. 03_fourth_down_simulator.ipynb  
   Simulate punt / FG / go-for-it and compute decision cost

4. 04_dolphins_case_study.ipynb  
   Dolphins vs league aggressiveness and decision quality

## Resume bullet
Built a win-probability model from NFL play-by-play data and developed a fourth-down
decision simulator quantifying expected win probability and decision cost, with a
team-level case study for the Miami Dolphins.