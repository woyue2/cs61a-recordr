test = {
  'name': 'ordered?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ordered? '(1 2 3 4 5))
          b6fb60cb671b6e7adfc3c9cad6a26635
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 5 2 4 3))
          e29066a226f93a491e36553d9813be5d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(2 2))
          b6fb60cb671b6e7adfc3c9cad6a26635
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (ordered? '(1 2 2 4 3))
          e29066a226f93a491e36553d9813be5d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw04)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
