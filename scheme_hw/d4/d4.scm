;; scheme daily homework 4
;; name: Ashley Towne
;; date: 1/29/16

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_dailies/d4/paradigms_d4.scm")
(use-modules (ice-9 paradigms_d4))

;; filterN
(define filterN
  (lambda (n m lat)
    (cond
      ((null? lat) '()) ; base case (end of list)
      ((number? (car lat)) ; if it's a number
        (cond 
          ((and (< (sub1 n) (car lat)) (> (add1 m) (car lat))) 
           (cons (car lat) (filterN n m (cdr lat))))
          (else (filterN n m (cdr lat)))
        )
      )
      (else (filterN n m (cdr lat)))
    )
  )
)
    ;; currently this function just returns the lat as it is given
    ;; change the function so that it returns /only/ the numbers
    ;; >= n and <= m
    ;; see below for examples...

;; tests!
(display (filterN 4 6 '(1 turkey 5 9 4 bacon 6 cheese)))
(display "\n")

(display (filterN 4 6 '(4 4 4 1 1 bacon 9 9 9 6 6 6 1 4 5)))
(display "\n")

;; correct output:
;;   $ guile d4.scm
;;   (5 4 6)
;;   (4 4 4 6 6 6 4 5)

