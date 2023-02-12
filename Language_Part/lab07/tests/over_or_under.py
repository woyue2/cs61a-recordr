test = {
  'name': 'over-or-under',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (over-or-under 5 5)
          67a37433345d12b97afe4885b1fa6019
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (over-or-under 5 4)
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (over-or-under 3 5)
          eda7995cc4df0b8743b9ae6e97979c69
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
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
