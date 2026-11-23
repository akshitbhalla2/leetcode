# Last updated: 11/23/2026, 1:19:05 AM
1class ListNode:
2    def __init__(self, val, prv=None, nxt=None):
3        self.val = val
4        self.prv = prv
5        self.nxt = nxt
6
7class BrowserHistory:
8
9    def __init__(self, homepage: str):
10        self.cur = ListNode(val=homepage, prv=None, nxt=None)
11
12    def visit(self, url: str) -> None:
13        node = ListNode(val=url, prv=self.cur, nxt=None)
14        self.cur.nxt = node
15        self.cur = node
16
17    def back(self, steps: int) -> str:
18        for _ in range(steps):
19            if self.cur.prv:            
20                self.cur = self.cur.prv
21            else:
22                break
23        
24        return self.cur.val
25
26    def forward(self, steps: int) -> str:
27        for _ in range(steps):
28            if self.cur.nxt:
29                self.cur = self.cur.nxt
30            else:
31                break
32
33        return self.cur.val
34
35
36# Your BrowserHistory object will be instantiated and called as such:
37# obj = BrowserHistory(homepage)
38# obj.visit(url)
39# param_2 = obj.back(steps)
40# param_3 = obj.forward(steps)