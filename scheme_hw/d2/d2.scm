;; scheme daily homework 2
;; name: Ashley Towne
;; date: 1/25/2016

;; the test lists
;; notice they have a ' in front of the lists; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define testlist1 '(turkey gravy stuffing potatoes ham peas))
(define testlist2 '(bacon turkey beef turkey))
(define testlist3 '(bacon turkey beef))

;; replacefirst
(define replacefirst
  (lambda (a b lat)
    (cond
      ((eq? lat '()) '()) ; check if lat is an empty list
      ((eq? (car lat) a) (cons b (cdr lat))) ; given a match, replace the first element in lat with b
      (else ; no match
        (cond
          ((eq? (cdr lat) '()) lat ) ; check if (cdr lat) is null - is this the last item in the list?
          (else
            (cons (car lat) (replacefirst a b (cdr lat)))))))))
; append the searched end of list to the first element of lat
    ;; right now replacefirst always returns an empty list
    ;; make it return a lat with the first instance of a replaced with b
    ;; see the tests and example output below...

;; tests!
(display (replacefirst 'turkey 'cheese testlist1))
(display "\n")

(display (replacefirst 'turkey 'bacon testlist2))
(display "\n")

(display (replacefirst 'sauce 'apple testlist3))
(display "\n")

;; notice that this is equivalent to using testlist3
(display (replacefirst 'beef 'carrots (list 'bacon 'turkey 'beef)))
(display "\n")

;; correct output:
;;   $ guile d2.scm
;;   (cheese gravy stuffing potatoes ham peas)
;;   (bacon bacon beef turkey)
;;   (bacon turkey beef)
;;   (bacon turkey carrots)

