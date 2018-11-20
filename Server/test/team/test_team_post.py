from test import TCBase, check_status_code
from model.user import UserModel


class TeamPostTest(TCBase):

    def team_post_request(self, team_number=1):
        return self.client.post(
            f'/team?team={team_number}',
            headers={'Authorization': f'Bearer {self._create_access_token()}'}
        )

    def check_user_team(self, user_id='test', team_number=0):
        user = UserModel.objects(userId=user_id).first()
        self.assertEqual(user.team.teamId, team_number)

    @check_status_code(201)
    def test_success_team_post(self):
        rv = self.team_post_request()
        self.check_user_team(team_number=1)
        return rv

    @check_status_code(204)
    def test_already_has_team(self):
        self.team_post_request()
        self.check_user_team(team_number=1)

        rv = self.team_post_request(team_number=2)
        self.check_user_team(team_number=1)
        return rv

    @check_status_code(205)
    def test_wrong_team_number1(self):
        rv = self.team_post_request(team_number=-1)
        self.check_user_team()
        return rv

    @check_status_code(205)
    def test_wrong_team_number2(self):
        rv = self.team_post_request(team_number=5)
        self.check_user_team()
        return rv