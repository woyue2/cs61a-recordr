;做过了没必要做Start
; Q1
(define (sign x)
  'YOUR-CODE-HERE
)

; Q2
(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
)
;做过了没必要做End
; Q3
(define (cddr s)
  (cdr (cdr s)));s[1:][1:]

(define (cadr s)
  (car (cdr s));s[1:][0]
)
(define (caddr s)
  (car (cdr (cdr s)));s[1:][1:][0]
)

; Q4 判断s是不是非单调递减的list，就是需要是 左一比左二 增加或相等 Start
(define (ordered? s)
  (cond 
      ((null? s) nil);本来就什么也没有，就是空List()
      ((null? (cdr s)) #t);剩下什么也没有了，排查完了
      ((>= (car (cdr s)) (car s)) (ordered? (cdr s)));xxx?只是一个symbol，?在这里不影响任何事情
      ;👆if  s[1:][0]  >= s[0]     下一个  func(s[1:])
      (else #f) ;有一个递减就是False 
))
;Q4 非单调递减的list End 抄的，没这么容易啊大哥

; Q5
; 将含.的list 去除. eg.(1 2 . 3 )--> (1 2 3)输出 Start
(define (nodots s)
  (if (null? s) ;如果是空集
    uil;输出空集
    (if (integer? s);否则，如果是单一整数num,不是集合
      (cons s nil);输出 [n]
      (if (pair? (car s));否则，如果s[0]是pair ，还有可能就是.
        (cons (nodots (car s)) (nodots (cdr s )));就 递归(nodots s[0])和(nodots s[1:])，并将递归结果组合
        ;这里写成[0]和[1:]有点不对了，Pair是只有(1.(2.3))的 可能就是 (1 2.3)会简写，但是本质上两两之间还是有点.
        (if (integer? (cdr s));如果是整数
          (cons (car s ) (cons (cdr s) nil));如果没为题就拆开来开来 再合起来，把整数变成pair,才能合起来
          (cons (car s) (nodots (cdr s)));最后这一步就是把.给去掉了！！！！
        );还是有点蒙，先放过我把靠        
      )
    )  
  )
)
; 将含.的list 去除End

; Q6 a set s and a value v 不重复 Start
(define (empty? s) (null? s))
;这种语言是从中间看到两边的！！写着写着就悟出来的
(define (add s v);不想让s里面的值和v重复
    (cond
      (empty? s)(list v)
      ((equal? (car s) v) s)
      (( > (car s) v) (cons v s))
      (else (cons (car s)  (add (cdr s) v)))      
    )
)
;End 我还是迷迷糊糊的…… a set s and a value v 不应该有重复的
; Q7
; s 已经被Sets as sorted lists 升序排序  s 包含 v Start 
(define (contains? s v)
    (cond
      ((equal? s nil) #f)
      ((equal? (car s) v) #t)
      (else (contains? (cdr s) v))
    )
  )

; Q8 这个就是递归，我做过有印象很简单
; returns a set containing only values that appear in both sets s and t Start
(define (intersect s t)
  (cond
    (eqv? s nil)(nil)
    (eqv? t nil)(nil)
    (eqv? (car s)(car t))(cons (car s) (intersect (cdr s)(cdr t)))
    (eqv? (cdr (car s))(car t))(cons (cdr (car s) ) (intersect (cdr (car(cdr s)))(cdr t)))
    (eqv? (car s)(cdr (car t)))(cons (cdr (car t) ) (intersect (cdr s)(cdr (car(cdr t)))))
  )
)
; returns a set containing only values that appear in both sets s and t End 这个我感觉我应该是对的，我的答案不过输出不了，然后别人的也不可以……

; returns a set containing all values that appear in either set s or t. Start
(define (union s t)
  (if (eqv? s nil)(t)
    (if (eqv? t nil)(s)
      (if (eqv? (car s)(car t)) (cons (nil) (union (cdr s)(cdr t)))
        (if (eqv? (cdar s)(car t)) (cons (nil) (union (cdadr s)(cdr t)))
           (eqv? (car s)(cdar t)) (cons (nil) (union (cdr s)(cdadr t)))
  ))))
)
; returns a set containing all values that appear in either set s or t. End这个里不等于不会写啊好烦尼玛