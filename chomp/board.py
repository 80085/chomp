class Board:

    def __init__(self, rows=0, columns=0):
        self._grid = [columns] * rows

    def pick(self, cord: tuple):
        row, col = cord
        if row >= len(self._grid) or col >= self._grid[row]:
            raise ValueError(f'Invalid action: {cord}')
        if col == 0:
            self._grid = self._grid[:row]
        else:
            for r in range(row, len(self._grid)):
                self._grid[r] = min(self._grid[r], col)

    def available_actions(self):
        return [(row, col) for row, cols in enumerate(self._grid) for col in range(cols)]

    @property
    def ended(self):
        return len(self._grid) == 0

    @property
    def hash(self):
        return str(self._grid)

    def copy(self):
        copy = Board()
        copy._grid = self._grid.copy()
        return copy

    def pretty(self):
        return '\n'.join(' '.join(str(1) for _ in range(row)) for row in self._grid)

    def __repr__(self):
        return str(self._grid)
