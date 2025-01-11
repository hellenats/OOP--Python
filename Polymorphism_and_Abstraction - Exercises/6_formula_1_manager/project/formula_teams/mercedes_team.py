from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam (FormulaTeam):

    def team_data(self):
        sponsors = {'Petronas': {1: 1_000_000, 3: 500_000}, 'TeamViewer': {5: 100_000, 7: 50_000}}
        expense = 200_000

        return sponsors, expense