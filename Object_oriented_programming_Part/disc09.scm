(define (stepper num)
    (define (step)(set! num (+ num 1))
    num
    )
step
)
"""piggy_bank"""
;抄的,基本忘了，看了一下又想起来了
(define (make-piggy-bank)
    (define total 0);total = 0
    (lambda (amount);没有明说要给予变量，却用了，说明是匿名的用lambda
        (if (> amount 0);if
            (set! total (+ total amount));then
            (begin 
                (define old-total total);else先 old-total = total 再total = 0
                (set! total 0)
                old-total;return old-total
            )
        )
    )
)