test = {
  'name': 'intersect',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (intersect odds (list 2 3 4 5))  ; Empty list is ()
          621aa58ed68375dc68499f8192673626
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds (list 2 4 6 8))  ; Empty list is ()
          b68398015cdf9adcce1748fdfc6b333b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (intersect odds eight)           ; Empty list is ()
          cf09180409a51c3769f448a0253039ba
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
