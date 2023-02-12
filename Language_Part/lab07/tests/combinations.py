test = {
  'name': 'What Would Scheme Display?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (- 10 4)
          5c5050141c04dffb4cedd647366d0e59
          # locked
          scm> (* 7 6)
          4a4a7dc4bf89623123d51470f06de402
          # locked
          scm> (+ 1 2 3 4)
          700368183fe24919898aaeca9b976fbd
          # locked
          scm> (/ 8 2 2)
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          scm> (quotient 29 5)
          b93035e430af620ab1eedc5adaea0a82
          # locked
          scm> (modulo 29 5)
          f2991d685f624ad59b79213e20800653
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison
          3c6c80f70953f551231b2e51b4d9b1ce
          # locked
          scm> (< 1 3)
          22366cc874047a10e8dc566d9bd86d5f
          # locked
          scm> (or #t #f)                 ; or special form short circuits
          22366cc874047a10e8dc566d9bd86d5f
          # locked
          scm> (and #t #f (/ 1 0))
          3c6c80f70953f551231b2e51b4d9b1ce
          # locked
          scm> (not #t)
          3c6c80f70953f551231b2e51b4d9b1ce
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (define x 3)
          e8bccfd485df815928620ee859d22623
          # locked
          scm> x
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          scm> (define y (+ x 4))
          516263f4e0556448f570fb3883d3465c
          # locked
          scm> y
          54668fb96734d9b52a588e4f9ab6ed24
          # locked
          scm> (define x (lambda (y) (* y 2)))
          e8bccfd485df815928620ee859d22623
          # locked
          scm> (x y)
          d4545de232b765370652baf634b18ad1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (if (print 1) (print 2) (print 3))
          030bca9dd0d55198e3fa5a2ab185b285
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          scm> (* (if (> 3 2) 1 2) (+ 4 5))
          0d66d07b30bc2b1b6722bd627905704c
          # locked
          scm> (define foo (lambda (x y z) (if x y z)))
          99c43267442bce98153fdd7c4e9b32a4
          # locked
          scm> (foo 1 2 (print 'hi))
          8f58112f9b6f3b582df45d024d3a6b11
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          scm> ((lambda (a) (print 'a)) 100)
          56a5849bd28287c17b6a476f0dac1eb7
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
