from flask import jsonify, Response, abort

from model import BoothModel
from view import BaseResource


class MapView(BaseResource):

    @staticmethod
    def get_team_name() -> str:
        user = MapView.get_current_user()
        if not user.team:
            abort(403)
        return user.team.team_name

    def get(self) -> Response:
        team_name = self.get_team_name()
        self.check_time()

        map_ = {
            'map': [],
            'myTeam': team_name,
            'endTimeTimestamp': self.get_end_time_timestamp(),
        }

        booths = BoothModel.get_all_booths()
        for booth in booths:
            map_['map'].append({
                'booth_name': booth.booth_name,
                'own_team': (booth.own_team and booth.own_team.team_name) or '',
                'location': booth.location,
                'x': booth.x,
                'y': booth.y,
            })

        return jsonify(map_)


class WebMapView(BaseResource):

    def get(self) -> Response:
        self.check_time()

        map_ = {
            'map': [],
            'endTimeTimestamp': self.get_end_time_timestamp(),
        }

        booths = BoothModel.get_all_booths()
        for booth in booths:
            map_['map'].append({
                'booth_name': booth.booth_name,
                'own_team': (booth.own_team and booth.own_team.team_name) or '',
                'x': booth.x,
                'y': booth.y,
            })

        return jsonify(map_)
