# User Interface - Beta

## Use:
- Requires flask to run
- python interface.py
- opens on localhost:5000 -- says so on run

## Webpage
- Two options on homepage
    (1) Train
    (2) Recognize
### Train
- Enter name, press submit
- On submit, opens "Cheese" to take photos.
    - Currently, no automated photos, so must manually taken 30 pictures. Can configure in "Cheese" settings
- On app close, interface.py runs make_align and make_classifier .py files, redirects to home

### Recognize
- "Start Recognition" button runs "realtime_facenet_git.py" file
