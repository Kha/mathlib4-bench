#!/usr/bin/env python3

import collections
import re
import sys

cats = collections.defaultdict(lambda: 0)
for line in sys.stdin:
    sys.stderr.write(line)
    if m := re.match("(.+?) ([\d.]+)(m?)s$", line):
        cats[m[1].strip()] += float(m[2]) * (1e-3 if m[3] else 1)

for cat in sorted(cats.keys()):
    cat2 = cat
    if len(sys.argv) > 1:
        cat2 = f"{sys.argv[1]} {cat}"
    print(f"{cat2!r}: {cats[cat]:f}")
