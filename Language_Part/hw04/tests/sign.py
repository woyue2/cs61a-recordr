test = {
  'name': 'sign',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cond ((= 1 1) 42))
          d783e51be48e22a4d1a25fbac9b656ce
          # locked
          scm> (cond ((= 1 1) 42) ((= 1 1) 24))
          d783e51be48e22a4d1a25fbac9b656ce
          # locked
          scm> (cond ((= 1 0) 42) ((= 0 1) 24) (else 999))
          eefd6bb671ba4bf6e6185ba2b8467816
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign -42)
          005e4250e9a3626d40d5e668df8f1c54
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 0)
          3b1537721b810d0d039c57193559b3d5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (sign 42)
          068e9264c743d8d37a776642cc095e2b
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
