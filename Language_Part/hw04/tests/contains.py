test = {
  'name': 'contains?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (contains? odds 3)
          b6fb60cb671b6e7adfc3c9cad6a26635
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 9)
          b6fb60cb671b6e7adfc3c9cad6a26635
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (contains? odds 6)
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
      scm> (define odds (list 3 5 7 9))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
