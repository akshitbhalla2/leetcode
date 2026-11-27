# Last updated: 11/23/2026, 1:19:05 AM
class ListNode:
    def __init__(self, val, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(val=homepage, prv=None, nxt=None)

    def visit(self, url: str) -> None:
        node = ListNode(val=url, prv=self.cur, nxt=None)
        self.cur.nxt = node
        self.cur = node

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.prv:
                self.cur = self.cur.prv
            else:
                break

        return self.cur.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.nxt:
                self.cur = self.cur.nxt
            else:
                break

        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
