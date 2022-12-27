from figures.figure import Figure


class Knight(Figure):

    def _check_pawn_moves(self, x, y):
        if y - self.y in range(1) and x == self.x in range(1):
            return True
        return False

    def _check(self, x, y):
        if self._check_borders(x, y) and self._check_other_figures(x, y, None) and self._check_pawn_moves(x, y):
            return True
        return False

    def move(self, x, y):

        if self._check(x, y):
            self.x = x
            self.y = y
        else:
            print("move is invalid")

