'''
811. Subdomain Visit Count
Rating: Easy

A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" implicitly.

Now, call a "count-paired domain" to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".

We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

Notes:
Hash map is definitely the way to go on this one. Runtime and space complexity of O(N)
'''


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        h = {}

        for s in cpdomains:
            split = s.split()
            count = int(split[0])
            dlist = split[1].split('.')

            for i in range(0, len(dlist)):
                sub = '.'.join(dlist[i:])
                if sub in h:
                    h[sub] += count
                else:
                    h[sub] = count

        res = []
        for key in h:
            res.append(str(h[key]) + ' ' + key)
        return res