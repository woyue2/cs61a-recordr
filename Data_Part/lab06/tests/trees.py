test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab06 import *
          >>> t = tree(1, tree(2))
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> t = tree(1, [tree(2)])
          75e7eb45dffa5d30654f02570401dfe8
          # locked
          >>> label(t)
          c659f52f950a31de33b0888e439f05a7
          # locked
          >>> label(branches(t)[0])
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> x = branches(t)
          >>> len(x)
          c659f52f950a31de33b0888e439f05a7
          # locked
          >>> is_leaf(x[0])
          ede6df328b7c3fa6304f7eb1608d9dc4
          # locked
          >>> branch = x[0]
          >>> label(t) + label(branch)
          214f1f0cf62380259278c29f0dd9185d
          # locked
          >>> len(branches(branch))
          5b62c9d6f358ce77683fee7b403e4cee
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from lab06 import *
          >>> b1 = tree(5, [tree(6), tree(7)])
          >>> b2 = tree(8, [tree(9, [tree(10)])])
          >>> t = tree(11, [b1, b2])
          >>> for b in branches(t):
          ...     print(label(b))
          73dc0de5202f020182ea500448cc846a
          64414da02f6d0be34bb8a70a1b0d595e
          # locked
          >>> for b in branches(t):
          ...     print(is_leaf(branches(b)[0]))
          ede6df328b7c3fa6304f7eb1608d9dc4
          a559f517e8f86de30b928d7e29ec2331
          # locked
          >>> [label(b) + 100 for b in branches(t)]
          8f041e2c1a87f6dc8b08bb4efb6963f1
          # locked
          >>> [label(b) * label(branches(b)[0]) for b in branches(t)]
          a4967e709f3194a2bbf1c32e10415f57
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
