# hatchConnect
Our childcare provider uses *Baby Connect* to the day.  We have used 'Hatch Baby' since birth.  This allows us to easily pull the days data out of *Baby Connect* and post it to *Hatch Baby*

## Hatch Baby Payloads
**Note:** There are many more properties available. Use a 'Get' function to view them
```python
length = {
    'length':60, # cm
    'measurementDate':'2019-11-25'
    }
weight = {
    'weight':38, #grams
    'measurementTime':'2019-11-25 10:25:00'
    }
feeding = {
    'startTime':'2019-11-25 09:00:00',
    'endTime':'2019-11-25 09:30:00',
    'category':'Manual',
    'method':'Bottle',
    'source':'Formula', # Breastmilk
    'amount':88.72 # ml
    }
diaper = {
    'diaperType':'Wet', # Dirty or Both
    'diaperDate':'2019-11-25 11:00:00'
    }
sleep = {
    'startTime':'2019-11-25 10:59:00',
    'endTime':'2019-11-25 13:59:00',
    'durationInSeconds':60000 # seconds
    }
```
