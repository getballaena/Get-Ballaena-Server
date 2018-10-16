from flasgger import swag_from
from flask import Response, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from random import choice

from view.base_resource import BaseResource
from docs.solve import SOLVE_GET, SOLVE_POST
from model.UserInfo import UserInfo
from model.Problem import ProblemBase
from model.Club import Club


class Solve(BaseResource):

    @swag_from(SOLVE_GET)
    @jwt_required
    def get(self, clubId: str):
        user = UserInfo.objects(userId=get_jwt_identity())
        if not user:
            return abort(403), 200

        problem = choice(ProblemBase.objects())
        response = {key: problem['key'] for key in problem}
        response['clubId'] = clubId

        return jsonify(response)

    @swag_from(SOLVE_POST)
    @jwt_required
    def post(self, clubId: str):
        user: UserInfo = UserInfo.objects(userId=get_jwt_identity()).first()
        if not user:
            return abort(403)
        payload: dict = request.json

        problem: ProblemBase = ProblemBase.objects(problemId=payload['problemId']).first()
        club: Club = Club.objects(clubId=clubId).first()
        if not all(problem, club):
            return Response('', 204)

        if payload['answer'] != problem.answer:
            return Response('', 205)

        club.ownTeam = user.team
        club.save()

        return Response('', 201)
