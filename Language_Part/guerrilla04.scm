;Question 4: Reverse, HOF Scheme Start
(define (reverse l)
    (if (null? l)
        l
        (append (reverse (cdr l))(list (car l)));append的用法我不会    
    )
)
;Question 4: Reverse, HOF Scheme End
;Q4 b return square of list Start
;My Code Start
(define (square lst)
    (if (null? l)
        l
        ;(append (* (car lst)(car lst))(square (cdr lst))) 没改之前是错的
        (append (list(* (car lst)(car lst))) (square (cdr lst)));这样才对，append是实现list + list的
    )
)
;My Code End 我们代码就唯一不同在append和cons，懂了是我错了，
;Copid Code Start
(define (list-of-squares lst)
    (define (squarer lst)
        (if (null? lst)
            (quote ());这时候的list本来就是'()
            (cons (* (car lst) (car lst))(squarer (cdr lst)))
        )
    )
    (squarer lst)
)
;Copied Code End 嵌套来干嘛呢？？？你就一个if判断你他妈是智障把@！
;Q4 b return square of list End

;Question 5: Add To All Start
;> (add-to-all 1 '())
;()
;> (add-to-all 'foo '((1 2) (3 4) (5 6)))
;((foo 1 2) (foo 3 4) (foo 5 6))
(define (add-to-all item lst)
    (if (null? lst)
        lst
        (cons (append(list item)(car lst)) 
        ;(cons (cons item (car lst)) 也可以用cons是一样的这个效果
              (add-to-all item (cdr lst)))
    )
)
;Question 5: Add To All End

;Question 6: Sublists Start 列出所有组合的可能，ps空集也是一个，所有子集
(define (sublists lst)
    (if 
        (null? lst) '(());判定条件
        ;True 时候执行 Start
        (let
            ;局部变量 Start 
            (
             (recur ;recur是一个变量，而不是一个 built-in func
                (sublists (cdr lst))
             )
            );局部变量 End
            ;body Start
            (append 
                recur 
                (add-to-all (car lst) recur);add-to-all item lst
            );body End
        )
        ;True 时候执行 End False是[]所以omit了
    )
)
;Question 6: Sublists ENd 我是抄的额，我不会啊

;Q7 Start
;Return the number of times that 1 follows 6 in the list.
;scm> (sixty-ones '(4 6 1 6 0 1))
;1
;scm> (sixty-ones '(1 6 1 4 6 1 6 0 1))
;2
;scm> (sixty-ones '(6 1 6 1 4 6 1 6 0 1))
;3
;MyStupidCode Start
(define (sixty-ones list)
  (define (helper list counter)
    (
       if (eqv? (cdr list) '());简化成(null? list)
          (print counter)
          (if (= (car list) 6)
              (
                if (= (car(cdr list)) 1)
                   (helper (cdr list) (+ counter 1))
              )
              (helper (cdr list) counter)
          )
    )
  )
  (helper list 0)
)
;MyStupidCode End
;reference Answer Start
(define (sixty-ones lst)
    (cond 
        ((or (null? lst) (null? (cdr lst))) 
            0
        )
        ((and (= 6 (car lst)) (= 1 (cadr lst)))
            (+ 1 (sixty-ones (cddr lst)))
        )
        (else 
            (sixty-ones (cdr lst))
        )
    )
)
;reference Answer End
;Q7 End

;Question 8: Replace X Start
;初级版 Start
(define (replace-x lst x y)
    (cond
        ((eqv? lst '())
            '()
        )
        ((eqv? (car lst) x) 
            (cons y (replace-x (cdr lst) x y))
        )
        (else
            (cons (car lst) (replace-x (cdr lst) x y))
        )
    )
)
;初级版 finish
;不创建新list版，mutate original list Start
;MyShitCode Start
(define (replace-x lst x y)
    (cond
        ((eqv? lst '())
            '()
        )
        ((eqv? (car lst) x) 
            (set-car x y)
        )
        (else
            ((replace-x (cdr lst) x y))
        )
    )
)
;MyShitCode End
;Reference Answer Start
 (define (replace-x lst x y)
    (cond 
        ((null? lst) 
            lst
        )
        ((eq? (car lst) x) 
            (begin 
                (set-car! 
                    lst 
                    y
                ) 
                (set-cdr! 
                    lst 
                    (replace-x (cdr lst) x y)
                ) 
                lst
            )
        )
        (else 
            (begin 
                (set-cdr! 
                    lst 
                    (replace-x (cdr lst) x y)
                ) 
                lst
            )
        )
    )
)
;Reference Answer End
;不创建新list版，mutate original list End
;Question 8: Replace X End

;Q9 Question 9: Sequence in List Start
;Require: Be in order, but not necessarily consecutive
;My code Start有点Bug
(define (seq-in-lst lst sub-lst)
    (cond
        ((null? (sub-lst))
            #t
        )
        ((eqv? (car lst)(car sub-lst)) 
            (seq-in-lst (cdr lst) (cdr sub-lst))
        )
        ((eqv? (car lst)(car (cdr sub-lst))) 
            (seq-in-lst (cdr lst) (cdr (cdr sub-lst)))
        )
        ((eqv? (car (cdr lst))(car sub-lst)) 
            (seq-in-lst (cdr (cdr lst)) (cdr sub-lst))
        )
        (else
            #f
        )
    )
);My code End有点Bug
;Reference Anw Start
(define (seq-in-lst lst sub-lst)
    (cond ((null? sub-lst) #t)
            ((null? lst) #f)
            ((eq? (car lst) (car sub-lst)) ;因为是子集，所以一直从lst选，选不到就往后选，对sub-lst就可以了
                (seq-in-lst (cdr lst) (cdr sub-lst))
            )
            (else (seq-in-lst (cdr lst) sub-lst))))
;Reference Anw End
;Q9 Question 9: Sequence in List End/