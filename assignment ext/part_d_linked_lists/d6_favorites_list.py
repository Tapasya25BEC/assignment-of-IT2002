# D6: Favorites List ADT

class FavoritesList:
    class _Item:
        def __init__(self, value):
            self.value = value
            self.count = 0

    def __init__(self):
        self._items = []

    def _find(self, e):
        for i, item in enumerate(self._items):
            if item.value == e:
                return i
        return -1

    def access(self, e):
        i = self._find(e)
        if i == -1:
            self._items.append(self._Item(e))
            i = len(self._items) - 1
        self._items[i].count += 1
        while i > 0 and self._items[i].count > self._items[i - 1].count:
            self._items[i], self._items[i - 1] = self._items[i - 1], self._items[i]
            i -= 1

    def remove(self, e):
        i = self._find(e)
        if i == -1:
            raise KeyError("Item not found")
        self._items.pop(i)

    def top(self, k):
        if not 1 <= k <= len(self._items):
            raise ValueError("Illegal value for k")
        return [self._items[i].value for i in range(k)]

f = FavoritesList()
for site in ["google", "yt", "google", "gmail", "yt", "google"]:
    f.access(site)
print(f.top(2))
f.remove("yt")
print(f.top(2))
try:
    f.top(5)
except ValueError as e:
    print("Error:", e)
try:
    f.remove("zzz")
except KeyError as e:
    print("Error:", e)
