test = {
  'name': 'make-adder',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add-two 2)
          f2991d685f624ad59b79213e20800653
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-two 3)
          b93035e430af620ab1eedc5adaea0a82
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-three 3)
          5c5050141c04dffb4cedd647366d0e59
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add-three 9)
          016ab17b3b3dfaabdbd1e107dc0508d1
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab07)
      scm> (load 'lab07_extra)
      scm> (define add-two (make-adder 2))
      scm> (define add-three (make-adder 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
