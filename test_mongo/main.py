from pprint import pprint

from mongo_collections.schools_list import SchoolsCollection

ins_list = [
    {'number': 44, 'capacity': 1000, 'principle': 'Robert P'},
    {'number': 35, 'capacity': 900, 'principle': 'Jane Y'},
    {'number': 17, 'capacity': 100, 'principle': 'Arron P'}
]

SchoolsCollection().insert_one({'number': 1, 'capacity': 240, 'principle': 'Roman S'})
SchoolsCollection().insert_many(ins_list)
SchoolsCollection().delete_by_number(35)
SchoolsCollection().find_one_by_number(44)
SchoolsCollection().delete_all()
SchoolsCollection().insert_one({'name': 'Smith'})
SchoolsCollection().insert_one_school_item(1, 200, 'Jose L')
pprint(SchoolsCollection().find_all())


