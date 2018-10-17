from mongoengine import *


class BoothModel(Document):
    """
    동아리에 관한 정보가 담겨있는 Collection
    """
    meta = {
        "collection": "booth"
    }

    boothName = StringField(
        primary_key=True,
        required=True
    )

    ownTeam = ReferenceField(
        document_type='TeamModel',
        required=True
    )