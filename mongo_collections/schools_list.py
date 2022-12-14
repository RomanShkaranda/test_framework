from utilities.mongo.baseMongo import BaseMongo


class SchoolsCollection(BaseMongo):
    def __init__(self):
        super().__init__()
        self.mycol = self.mydb["schools_list"]

