from utilities.mongo.baseMongo import BaseMongo


class SchoolsCollection(BaseMongo):
    def __init__(self):
        super().__init__()
        self.mycol = self.mydb["schools_list"]

    def insert_one_school_item(self, number: int, capacity: int, principle: str):
        self.mycol.insert_one({'number': number, 'capacity': capacity, 'principle': f'{principle}'})
        return print(f"created number {number}, capacity {capacity}, principle {principle}")

    def delete_by_number(self, number: int):
        self.mycol.delete_one({'number': number})

    def find_one_by_number(self, number: int):
        return print(self.mycol.find_one({'number': number}))

