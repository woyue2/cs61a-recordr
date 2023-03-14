test = {
  'name': 'make-fib',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define fib (make-fib))
          967ec852b56072de79fcad084a3ae169
          # locked
          scm> (fib)
          c710ce1013f52240259ea23a1deec786
          # locked
          scm> (fib)
          c4b729b50e733e03cc8b3108424860bc
          # locked
          scm> (fib)
          c4b729b50e733e03cc8b3108424860bc
          # locked
          scm> (fib)
          08f487e203b345ff9ef0b79cf2145c45
          # locked
          scm> (fib)
          5bdc1a36916860da425c57de281c2173
          # locked
          scm> (fib)
          8b5c3c1c6a4eaf75cbe5dec8ce3970a7
          # locked
          scm> (fib)
          ba5153e04a98fc31021e0b75d76b0676
          # locked
          scm> (fib)
          4c7d469befb0bece66867ef1104811f8
          # locked
          scm> (define fib2 (make-fib))
          ac1b3f8235b48071cb8a847acbe5fd99
          # locked
          scm> (fib2)
          c710ce1013f52240259ea23a1deec786
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw05)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
