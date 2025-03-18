---
title: Sorted list of items with Python
date: February 4, 2023
---

A list of dictionaries can be sorted using the keys in the dictionaries, while a list of tuples can be sorted using the tuple's index.

## Sorted list of dictionaries

This example sorts a list of dictionaries using the `section` and `title` keys.

```python
# List of dictionaries
items = [
    {'section': 'cars', 'link': '/cars/tesla.html', 'title': 'Tesla charging'},
    {'section': 'cars', 'link': '/cars/mustang-races.html', 'title': 'Mustang races'},
    {'section': 'cars', 'link': '/cars/delorean.html', 'title': 'Delorean company'},
    {'section': 'vans', 'link': '/vans/astro.html', 'title': 'Astro van styles'},
    {'section': 'trucks', 'link': '/trucks/toyota.html', 'title': 'Toyota maintenance'},
    {'section': 'trucks', 'link': '/trucks/appliances.html', 'title': 'Appliances to get'}
]

print('\nDictionaries')
for item in items:
    print(f'{item["section"]:10} {item["link"]:26} {item["title"]}')

# Sort the list of dictionaries using keys
newitems = sorted(items, key=itemgetter('section', 'title'))

print('\nSorted dictionaries')
for item in newitems:
    print(f'{item["section"]:10} {item["link"]:26} {item["title"]}')
```

The output from the above example is shown here. Notice the dictionaries are sorted alphabetically from cars to vans and the titles within each group are sorted too.

```
Dictionaries
cars       /cars/tesla.html           Tesla charging
cars       /cars/mustang-races.html   Mustang races
cars       /cars/delorean.html        Delorean company
vans       /vans/astro.html           Astro van styles
trucks     /trucks/toyota.html        Toyota maintenance
trucks     /trucks/appliances.html    Appliances to get

Sorted dictionaries
cars       /cars/delorean.html        Delorean company
cars       /cars/mustang-races.html   Mustang races
cars       /cars/tesla.html           Tesla charging
trucks     /trucks/appliances.html    Appliances to get
trucks     /trucks/toyota.html        Toyota maintenance
vans       /vans/astro.html           Astro van styles
```

## Sorted list of tuples

In this example, a list of tuples are sorted using the first and third indices.

```python
items = [
    ('cars', '/cars/tesla.html', 'Tesla charging'),
    ('cars', '/cars/mustang-races.html', 'Mustang races'),
    ('cars', '/cars/delorean.html', 'Delorean company'),
    ('vans', '/vans/astro.html', 'Astro van styles'),
    ('trucks', '/trucks/toyota.html', 'Toyota maintenance'),
    ('trucks', '/trucks/appliances.html', 'Appliances to get')
]

print('\nTuples')
for item in items:
    print(f'{item[0]:10} {item[1]:26} {item[2]}')

# Sort the list of tuples using index
newitems = sorted(items, key=itemgetter(0, 2))

print('\nSorted tuples')
for item in newitems:
    print(f'{item[0]:10} {item[1]:26} {item[2]}')
```

The output from this example is shown below. Notice the tuples are sorted alphabetically from cars to vans and the last items within each group are sorted too.

```
Tuples
cars       /cars/tesla.html           Tesla charging
cars       /cars/mustang-races.html   Mustang races
cars       /cars/delorean.html        Delorean company
vans       /vans/astro.html           Astro van styles
trucks     /trucks/toyota.html        Toyota maintenance
trucks     /trucks/appliances.html    Appliances to get

Sorted tuples
cars       /cars/delorean.html        Delorean company
cars       /cars/mustang-races.html   Mustang races
cars       /cars/tesla.html           Tesla charging
trucks     /trucks/appliances.html    Appliances to get
trucks     /trucks/toyota.html        Toyota maintenance
vans       /vans/astro.html           Astro van styles
```

This example sorts a list of tuples by date. The date is the last item in the tuple.

```python
items = [
    ('cars', '/cars/tesla.html', 'Tesla charging', 'November 21, 2020'),
    ('cars', '/cars/mustang-races.html', 'Mustang races', 'June 3, 2019'),
    ('cars', '/cars/delorean.html', 'Delorean company', 'August 19, 2020'),
    ('vans', '/vans/astro.html', 'Astro van styles', 'October 5, 2022'),
    ('trucks', '/trucks/toyota.html', 'Toyota maintenance', 'January 3, 2023'),
    ('trucks', '/trucks/appliances.html', 'Appliances to get', 'January 10, 2023')
]

print('\nTuples')
for item in items:
    print(f'{item[0]:10} {item[1]:26} {item[2]:20} {item[3]}')

# Sort the list of tuples using index
newitems = sorted(items, key=lambda x: datetime.strptime(x[3], '%B %d, %Y'))

print('\nSorted tuples')
for item in newitems:
    print(f'{item[0]:10} {item[1]:26} {item[2]:20} {item[3]}')
```

The output is shown below. Notice the tuples are sorted by date from oldest to newest.

```
Tuples
cars       /cars/tesla.html           Tesla charging       November 21, 2020
cars       /cars/mustang-races.html   Mustang races        June 3, 2019
cars       /cars/delorean.html        Delorean company     August 19, 2020
vans       /vans/astro.html           Astro van styles     October 5, 2022
trucks     /trucks/toyota.html        Toyota maintenance   January 3, 2023
trucks     /trucks/appliances.html    Appliances to get    January 10, 2023

Sorted tuples
cars       /cars/mustang-races.html   Mustang races        June 3, 2019
cars       /cars/delorean.html        Delorean company     August 19, 2020
cars       /cars/tesla.html           Tesla charging       November 21, 2020
vans       /vans/astro.html           Astro van styles     October 5, 2022
trucks     /trucks/toyota.html        Toyota maintenance   January 3, 2023
trucks     /trucks/appliances.html    Appliances to get    January 10, 2023
```
