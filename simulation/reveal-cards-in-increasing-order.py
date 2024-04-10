class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck) == 1:
            return deck
        deck.sort()
        reverse_engineered_list = deque(deck[-2:])
        for x in range(len(deck) - 3, -1, -1):
            reverse_engineered_list.appendleft(reverse_engineered_list.pop())
            reverse_engineered_list.appendleft(deck[x])
        return reverse_engineered_list
        