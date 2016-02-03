;; this is how to load external modules in scheme
(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_dailies/d1/paradigms_d1.scm")
(use-modules (ice-9 paradigms_d1))

;; Ashley Towne

;; the list q
;; notice it has a ' in front of the list; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define q '(turkey (gravy) (stuffing potatoes ham) peas))

;; question 1
(display "question 1: ")
(display (atom? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; (copy the output you saw here)
;; question 1: #f
;; with guile: question 1: guile> #fguile> (this output is how all the
;; questions appeared)
;; 
;; explanation:
;; "question 1: " is printed. Then q is cdr'd twice then car'd, which is not an
;; atom. q = (turkey (gravy) (stuffing potatoes ham) peas) -> ((gravy)
;; (stuffing potatoes ham) peas) -> ((stuffing potatoes ham) peas) -> (stuffing
;; potatoes ham) != atom
;; After that, a newline was printed so that the guile prompt would show up on
;; the next line.


;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; question 2: #t
;;
;; explanation:
;; The printing explanation is the same as in #1 (assumed for all questions of
;; the same format). q was cdr'd twice, leaving only the 3rd and later
;; elements, as in question 1. True was returned because '(stuffing potatoes
;; ham) is a list of atoms.
;;


;; question 3
(display "question 3: ")
(display (cond 
           ((atom? 
              (car q)) 
            (car q)) 
           (else '())))
(display "\n")
;; output:
;; question 3: turkey
;;
;; explanation:
;; This mess of parentheses evaluates (car q) (take the first item) and evaluate
;; if it's an atom. Turkey is an atom, so this conidtional evaluates to true
;; and executes (car q) (and obviously prints it). The else is never evaluated,
;; but it would create an empty list if it were.
;;

