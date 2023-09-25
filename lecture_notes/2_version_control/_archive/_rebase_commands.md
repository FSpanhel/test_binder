# messy
python3 lecture_notes/1_version_control/rebase.py clear &&
python3 lecture_notes/1_version_control/rebase.py messy;

# rebased
python3 lecture_notes/1_version_control/rebase.py clear &&
python3 lecture_notes/1_version_control/rebase.py rebased;

# rebased_no_ff
python3 lecture_notes/1_version_control/rebase.py clear &&
python3 lecture_notes/1_version_control/rebase.py rebased_no_ff;

# interactive_rebase before 1st merge
python3 lecture_notes/1_version_control/rebase.py clear &&
python3 lecture_notes/1_version_control/rebase.py rebased_no_ff;



#
python3 lecture_notes/1_version_control/rebase.py clear &&
python3 lecture_notes/1_version_control/rebase.py interactive_rebase;
python3 lecture_notes/1_version_control/rebase.py finish_with_squash;
