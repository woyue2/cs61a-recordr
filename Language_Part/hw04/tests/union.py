test = {
  'name': 'union',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (union odds (list 2 3 4 5))
          47889053bc87646b49cd9be9cd908e4b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds (list 2 4 6 8))
          d4fc3e398e1962e4e30dff04f29bf17d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (union odds eight)
          6c1809f473ec8e01fb3944ac52497853
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
      scm> (define eight (list 1 2 3 4 5 6 7 8))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
