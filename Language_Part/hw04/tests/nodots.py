test = {
  'name': 'nodots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          51b8ab6e4578438ddc316347c73522db
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 2 . 3))
          ddbf926e687bfb00fe3a00a7dffd664e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '((1 . 2) 3))
          17870be2786fe8ba41c5113ecc08eebb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 (2 3 . 4) . 3))
          bfc44f181f1c905ed806ad13bc0b4539
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          bfc44f181f1c905ed806ad13bc0b4539
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
