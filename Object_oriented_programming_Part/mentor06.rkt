;check list or pair Start
(define (well-formed lst)
  (cond
    ((eqv? lst '())
      #t   
    )
    ((number? lst) ;ps: pair(1.2) cdr 之后 = 2 而list(1 2) cdr之后为(2)
     #f
    )
    (else
     (well-formed (cdr lst))
     )
  )
)
;check list or pair End
;在这里写，在DrRacket里debug
;Q3 Define is-prefix Start
;MyStupidCode Start
(define (is-prefix p lst)
    (cond
        ((null? lst)
            #t
        )
        ((null? lst)
            #f
        )
        ((eqv? (car p)(car lst))
            (is-prefix (cdr p)(cdr lst))
        )
        (else
            (is-prefix p (cdr lst))
        )
    )
)
;MyStupidCode End
;ReferenceAnswerStart
(define (is-prefix p lst)
    (cond
        ((null? lst)
            #t
        )
        ((null? lst)
            #f
        )
        (else
            (and;用and直接来递归，这tm太聪明
                (= (car p)(car lst))
                (is-prefix(cdr p )(cdr lst))
            )
        )
    )
)
;ReferenceAnswerEnd
;Q3 Define is-prefix End
;Q4 Define waldo which takes in a list. Start
;MyStupidCode Start
(define (waldo lst)
    (define (helper lst counter)
        (if (eqv? lst '())
            #f
            (if (= (car lst) 'waldo)
            (if (= counter 0)
                #f
                counter
            )
            (helper (cdr lst)(counter +1);这里运算符错了傻鸟就
            )
        )
        )
    )
    (helper lst 0)
)
;MyStupidCode End 大致思路对了，但是字符串……为什么报错啊我用'waldo也不对
;Reference Start
(define (waldo lst)
    (define (helper lst counter)
        (cond
            ((null? lst) 
                #f
            )
            ((eq? (car lst) 'walao)
                counter
            )
            (helper (cdr lst)(+ counter 1)
            )
        )
    )
)
;Reference End
;Q4 Define waldo which takes in a list. End
;Q5 第2位变成第1位的内容，第4位变成第3位的内容 list以此类推 Start
(define (double-link lst)
    (if (or (null? lst) (null? (cdr lst)))
        lst
        (begin
            (set-car! (cdr lst)(car lst))
            (double-link (cdr(cdr lst)));连用两个cdr来达到双数的目的
            lst;返回这个
        )
    )
)
;Q5 End 抄的