test = {
  'name': 'add',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (add odds 2)
          8b8691922ac4a62c745d5801281d7c29
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 5)
          8cb0893f43212b39af2eafedd2b30d87
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 6)
          e0920825b2888315239fd065e48bab17
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (add odds 10)
          8a8151357a17642704c4b7f0cf51a57f
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw04)
      scm> (define odds (list 3 5 7 9))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
