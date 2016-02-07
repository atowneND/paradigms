;; scheme tictactoe homework
;; name: Ashley Towne
;; date: 2/10/16

(load-from-path "/afs/nd.edu/user37/cmc/Public/cse332_sp16/scheme_tictactoe/paradigms_ttt.scm")
(use-modules (ice-9 paradigms_ttt))
(use-modules (ice-9 debugging traps) (ice-9 debugging trace))

;; REPLACE WITH YOUR FUNCTIONS FROM A PREVIOUS HOMEWORK:
;;  greatest
;;  positionof
;;  value

(define greatest
  (lambda (tup)
    (cond
      ((null? (cdr tup)) (car tup))
      ((> (car tup) (greatest (cdr tup))) (car tup))
      (else (greatest (cdr tup))))))

(define positionof
  (lambda (n tup)
    (cond
      ((null? tup) 0)
      ((eq? n (car tup)) 1)
      (else (+ 1 (positionof n (cdr tup)))))))

(define value
  (lambda (p gs)
    (cond
      ((win? p gs) 10)
      ((win? (other p) gs) -10)
      (else 0))))

;; MODIFY your sum* function for this assignment...
(define atom?
  (lambda (x)
    (and (not (null? x)) (not (pair? x)))))

(define sum*-g
  (lambda (ttup f) ;; remember, the parameter f should be a FUNCTION
    (cond
      ((null? ttup) 0)
      ((atom? (car ttup)) (f ttup))
      (not (eq? (positionof 'e ttup) 0) (+ (sum*-g (car ttup) f) (sum*-g (cdr ttup) f)))
      (else (+ (sum*-g (car ttup) f) (sum*-g (cdr ttup) f))))))

;; MODIFY this function so that given the game tree 
;; (where the current situation is at the root),
;; it returns the recommendation for the next move
(define nextmove
  (lambda (p gt)
    (cond
      ((null? gt) '())
      (else (car (pick (positionof (greatest 
                                     (map 
                                       (lambda (tup) (sum*-g tup (lambda (x) (value p x)))) 
                                       (cdr gt)))
                                   (map 
                                     (lambda (tup) (sum*-g tup (lambda (x) (value p x)))) 
                                     (cdr gt)))
                       (cdr gt))))))) 

;; onegametree is defined in paradigms_ttt
;; be sure to look at that file!

;; what is the current game situation?
(display "Current State:     ")
(display (car (onegametree)))
(display "\n")

;; test of nextmove, where should we go next?
(display "Recommended Move:  ")
(display (nextmove 'x (onegametree)))
(display "\n")

;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

