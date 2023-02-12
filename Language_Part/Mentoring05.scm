;从seed开始走n步，按照hailstone的规律，输出结果 Start
(define (hailstone seed n)
    if (= n 0)
        seed
        (if (= 0 (remainder seed 2))
            (hailstone
            (quotient seed 2)
            (- n 1))
          (hailstone
          (+ 1 (* seed 3))
          (- n 1))
        )
)
;从seed开始走n步，按照hailstone的规律，输出结果 End
;Copy Code End这样可读性确实是强一点啊（if的部分分了3行)，我的code混用了cond 和if不行