test = {
  'name': 'cadr-caddr',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cddr '(1 2 3 4))
          759e717ee14137fecfdc2c24284ecb58
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (cadr '(1 2 3 4))
          9996cdd6ea6156c9c9c8347e762d0ec8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (caddr '(1 2 3 4))
          f2f40b96ab6493fb082aedde3c0ace60
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
