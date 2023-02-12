test = {
  'name': 'pow',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (pow 2 5)
          6f066a5ea36822ee02b13277317ad7a8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 10 3)
          6c3e2b869b5d3b4719b4c97396caa474
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (pow 3 3)
          b5547241e8be8001f620abf9f066b80c
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
