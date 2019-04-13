from typing import List
from datetime import datetime

from mongoengine import *


class TeamModel(Document):

    meta = {
        'collection': 'team'
    }

    team_name: str = StringField(
        primary_key=True
    )


class BoothModel(Document):

    meta = {
        "collection": "booth"
    }

    booth_name: str = StringField(
        primary_key=True,
        required=True
    )

    own_team: TeamModel = ReferenceField(
        document_type=TeamModel
    )

    next_capture_time: datetime = DateTimeField(
        default=datetime(2001, 4, 20)
    )

    latitude: float = FloatField()

    longitude: float = FloatField()


class AlwaysBoothModel(Document):

    meta = {
        "collection": "always_booth"
    }

    booth_name: str = StringField(
        primary_key=True,
        required=True
    )

    latitude: float = FloatField()

    longitude: float = FloatField()


class AdQRModel(Document):

    meta = {
        "collection": "ad_qr"
    }

    ad: str = StringField(
        primary_key=True,
        required=True
    )


class ProblemModel(Document):

    meta = {
        'collection': 'problem'
    }

    content: str = StringField(
        required=True
    )

    answer: str = StringField(
        required=True
    )

    choices: List[str] = ListField(
        StringField(
            required=True
        )
    )


class UserModel(Document):

    meta = {
        'collection': 'user'
    }

    name: str = StringField(
        required=True
    )

    device_uuid: str = StringField(
        required=True
    )

    team: TeamModel = ReferenceField(
        document_type=TeamModel
    )

    always_capture: List[AlwaysBoothModel] = ListField(
        ReferenceField(
            document_type=AlwaysBoothModel,
            reverse_delete_rule=CASCADE,
        ),
        default=[],
    )

    ad_capture: List[AdQRModel] = ListField(
        ReferenceField(
            document_type=AdQRModel,
            reverse_delete_rule=CASCADE,
        ),
        default=[],
    )


class CouponModel(Document):

    meta = {
        'collection': 'coupon'
    }

    coupon_name: str = StringField(
        required=True
    )
    user: UserModel = ReferenceField(
        document_type=UserModel,
        reverse_delete_rule=CASCADE,
    )