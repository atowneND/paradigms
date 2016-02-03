(define-module (ice-9 paradigms_d1))

(define-public (atom? x)
  (and (not (null? x))
       (not (pair? x))))

(define-public lat?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((atom? (car l)) (lat? (cdr l)))
      (else #f))))

