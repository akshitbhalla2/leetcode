# Last updated: 4/19/2026, 11:22:20 PM
class ListNode:
    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(homepage, None, None)
        self.cur = node

    def visit(self, url: str) -> None:
        node = ListNode(url, self.cur, None)
        self.cur.next = node
        self.cur = node

    def back(self, steps: int) -> str:

        for _ in range(steps):
            prev = self.cur.prev
            if not prev:
                break
            self.cur = prev
        
        return self.cur.url

    def forward(self, steps: int) -> str:

        for _ in range(steps):
            next = self.cur.next
            if not next:
                break
            self.cur = next

        return self.cur.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)