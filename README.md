This is a set of scripts to prepare, run, and analyze
an A/B comparison listening test.

**PREREQUISITES**<br>
  The runtest.py runs only on Windows.
  Python 3 is necessary to run scripts.

**FILES**
- makelist.py : makes a test pairs list from a wav file list.
- wav-list-sample.txt : an example wav file list.
- pairs-list-sample.txt : an example wav file pairs list.
- runtest.py : executes the listening test.
- start_mark.wav : tone marker indicating start of each comparison.
- end_mark.wav : tone marker indicating end of each comparison.
- finish_mark.wav : tone marker indicating the session finishes.
- analysis.py : calculates scores and 95% confidence interval for each test samples.
