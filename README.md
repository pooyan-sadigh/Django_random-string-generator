# random-string-generator:
random string generator to auto fill the slug field for model objects (by pre-save method)
# purpose:
This is for a Django project and it assumes your instance has a model with a slug field and a title character (char) field.
# notice:
1) You need to copy and paste ulits.py in model directory to generate a random unique tag for each object.
2) It automatically generates different unique tag even if the object is a duplicate.
# requirements:
1) python 3.9
2) django 3.1.5
