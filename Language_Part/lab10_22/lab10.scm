;if和cond的两种写法 Start
;Way1 Start
(define (over-or-under num1 num2) 
    (if (< num1 num2) -1 
        (if (= num1 num2) 0 1 )))
;Way1 End
;Way2 Start
(define (over-or-under num1 num2) 
    (cond ((< num1 num2) -1)
          ((= num1 num2) 0)
           (else 1)))
;Way2 End
;if和cond的两种写法 End


;higher-orderFunc Start
;Way1 Start
(define (make-adder num) 
    (lambda (inc) (+ inc num))
)
;Way1 End
;Way2 Start
(define (make-adder num) 
    (define (new inc) (+ inc num))
    new
    ; 这里要加上调用的内函数，少了这一行不行
)
;Way2 End
;higher-orderFunc End

;CompoundFunc Start CallFunSyntax:(func <para>)
(define (composed f g) 
    (lambda (x) (f (g x)))
)
;CompoundFunc End

;Logrithemiatic Way To Decrease the time complexity Start
;helper Start
(define (square n) (* n n))
;helper End
;My code Start
(define (pow base exp) 
    (cond 
          ((= exp 0) 1)
          ((even? exp) (pow (square base) (/ exp 2)));even
          (else (* base (pow base (- exp 1))));odd除了1所以用else
    )
    )
;My code end
;Logrithemiatic Way To Decrease the time complexity End